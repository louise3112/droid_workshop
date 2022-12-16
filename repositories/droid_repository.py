from db.run_sql import run_sql
from models.droid import Droid

# CREATE
def save(droid):
    sql = "INSERT INTO droids (name, type, registration_date, repair_notes, owner_id, technician_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [droid.name, droid.type, droid.registration_date, droid.repair_notes, droid.owner_id, droid.technician_id]
    run_sql(sql, values)


# READ
def select_all():
    droids = []

    sql = "SELECT * FROM droids"
    output = run_sql(sql)

    for row in output:
        droid = Droid(row['name'], row['type'], row['registration_date'], row['repair_notes'], row['owner_id'], row['technician_id'], row['id'])
        droids.append(droid)

    return droids

def select(id):
    droid = None

    sql = "SELECT * FROM droids WHERE id = %s"
    values = [id]
    output = run_sql(sql, values)

    if output is not None:
        droid = Droid(output['name'], output['type'], output['registration_date'], output['repair_notes'], output['owner_id'], output['technician_id'], output['id'])
    
    return droid


# UPDATE
def update(droid):
    sql = "UPDATE droids SET (name, type, registration_date, repair_notes, owner_id, technician_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [droid.name, droid.type, droid.registration_date, droid.repair_notes, droid.owner_id, droid.technician_id]
    run_sql(sql, values)


# DELETE
def delete(id):
    sql = "DELETE FROM droids WHERE id = %s"
    values = [id]
    run_sql(sql, values)