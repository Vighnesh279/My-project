# EXP-06 - Docker Image Deployment

## Aim

To create Docker images and deploy a containerized Flask web application, verify the deployment, and demonstrate application update and redeployment using Docker image versions.

## Tools Used

- Docker Desktop
- Docker Engine
- Python
- Flask
- Windows 11
- Command Prompt
- cURL

## Application

A Flask web application was created with:

- app.py
- requirements.txt
- Dockerfile

The application provides:

- / - Application response
- /health - Health check

## Docker Image

The application was first built as:

mywebapp:1.0

The image was verified using:

docker images

## Local Container Testing

The Version 1.0 image was tested using a Docker container with port mapping:

5000:5000

The application was verified using:

curl http://localhost:5000

curl http://localhost:5000/health

The application returned the expected response and the health endpoint returned OK.

## Deployment

The application was deployed using:

mywebapp:1.0

The deployment configuration was:

Container name: deployed-webapp

Host port: 8080

Container port: 5000

Restart policy: unless-stopped

The deployed application was verified using:

curl http://localhost:8080

The response confirmed successful deployment.

## Application Update and Redeployment

The application was updated from Version 1.0 to Version 2.0.

A new Docker image was built:

mywebapp:2.0

The previous deployed-webapp container was stopped and removed.

The Version 2.0 image was then deployed using the same port mapping:

8080:5000

The final deployment was verified using:

docker ps

curl http://localhost:8080

docker logs deployed-webapp

The final application returned:

Application deployed successfully using Docker! Version 2.0

The container logs also showed a successful HTTP 200 response.

## Evidence

The complete faculty submission will be available in:

Submission/DEV_VIG6.pdf

The submission file will be added separately when required.

## Result

Docker images were successfully created and deployed. The Flask application was tested locally, deployed using port mapping and a restart policy, and successfully updated and redeployed using Docker image Version 2.0.