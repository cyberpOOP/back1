from Modules import app
from flask import jsonify, request
from datetime import datetime
import json

# GET /categories /users
# POST /category /user

CATEGORIES = [
    {
        "id": 0,
        "category": "Food"
    }
]


@app.route("/categories")
def get_categories():
    return jsonify(CATEGORIES)
