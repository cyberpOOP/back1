from modules import app
from flask import jsonify, request
from datetime import datetime
import json

# GET /categories /users /records
# POST /category /user /by_user /by_category /user_record

CATEGORIES = [
    {
        "id": 0,
        "category": "Food"
    }
]

RECORDS = [

]

USERS = [
    {
        "id": 0,
        "name": "Ben"
    }
]


@app.route("/")
def start():
    return jsonify("I'm working")


@app.route("/categories")
def get_categories():
    return jsonify(CATEGORIES)


@app.route("/users")
def get_users():
    return jsonify(USERS)


@app.route("/records")
def get_records():
    return jsonify(RECORDS)


@app.route("/by_user", methods=["POST"])
def get_by_user():
    user = str(request.get_json())
    result = [

    ]
    for i in range(len(RECORDS)):
        if (RECORDS[i]["user"]) == user:
            result.append(RECORDS[i])

    return jsonify(result)


@app.route("/by_category", methods=["POST"])
def get_by_category():
    info = dict(request.get_json())
    result = [

    ]
    for i in range(len(RECORDS)):
        if (RECORDS[i]["user"]) == info["name"] and RECORDS[i]["category"] == info["category"]:
            result.append(RECORDS[i])

    return jsonify(result)


@app.route("/category", methods=["POST"])
def create_category():
    category = request.get_json()
    CATEGORIES.append(
        {
            "id": int(len(CATEGORIES)),
            "category": str(category)
        }
    )

    return jsonify(CATEGORIES)


@app.route("/user", methods=["POST"])
def create_user():
    user = request.get_json()
    USERS.append(
        {
            "id": int(len(USERS)),
            "name": str(user)
        }
    )

    return jsonify(USERS)


@app.route("/user_record", methods=["POST"])
def create_record_user():
    name = dict(request.get_json())
    date = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    for i in range(len(USERS)):
        if USERS[i]["name"] == name["name"]:
            user = str(USERS[i]["name"])
    for i in range(len(CATEGORIES)):
        if CATEGORIES[i]["category"] == name["category"]:
            category = str(CATEGORIES[i]["category"])

    RECORDS.append(
        {
            "id": int(len(RECORDS)),
            "user": user,
            "category": category,
            "date": str(date),
            "sum": int(name["value"])
        }
    )

    return jsonify(RECORDS)
