import requests

# Replace these values with your actual API credentials and email account details
API_KEY = 'your_api_key'
API_SECRET = 'your_api_secret'
DOMAIN = 'your_domain.com'
EMAIL = 'email_address@your_domain.com'
PASSWORD = 'email_password'

# Endpoint for creating an email account
url = f'https://api.godaddy.com/v1/domains/{DOMAIN}/emails'

headers = {
    'Authorization': f'sso-key {API_KEY}:{API_SECRET}',
    'Content-Type': 'application/json'
}

data = {
    'email': EMAIL,
    'password': PASSWORD,
    'storage': 5  # Example storage limit in GB
}

# Send POST request to create the email account
response = requests.post(url, headers=headers, json=data)

if response.status_code == 201:
    print('Email account created successfully.')
else:
    print(f'Error creating email account: {response.text}')
