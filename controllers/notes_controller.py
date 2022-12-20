from flask import Blueprint, render_template, request, redirect
from models.note import Note
from datetime import date

import repositories.note_repository as note_repo
import repositories.service_repository as service_repo
import repositories.droid_repository as droid_repo
import repositories.type_repository as type_repo

notes_blueprint = Blueprint("notes", __name__)


@notes_blueprint.route("/notes/<droid_id>/new")
def new(droid_id):
    droid = droid_repo.select(droid_id)
    services = service_repo.select_services_by_type(droid.type.id)
    actual_date = date.today()
    current_date = date(actual_date.year - 960, actual_date.month, actual_date.day)
    return render_template("notes/new.html", droid = droid, available_services = services, current_date = current_date)

@notes_blueprint.route("/notes", methods=['POST'])
def create():
    date = request.form['date']
    note_text = request.form['note_text']
    droid_id = request.form['droid_id']
    service_id = request.form['service_id']

    droid = droid_repo.select(droid_id)
    service = service_repo.select(service_id)

    note = Note(date, note_text, droid, service)
    note_repo.save(note)
    return redirect(f"/droids/{droid.id}/show")


@notes_blueprint.route("/notes/<id>/edit")
def edit(id):
    note = note_repo.select(id)
    droid = droid_repo.select(note.droid.id)
    services = service_repo.select_services_by_type(droid.type.id)
    return render_template("notes/edit.html", note = note, droid = droid, available_services = services)

@notes_blueprint.route("/notes/<id>/show", methods=['POST'])
def update(id):
    date = request.form['date']
    service_id = request.form['service_id']
    note_text = request.form['note_text']
    droid_id = request.form['droid_id']

    droid = droid_repo.select(droid_id)
    service = service_repo.select(service_id)

    note = Note(date, note_text, droid, service, id)
    note_repo.update(note)

    return redirect(f"/droids/{droid_id}/show")


@notes_blueprint.route("/notes/<id>/delete", methods=['POST'])
def delete(id):
    note = note_repo.select(id)
    droid = droid_repo.select(note.droid.id)
    note_repo.delete(id)
    return redirect(f"/droids/{droid.id}/show")

