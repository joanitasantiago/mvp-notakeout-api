from flasgger import Swagger
from flask import Flask
from database import db
from routes.food_routes import food_bp

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///notakeout.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
swagger = Swagger(app)
app.register_blueprint(food_bp)

@app.route("/")
def home():
    return "API de Gerenciamento de Refeições - MVP"
if __name__ == "__main__":
    from models.recipe import Recipe
    from models.recipe_food import  RecipeFood
    from models.food import Food
    with app.app_context():
        db.create_all()
    app.run(debug=True)