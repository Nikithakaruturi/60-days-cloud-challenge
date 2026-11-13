**Day 37 - Three-Tier Architecture Demo**

**Project Name**
Employee Management System

**Objective**
Build a three-tier web application with a React frontend, Flask REST API backend, and MySQL database.

**Technology Stack**
- Frontend: React with Vite
- Backend: Python Flask
- Database: MySQL
- Version Control: Git and GitHub

**Architecture**
1. Presentation Tier - React frontend.
2. Application Tier - Flask REST API.
3. Data Tier - MySQL database.

**Completed Tasks**
- Created the project directory structure.
- Created a React application using Vite.
- Installed frontend dependencies.
- Created a Python virtual environment.
- Installed Flask and MySQL Connector.
- Created backend requirements.txt.
- Developed initial Flask API endpoints.
- Tested the backend health endpoint.
- Tested the employees API endpoint.

**API Endpoints**
- GET /api/health - Check backend status.
- GET /api/employees - Retrieve employee records.

**Result**
Created the initial frontend and backend structure for a three-tier Employee Management System.


**Day 38 - React Frontend and Flask API Integration**

**Objective**
Connect the React frontend with the Flask REST API.

**Completed Tasks**
- Created the Employee Management System interface using React.
- Added employee name, email, and department input fields.
- Connected React to the Flask backend using Fetch API.
- Implemented GET API to retrieve employee records.
- Implemented POST API to add new employees.
- Configured Flask-CORS for frontend-backend communication.
- Tested employee creation and retrieval.
- Verified frontend and backend integration.

**API Endpoints**
- GET /api/health - Check backend status.
- GET /api/employees - Retrieve employee records.
- POST /api/employees - Add a new employee.

**Result**
Successfully connected the React frontend with the Flask REST API. Employees can be added and displayed in the Employee Management System.


**Day 39 - MySQL Database Integration**

**Objective**
Connect Flask REST API with MySQL for persistent employee storage.

**Completed Tasks**
- Reused the existing MySQL Docker container.
- Created the employee_management database.
- Created the employees table.
- Configured database credentials using backend .env.
- Connected Flask to MySQL using mysql-connector-python.
- Loaded environment variables using python-dotenv.
- Updated GET /api/employees to retrieve records from MySQL.
- Updated POST /api/employees to insert records into MySQL.
- Tested employee creation and retrieval.
- Verified records through the React frontend.

**Result**
Connected the Flask API to MySQL. Employee records are stored persistently in the employee_management database.
