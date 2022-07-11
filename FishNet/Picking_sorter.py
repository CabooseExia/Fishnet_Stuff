import os
import csv
import pandas as pd
import Constant_vars
from datetime import datetime

main_dir = 'C://Users//User//Desktop//Ethan//Picking_sorter'

def convert_excel_to_csv(excel_file):
    read_file = pd.read_excel(excel_file)
    temp = f'{os.path.splitext(excel_file)[0]}.csv'
    read_file.to_csv(temp, index= 0)
    return temp

def convert_csv_to_excel(csv_file): #for output
    read_file = pd.read_csv(csv_file)
    temp = f'{os.path.dirname(csv_file)}//Output//{os.path.basename(csv_file)[:-4]}.xlsx'
    read_file.to_excel(temp, index= 0)
    return temp

def sorter(csv_path, code_column):

    header_buffer = 1
    data = []

    with open(csv_path, 'r') as csv_file:
        csv_file = csv.reader(csv_file)
        for row in csv_file:

            if header_buffer == 1:
                header = row
                header_buffer = 0
                continue

            data.append(row)

    sorted_data = []
    where_did_you_come_from = [] #where did you go

    for freezer in Constant_vars.For_picking:
        sorted_data.append([freezer],)
        for item in Constant_vars.For_picking[freezer]:
            for row in data:
                if row[code_column].replace('"', '') == item:
                    sorted_data.append(row.copy())
                    row.append('used')
                    break
        sorted_data.append(['\n'],)

    for row in data:
        if row[-1] != 'used':
            where_did_you_come_from.append(row) 
     
    output_path = f'{os.path.splitext(csv_path)[0]}_out.csv'
    output = open(output_path, 'w', newline='')
    writer = csv.writer(output)
    writer.writerow(header)
    for row in sorted_data:
        writer.writerow(row)

    writer.writerow(('Loose items',))
    for row in where_did_you_come_from:
        writer.writerow(row)
    output.close()

    return output_path


def prepare_for_redmart(csv_path):
    
    with open(csv_path, 'r') as csv_file:
        csv_file = csv.reader(csv_file)
        header_buffer = 1

        rm_dict = {}

        for row in csv_file:
            if header_buffer == 1:
                header = row
                del header[7]
                header_buffer = 0
                continue

            key = tuple(row[0:3] + row[4:7] + row[8:])
            
            if key not in rm_dict:
                rm_dict[key] = int(row[3])
            else:
                rm_dict[key] += int(row[3])

    output_path = f'{os.path.dirname(csv_path)}//Redmart_{datetime.today().strftime("%d-%m-%Y")}.csv'
    output = open(output_path,'w', newline='')
    writer = csv.writer(output)

    writer.writerow(header)
    for item in rm_dict.items():
        writer.writerow(item[0][0:3] + (item[1],) + item[0][3:])

    output.close()
    return output_path

    


def main():
    to_delete = []
    files = os.listdir(main_dir)
    while True:
        outlet = input('ntuc or rm? : ')
        if outlet == 'ntuc':
            column_code = 0
            break
        elif outlet == 'rm':
            column_code = 6
            break
        else:
            print('Try again')
        
        

    for file in files:
        if file.endswith('.xlsx'):
            csv_in = convert_excel_to_csv(f'{main_dir}//{file}')
            to_delete.append(csv_in)
            if outlet == "rm":
                csv_in = prepare_for_redmart(csv_in)
                to_delete.append(csv_in)
            csv_out = sorter(csv_in, column_code)
            to_delete.append(csv_out)
            convert_csv_to_excel(csv_out)
    
    for i in to_delete:
        os.remove(i)

    print('Done')

main()