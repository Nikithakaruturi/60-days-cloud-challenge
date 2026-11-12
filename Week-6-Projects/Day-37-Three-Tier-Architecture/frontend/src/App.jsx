import { useEffect, useState } from "react";
import "./App.css";

const API_URL = "http://localhost:5000/api/employees";

function App() {
  const [employees, setEmployees] = useState([]);
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [department, setDepartment] = useState("");
  const [error, setError] = useState("");

  async function fetchEmployees() {
    try {
      const response = await fetch(API_URL);

      if (!response.ok) {
        throw new Error("Unable to fetch employees");
      }

      const data = await response.json();
      setEmployees(data);
      setError("");
    } catch (err) {
      setError(err.message);
    }
  }

  useEffect(() => {
    fetchEmployees();
  }, []);

  async function addEmployee(event) {
    event.preventDefault();

    try {
      const response = await fetch(API_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ name, email, department }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || "Unable to add employee");
      }

      setName("");
      setEmail("");
      setDepartment("");
      setError("");

      fetchEmployees();
    } catch (err) {
      setError(err.message);
    }
  }

  return (
    <div className="container">
      <h1>Employee Management System</h1>
      <p>Manage your employee records</p>

      <form onSubmit={addEmployee}>
        <input
          type="text"
          placeholder="Employee Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />

        <input
          type="email"
          placeholder="Email Address"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />

        <input
          type="text"
          placeholder="Department"
          value={department}
          onChange={(e) => setDepartment(e.target.value)}
          required
        />

        <button type="submit">Add Employee</button>
      </form>

      {error && <p>{error}</p>}

      <h2>Employee Records</h2>

      {employees.length === 0 ? (
        <p>No employees added yet.</p>
      ) : (
        <table>
          <thead>
            <tr>
              <th>Name</th>
              <th>Email</th>
              <th>Department</th>
            </tr>
          </thead>

          <tbody>
            {employees.map((employee) => (
              <tr key={employee.id}>
                <td>{employee.name}</td>
                <td>{employee.email}</td>
                <td>{employee.department}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default App;
