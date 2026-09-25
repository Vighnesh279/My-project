# EXP-05 - Docker Containerization



## Aim



To understand and implement application containerization using Docker by creating a Docker image and running the application inside a Docker container.



## Tools Used



- Docker

- Python

- Flask

- Command Line



## Application



The experiment uses a simple Flask web application.



Project files include:



- app.py

- requirements.txt

- Dockerfile



## Dockerfile



The Dockerfile defines the instructions required to build the application image.



It uses a Python base image, installs the required Flask dependency, copies the application files, exposes port 5000, and starts the Flask application.



## Docker Image



The Docker image was built using:



docker build -t myapp:1.0 .



The created image was verified using:



docker images



## Docker Container



The application was executed inside a Docker container with port mapping between the host and container.



The running container was verified using:



docker ps



Container logs were also checked to confirm that the Flask application started successfully.



## Application Verification



The containerized application was accessed using the mapped port.



The response was verified using:



curl http://localhost:5000



The application returned:



Hello from Docker Container



The HTTP response was successfully verified.



## Container Management



The experiment also included stopping and removing the Docker container after verification.



## Evidence



The complete faculty submission is available here:



Submission/DEV_VIG5.pdf



## Result



The Flask application was successfully containerized using Docker. A Docker image was created, a container was started with port mapping, application logs were verified, and the containerized application was accessed successfully.


