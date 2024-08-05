from kubernetes import client, config
from kubernetes.client.rest import ApiException

def get_pod_container(namespace, pod_name):
    config.load_kube_config()  # Load kube config from default location

    api_instance = client.CoreV1Api()

    try:
        # Fetch pod details
        pod = api_instance.read_namespaced_pod(name=pod_name, namespace=namespace)

        # Get the first container in the pod
        container_name = pod.spec.containers[0].name

        return container_name

    except ApiException as e:
        print("Exception when calling CoreV1Api->read_namespaced_pod: %s\n" % e)
        return None

def get_file_from_pod(namespace, pod_name, container_name, file_path):
    config.load_kube_config()  # Load kube config from default location

    api_instance = client.CoreV1Api()

    try:
        # Execute command in the pod
        exec_command = [
            '/bin/sh',
            '-c',
            'cat ' + file_path
        ]

        # Use the ApiClient for executing the command
        api_client = client.ApiClient()
        resp = api_client.call_api(
            f'/api/v1/namespaces/{namespace}/pods/{pod_name}/exec',
            'POST',
            _preload_content=False,
            namespace=namespace,
            name=pod_name,
            stdin=False,
            stdout=True,
            stderr=True,
            tty=False,
            container=container_name,
            command=exec_command
        )

        # Print the file content
        print("File Content:")
        for line in resp[0].stream():
            print(line.decode('utf-8'), end='')

    except ApiException as e:
        print("Exception when calling CoreV1Api->exec_namespaced_pod: %s\n" % e)

# Define your namespace and pod name
namespace = "pp"
pod_name = "pp-odoo-6ccb8b7b56-8nckl"

# Get the container name dynamically
container_name = get_pod_container(namespace, pod_name)

if container_name:
    # Define the file path you want to retrieve
    file_path = "/opt/bitnami/odoo/conf/odoo.conf"

    # Fetch and print the file content
    get_file_from_pod(namespace, pod_name, container_name, file_path)
else:
    print("Failed to retrieve container name.")
