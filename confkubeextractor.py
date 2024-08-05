import yaml
import base64
import os

def extract_cert_and_key(config_path):
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    for user in config.get('users', []):
        user_data = user.get('user', {})
        client_cert_data = user_data.get('client-certificate-data', None)
        client_key_data = user_data.get('client-key-data', None)

        if client_cert_data and client_key_data:
            cert_path = 'client.crt'
            key_path = 'client.key'

            with open(cert_path, 'wb') as cert_file:
                cert_file.write(base64.b64decode(client_cert_data))

            with open(key_path, 'wb') as key_file:
                key_file.write(base64.b64decode(client_key_data))

            return cert_path, key_path

    return None, None

def main():
    kube_config_path = input("Enter the path to your Kubernetes config file: ")
    cert_path, key_path = extract_cert_and_key(kube_config_path)

    if cert_path and key_path:
        print(f"Certificate saved to: {os.path.abspath(cert_path)}")
        print(f"Key saved to: {os.path.abspath(key_path)}")
    else:
        print("Unable to find client certificate and key in the config file.")

if __name__ == "__main__":
    main()
