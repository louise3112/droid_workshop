from db.run_sql import run_sql
from models.note import Note

import repositories.service_repository as service_repo

# CREATE
# def save(type):
#     sql = "INSERT INTO types (name, picture) VALUES (%s, %s) RETURNING *"
#     values = [type.name, type.picture]
#     run_sql(sql, values)


# READ
def select_notes_by_droid(droid):
    notes = []

    sql = "SELECT * FROM notes WHERE droid_id = %s"
    values = [droid.id]
    output = run_sql(sql, values)

    for row in output:
        service = service_repo.select(row['service_id'])
        note = Note(row['date'], row['note'], droid, service, row['id'])
        notes.append(note)
    
    return notes


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