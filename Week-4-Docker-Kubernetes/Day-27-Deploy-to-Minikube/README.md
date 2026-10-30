**Day 27 – Deploy Container to Minikube**

**Objective**

Deploy the Docker application created on Day 24 to a local Kubernetes cluster using Minikube.

**Environment**

- Minikube: v1.39.0
- Kubernetes: v1.37.0
- Docker Driver
- Application Image: `day24-web-app:latest`

**Deployment Steps**

- Started the Minikube cluster.
- Verified the existing Docker image.
- Loaded `day24-web-app:latest` into Minikube.
- Created a Kubernetes Deployment.
- Created one application Pod.
- Created a Kubernetes NodePort Service.
- Accessed the application through the Minikube Service URL.

**Kubernetes Resources**

Deployment: `day24-web-app`

Pod: `day24-web-app-7864bbd54-f5zhl`

Service: `day24-web-app-service`

Service Type: `NodePort`

Container Port: `80`

**Files**

`deployment.yaml` – Kubernetes Deployment configuration.

`service.yaml` – Kubernetes Service configuration.

**Commands Practiced**

`minikube image load day24-web-app:latest`

`minikube kubectl -- apply -f deployment.yaml`

`minikube kubectl -- get deployments`

`minikube kubectl -- get pods`

`minikube kubectl -- apply -f service.yaml`

`minikube kubectl -- get services`

`minikube service day24-web-app-service --url`

**Key Learnings**

- A Kubernetes Deployment manages application Pods.
- Pods run containers inside the Kubernetes cluster.
- A Service provides network access to an application.
- NodePort can expose a Service outside the cluster.
- Minikube can run Kubernetes locally for learning and testing.
- A Docker image can be loaded directly into Minikube and used by a Deployment.

**Result**

Successfully deployed the Day 24 Docker web application to Kubernetes using Minikube and accessed the application through a Kubernetes NodePort Service.
