import React from "react";

const PersonList = ({ people }) => {
  return (
    <div>
      <h2>People</h2>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Phone Number</th>
            <th>Email</th>
          </tr>
        </thead>
        <tbody>
          {people.map((person) => (
            <tr key={person.id}>
              <td>{person.name}</td>
              <td>{person.phone}</td>
              <td>{person.email}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default PersonList;
