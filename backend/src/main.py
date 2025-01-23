from flask import request, jsonify
from config import app, db
from models import Contact


@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda contact: contact.to_json(), contacts))
    return jsonify({"contacts": json_contacts})


@app.route("/create_contact", methods=["POST"])
def create_contact():
    if not request.json:
        return jsonify({"message": "Must include a JSON body!"}), 400
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")
    if not first_name or not last_name or not email:
        return (
            jsonify({"message": "Must include a first name, last name, and email!"}),
            400,
        )

    new_contact = Contact(first_name, last_name, email)
    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": "Contact created!"}), 201


@app.route("/update_contact/<int:contact_id>", methods=["PATCH"])
def update_contact(contact_id):
    contact = Contact.query.get(contact_id)
    if not contact:
        return jsonify({"message": "Contact not found!"}), 404

    if not request.json:
        return jsonify({"message": "Must include a JSON body!"}), 400
    contact.first_name = request.json.get("firstName", contact.first_name)
    contact.last_name = request.json.get("lastName", contact.last_name)
    contact.email = request.json.get("email", contact.email)

    try:
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": "Contact updated!"}), 204


@app.route("/delete_contact/<int:contact_id>", methods=["DELETE"])
def delete_contact(contact_id):
    contact = Contact.query.get(contact_id)
    if not contact:
        return jsonify({"message": "Contact not found!"}), 404

    try:
        db.session.delete(contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": "Contact deleted!"}), 204


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
