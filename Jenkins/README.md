# Install Jenkins with Docker

It is possible to install Jenkins in a number of different ways:

* Directly on your Windows/Mac/Linux machine; this option seems simpler, but it is quite resource-intensive and may prevent your machine from working normally.
- On a virtual machine
+ Directly with Docker, and in this case we will use the Docker in Docker technology to run our different jobs in image containers of our choice.

## Prerequisites
+ Docker
+ Docker-Compose

At the following link ([https://docs.docker.com/get-docker]) you can download and install Docker for the respective system.

Use your operating system's package manager to install Docker on Mac/Linux. 

```bash
brew install docker  # Mac
yum install docker # RHEL
apt-get install docker # Ubuntu
```

## Create Network and volumes
Open the Terminal and run the following commands to create the network and volumes 

```bash
docker network create jenkins
docker volume create jenkins-data
docker volume create jenkins-docker-certs
```

## Build Jenkins Docker Image
in the MLOps/Jenkins directory, run the following command
```bash
docker build -t jenkinsci . 
```
## Jenkins Launch
Jenkins needs to be able to run the various jobs in Docker containers, but Jenkins itself runs in a container, so we need to use Docker in Docker, and to do that Jenkins needs to access the host machine's Docker daemon. 
```bash
docker container run --name jenkins-docker \
  --detach --restart unless-stopped \
  --privileged \
  --network jenkins --network-alias docker \ 
  --env DOCKER_TLS_CERTDIR="/certs" \
  --volume jenkins-docker-certs:/certs/client \
  --volume jenkins-data:/var/jenkins_home \
  docker:dind
```
Launch Jenkins
```bash
docker container run --name jenkins-blueocean \
  --detach --restart unless-stopped \
  --network jenkins \
  --env DOCKER_HOST="tcp://docker:2376" \
  --env DOCKER_CERT_PATH=/certs/client \
  --env DOCKER_TLS_VERIFY=1 \
  --volume jenkins-docker-certs:/certs/client:ro \
  --volume jenkins-data:/var/jenkins_home \
  --publish 8081:8080 --publish 50000:50000 \
  jenkinsci
```
## Configuration
To access Jenkins, the admin password is stored in the container and can be retrieved with the following command:
```bash
cat /var/jenkins_home/secrets/initialAdminPassword
```
# DockerCloud Configuration
## Prerequisites
+ Docker Plugin

Installs the Docker plugin from the Jenkins UI.

Under Jenkins Manage -> Manage Nodes, select Configure Cloud-> Add New Cloud in the Cloud Details pane.
+ DockerHost URI= tcp://docker:2376
+ Select add new Server Credentials

For Credential Type, select X.509 client certificate.
Information about the client key, client certificate, and server CA certificate can be obtained using the following commands from the host:
```bash
docker exec jenkins-docker cat /certs/client/key.pem
docker exec jenkins-docker cat /certs/client/cert.pem
docker exec jenkins-docker cat /certs/server/ca.pem
```
Then test the connection, if you get the docker version in response, then Jenkins is ready.

[MIT](https://choosealicense.com/licenses/mit/)