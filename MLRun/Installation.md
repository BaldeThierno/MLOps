MLRun Installation
MlRun kann über mehrere Wege istalliert werden
    MLRun direkt auf dem lokalen Rechner installieren
    MLRun mit Minikube installieren
    Installation auf Google Cloud Plattform Kubernetes

Prerequities
um MLRun zu installieren werden folgende Tools benötigt:
    docker
    gcloud SDK installieren
    Helm installieren
    kubectl

MLRun direkt auf dem lokalen Rechner installieren
folgende env_vars müssen vorher erstellt werden
    set HOST_IP=<your host IP address>
    set SHARED_DIR=c:\mlrun-data
    mkdir %SHARED_DIR%
<your host IP address> kann mit dem Command ipconfig gefunden werden.
Die docker-compose Datei kann hier heruntergeladen werden, und gestartet werden:
    docker-compose -f <docker-compose-file-name> up -d




Installation auf Google Cloud Plattform K8s

    HTTP-Load-Balancing aktivieren
    externe HTTP(S) Load-Balancer erstellen
    Domain Name bei einem anbieter kaufen
    Domain Name direkt auf die IP Adresse der externe Load-balancer einstellen
