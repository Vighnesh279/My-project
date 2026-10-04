# EXP-08 – Automated Deployment Pipeline

## Automated Deployment Pipeline

The EXP-08 pipeline automates application testing, Docker image creation, Docker Hub publishing, and deployment to a local Kubernetes cluster.

## Pipeline Flow

GitHub Repository  
↓  
GitHub Actions  
↓  
Python Tests  
↓  
Docker Build  
↓  
Docker Hub  
↓  
Self-Hosted Windows Runner  
↓  
Minikube  
↓  
Kubernetes Deployment  
↓  
Running Application

## GitHub Actions Workflow

Workflow file:

`.github/workflows/exp08-deployment.yml`

The workflow contains two jobs:

### 1. Build, Test and Push Docker Image

- Checks out the source code.
- Sets up Python 3.12.
- Installs Flask and pytest.
- Runs automated tests.
- Logs in to Docker Hub using GitHub repository secrets.
- Builds the Docker image.
- Pushes the Docker image to Docker Hub using the Git commit SHA as the image tag.

### 2. Deploy to Minikube

- Runs on the self-hosted Windows runner.
- Verifies the Kubernetes cluster.
- Updates the Kubernetes Deployment with the newly created Docker Hub image.
- Waits for the Kubernetes rollout to complete.
- Verifies the deployment, pods, and service.

## Docker Image

Docker Hub repository:

`24107108/mywebapp`

The successful pipeline generated and deployed the following image:

`24107108/mywebapp:c917c9a1bcdcd77fc1acf35fbdf413c06adfc67b`

The image uses the Git commit SHA as its version tag.

## Automated Testing

The application contains three tests:

- Home page returns HTTP 200.
- Health endpoint returns HTTP 200 and `OK`.
- Invalid endpoint returns HTTP 404.

Local test result:

`3 passed`

The same tests are executed automatically by GitHub Actions before the Docker image is pushed.

## Kubernetes Deployment

The application is deployed to Minikube using:

- Deployment: `mywebapp-deployment`
- Replicas: 2
- Service: `mywebapp-service`
- Service type: NodePort
- Container port: 5000
- Service port: 80
- NodePort: 30080

The automated deployment successfully updated the Kubernetes Deployment to the Docker Hub image.

Final deployment status:

`mywebapp-deployment  2/2  Ready`

Both Kubernetes pods reached the `Running` state.

## Deployment Verification

The deployed application was tested through the Minikube service.

Final response:

`Application deployed successfully using Docker! Version 2.0`

This confirms that the new Docker image was successfully built, pushed to Docker Hub, deployed to Kubernetes, and served by the application.

## Result

The automated deployment pipeline was successfully implemented using GitHub Actions, Docker Hub, a self-hosted Windows runner, and Minikube Kubernetes.

The pipeline automatically tests the application, builds and publishes a versioned Docker image, updates the Kubernetes deployment, waits for a successful rollout, and verifies the running deployment.