# wht_COMP6103_FP

## Install components

```shell
# Create namespace 
kubectl create ns g2-faas # for core componets
kubectl create ns function # for functions

# install ingress-controller
kubectl apply -f component_manifest/nginx_ingress.yaml

# install prometheus
kubectl apply --kustomize component_manifest/prometheus

# install grafana
kubectl apply --kustomize component_manifest/grafana
```

### Config grafana dashboard
- Open your browser and visit the following URL: http://{node IP address}:{grafana-svc-nodeport} to load the Grafana Dashboard.

> The username and password is `admin`

- After the login you can import the Grafana dashboard from official dashboards, by following steps given below :

  - Navigate to lefthand panel of grafana
Hover on the gearwheel icon for Configuration and click "Data Sources"
  - Click "Add data source"
  - Select "Prometheus"
Enter the details (note: I used http://CLUSTER_IP_PROMETHEUS_SVC:9090)
Left menu (hover over +) -> Dashboard
Click "Import"
Enter the copy pasted json from https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/grafana/dashboards/nginx.json
Click Import JSON
Select the Prometheus data source
Click "Import"


## Create functions (with examples)

### 
