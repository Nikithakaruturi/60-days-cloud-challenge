**Day 31: Jenkins Basics (Optional)**

**Objective**

Learn Jenkins basics and execute a simple automated build job.

**Tools Used**
- Jenkins
- Docker
- WSL Ubuntu

**Practice**
- Downloaded the Jenkins LTS Docker image.
- Created and started a Jenkins container.
- Accessed Jenkins through `http://localhost:8081`.
- Completed the initial Jenkins setup.
- Created a Freestyle project named `day31-first-job`.
- Added shell commands as a build step.
- Executed the Jenkins job and verified the successful build.

**Docker Container**
- Container name: `jenkins-day31`
- Image: `jenkins/jenkins:lts`
- Port: `8081`

**Key Learnings**
- Understanding Jenkins and CI/CD.
- Creating Jenkins Freestyle jobs.
- Executing shell commands through Jenkins.
- Checking build status and Console Output.

**Result**

Successfully created and executed my first Jenkins job. Build #1 completed with SUCCESS status.
