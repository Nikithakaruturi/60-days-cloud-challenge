**Day 32: CI/CD with Kubernetes**

**Objective:**
Practice how a Docker application can be deployed and managed in a Kubernetes cluster using Minikube.

**Practice Tasks:**
- Started the existing Minikube cluster.
- Verified the Kubernetes node status.
- Checked the existing Day 24 Docker application.
- Inspected the Kubernetes Deployment and Service.
- Loaded the existing Docker image into Minikube.
- Updated the Deployment image using kubectl.
- Verified the Deployment rollout.
- Checked that the application pod was running successfully.

**Key Learnings:**
- Kubernetes Deployments manage application pods.
- Minikube provides a local Kubernetes environment.
- Docker images must be available to the cluster before deployment.
- The `kubectl set image` command updates a Deployment's container image.
- The `kubectl rollout status` command checks deployment progress.

**CI/CD Understanding:**

The Day 30 GitHub Actions workflow builds the Docker image on a GitHub-hosted runner. Since the workflow uses `push: false`, the image is not published to a container registry or automatically transferred to the local Minikube cluster.

A complete automated pipeline would require publishing the image to a container registry and configuring Kubernetes deployment steps.

**Result:**

Successfully verified the existing application Deployment and Running pod in Minikube.
