from flask import Blueprint, render_template, request, redirect
from models.droid import Droid
import repositories.droid_repository as droid_repo
import repositories.type_repository as type_repo
import repositories.owner_repository as owner_repo
import repositories.technician_repository as tech_repo

droids_blueprint = Blueprint("droids", __name__)


@droids_blueprint.route("/droids")
def index():
    droids = droid_repo.select_all()
    return render_template("droids/index.html", all_droids = droids)


@droids_blueprint.route("/droids/<id>/show")
def show_droid(id):
    droid = droid_repo.select(id)
    owner = owner_repo.select(droid.owner.id)
    return render_template("droids/show.html", droid = droid, owner = owner)


@droids_blueprint.route("/droids/<id>/edit")
def edit(id):
    droid = droid_repo.select(id)
    types = type_repo.select_all()
    owner = owner_repo.select(droid.owner.id)
    relevant_technicians = tech_repo.select_technicians_by_type(droid.type.id)
    return render_template("droids/edit.html", droid = droid, all_types = types, owner = owner, relevant_techs = relevant_technicians)

@droids_blueprint.route("/droids/<id>/show", methods=['POST'])
def update(id):
    name = request.form['name']
    type_id = request.form['type_id']
    registration_date = request.form['reg_date']
    repair_notes = request.form['notes']
    owner_id = request.form['owner_id']
    technician_id = request.form['tech_id']

    type = type_repo.select(type_id)
    owner = owner_repo.select(owner_id)  # ADD SOMETHING HERE TO DEAL WITH CHANGE IN OWNER??
    technician = tech_repo.select(technician_id)
    droid = Droid(name, type, registration_date, repair_notes, owner, technician, id)

    droid_repo.update(droid)
    return redirect("/droids")


@droids_blueprint.route("/droids/<id>/delete", methods=['POST'])
def delete(id):
    droid_repo.delete(id)
    return redirect("/droids")


@droids_blueprint.route("/droids/new")
def new():
    types = type_repo.select_all()
    # ADD SOMETHING TO CALCULATE "TODAY" DATE - ACTUAL DATE - ~950 YEARS?
    # ADD SOMETHING TO ALLOW CAPTURE OF OWNER INFO?
    # ADD SOMETHING TO CREATE LIST OF RELEVANT TECHNICIANS - HOW TO DO THIS IF WE DON'T YET KNOW DROID TYPE??
    return render_template("droids/new.html", all_types = types)

@droids_blueprint.route("/droids", methods=['POST'])
def create():
    name = request.form['name']
    type_id = request.form['type_id']
    registration_date = request.form['reg_date']
    repair_notes = request.form['notes']
    owner_id = request.form['owner_id']
    technician_id = request.form['tech_id']

    type = type_repo.select(type_id)
    owner = owner_repo.select(owner_id)  # ADD SOMETHING HERE TO ALLOW FOR CREATION OF NEW OWNER??
    technician = tech_repo.select(technician_id)
    droid = Droid(name, type, registration_date, repair_notes, owner, technician)

    droid_repo.save(droid)
    return redirect("/droids")