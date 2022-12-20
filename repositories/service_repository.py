from db.run_sql import run_sql
from models.service import Service

import repositories.type_repository as type_repo

# CREATE
# def save(type):
#     sql = "INSERT INTO types (name, picture) VALUES (%s, %s) RETURNING *"
#     values = [type.name, type.picture]
#     run_sql(sql, values)


# READ
# def select_all():
#     types = []

#     sql = "SELECT * FROM types"
#     output = run_sql(sql)

#     for row in output:
#         type = Type(row['name'], row['picture'], row['id'])
#         types.append(type)

#     return types

def select(id):
    service = None

    sql = "SELECT * FROM services WHERE id = %s"
    values = [id]
    output = run_sql(sql, values)[0]

    if output is not None:
        type_id = output['type_id']
        if type_id is not None:
            type = type_repo.select(type_id)
        else:
            type = None
            
        service = Service(output['name'], type, output['id'])
    
    return service