from kubernetes import config, client
from kubernetes.client.rest import ApiException

import yaml
import logging

_logger = logging.getLogger(__name__)

def read_kubernetes_logs(app_name, namespace='default', label_selector='', tail_lines=None, since_seconds=None):
    try:
        # Load Kubernetes config
        config.load_kube_config()

        # Create Kubernetes API client
        api_instance = client.CoreV1Api()

        # List pods with specific label selector
        pods = api_instance.list_namespaced_pod(namespace=namespace, label_selector=label_selector).items

        # Find the pod related to the application
        for pod in pods:
            print(pod.metadata.name)
            if pod.metadata.name and (app_name + '-odoo' in pod.metadata.name):
                # Read logs from the pod
                odoo_logs = api_instance.read_namespaced_pod_log(
                    name=pod.metadata.name,
                    namespace=namespace,
                    tail_lines=tail_lines,
                    since_seconds=since_seconds
                )
                print(odoo_logs)
                return odoo_logs
        return False
    except ApiException as e:
        _logger.error("Exception when calling CoreV1Api->list_namespaced_pod: %s\n" % e)
        return False
    except Exception as e:
        _logger.error("An error occurred: %s\n" % e)
        return False
label_selector = 'app.kubernetes.io/instance=midhu,app.kubernetes.io/name=odoo'

# Example usage:
logs = read_kubernetes_logs('midhu-odoo-6777554898-jlfrn', namespace='midhu', label_selector=label_selector)
if logs:
 print(logs)
else:
 print("Failed to retrieve logs.")
