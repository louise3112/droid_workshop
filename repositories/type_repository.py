from db.run_sql import run_sql
from models.type import Type


# READ
def select_all():
    types = []

    sql = "SELECT * FROM types"
    output = run_sql(sql)

    for row in output:
        type = Type(row['name'], row['picture'], row['id'])
        types.append(type)

    return types

def select(id):
    type = None

    sql = "SELECT * FROM types WHERE id = %s"
    values = [id]
    output = run_sql(sql, values)[0]

    if output is not None:
        type = Type(output['name'], output['picture'], output['id'])
    
    return type

def select_types_by_service(service_id):
    types = []

    sql = "SELECT * FROM services_types WHERE service_id = %s"
    values = [service_id]
    output = run_sql(sql, values)

    for row in output:
        type = select(row['type_id'])
        types.append(type)
    
    return types


# UPDATE
def update(type):
    sql = "UPDATE types SET (name, picture) = (%s, %s) WHERE id = %s"
    values = [type.name, type.picture, type.id]
    run_sql(sql, values)
