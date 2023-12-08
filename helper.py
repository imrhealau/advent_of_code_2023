import requests
import os
    
class Day():
    def __init__(self,day,solver):
        self.day = day
        self.solver = solver

    def test(self):
        print('Part 1:',self.solver(self.get_test_data(),False))
        print('Part 2:',self.solver(self.get_test_data(),True))

    def solve(self):
        print('Part 1:',self.solver(self.get_day(),False))
        print('Part 2:',self.solver(self.get_day(),True))

    def read_cookie(self):
        file_path = ".cookie"
        with open(file_path, 'r') as file:
            return file.readline()
    
    def get_day(self):
        header = {'Cookie':self.read_cookie()}
        url = f'https://adventofcode.com/2023/day/{self.day}/input'
        file_path = f'data/day_{str(self.day) if self.day > 10 else "0"+str(self.day)}'

        if not os.path.exists(file_path):
            response = requests.get(url, headers=header)
            with open(file_path, 'w') as file:
                file.write(response.text)

        with open(file_path, 'r') as file:
            return [x.strip() for x in file.readlines()]

    def get_test_data(self):
        with open('data/test', 'r') as file:
            return [x.strip() for x in file.readlines()]

