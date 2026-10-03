\# EXP-07 - Kubernetes Deployment and Management



\## Aim



To deploy and manage a containerized web application using Kubernetes Deployment and Service resources, perform scaling, self-healing, rolling update, rollback, verification, and cleanup.



\## Tools Used



\- Docker Desktop

\- Kubernetes

\- Minikube

\- kubectl

\- Windows 11

\- PowerShell

\- cURL



\## Docker Image



The Docker image created in EXP-06 was used:



mywebapp:1.0



The updated image was also used:



mywebapp:2.0



The images were loaded into the Minikube cluster using:



minikube image load mywebapp:1.0

minikube image load mywebapp:2.0



\## Kubernetes Deployment



The application was deployed using `deployment.yaml`.



Deployment name:



mywebapp-deployment



Initial replicas:



2



Container port:



5000



Image:



mywebapp:1.0



The Deployment was successfully created and verified using kubectl.



\## Kubernetes Service



The application was exposed using a NodePort Service defined in `service.yaml`.



Service name:



mywebapp-service



Service type:



NodePort



Service port:



80



Target port:



5000



Node port:



30080



The application was accessed through the Minikube service tunnel.



\## Application Verification



The deployed application was tested using cURL.



The application returned HTTP 200 OK and the expected Version 1.0 response.



\## Self-Healing



One running Pod was deleted manually.



Kubernetes automatically created a replacement Pod, demonstrating the self-healing capability of the Deployment.



\## Scaling



The Deployment was scaled from 2 replicas to 4 replicas using:



kubectl scale deployment mywebapp-deployment --replicas=4



All 4 Pods reached the Running state successfully.



\## Rolling Update



The application was updated from:



mywebapp:1.0



to:



mywebapp:2.0



The image was updated using:



kubectl set image deployment/mywebapp-deployment mywebapp=mywebapp:2.0



The rollout completed successfully.



The application was verified through the Minikube service URL and returned:



Application deployed successfully using Docker! Version 2.0



\## Rollback



The deployment was rolled back from Version 2.0 to Version 1.0 using:



kubectl rollout undo deployment/mywebapp-deployment



The rollback completed successfully.



The Version 2.0 image was subsequently restored and verified.



\## Final Deployment



The final deployment used:



Image: mywebapp:2.0



Replicas: 4



All 4 Pods were Running and Available.



\## Cleanup



The Kubernetes Service and Deployment were deleted after completing the experiment.



The Minikube cluster was then stopped using:



minikube stop



\## Result



The containerized Flask application was successfully deployed and managed using Kubernetes. Deployment, NodePort Service, self-healing, scaling, rolling update, rollback, final verification, and resource cleanup were successfully demonstrated.

