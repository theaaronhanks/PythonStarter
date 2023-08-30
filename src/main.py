from greeting import getGreeting
import urllib3
import json

def main():
    print(getGreeting())
    print()
    print("You should... ")
    resp = urllib3.request("GET", "https://www.boredapi.com/api/activity")
    data = json.loads(resp.data.decode("utf-8"))
    print(data["activity"] + " today!")

if __name__ == '__main__':
    main()