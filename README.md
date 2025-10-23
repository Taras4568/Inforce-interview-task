# Inforce-interview-task

# How to start aplication:

1) Using docker-compose:
docker-compose up --build -d

2) Using minikube cluster:
docker build -t myflaskapi:latest ./api

minikube start

kubectl apply -f k8s/namespace.yaml

kubectl apply -f k8s/postgres-configmap.yaml
kubectl apply -f k8s/postgres-secret.yaml

kubectl apply -f k8s/postgres-statefulset.yaml

kubectl apply -f k8s/api-deployment.yaml
kubectl apply -f k8s/api-service.yaml

kubectl apply -f k8s/ingress.yaml
kubectl apply -f k8s/hpa.yaml

kubectl get all -n myapp

# API endpoints:

/health(get): body=none   response: {"status": "ok"} (200)

/users(post): body={"name": "John Doe"} response:{"id": 1, "name": "John Doe"} (201)

/users(get): body=none response: [{"id": 1, "name": "John Doe"}, ...] (200)

# API was tested using Postman 