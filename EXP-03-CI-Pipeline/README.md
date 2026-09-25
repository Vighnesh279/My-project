# EXP-03 - Continuous Integration Using GitHub Actions



## Aim



To implement a Continuous Integration (CI) pipeline that automatically builds and tests the application whenever code changes are pushed to the repository or a pull request is created.



## Tools Used



- Git

- GitHub

- GitHub Actions

- Python

- Pytest



## Application



The experiment uses a simple Python application with an automated test suite.



Project files include:



- app.py

- test_app.py

- requirements.txt

- .github/workflows/ci.yml



## CI Workflow



The GitHub Actions workflow is configured to run when changes are pushed to the main branch or when a pull request is created.



The workflow performs the following steps:



1. Checks out the repository code.

2. Sets up the Python environment.

3. Installs the required dependencies.

4. Runs the automated tests using Pytest.

5. Reports the test result through GitHub Actions.



## Workflow File



The CI workflow is available at:



.github/workflows/ci.yml



## Testing



The automated test suite is executed using:



pytest -q



A successful workflow indicates that the application tests have passed.



## Evidence



The complete faculty submission is available here:



Submission/DEV_VIG3.pdf



## Result



A Continuous Integration pipeline was successfully implemented using GitHub Actions. Code changes trigger the workflow automatically, dependencies are installed, and automated tests are executed to verify the application.


