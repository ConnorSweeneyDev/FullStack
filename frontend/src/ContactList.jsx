import React from "react";

const ContactList = ({ contacts, updateContact, updateCallback }) => {
  const deleteContact = async (id) => {
    try {
      const options = { method: "DELETE" };
      const response = await fetch(
        `http://127.0.0.1:5000/delete_contact/${id}`,
        options,
      );
      if (response.status === 204) {
        updateCallback();
      } else {
        console.error(response.status);
      }
    } catch (error) {
      alert(error);
    }
  };

  return (
    <div>
      <h2>Contact List</h2>
      <table>
        <thead>
          <tr>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Email</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {contacts.map((contact) => (
            <tr key={contact.id}>
              <td>{contact.firstName}</td>
              <td>{contact.lastName}</td>
              <td>{contact.email}</td>
              <td>
                <button onClick={() => updateContact(contact)}>Update</button>
                <button onClick={() => deleteContact(contact.id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ContactList;
