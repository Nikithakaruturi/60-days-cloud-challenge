**Day 25: Install Minikube**

**Objective**

Install Minikube and set up a local Kubernetes cluster using Docker as the driver.

**Environment**

- Operating System: Ubuntu on WSL
- Docker: Installed and running
- Minikube Version: v1.39.0
- Kubernetes Version: v1.37.0

**Tasks Completed**

- Installed Minikube.
- Configured Docker permissions for the current user.
- Started a local Kubernetes cluster using the Docker driver.
- Verified that the Minikube node status is Ready.
- Checked Kubernetes system pods across all namespaces.
- Confirmed that the Kubernetes system pods are running.

**Commands Practiced**

- `minikube version` — Check the installed Minikube version.
- `minikube start --driver=docker` — Start the Kubernetes cluster using Docker.
- `minikube kubectl -- get nodes` — Check Kubernetes node status.
- `minikube kubectl -- get pods -A` — View pods across all namespaces.
- `docker ps` — Check running Docker containers.

**Key Learnings**

- Minikube runs a local Kubernetes cluster for learning and testing.
- Docker can be used as the Minikube driver.
- A Kubernetes node hosts the components required to run workloads.
- Kubernetes system pods provide cluster services such as networking, scheduling, and API access.

**Result**

Successfully installed Minikube and started a local Kubernetes cluster. Verified that the node is Ready and all listed Kubernetes system pods are running.
