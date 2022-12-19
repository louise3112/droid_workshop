from db.run_sql import run_sql
from models.technician import Technician
import repositories.type_repository as type_repo

# CREATE
def save(technician):
    sql = "INSERT INTO technicians (name, type_id) VALUES (%s, %s) RETURNING *"
    values = [technician.name, technician.type.id]
    run_sql(sql, values)


# READ
def select_all():
    technicians = []

    sql = "SELECT * FROM technicians ORDER BY name ASC"
    output = run_sql(sql)

    for row in output:
        type = type_repo.select(row['type_id'])
        technician = Technician(row['name'], type, row['id'])
        technicians.append(technician)

    return technicians

def select(id):
    technician = None

    sql = "SELECT * FROM technicians WHERE id = %s"
    values = [id]
    output = run_sql(sql, values)[0]

    if output is not None:
        type = type_repo.select(output['type_id'])
        technician = Technician(output['name'], type, output['id'])
    
    return technician

def select_technicians_by_type(type_id):
    technicians = []

    sql = "SELECT * FROM technicians WHERE type_id = %s ORDER BY name ASC"
    values = [type_id]
    output = run_sql(sql, values)

    for row in output:
        type = type_repo.select(row['type_id'])
        technician = Technician(row['name'], type, row['id'])
        technicians.append(technician)

    return technicians


# UPDATE
def update(technician):
    sql = "UPDATE technicians SET (name, type_id) = (%s, %s) WHERE id = %s"
    values = [technician.name, technician.type.id, technician.id]
    run_sql(sql, values)


# DELETE
def delete(id):
    sql = "DELETE FROM technicians WHERE id = %s"
    values = [id]
    run_sql(sql, values)