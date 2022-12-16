from db.run_sql import run_sql
from models.technician import Technician

# CREATE
def save(technician):
    sql = "INSERT INTO technicians (name, speciality) VALUES (%s, %s) RETURNING *"
    values = [technician.name, technician.speciality]
    run_sql(sql, values)


# READ
def select_all():
    technicians = []

    sql = "SELECT * FROM technicians"
    output = run_sql(sql)

    for row in output:
        technician = Technician(row['name'], row['speciality'], row['id'])
        technicians.append(technician)

    return technicians

def select(id):
    technician = None

    sql = "SELECT * FROM technicians WHERE id = %s"
    values = [id]
    output = run_sql(sql, values)

    if output is not None:
        technician = Technician(output['name'], output['speciality'], output['id'])
    
    return technician


# UPDATE
def update(technician):
    sql = "UPDATE technicians SET (name, speciality) = (%s, %s) WHERE id = %s"
    values = [technician.name, technician.speciality, technician.id]
    run_sql(sql, values)


# DELETE
def delete(id):
    sql = "DELETE FROM technicians WHERE id = %s"
    values = [id]
    run_sql(sql, values)