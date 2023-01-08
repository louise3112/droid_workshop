from flask import Blueprint, render_template, request, redirect
from models.service import Service

import repositories.service_repository as service_repo
import repositories.type_repository as type_repo

services_blueprint = Blueprint("services", __name__)


@services_blueprint.route("/services")
def index():
    services = service_repo.select_all()
    for service in services:
        types = type_repo.select_types_by_service(service.id)
        for type in types:
            service.valid_types.append(type)

    return render_template("services/index.html", all_services = services)


@services_blueprint.route("/services/<id>/edit")
def edit(id):
    service = service_repo.select(id)
    all_types = type_repo.select_all()
    relevant_types = type_repo.select_types_by_service(id)
    relevant_type_ids = []
    for type in relevant_types:
        relevant_type_ids.append(type.id)
    
    relevant_type_ids.sort()

    return render_template("services/edit.html", service = service, all_types = all_types, relevant_type_ids = relevant_type_ids)

@services_blueprint.route("/services/<id>/edit", methods=['POST'])
def update(id):
    name = request.form['name']
    cost = request.form['cost']
    service = Service(name, cost, id)
    service_repo.update(service)

    existing_types = type_repo.select_types_by_service(id)
    existing_type_ids = []
    for type in existing_types:
        existing_type_ids.append(type.id)
    
    all_types = type_repo.select_all()
    for type in all_types:
        if (f'{type.id}' in request.form) and (type.id not in existing_type_ids):
            service_repo.save_services_types(id, type.id)
        elif (f'{type.id}' not in request.form) and (type.id in existing_type_ids):
            service_repo.delete_services_types(id, type.id)
    return redirect("/services")


@services_blueprint.route("/services/<id>/delete", methods=['POST'])
def delete(id):
    service_repo.delete_services_types_for_service(id)
    service_repo.delete(id)
    return redirect("/services")


@services_blueprint.route("/services/new")
def new():
    types = type_repo.select_all()
    return render_template("services/new.html", all_types = types)

@services_blueprint.route("/services/new", methods=['POST'])
def create():
    name = request.form['name']
    cost = request.form['cost']
    new_service = Service(name, cost)
    service = service_repo.save(new_service)

    all_types = type_repo.select_all()
    for type in all_types:
        if f'{type.id}' in request.form:
            service_repo.save_services_types(service.id, type.id)

    return redirect("/services")