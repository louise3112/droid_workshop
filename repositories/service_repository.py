from db.run_sql import run_sql
from models.service import Service

import repositories.type_repository as type_repo

# CREATE
# def save(type):
#     sql = "INSERT INTO types (name, picture) VALUES (%s, %s) RETURNING *"
#     values = [type.name, type.picture]
#     run_sql(sql, values)


# READ
def select(id):
    service = None

    sql = "SELECT * FROM services WHERE id = %s"
    values = [id]
    output = run_sql(sql, values)[0]

    if output is not None:
        type = type_repo.select(output['type_id'])
        service = Service(output['name'], type, output['id'])
    
    return service

def select_services_by_type(type):
    services = []

    sql = "SELECT * FROM services WHERE type_id = %s ORDER BY name ASC"
    values = [type.id]
    output = run_sql(sql, values)

    for row in output:
        service = Service(row['name'], type, row['id'])
        services.append(service)
    
    return services