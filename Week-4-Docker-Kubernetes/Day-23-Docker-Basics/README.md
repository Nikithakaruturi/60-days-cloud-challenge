**Day 23: Docker Basics**

**Objective**

Learn Docker fundamentals and verify that Docker can download images and run containers.

**Environment**

- Operating System: Ubuntu on WSL
- Docker Version: 29.1.3

**Tasks Completed**

- Installed Docker using the Ubuntu package manager.
- Checked the Docker service status.
- Verified the Docker version.
- Downloaded and ran the `hello-world` image.
- Listed Docker images.
- Listed running containers.
- Listed all containers, including stopped containers.

**Commands Practiced**

- `sudo docker --version` — Check the installed Docker version.
- `sudo docker run hello-world` — Download the image if needed and run a container.
- `sudo docker images` — List downloaded images.
- `sudo docker ps` — List running containers.
- `sudo docker ps -a` — List all containers, including stopped containers.

**Key Learnings**

- A Docker image is a template used to create a container.
- A container is an instance created from an image.
- Docker Hub provides images that can be downloaded.
- The `Exited (0)` status indicates that a container completed successfully.
- The `docker ps` command shows running containers, while `docker ps -a` also shows stopped containers.

**Result**

Successfully installed and verified Docker in WSL Ubuntu. Downloaded the `hello-world` image and ran containers successfully.
