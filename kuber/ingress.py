from kubernetes import client, config
from kubernetes.client.rest import ApiException

# Load Kubernetes configuration from default location
config.load_kube_config()

# Create Kubernetes API client
v1 = client.CoreV1Api()

def get_service_info(service_name):
    try:
        # Retrieve service details
        service = v1.read_namespaced_service(name=service_name, namespace="default")

        # Print information about the service
        print("Service Name:", service.metadata.name)
        print("Namespace:", service.metadata.namespace)
        print("Type:", service.spec.type)
        print("Cluster IP:", service.spec.cluster_ip)
        print("Ports:")
        for port in service.spec.ports:
            print(f"\tName: {port.name}, Protocol: {port.protocol}, Port: {port.port}, Target Port: {port.target_port}")
    except ApiException as e:
        print("Exception when calling CoreV1Api->read_namespaced_service:", e)

# Replace 'your_service_name' with the name of the service you want to retrieve data for
get_service_info("chummi-odoo")
