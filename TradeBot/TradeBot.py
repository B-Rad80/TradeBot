import json
import requests
import os


def Get_API_Key(path = "../../Alpha_API.key"):
    f = open(path, "r")
    API_KEY = str(f.read())

    if "\n" in API_KEY:
           API_KEY = API_KEY[:-1]

    return API_KEY

if __name__ == "__main__":
    key = Get_API_Key()
    print(key, "is the API key!")