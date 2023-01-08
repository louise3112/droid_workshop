from flask import Blueprint, render_template, request, redirect
from models.owner import Owner 

import repositories.owner_repository as owner_repo

owners_blueprint = Blueprint("owners", __name__)


@owners_blueprint.route("/droids/<droid_id>/owner/<owner_id>/edit")
def edit(droid_id, owner_id):
    owner = owner_repo.select(owner_id)
    # droid_id = request.form['droid_id']
    return render_template("owners/edit.html", owner = owner, droid_id = droid_id)


@owners_blueprint.route("/droids/<droid_id>/owner/<owner_id>/edit", methods=['POST'])
def update(droid_id, owner_id):
    name = request.form['name']
    home_planet = request.form['home_planet']
    comlink_freq = request.form['comlink_freq']
    # droid_id = request.form['droid_id']
    owner = Owner(name, home_planet, comlink_freq, owner_id)
    owner_repo.update(owner)

    return redirect(f"/droids/{droid_id}/show")

