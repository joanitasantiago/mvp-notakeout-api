from flask import Blueprint, request, jsonify
from models.food import Food
from database import db
from schemas.food_schema import food_schema
from schemas.food_schema import foods_schema


food_bp = Blueprint("food_bp", __name__)

@food_bp.route("/foods", methods=["POST"])
def create_food():
    """
    Cadastrar um novo alimento
    ---
    tags:
      - Alimentos
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            category:
              type: string
            nutritional_value:
              type: string
            unit:
              type: string
            in_stock:
              type: boolean
    responses:
      201:
        description: Alimento criado com sucesso
    """
    data = request.get_json()
    new_food = Food(
        name=data.get("name"),
        category=data.get("category"),
        nutritional_value=data.get("nutritional_value"),
        unit=data.get("unit"),
        in_stock=data.get("in_stock", False)
    )
    db.session.add(new_food)
    db.session.commit()

    return jsonify(food_schema(new_food)), 201

@food_bp.route("/foods", methods=["GET"])
def get_all_foods():
    """
    Listar todos os alimentos cadastrados
    ---
    tags:
      - Alimentos
    responses:
      200:
        description: Lista de alimentos retornada com sucesso
    """
    foods = Food.query.all()
    result = foods_schema(foods)
    return jsonify(result), 200