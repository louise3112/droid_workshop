from db.run_sql import run_sql
from models.technician import Technician
import repositories.type_repository as type_repo

# CREATE
def save(technician):
    sql = "INSERT INTO technicians (name, picture, bio, type_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [technician.name, technician.picture, technician.bio, technician.type.id]
    run_sql(sql, values)


# READ
def select_all():
    technicians = []

    sql = "SELECT * FROM technicians"
    output = run_sql(sql)

    for row in output:
        type = type_repo.select(row['type_id'])
        technician = Technician(row['name'], row['picture'], row['bio'], type, row['id'])
        technicians.append(technician)

    return technicians

def select(id):
    technician = None

    sql = "SELECT * FROM technicians WHERE id = %s"
    values = [id]
    output = run_sql(sql, values)

    if output is not None:
        type = type_repo.select(output['type_id'])
        technician = Technician(output['name'], output['picture'], output['bio'], type, output['id'])
    
    return technician


# UPDATE
def update(technician):
    sql = "UPDATE technicians SET (name, picture, bio, type_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [technician.name, technician.picture, technician.bio, technician.type.id, technician.id]
    run_sql(sql, values)


# DELETE
def delete(id):
    sql = "DELETE FROM technicians WHERE id = %s"
    values = [id]
    run_sql(sql, values)