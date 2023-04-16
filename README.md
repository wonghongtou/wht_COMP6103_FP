# G2-faas

## Architecture
PlaceHolder

## Install components of `G2-faas`

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

### Simple command
Inside the folder `function creation\script`, there are 5 scripts availabe for managing lifecycle of function, following the steps.

1. First, edit `00-config.json`, to provide all nessesary configuration details of the simple function
   - `FunctionName`- Name of the function
   - `Image` - not nessesary to change for this type of function
   - `ExecutionArgs` - which requires a list of string arrays, to represent the command that will be executed in the container.
2. Once the configuration is completed on `00-config.json`, run `python 01-build.py` to package all nessesary files into a new folder with a same name as the `FunctionName`
3. Excecute `python 02-deploy.py`, this script responds to deploy the function package into the K8S cluser that has pre-installed the FaaS platform `G2-faas`.
4. `03-delete.py` and `04-getfunc.py` cooresponds the delete and get operations, to delete the function according to the configuration file or get all function installed in the cluster respectively.

### Self develop python script (Build image)

For some more sophiscate scenario, we need to run our own code as a function, this step will guide you how to build your own image and deploy it as a function on the `G2-faas` platform.

1. Prepare your own code and the dependency requirement file, and save them into a folder `func`, the folder structure could reference `function creation\self-image\get-weather`, and should be same as the following.
   ```
    YourCodeFolder/
    ├─ func/
    │  ├─ requirements.txt
    │  ├─ YourCode.py
    ├─ Dockerfile
   ```
2. Prepare the `Dockerfile` as following
    ```dockerfile
    FROM wonghongtou/forkingdog:latest
    COPY ./func/ ./app/func/
    RUN pip install -r ./app/func/requirements.txt
    ENV ARGS '["python", "./app/func/YourCode.py"]'
    ```
3. build and deploy the docker image.
   ```shell
   docker image build -t yourrepo/forkingdog-yourfuction:0.1 . --no-cache
   docker push yourrepo/forkingdog-yourfunction:0.1
   ```
4. do the steps same as [simple-command](#simple-command), but configure the `00-config.json` as following
    ```json
    {
        "FunctionName": "YourFunction",
        "Image": "yourrepo/forkingdog-yourfunction:0.1",
        "ExecutionArgs": ["python", "./app/func/YourCode.py"]
    }
    ```