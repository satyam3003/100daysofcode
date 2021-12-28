import requests

USERNAME = "satyam30"
TOKEN = "**********"
pixela_post = 'https://pixe.la/v1/users'

headers = {
    "X-USER-TOKEN": TOKEN,
}

pixela_get_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_post, json=pixela_get_parameters)
# print(response.text)

graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"

graph_parameters = {
    "id": "a1",
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora",
}

# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)

graph_adding_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{graph_parameters['id']}"

graph_add_pixel = {
    "date": "20210811",
    "quantity": "2.02",
}

response = requests.post(url=graph_adding_pixel_endpoint, json=graph_add_pixel, headers=headers)
print(response.text)
