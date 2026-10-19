# DevOps Experiments Repository

This repository contains the implementation and documentation of DevOps experiments covering Agile project management, version control, Continuous Integration, configuration management, containerization, Kubernetes deployment, monitoring, and machine learning lifecycle management.

## Experiments

| Experiment | Topic | Status |
|---|---|---|
| EXP-01 | Agile SDLC Using Jira | Completed |
| EXP-02 | Git and GitHub Version Control | Completed |
| EXP-03 | Continuous Integration Using GitHub Actions | Completed |
| EXP-04 | Ansible Configuration Management | Completed |
| EXP-05 | Docker Containerization | Completed |
| EXP-06 | Docker Image Deployment | Completed |
| EXP-07 | Kubernetes Deployment and Management | Completed |
| EXP-08 | Automated Deployment Pipeline | Completed |
| EXP-09 | System Monitoring Using Prometheus and Grafana | Completed |
| EXP-10 | MLflow Machine Learning Lifecycle | Completed |

## Repository Structure

```text
My-project/
|-- .github/
|-- EXP-01-Jira/
|-- EXP-02-Git-GitHub/
|-- EXP-03-CI-Pipeline/
|-- EXP-04-Ansible/
|-- EXP-05-Docker/
|-- EXP-06/
|-- EXP-06-Docker-Deployment/
|-- EXP-07/
|-- EXP-07-Kubernetes-Deployment/
|-- EXP-08/
|-- EXP-08-Automated-Deployment-Pipeline/
|-- EXP-09/
`-- EXP-10/
```
## EXP-01 - Agile SDLC Using Jira

Jira Scrum was used to manage the Agile development workflow, including epics, user stories, sprint planning, Scrum board tracking, GitHub integration, Burndown, and Velocity reporting.

Faculty submission:

`EXP-01-Jira/Submission/DEV_VIG1.pdf`

## EXP-02 - Git and GitHub Version Control

Git and GitHub operations were performed including repository initialization, commits, feature branching, merging, merge conflict resolution, remote repository operations, push, and pull.

Faculty submission:

`EXP-02-Git-GitHub/Submission/DEV_VIG2.pdf`

## EXP-03 - Continuous Integration Using GitHub Actions

A Python application was configured with a GitHub Actions CI workflow to install dependencies and execute automated tests using Pytest.

Faculty submission:

`EXP-03-CI-Pipeline/Submission/DEV_VIG3.pdf`

## EXP-04 - Ansible Configuration Management

Ansible was used to automate Nginx installation, service configuration, web page deployment, connectivity testing, and idempotence verification.

Faculty submission:

`EXP-04-Ansible/Submission/DEV_VIG4.pdf`

## EXP-05 - Docker Containerization

A Flask application was containerized using Docker. The Docker image was built, a container was started with port mapping, logs were verified, and the application was accessed successfully.

Faculty submission:

`EXP-05-Docker/Submission/DEV_VIG5.pdf`

## EXP-06 - Docker Image Deployment

A Flask application was packaged into Docker images and deployed in a container. The application was updated to a new version and verified through the mapped HTTP port.

Project files:

`EXP-06-Docker-Deployment/`

Faculty submission:

`EXP-06-Docker-Deployment/Submission/DEV_VIG6.pdf`

## EXP-07 - Kubernetes Deployment and Management

A Kubernetes Deployment and NodePort Service were configured to deploy the application. Replica scaling, pod replacement, rolling updates, and rollback were tested.

Project files:

`EXP-07-Kubernetes-Deployment/`

Faculty submission:

`EXP-07-Kubernetes-Deployment/Submission/DEV_VIG7.pdf`

## EXP-08 - Automated Deployment Pipeline

A GitHub Actions pipeline was configured to test the application, build and push a Docker image to Docker Hub, and deploy the image to Kubernetes using a self-hosted runner.

Project files:

`EXP-08-Automated-Deployment-Pipeline/`

Faculty submission:

`EXP-08-Automated-Deployment-Pipeline/Submission/DEV_VIG8.pdf`

## EXP-09 - System Monitoring Using Prometheus and Grafana

Prometheus and Node Exporter were configured for system metrics collection. PromQL was used to query CPU, memory, and filesystem metrics, while Grafana was used for dashboards and alert configuration.

Project files and evidence:

- `EXP-09/README.md`
- `EXP-09/prometheus.yml`
- `EXP-09/Submission/EXP-09-Screenshots.pdf`

The Prometheus configuration in this repository documents the experiment setup.

## EXP-10 - MLflow Machine Learning Lifecycle

An Iris classification model was trained with multiple Random Forest configurations. MLflow was used to track experiment parameters, accuracy metrics, and model artifacts. A model was registered and served for prediction requests.

Project files:

- `EXP-10/train.py`
- `EXP-10/README.md`

The `Submission` folder is reserved for the final faculty submission document and supporting evidence.

## Jira Integration

This repository is linked with Jira issue `DEVOPS-3`.

The corresponding GitHub branch is:

`DEVOPS-3-jira-integration`

## Repository Purpose

This repository serves as the consolidated implementation and documentation repository for the DevOps experiments.
