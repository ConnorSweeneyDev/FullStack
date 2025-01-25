from src.prog.config import app, db
from src.prog.models import Contact
from src.prog.routes import *
import unittest
import json


class TestMain(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.api = app.test_client()
        with app.app_context():
            db.drop_all()
            db.create_all()
        self.assertEqual(app.config["TESTING"], True)

    def tearDown(self):
        with app.app_context():
            db.drop_all()

    def test_get_contacts(self):
        first_names = ["John", "Jane"]
        last_names = ["Doe", "Deer"]
        emails = ["john@example.com", "jane@example.com"]
        contact1 = Contact(first_names[0], last_names[0], emails[0])
        contact2 = Contact(first_names[1], last_names[1], emails[1])
        with app.app_context():
            db.session.add(contact1)
            db.session.add(contact2)
            db.session.commit()

        response = self.api.get("/contacts")
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)

        self.assertEqual(len(response_data["contacts"]), 2)
        self.assertEqual(response_data["contacts"][0]["firstName"], first_names[0])
        self.assertEqual(response_data["contacts"][0]["lastName"], last_names[0])
        self.assertEqual(response_data["contacts"][0]["email"], emails[0])
        self.assertEqual(response_data["contacts"][1]["firstName"], first_names[1])
        self.assertEqual(response_data["contacts"][1]["lastName"], last_names[1])
        self.assertEqual(response_data["contacts"][1]["email"], emails[1])


if __name__ == "__main__":
    unittest.main()
