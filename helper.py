import requests
import os

def read_cookie():
    file_path = ".cookie"
    with open(file_path, 'r') as file:
        return file.readline()
    
def get_day(day):
    header = {'Cookie':read_cookie()}
    url = f'https://adventofcode.com/2023/day/{day}/input'
    file_path = f'data/day_{str(day) if day > 10 else "0"+str(day)}'

    if not os.path.exists(file_path):
        response = requests.get(url, headers=header)
        with open(file_path, 'w') as file:
            file.write(response.text)

    with open(file_path, 'r') as file:
        return [x.strip() for x in file.readlines()]

def get_test_data():
    with open('data/test', 'r') as file:
        return [x.strip() for x in file.readlines()]