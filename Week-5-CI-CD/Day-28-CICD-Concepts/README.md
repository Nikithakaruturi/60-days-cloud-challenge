**Day 28 – CI/CD Concepts**

**Objective**

Understand the basic concepts of Continuous Integration (CI), Continuous Delivery (CD), Continuous Deployment, and CI/CD pipelines.

**What is CI?**

Continuous Integration is the practice of frequently integrating code changes into a shared repository.

When developers push changes, automated processes can build and test the code to identify problems early.

**What is CD?**

Continuous Delivery is the practice of automatically preparing validated code for release.

Continuous Deployment goes one step further by automatically deploying validated changes to the target environment.

**CI/CD Pipeline**

A basic CI/CD pipeline can follow this flow:

Code → Build → Test → Deploy

**Build**

The application or project is prepared for execution or packaging.

**Test**

Automated tests are executed to check whether the application works correctly.

**Deploy**

The validated application is delivered to the required environment.

**Benefits of CI/CD**

- Faster software delivery
- Early detection of errors
- Reduced manual work
- Consistent deployment processes
- Better collaboration between development and operations
- More reliable software releases

**Example Workflow**

1. Developer makes a code change.
2. Code is pushed to GitHub.
3. CI process starts automatically.
4. Application is built.
5. Automated tests are executed.
6. If validation succeeds, the application can be prepared for deployment.
7. The application is deployed to the target environment.

**Cloud and CI/CD**

CI/CD can be used with cloud applications to automate the process of building, testing, and deploying applications.

In this challenge, GitHub Actions will be used to practice CI/CD automation in the next step.

**Key Learnings**

- CI helps integrate and validate code changes frequently.
- Continuous Delivery prepares validated changes for release.
- Continuous Deployment automatically releases validated changes.
- A CI/CD pipeline automates repetitive software delivery steps.
- GitHub can be used as the source-code platform for CI/CD workflows.

**Result**

Learned the fundamentals of CI/CD and understood the basic flow from code changes through build, testing, and deployment.
