from flask import Flask, render_template, request, redirect, url_for
from data import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recipes/<recipe_type>')
def recipes(recipe_type):
    recipes_list = read_recipes_by_recipe_type(recipe_type)
    return render_template("recipes.html", recipe_type=recipe_type, recipes=recipes_list)

@app.route('/recipes/<int:recipe_id>')
def recipe(recipe_id):
    recipe = read_recipe_by_recipe_id(recipe_id)
    return render_template("recipe.html",recipe=recipe)

@app.route('/add-a-recipe')
def register():
    return render_template('register.html')

@app.route('/processed', methods=['post'])
def processing():
    recipe_data = {
       "recipe_type": request.form['recipe_type'],
        "name": request.form['recipe_name'],
        "time": request.form['recipe_time'],
        "description": request.form['recipe_desc'],
        "url": request.form['recipe_url'],
        "source": request.form['recipe_source']
    }
    insert_recipe(recipe_data)
    return redirect(url_for('recipes', recipe_type=request.form['recipe_type']))


@app.route('/modify', methods=['post'])
def modify():
    if request.form["modify"] == "edit":
        recipe_id = request.form["recipe_id"] 
        recipe = read_recipe_by_recipe_id(int(recipe_id))
        return render_template('update.html', recipe=recipe)
    elif request.form["modify"] == "delete":
        recipe_id = request.form["recipe_id"] 
        recipe = read_recipe_by_recipe_id(recipe_id)
        delete_recipe(recipe_id)
        return redirect(url_for("recipes", recipe_type=recipe['recipe_type']))
        pass

@app.route('/update', methods=['post'])
def update():
   recipe_data = {
        "recipe_id" : request.form["recipe_id"],
        "recipe_type": request.form['recipe_type'],
        "name": request.form['recipe_name'],
        "time": request.form['recipe_time'],
        "description": request.form['recipe_desc'],
        "url": request.form['recipe_url'],
        "source": request.form['recipe_source']
    }
   update_recipe(recipe_data)
   return redirect(url_for('recipe',recipe_id = request.form['recipe_id']))

if __name__ == "__main__":
    app.run(debug=True)