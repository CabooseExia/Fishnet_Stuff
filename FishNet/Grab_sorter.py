import os
import pdb
import csv

input_path = 'C://Users//User//Desktop//Data_analytics//Grab'

def sort(path):
    files = os.listdir(path)
    header_buffer = 1
    data = []
    for file in files:
        if file.endswith('csv'):
            raw = open(f'{input_path}//{file}','r')
            raw = csv.reader(raw)
            for row in raw:
                if header_buffer == 1:
                    header = ([row[5], row[6], row[7]])
                    header_buffer = 0
                    continue
                data.append(([row[5], row[6], row[7]]))
    
            sorted_data = sorted(data, key = lambda x: x[1], reverse=True)
            output = open(f'{input_path}//output//Grab_report.csv','w', newline='')
            writer = csv.writer(output)

            writer.writerow(header)
            for row in sorted_data:
                writer.writerow(row)
            
            print(f'sorted {file}')

sort(input_path)