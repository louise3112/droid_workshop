from flask import Blueprint, render_template, request, redirect
from datetime import date

from models.droid import Droid
from models.owner import Owner

import repositories.droid_repository as droid_repo
import repositories.type_repository as type_repo
import repositories.owner_repository as owner_repo
import repositories.technician_repository as tech_repo
import repositories.note_repository as notes_repo

droids_blueprint = Blueprint("droids", __name__)


@droids_blueprint.route("/droids")
def index():
    droids = droid_repo.select_all()
    return render_template("droids/index.html", all_droids = droids)


@droids_blueprint.route("/droids/<id>/show")
def show_droid(id):
    droid = droid_repo.select(id)
    notes = notes_repo.select_notes_by_droid(droid)
    owner = owner_repo.select(droid.owner.id)
    return render_template("droids/show.html", droid = droid, notes = notes, owner = owner)


@droids_blueprint.route("/droids/<id>/edit")
def edit(id):
    droid = droid_repo.select(id)
    types = type_repo.select_all()
    owner = owner_repo.select(droid.owner.id)
    relevant_technicians = tech_repo.select_technicians_by_type(droid.type.id)
    return render_template("droids/edit.html", droid = droid, all_types = types, owner = owner, relevant_techs = relevant_technicians)

@droids_blueprint.route("/droids/<id>/edit", methods=['POST'])
def update(id):    
    name = request.form['name']
    type_id = request.form['type_id']
    technician_id = request.form['tech_id']
    activation_date = request.form['activation_date']

    type = type_repo.select(type_id)
    technician = tech_repo.select(technician_id)

    original_droid = droid_repo.select(id)
    owner = original_droid.owner

    droid = Droid(name, type, activation_date, owner, technician, id)
    droid_repo.update(droid)

    return redirect(f"/droids/{id}/show")


@droids_blueprint.route("/droids/<id>/delete", methods=['POST'])
def delete(id):
    droid = droid_repo.select(id)
    owner = owner_repo.select(droid.owner.id)

    droid_repo.delete(id)
    
    remaining_droids = droid_repo.select_droids_by_owner(owner)
    if remaining_droids == []:
        owner_repo.delete(owner.id)

    return redirect("/droids")


@droids_blueprint.route("/droids/new")
def new():
    types = type_repo.select_all()
    owners = owner_repo.select_all()
    actual_date = date.today()
    current_date = date(actual_date.year - 960, actual_date.month, actual_date.day)
    return render_template("droids/new.html", all_types = types, all_owners = owners, current_date = current_date)

@droids_blueprint.route("/droids/new", methods=['POST'])
def new_further_info():
    name = request.form['name']
    type_id = request.form['type_id']
    activation_date = request.form['activation_date']
    owner_id = request.form['owner_id']

    type = type_repo.select(type_id)
    relevant_technicians = tech_repo.select_technicians_by_type(type_id)

    if len(relevant_technicians) > 1 or owner_id == "New":
        droid = Droid(name, type, activation_date, 0, 0)
        return render_template("droids/new_further_info.html", droid = droid, relevant_techs = relevant_technicians, owner_id = owner_id)

    elif len(relevant_technicians) == 1:
        technician = relevant_technicians[0]
        owner = owner_repo.select(owner_id)
        droid = Droid(name, type, activation_date, owner, technician)
        droid_repo.save(droid)
        return redirect("/droids")
    
    else:
        owner = owner_repo.select(owner_id)
        droid = Droid(name, type, activation_date, owner)
        droid_repo.save_no_tech(droid)
        return redirect("/droids")


@droids_blueprint.route("/droids/new/further-info", methods=['POST'])
def create():
    type_id = request.form['droid_type_id']
    type = type_repo.select(type_id)

    num_of_techs = int(request.form['num_of_techs'])
    if num_of_techs > 1:
        tech_id = request.form['tech_id']
        technician = tech_repo.select(tech_id)
    else:
        technician = tech_repo.select_technicians_by_type(type_id)[0]

    owner_id = request.form['owner_id']
    if owner_id == "New":
        owner_name = request.form['name']
        home_planet = request.form['home_planet']
        comlink_freq = request.form['comlink_freq']
        new_owner = Owner(owner_name, home_planet, comlink_freq)
        owner = owner_repo.save(new_owner)
    else:
        owner = owner_repo.select(owner_id)
    
    droid_name = request.form['droid_name']
    activation_date = request.form['activation_date']

    droid = Droid(droid_name, type, activation_date, owner, technician)
    droid_repo.save(droid)

    return redirect("/droids")


@droids_blueprint.route("/droids/unassigned")
def show_unassigned_droids():
    unassigned_droids = droid_repo.select_unassigned_droids()
    return render_template("droids/unassigned.html", unassigned_droids = unassigned_droids)

