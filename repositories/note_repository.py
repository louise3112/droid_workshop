from db.run_sql import run_sql
from models.note import Note

import repositories.service_repository as service_repo
import repositories.droid_repository as droid_repo

# CREATE
def save(note):
    sql = "INSERT INTO notes (date, note, droid_id, service_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [note.date, note.note, note.droid.id, note.service.id]
    run_sql(sql, values)


# READ
def select(id):
    note = None

    sql = "SELECT * FROM notes WHERE id = %s"
    values = [id]
    output = run_sql(sql, values)[0]

    if output is not None:
        service = service_repo.select(output['service_id'])
        droid = droid_repo.select(output['droid_id'])
        note = Note(output['date'], output['note'], droid, service, output['id'])
    
    return note

def select_notes_by_droid(droid):
    notes = []

    sql = "SELECT * FROM notes WHERE droid_id = %s ORDER BY date ASC"
    values = [droid.id]
    output = run_sql(sql, values)

    for row in output:
        service = service_repo.select(row['service_id'])
        note = Note(row['date'], row['note'], droid, service, row['id'])
        notes.append(note)
    
    return notes


# UPDATE
def update(note):
    sql = "UPDATE notes SET (date, note, service_id) = (%s, %s, %s) WHERE id = %s"
    values = [note.date, note.note, note.service.id, note.id]
    run_sql(sql, values)


# DELETE
def delete(id):
    sql = "DELETE FROM notes WHERE id = %s"
    values = [id]
    run_sql(sql, values)