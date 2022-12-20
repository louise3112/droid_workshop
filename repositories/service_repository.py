from db.run_sql import run_sql
from models.service import Service

import repositories.type_repository as type_repo

# CREATE
# def save(type):
#     sql = "INSERT INTO types (name, picture) VALUES (%s, %s) RETURNING *"
#     values = [type.name, type.picture]
#     run_sql(sql, values)


# READ
def select_all():
    services = []

    sql = "SELECT * FROM services"
    output = run_sql(sql)

    for row in output:
        service = Service(row['name'], row['id'])
        services.append(service)

    return services

def select(id):
    service = None

    sql = "SELECT * FROM services WHERE id = %s"
    values = [id]
    output = run_sql(sql, values)[0]

    if output is not None:
        service = Service(output['name'], output['id'])
    
    return service

# def select(id):
#     service = None

#     sql = "SELECT * FROM services WHERE id = %s"
#     values = [id]
#     output = run_sql(sql, values)[0]

#     if output is not None:
#         type = type_repo.select(output['type_id'])
#         service = Service(output['name'], type, output['id'])
    
#     return service

def select_services_by_type(type_id):
    services = []

    sql = "SELECT * FROM services_types WHERE type_id = %s"
    values = [type_id]
    output = run_sql(sql, values)

    for row in output:
        # service = Service(row['name'], type, row['id'])
        service = select(row['service_id'])
        services.append(service)
    
    return services