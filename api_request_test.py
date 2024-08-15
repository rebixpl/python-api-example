import requests

# base_url = "http://localhost:5000/uppercase"

# # this works too
# # base_url = "http://localhost:5000/uppercase?text=hello world"

# params = {"text": "hello world"}

# response = requests.get(base_url, params=params)

# print(response.json())  # {'text': 'HELLO WORLD'}

# print(response.status_code)  # 200 Success


# Testing endpoint 2
base_url = "http://localhost:5000/process_text"

params = {
    "text": "suck my avocado ",
    "duplication_factor": 13,
    "capitalization": "UPPER",
}

response = requests.get(base_url, params=params)

print(response.json())  # {'processed_text': 'SUCK MY AVOCA...'}
