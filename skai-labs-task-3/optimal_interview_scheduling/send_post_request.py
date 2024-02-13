import requests
import json

# Define the URL of the endpoint
url = 'http://localhost:8000/api/calculate_max_interviews/'

# Define the JSON data to send in the POST request
data = {
    "start_times": [10, 20, 30, 40, 50, 60],
    "end_times": [15, 25, 35, 45, 55, 65]
}

print(data)
# Convert the data to JSON format
json_data = json.dumps(data)

# Define the headers for the request and send it as POST request
headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=json_data, headers=headers)

# Print the response
print(f'\nResponse: {response.json()}')
