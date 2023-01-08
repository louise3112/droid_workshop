from db.run_sql import run_sql
from models.owner import Owner

# CREATE
def save(owner):
    sql = "INSERT INTO owners (name, home_planet, comlink_frequency) VALUES (%s, %s, %s) RETURNING *"
    values = [owner.name, owner.home_planet, owner.comlink_frequency]
    output = run_sql(sql, values)
    owner.id = output[0]['id']
    return owner


# READ
def select_all():
    owners = []

    sql = "SELECT * FROM owners ORDER BY name ASC"
    output = run_sql(sql)

    for row in output:
        owner = Owner(row['name'], row['home_planet'], row['comlink_frequency'], row['id'])
        owners.append(owner)

    return owners

def select(id):
    owner = None

    sql = "SELECT * FROM owners WHERE id = %s"
    values = [id]
    output = run_sql(sql, values)[0]

    if output is not None:
        owner = Owner(output['name'], output['home_planet'], output['comlink_frequency'], output['id'])
    
    return owner


# UPDATE
def update(owner):
    sql = "UPDATE owners SET (name, home_planet, comlink_frequency) = (%s, %s, %s) WHERE id = %s"
    values = [owner.name, owner.home_planet, owner.comlink_frequency, owner.id]
    run_sql(sql, values)


# DELETE
def delete(id):
    sql = "DELETE FROM owners WHERE id = %s"
    values = [id]
    run_sql(sql, values)