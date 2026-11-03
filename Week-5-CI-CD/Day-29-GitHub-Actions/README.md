**Day 29 – GitHub Actions Basics**

**Objective**

Learn the basics of GitHub Actions and create a simple CI workflow.

**What is GitHub Actions?**

GitHub Actions is a CI/CD automation platform integrated with GitHub. It can automatically run tasks when events occur in a repository.

**Workflow**

A GitHub Actions workflow is defined using a YAML file stored inside `.github/workflows/`.

**Workflow File**

`day29-ci.yml`

**Trigger**

The workflow runs when code is pushed to the `main` branch. It can also be started manually using `workflow_dispatch`.

**Job**

The workflow contains a job named `basic-ci` that runs on an Ubuntu environment.

**Steps**

1. Checkout the repository using `actions/checkout@v4`.
2. Run a simple CI message using a shell command.

**CI Flow**

Code Push → GitHub Actions → Checkout Repository → Run CI Step

**Practice Completed**

Created the `.github/workflows/` directory and added a basic GitHub Actions CI workflow.

**Key Learnings**

- GitHub Actions can automate development tasks.
- Workflow files use YAML.
- Workflow files are stored in `.github/workflows/`.
- Workflows can be triggered by repository events.
- Jobs contain one or more steps.
- GitHub provides hosted runners such as Ubuntu.

**Result**

Created my first GitHub Actions workflow and learned the basic structure of a CI pipeline.
