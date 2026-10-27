**Day 24: Containerize a Simple Application**

**Objective**

Create a simple HTML application and run it inside a Docker container using Nginx.

**Environment**

- Operating System: Ubuntu on WSL
- Docker Version: 29.1.3
- Base Image: nginx:alpine

**Files Created**

- `index.html` — Contains the web page content.
- `Dockerfile` — Defines how to build the application image.
- `README.md` — Documents the practice.

**Tasks Completed**

- Created a simple HTML web application.
- Created a Dockerfile using the Nginx Alpine image.
- Built the Docker image named `day24-web-app`.
- Started a container named `day24-container`.
- Mapped host port 8080 to container port 80.
- Opened the application in a web browser.
- Verified the HTML response using curl.

**Commands Practiced**

- `sudo docker build -t day24-web-app ./Week-4-Docker-Kubernetes/Day-24-Containerize-App` — Build the Docker image.
- `sudo docker run -d -p 8080:80 --name day24-container day24-web-app` — Start the container.
- `sudo docker ps` — Check running containers.
- `curl http://localhost:8080` — Verify the web page response.

**Key Learnings**

- A Dockerfile defines the instructions for building an image.
- Docker images package the application and its required environment.
- Containers run applications using Docker images.
- Nginx can serve static HTML content from inside a container.
- Port mapping makes the container's web server accessible through the host port.

**Result**

Successfully built a Docker image, ran the HTML application inside a container, and accessed the application at `http://localhost:8080`.
