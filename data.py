import requests

parameters={
    "amount":10,
    "type": "boolean",
    "category": 14,
}

response=requests.get(url="https://opentdb.com/api.php",params=parameters)
data=response.json()
question_data=data["results"]