import sqlite3

db_path = "recipes.db"

def connect_to_db(path):
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return (conn, conn.cursor())

def read_recipes_by_recipe_type(recipe_type):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM recipes WHERE recipe_type = ?'
    value = recipe_type
    results = cur.execute(query,(value,)).fetchall()
    conn.close()
    return results

def read_recipe_by_recipe_id(recipe_id):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM recipes WHERE recipe_id = ?'
    value = recipe_id
    result = cur.execute(query,(value,)).fetchone()
    conn.close()
    return result

def insert_recipe(recipe_data):
    conn, cur = connect_to_db(db_path)
    query = 'INSERT INTO recipes (recipe_type, name, time, description, url, source) VALUES (?,?,?,?,?,?)'
    values = (recipe_data['recipe_type'], recipe_data['name'],
              recipe_data['time'], recipe_data['description'],
              recipe_data['url'], recipe_data['source'])
    cur.execute(query,values)
    conn.commit()
    conn.close()

def update_recipe(recipe_data):
    conn, cur = connect_to_db(db_path)
    query = "UPDATE recipes SET recipe_type=?, name=?, time=?, description=?, url=?, source=? WHERE recipe_id=?"
    values = (recipe_data['recipe_type'], recipe_data['name'],
              recipe_data['time'], recipe_data['description'],
              recipe_data['url'], recipe_data['source'],
              recipe_data['recipe_id'])
    cur.execute(query, values)
    conn.commit()
    conn.close()

# This function deletes a record
def delete_recipe(recipe_id):
    conn, cur = connect_to_db(db_path)
    query = "DELETE FROM recipes WHERE recipe_id = ?"
    values = (recipe_id,)
    cur.execute(query, values)
    conn.commit()
    conn.close()