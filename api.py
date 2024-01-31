from flask import Flask, request, jsonify, render_template, Blueprint

from models import db, Cupcake

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/cupcakes')
def show_all_cupcakes():
    serialized_cupcakes = [c.serialize() for c in Cupcake.query.all()]
    return jsonify(cupcakes = serialized_cupcakes)

@api_bp.route('/api/cupcakes/<cupcake_id>')
def show_a_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake = cupcake.serialize())

@api_bp.route('/api/cupcakes', methods = ["POST"])
def create_a_cupcake():
    new_cupcake = Cupcake(
        flavor = request.json.get("flavor"),
        size = request.json.get("size"),
        rating = request.json.get("rating"),
        image = request.json.get("image")
    )

    db.session.add(new_cupcake)
    db.session.commit()
    response_json = jsonify(cupcake = new_cupcake.serialize())
    return (response_json, 201)

@api_bp.route('/api/cupcakes/<cupcake_id>', methods = ["PATCH"])
def update_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)
    db.session.commit()
    return jsonify(cupcake = cupcake.serialize())

@api_bp.route('/api/cupcakes/<cupcake_id>', methods = ['DELETE'])
def delete_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="Deleted Cupcake")
