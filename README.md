# Dummy Django Kubernetes

This is just a dummy project to learn how to use Kubernetes.

Here I created this architecture:

* A redis server, this is used by django as cache and by celery as a broker
* Postgres DB, used by django as DB.
* Celery, used to executed async jobs.
* Celery beat, used to schedule task to celery.
* A web server. 

## Run using docker-compose
```
$ docker-compose up
```
Then go to `http://localhost:8080/`

# Kubernetes

## Build & push the docker image
```
$ docker build -t dockerusername/dockerrepo .
$ docker push dockerusername/dockerrepo:latest
```

## Deploy
```
# Create the credentiasl
$ kubectl create secret generic app-secrets --from-env-file=.secrests.env
# If there are some creadentiaslc reated run this
$ kubectl delete secret app-secrets 
# Run the kubernetes infraestructure
$ kubectl apply -f kuberntes/.
# To veryfy
$ kubectl get all
```

## Secreats
```
$ cp kubernetes/.secrets.env.example kubernetes/.secrets.env
$ kubectl create secret generic app-secrets --from-env-file=kubernetes/.secrests.env
```

# Minikube easy commands
```
$ minikube start
$ minikube dashboard

$ minikube service --url <service-name>

$ kubectl port-forward <app-name> port:port

```