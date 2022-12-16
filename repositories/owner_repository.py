from db.run_sql import run_sql
from models.owner import Owner

# CREATE
def save(owner):
    sql = "INSERT INTO owners (name, contact_info) VALUES (%s, %s) RETURNING *"
    values = [owner.name, owner.contact_details]
    run_sql(sql, values)
    # output = run_sql(sql, values)

    # id = output[0]['id']
    # owner.id = id

    # return owner


# READ
def select_all():
    owners = []

    sql = "SELECT * FROM owners"
    output = run_sql(sql)

    for row in output:
        owner = Owner(row['name'], row['contact_details'], row['id'])
        owners.append(owner)

    return owners

def select(id):
    owner = None

    sql = "SELECT * FROM owners WHERE id = %s"
    values = [id]
    output = run_sql(sql, values)

    if output is not None:
        owner = Owner(output['name'], output['contact_details'], output['id'])
    
    return owner


# UPDATE
def update(owner):
    sql = "UPDATE owners SET (name, contact_details) = (%s, %s) WHERE id = %s"
    values = [owner.name, owner.contact_details, owner.id]
    run_sql(sql, values)


# DELETE
# def delete(id):
#     sql = "DELETE FROM owners WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)