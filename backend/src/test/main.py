from src.prog.config import app, db
from src.prog.model import Person
from src.prog.route import *
import unittest
import json


class TestMain(unittest.TestCase):
    def setUp(self): # camelCase because unittest expects it
        app.config["TESTING"] = True
        self.api = app.test_client()
        with app.app_context():
            db.drop_all()
            db.create_all()
        self.assertEqual(app.config["TESTING"], True)

    def tearDown(self): # camelCase because unittest expects it
        with app.app_context():
            db.drop_all()

    def test_get_people(self):
        names = ["John Doe", "Jane Deer"]
        phones = ["0123456789", "9876543210"]
        emails = ["john@example.com", "jane@example.com"]
        person1 = Person(names[0], phones[0], emails[0])
        person2 = Person(names[1], phones[1], emails[1])
        with app.app_context():
            db.session.add(person1)
            db.session.add(person2)
            db.session.commit()

        response = self.api.get("/people")
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)

        self.assertEqual(len(response_data["people"]), 2)
        self.assertEqual(response_data["people"][0]["name"], names[0])
        self.assertEqual(response_data["people"][0]["phone"], phones[0])
        self.assertEqual(response_data["people"][0]["email"], emails[0])
        self.assertEqual(response_data["people"][1]["name"], names[1])
        self.assertEqual(response_data["people"][1]["phone"], phones[1])
        self.assertEqual(response_data["people"][1]["email"], emails[1])


if __name__ == "__main__":
    unittest.main()
