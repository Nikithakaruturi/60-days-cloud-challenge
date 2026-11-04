**Day 30: Docker Build with GitHub Actions**

**Objective**
Automate Docker image building using GitHub Actions.

**Tools Used**
- Docker
- GitHub Actions
- Docker Buildx

**Practice**
- Reused the Dockerfile from Day 24.
- Created a GitHub Actions workflow.
- Configured the workflow to run on pushes to the main branch.
- Added Docker Buildx to build the Docker image.
- Configured the workflow to build the image without pushing it to a container registry.

**Workflow File**
`.github/workflows/day30-docker-build.yml`

**Application Used**
`Week-4-Docker-Kubernetes/Day-24-Containerize-App`

**Key Learnings**
- Automating Docker image builds.
- Using Docker Buildx in GitHub Actions.
- Integrating Docker builds into a CI pipeline.

**Result**
Created a GitHub Actions workflow to automatically build the Docker image whenever changes are pushed to the main branch.
