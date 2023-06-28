import requests

token = input('What\'s your token?: ')
house = input('Which HypeSquad Badge do you want?\n[1]: Bravery\n[2]: Brilliance\n[3]: Balance\n\n> ')
try:
  house_id = int(house)
except:
  print("You must input 1, 2, or 3!")

JSON_PAYLOAD = {'house_id': house_id}
JSON_HEADERS = {'Authorization': f'{token}'}

r = requests.post('https://discordapp.com/api/v9/hypesquad/online', headers=JSON_HEADERS, json=JSON_PAYLOAD, timeout=10)
if r.status_code == 204:
  print(f"Badge successfully changed!")
else:
  print("There was an error changing your badge.")