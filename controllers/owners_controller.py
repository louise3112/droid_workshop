from flask import Blueprint, render_template, request, redirect
from models.owner import Owner 

import repositories.owner_repository as owner_repo
import repositories.droid_repository as droid_repo

owners_blueprint = Blueprint("owners", __name__)


@owners_blueprint.route("/owners/<id>/edit")
def edit(id):
    owner = owner_repo.select(id)
    return render_template("owners/edit.html", owner = owner)


@owners_blueprint.route("/owners/<id>/show", methods=['POST'])
def update(id):
    name = request.form['name']
    home_planet = request.form['home_planet']
    comlink_freq = request.form['comlink_freq']
    droid_id = request.form['droid_id']
    owner = Owner(name, home_planet, comlink_freq, id)
    owner_repo.update(owner)

    return redirect(f"/droids")

