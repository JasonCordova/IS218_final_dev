import csv
import logging
import os
import sys
import datetime
import time

from flask import Blueprint, render_template, abort, url_for,current_app
from flask_login import current_user, login_required
from jinja2 import TemplateNotFound
from rfc3339 import rfc3339

from app.db import db
from app.db.models import Record
from app.records.forms import csv_upload
from werkzeug.utils import secure_filename, redirect

records = Blueprint('records', __name__,
                        template_folder='templates')

@records.route('/records', methods=['GET'], defaults={"page": 1})
@records.route('/records/<int:page>', methods=['GET'])
@login_required
def records_browse(page):
    page = page
    per_page = 1000
    pagination = Record.query.paginate(page, per_page, error_out=False)
    data = pagination.items
    try:
        return render_template('browse_records.html',data=data,pagination=pagination)
    except TemplateNotFound:
        abort(404)

@records.route('/records/upload', methods=['POST', 'GET'])

def records_upload():
    form = csv_upload()

    if form.validate_on_submit():
        log = logging.getLogger("myApp")
        filename = secure_filename(form.file.data.filename)

        if filename == '':
            return redirect(url_for('records.records_upload'))

        # Logging info for when a user successfully uploads a CSV file.
        log.info("\"%s\" has successfully uploaded a CSV file (%s) at %s", current_user.email, filename, datetime.datetime.now().strftime('%m/%d/%Y - %H:%M:%S'))

        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        form.file.data.save(filepath)
        list_of_records = []
        with open(filepath) as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                list_of_records.append(Record(row['\ufeffAMOUNT'], row['TYPE']))
                current_user.balance += float(row['\ufeffAMOUNT'])

        current_user.records += list_of_records
        db.session.commit()

        return redirect(url_for('auth.dashboard'))

    try:
        return render_template('upload.html', form=form)
    except TemplateNotFound:
        abort(404)