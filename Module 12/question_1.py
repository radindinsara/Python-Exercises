import requests

def get_chuck_norris_joke():
    try:
        response = requests.get("https://api.chucknorris.io/jokes/random")
        if response.status_code == 200:
            data = response.json()
            print(data["value"])
        else:
            print("Error: Failed to fetch joke.")
    except Exception as e:
        print("Error:", e)

get_chuck_norris_joke()
