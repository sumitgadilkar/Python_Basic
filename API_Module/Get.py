import requests

response = requests.get("https://reqres.in/api/users?page=2")
code = requests.status_code
assert code==200 , "Reponse doesn't match"

