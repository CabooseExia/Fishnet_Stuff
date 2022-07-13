import csv
import os
import pandas as pd
import pdb
import Constant_vars

main_path = 'C://Users//User//Desktop//Data_analytics//Top_few' #not useful anymore, integrated into Madsoft_stock.py

# def convert_excel_to_csv(excel_file):
#     output_file_name = f'{os.path.splitext(excel_file)[0]}.csv'
#     read_file = pd.read_excel(excel_file)
#     read_file.to_csv(output_file_name, index=None)
#     print(f'converted {os.path.basename(excel_file)} to a csv_file')

# def top_few(excel, top_number):
#     file_path = os.path.dirname(excel)
#     file_name = os.path.basename(excel)
#     csv_path = f'{file_path}//{file_name[:-5]}.csv'
#     convert_excel_to_csv(excel)

    data = []
    with open(csv_path,'r',) as csv_file:
        csv_file = csv.reader(csv_file)
        header_buffer = 1
        for row in csv_file:
            if header_buffer == 1:
                header = (row[0],row[1], row[4])
                header_buffer = 0
                continue
            if row[0] in Constant_vars.internal_code_list and row[0] not in Constant_vars.by_kg:
                data.append((row[0],row[1], float(row[4])))
        
        sorted_data = sorted(data, key = lambda x: x[2], reverse = True)

    output = open(f'{file_path}//output//{file_name[:-5]}_report.csv','w', newline='')
    writer = csv.writer(output)

    writer.writerow(header)
    for rows in range(int(top_number)):
        writer.writerow(sorted_data[rows])
    
    os.remove(csv_path)
    print(f'Done calculating top {top_number}')


def main_func():
    number = input("Top how many? : ")
    files = os.listdir(main_path)
    for i in files:
        if i.endswith('.xls') or i.endswith('.xlsx'):
            top_few(f'{main_path}//{i}', number)
    
    print('yay')

main_func()