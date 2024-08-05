import requests
import time

def check_webpage(endpoint):
    start_time = time.time()
    while time.time() - start_time < 180:  # Run for 3 minutes
        try:
            response = requests.get(endpoint)
            if response.status_code == 503:
                print("503 Service Temporarily Unavailable. Retrying...")
            elif response.status_code == 200:
                print("Website is accessible.")
                return {"status": "pass"}
            else:
                print(f"Unexpected status code: {response.status_code}. Retrying...")
            time.sleep(5)  # Wait for 5 seconds before retrying
        except requests.RequestException as e:
            print(f"Error: {str(e)}. Retrying...")
            time.sleep(5)  # Wait for 5 seconds before retrying
    print("Timeout reached. Website is not accessible.")
    return {"status": "fail"}

# Example usage:
endpoint = 'http://bbb.cyllo.cloud'
result = check_webpage(endpoint)
print(result)

