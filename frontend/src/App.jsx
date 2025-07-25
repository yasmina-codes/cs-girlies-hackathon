import { useState, useEffect } from "react";
import PersonList from "./PersonList";
import "./App.css";

function App() {
  const [people, setPeople] = useState([]);

  useEffect(() => {
    fetchPeople();
  }, []);

  const fetchPeople = async () => {
    const response = await fetch("http://127.0.0.1:5000/people");
    const data = await response.json();
    setPeople(data.people);
  };

  return <PersonList people={people} />;
}

export default App;
