import csv
import os
import pdb

input_path = 'C://Users//User//Desktop//Data_analytics//RedMart'

def sort(path):
    files = os.listdir(path)
    header_buffer = 1
    data = {}
    for file in files:
        if file.endswith('csv'):
            raw = open(f'{input_path}//{file}','r')
            raw = csv.reader(raw)
            for row in raw:
                if header_buffer == 1:
                    header = ([row[7], row[5], row[9]])
                    header_buffer = 0
                    continue
                if data == {} or (row[7], row[5]) not in data:  
                    data[row[7], row[5]] = int(row[9])
                else: 
                    data[row[7], row[5]] += int(row[9])

            data = tuple(data.items())
    
            sorted_data = sorted(data, key = lambda x: x[1], reverse=True)
            output = open(f'{input_path}//output//RedMart_report.csv','w', newline='')
            writer = csv.writer(output)

            writer.writerow(header)
            for row in sorted_data:
                writer.writerow((row[0][0], row[0][1], row[1]))
            
            print(f'sorted {file}')

sort(input_path)
