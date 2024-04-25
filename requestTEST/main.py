import requests
def mget_request(url):
    response = requests.get(url)

    if response.status_code == 200:
        print("GET request was successful!")
        print("Response Content:")
        print(response.json())
    else:
        print(f"GET request failed with status code: {response.status_code}")
def make_post_request(url, data):
    response = requests.post(url, json=data)

    if response.status_code == 201:
        print("POST request was successful!")
        print("Response Content:")
        print(response.json())
    else:
        print(f"POST request failed with status code: {response.status_code}")



get_url = "https://jsonplaceholder.typicode.com/todos"
post_url = "https://jsonplaceholder.typicode.com/todos"

# Test data for POST
post_data = {
    "userId": 1,
    "title": "Buy groceries",
    "completed": False
}

print("Making GET request...")
mget_request(get_url)
print("Making POST request...")
make_post_request(post_url, post_data)
