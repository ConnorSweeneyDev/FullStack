from src.prog.config import app, db
from src.prog.models import Contact
from src.prog.main import *
import unittest
import json


class TestMain(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.api = app.test_client()
        with app.app_context():
            db.drop_all()
            db.create_all()
        self.assertEqual(app.debug, False)

    def test_get_contacts(self):
        contact1 = Contact("John", "Doe", "john@example.com")
        contact2 = Contact("Jane", "Deer", "jane@example.com")
        with app.app_context():
            db.session.add(contact1)
            db.session.add(contact2)
            db.session.commit()

        response = self.api.get("/contacts")
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertEqual(len(response_data["contacts"]), 2)


if __name__ == "__main__":
    unittest.main()
