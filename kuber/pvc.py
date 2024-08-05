import os
from kubernetes import client, config

def read_odoo_conf(namespace, pvc_name):
    # Load kubeconfig
    config.load_kube_config()

    # Create API client
    api_instance = client.CoreV1Api()

    try:
        # Get the PVC
        pvc = api_instance.read_namespaced_persistent_volume_claim(pvc_name, namespace)
        
        # Get the volume name from the PVC
        volume_name = pvc.spec.volume_name

        # Get the PV using the volume name
        pv = api_instance.read_persistent_volume(volume_name)
        
        # Extract hostPath from PV
        host_path = None
        if pv.spec.host_path:
            host_path = pv.spec.host_path.path
        
        # Check if hostPath is available
        if host_path:
            odoo_conf_path = os.path.join(host_path, "conf", "odoo.conf")
            if os.path.exists(odoo_conf_path):
                with open(odoo_conf_path, "r") as odoo_conf_file:
                    odoo_conf_text = odoo_conf_file.read()
                return odoo_conf_text
            else:
                return "odoo.conf not found in the specified path: {}".format(odoo_conf_path)
        else:
            return "HostPath not found for PVC '{}'.".format(pvc_name)

    except Exception as e:
        return "Error: {}".format(e)

# Set your namespace and PVC name
namespace = "pp"
pvc_name = "pp-odoo"

# Read odoo.conf from the hostPath associated with the PVC
odoo_conf_text = read_odoo_conf(namespace, pvc_name)

print(odoo_conf_text)
