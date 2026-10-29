**Day 26 – Kubernetes Basics**

**Objective**

Learn the basic Kubernetes concepts and explore a local Kubernetes cluster using Minikube.

**Environment**

- Minikube: v1.39.0
- Kubernetes: v1.37.0
- Driver: Docker
- Cluster: Minikube

**Kubernetes Basics Practiced**

- Checked Kubernetes namespaces.
- Checked Pods in the default namespace.
- Checked system Pods across all namespaces.
- Checked Kubernetes Services.
- Inspected the Minikube node details.
- Verified that the Minikube node is Ready.

**Commands Practiced**

`minikube kubectl -- get namespaces`

`minikube kubectl -- get pods`

`minikube kubectl -- get pods -A`

`minikube kubectl -- get services`

`minikube kubectl -- describe node minikube`

`minikube kubectl -- get nodes`

**Key Learnings**

- A Kubernetes cluster can contain multiple namespaces.
- Pods are the basic execution units in Kubernetes.
- Services provide networking access to Kubernetes resources.
- The Minikube node acts as the local Kubernetes control-plane node.
- Kubernetes system components run in the `kube-system` namespace.
- The `Ready` node status indicates that the node is available to run workloads.

**Result**

Successfully explored the basic Kubernetes resources in Minikube and verified that the Kubernetes node is in the `Ready` state.
