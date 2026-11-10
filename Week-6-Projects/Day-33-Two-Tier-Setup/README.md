**Project: DevOps Two-Tier Flask Application**

**Week:** 6 - Projects
**Day:** 33
**Challenge:** 60 Days Cloud Challenge

**Objective**
Set up the initial structure for a two-tier application using Python and Flask.

**Technologies Used**
- Python
- Flask
- MySQL Connector
- HTML
- Docker (planned for project setup)

**Project Structure**
- app/ - Flask application
- app/templates/ - HTML templates
- app/static/ - Static files
- database/ - Database-related files
- requirements.txt - Python dependencies
- .gitignore - Excludes virtual environment and temporary files

**Completed Tasks**
- Created the project directory structure.
- Created a Python virtual environment.
- Installed Flask and MySQL Connector.
- Created the Flask application.
- Created the HTML home page.
- Added a health-check endpoint.
- Tested the application successfully in a browser.
- Created requirements.txt and .gitignore.

**Application Endpoints**
- `/` - Home page
- `/health` - Application health check

**Result**
Successfully created and tested the initial Flask application setup. MySQL integration and Docker Compose configuration will be completed in the upcoming project days.
---

**Day 34 - Flask Application Development**

**Completed Tasks**
- Created a Flask home page with an HTML form.
- Implemented a POST route to process form submissions.
- Retrieved user input using Flask request.
- Created a result page using Jinja2 templates.
- Tested form submission successfully.
- Verified the health-check endpoint.

**Application Routes**
- `/` - Displays the home page and input form.
- `/submit` - Processes submitted form data.
- `/health` - Returns application health status.

**Result**
Successfully developed and tested a Flask application with form submission and dynamic response handling.


---

**Day 35 - MySQL Database Integration**

**Completed Tasks**
- Downloaded and started MySQL 8.0 using Docker.
- Created the `two_tier_db` database.
- Created the `users` table with ID, username, and timestamp columns.
- Connected the Flask application to MySQL using `mysql-connector-python`.
- Used environment variables to configure database credentials.
- Implemented database insertion when users submit the form.
- Verified that submitted user records were saved successfully.

**Database Details**
- Database: `two_tier_db`
- Table: `users`
- Database container: `two-tier-mysql`
- MySQL host port: `3307`

**Result**

Successfully integrated MySQL with the Flask application and verified that submitted usernames are stored in the database.


---

**Day 36 - Docker Compose and Two-Tier Application Testing**

**Completed Tasks**
- Created a Dockerfile to containerize the Flask application.
- Created a Docker Compose configuration for Flask and MySQL.
- Configured communication between the application and database containers.
- Reused the existing MySQL persistent volume.
- Built and started both containers using Docker Compose.
- Verified that the MySQL container became healthy.
- Tested the Flask home page and health-check endpoint.
- Submitted user data through the application.
- Verified that submitted records were stored successfully in MySQL.

**Docker Services**
- `web` - Flask application running on port 5000.
- `db` - MySQL 8.0 database running on port 3306 inside the container.
- Persistent volume: `two_tier_mysql_data`.

**Testing Results**
- Docker Compose containers started successfully.
- Flask application accessible at `http://localhost:5000`.
- Health endpoint returned a healthy status.
- Form submission worked successfully.
- MySQL records were retrieved using `SELECT * FROM users;`.

**Result**

Successfully containerized and tested a two-tier Flask and MySQL application using Docker Compose with persistent database storage.
