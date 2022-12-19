from flask import Blueprint, render_template, request, redirect
from models.technician import Technician
import repositories.technician_repository as tech_repo
import repositories.type_repository as type_repo
import repositories.droid_repository as droid_repo

technicians_blueprint = Blueprint("technicians", __name__)


@technicians_blueprint.route("/technicians")
def index():
    technicians = tech_repo.select_all()
    return render_template("technicians/index.html", all_technicians = technicians)


@technicians_blueprint.route("/technicians/<id>/show")
def show_technician(id):
    technician = tech_repo.select(id)
    droids = droid_repo.select_droids_by_technician(technician)
    return render_template("technicians/show.html", technician = technician, droids_assigned = droids)


@technicians_blueprint.route("/technicians/<id>/edit")
def edit(id):
    technician = tech_repo.select(id)
    types = type_repo.select_all()
    return render_template("technicians/edit.html", technician = technician, all_types = types)

@technicians_blueprint.route("/technicians/<id>/show", methods=['POST'])
def update(id):
    name = request.form['name']
    picture = request.form['picture']
    type_id = request.form['type_id']
    type = type_repo.select(type_id)
    technician = Technician(name, picture, type, id)
    tech_repo.update(technician)
    return redirect("/technicians")


@technicians_blueprint.route("/technicians/<id>/delete", methods=['POST'])
def delete(id):
    tech_repo.delete(id)
    return redirect("/technicians")


@technicians_blueprint.route("/technicians/new")
def new():
    types = type_repo.select_all()
    return render_template("technicians/new.html", all_types = types)

@technicians_blueprint.route("/technicians", methods=['POST'])
def create():
    name = request.form['name']
    picture = request.form['picture']
    type_id = request.form['type_id']
    type = type_repo.select(type_id)
    technician = Technician(name, picture, type)
    tech_repo.save(technician)
    return redirect("/technicians")