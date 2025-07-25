from flask import jsonify

from src.prog.config import app
from src.prog.model import Person


@app.route("/people", methods=["GET"])
def get_people():
    people = Person.query.all()
    json_people = list(map(lambda person: person.to_json(), people))
    return jsonify({"people": json_people}), 200
