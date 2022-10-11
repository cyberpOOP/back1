from modules import app
from flask import jsonify, request
from datetime import datetime
import json

file = open("modules/CATEGORIES.json")
CATEGORIES = json.load(file)

file = open("modules/USERS.json")
USERS = json.load(file)

file = open("modules/RECORDS.json")
RECORDS = json.load(file)


# GET /categories /users
# POST /category /user

@app.route("/")
def start():
    return "Hello"


@app.route("/categories")
def get_categories():
    return jsonify(CATEGORIES)


@app.route("/by_user")
def get_by_user():
    user = str(request.get_json())
    result = [

    ]
    for i in range(len(USERS)):
        if USERS[i]["name"] == user:
            user_id = USERS[i]["id"]

    for i in range(len(RECORDS)):
        if (RECORDS[i]["user id"]) == user_id:
            result.append(RECORDS[i])

    return result


@app.route("/by_category")
def get_by_category():
    user = dict(request.get_json())
    result = [

    ]
    for i in range(len(USERS)):
        if USERS[i]["name"] == user["name"]:
            user_id = USERS[i]["id"]

    for i in range(len(CATEGORIES)):
        if CATEGORIES[i]["category"] == user["category"]:
            category_id = CATEGORIES[i]["id"]

    for i in range(len(RECORDS)):
        if (RECORDS[i]["user id"]) == user_id and RECORDS[i]["category id"] == category_id:
            result.append(RECORDS[i])

    return result


@app.route("/category", methods=["POST"])
def create_category():
    category = request.get_json()
    CATEGORIES.append(
        {
            "id": int(len(CATEGORIES)),
            "category": str(category)
        }
    )

    with open("modules/CATEGORIES.json", "w") as file:
        json.dump(CATEGORIES, file, indent=4)

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

    with open("modules/USERS.json", "w") as file:
        json.dump(USERS, file, indent=4)

    return jsonify(USERS)


@app.route("/user_record", methods=["POST"])
def create_record_user():
    name = dict(request.get_json())
    date = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    for i in range(len(USERS)):
        if USERS[i]["name"] == name["name"]:
            user_id = int(USERS[i]["id"])
    for i in range(len(CATEGORIES)):
        if CATEGORIES[i]["category"] == name["category"]:
            category_id = int(CATEGORIES[i]["id"])

    RECORDS.append(
        {
            "id": int(len(RECORDS)),
            "user id": user_id,
            "category id": category_id,
            "date": str(date),
            "sum": int(name["value"])
        }
    )

    with open("modules/RECORDS.json", "w") as file:
        json.dump(RECORDS, file, indent=4)

    return jsonify(RECORDS)
