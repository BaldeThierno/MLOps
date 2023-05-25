# Install MlRun with Docker

There are several ways to install MLRun:
+ Iguazio
+ AWS
+ GCP
+ Docker

We will focus on the Docker option because the others are not free.

## Prerequisites
+ Docker
+ Docker-Compose

```bash
export HOST_IP=<your host IP address>
export SHARED_DIR=~/mlrun-data
mkdir $SHARED_DIR -p
```
To install MLRun with Docker, run the docker-compose file in the MLRun/Infrastructure/ directory with the following command:

```bash
docker-compose -f compose-with-jupyter.yaml up -d
```

## Access to MLRun

+ http://localhost:8060/mlrun/projects
+ http://localhost:8070/projects
+ http://localhost:8888/lab?
