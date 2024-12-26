import os
import requests
from requests.auth import HTTPBasicAuth
import json

# Retrieve environment variables
email = os.getenv("ATLASSIAN_EMAIL")
api_token = os.getenv("ATLASSIAN_API_TOKEN")

if not email or not api_token:
    raise ValueError("Environment variables ATLASSIAN_EMAIL and ATLASSIAN_API_TOKEN must be set.")

# Define the URL
url = "https://your_domain.atlassian.net/rest/api/3/project"

# Define authentication after fetching environment variables
auth = HTTPBasicAuth(email, api_token)

# Define headers
headers = {
    "Accept": "application/json"
}

# Make the request
response = requests.request("GET", url, headers=headers, auth=auth)

# Parse and print project names
output = json.loads(response.text)
for project in output:
    name = project["name"]
    print(name)