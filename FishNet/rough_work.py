import pdb
import os
import csv
from numpy import double
import pandas as pd
import pyperclip

path = 'C://Users//User//Desktop//food_dict.xlsx'

def main(): # to help me copy pasta constant vars dict
    copy_pasta = {}
    temp = f'{path[:-4]}csv'
    read_file = pd.read_excel(path)
    read_file.to_csv(temp,index=None)
    with open(temp, 'r') as rly:
        maybe = csv.reader(rly)
        for row in maybe:
            copy_pasta[row[0]] = row[1]
    print(copy_pasta)
    pyperclip.copy(str(copy_pasta))
    os.remove(temp)

# main()

def double_loop():
    for i in range(5):
        for j in range(6):
            if i == j:
                print(f'{i},{j}')

double_loop()