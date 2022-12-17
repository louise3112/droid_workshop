from db.run_sql import run_sql
from models.droid import Droid
import repositories.owner_repository as owner_repo
import repositories.technician_repository as tech_repo

# CREATE
def save(droid):
    sql = "INSERT INTO droids (name, type, registration_date, repair_notes, owner_id, technician_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [droid.name, droid.type, droid.registration_date, droid.repair_notes, droid.owner.id, droid.technician.id]
    run_sql(sql, values)


# READ
def select_all():
    droids = []

    sql = "SELECT * FROM droids"
    output = run_sql(sql)

    for row in output:
        owner = owner_repo.select(row['owner_id'])
        technician = tech_repo.select(row['technician_id'])
        droid = Droid(row['name'], row['type'], row['registration_date'], row['repair_notes'], owner, technician, row['id'])
        droids.append(droid)

    return droids

def select(id):
    droid = None

    sql = "SELECT * FROM droids WHERE id = %s"
    values = [id]
    output = run_sql(sql, values)

    if output is not None:
        owner = owner_repo.select(output['owner_id'])
        technician = tech_repo.select(output['technician_id'])
        droid = Droid(output['name'], output['type'], output['registration_date'], output['repair_notes'], owner, technician, output['id'])
    
    return droid

def select_droid_by_technician(technician_id):
    droids = []

    sql = "SELECT * FROM droids WHERE technician_id = %s"
    values = [technician_id]
    output = run_sql(sql, values)

    for row in output:
        owner = owner_repo.select(row['owner_id'])
        technician = tech_repo.select(row['technician_id'])
        droid = Droid(row['name'], row['type'], row['registration_date'], row['repair_notes'], owner, technician, row['id'])
        droids.append(droid)

    return droids


# UPDATE
def update(droid):
    sql = "UPDATE droids SET (name, type, registration_date, repair_notes, owner_id, technician_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [droid.name, droid.type, droid.registration_date, droid.repair_notes, droid.owner.id, droid.technician.id]
    run_sql(sql, values)


# DELETE
def delete(id):
    sql = "DELETE FROM droids WHERE id = %s"
    values = [id]
    run_sql(sql, values)