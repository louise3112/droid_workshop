from db.run_sql import run_sql
from models.type import Type

# CREATE
# def save(type):
#     sql = "INSERT INTO types (name, picture) VALUES (%s, %s) RETURNING *"
#     values = [type.name, type.picture]
#     run_sql(sql, values)


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
    output = run_sql(sql, values)

    if output is not None:
        type = Type(output['name'], output['picture'], output['id'])
    
    return type


# UPDATE
def update(type):
    sql = "UPDATE types SET (name, picture) = (%s, %s) WHERE id = %s"
    values = [type.name, type.picture, type.id]
    run_sql(sql, values)


# DELETE
# def delete(id):
#     sql = "DELETE FROM types WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)