from db.run_sql import run_sql
from models.service import Service


# CREATE
def save(service):
    sql = "INSERT INTO services (name, cost) VALUES (%s, %s) RETURNING *"
    values = [service.name, service.cost]
    output = run_sql(sql, values)
    service.id = output[0]['id']
    return service

def save_services_types(service_id, type_id):
    sql = "INSERT INTO services_types (service_id, type_id) VALUES (%s, %s)"
    values = [service_id, type_id]
    run_sql(sql, values)

# READ
def select_all():
    services = []

    sql = "SELECT * FROM services ORDER BY name ASC"
    output = run_sql(sql)

    for row in output:
        service = Service(row['name'], row['cost'], row['id'])
        services.append(service)

    return services

def select(id):
    service = None

    sql = "SELECT * FROM services WHERE id = %s"
    values = [id]
    output = run_sql(sql, values)[0]

    if output is not None:
        service = Service(output['name'], output['cost'], output['id'])
    
    return service

def select_services_by_type(type_id):
    services = []

    sql = "SELECT * FROM services_types WHERE type_id = %s"
    values = [type_id]
    output = run_sql(sql, values)

    for row in output:
        service = select(row['service_id'])
        services.append(service)
    
    return services


# UPDATE
def update(service):
    sql = "UPDATE services SET (name, cost) = (%s, %s) WHERE id = %s"
    values = [service.name, service.cost, service.id]
    run_sql(sql, values)


# DELETE
def delete(id):
    sql = "DELETE FROM services WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_services_types(service_id, type_id):
    sql = "DELETE FROM services_types WHERE service_id = %s AND type_id = %s"
    values = [service_id, type_id]
    run_sql(sql, values)

def delete_services_types_for_service(service_id):
    sql = "DELETE FROM services_types WHERE service_id = %s"
    values = [service_id]
    run_sql(sql, values)


