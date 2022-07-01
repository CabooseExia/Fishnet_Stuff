import pdb
import csv
import os
import pandas as pd
import Constant_vars

###   paths and such   ###
main_path = 'C://Users//User//Desktop//Data_analytics//Madsoft_stock//data//main'
months_path = "C://Users//User//Desktop//Data_analytics//Madsoft_stock//data//months"
###   i hope it works   ###

to_delete = []

def convert_excel_to_csv(excel_file):
    output_file_name = f'{os.path.splitext(excel_file)[0]}.csv'
    read_file = pd.read_excel(excel_file)
    read_file.to_csv(output_file_name, index=None)
    to_delete.append(output_file_name)
    print(f'converted {os.path.basename(excel_file)} to a csv_file')

def mass_insert_function_here(input_path,  function): 
    files = os.listdir(input_path)

    if function == cleaner: #lol this is trash
        file_type = '.csv'
    else:
        file_type = '.xls'
    
    for file in files:
        if file.endswith(file_type):
            function(f'{input_path}//{file}') #lol this is so poorly implemented... 

def cleaner(csv_file):
    file_path = os.path.splitext(csv_file)[0]

    with open(csv_file, 'r') as csv_read:
        csv_read = csv.reader(csv_read)
        header_buffer = 1
        data = []
        data_by_kg = []
        for row in csv_read:
        
            if header_buffer == 1: # creates header
                header = [row[0], row[1], row[4]]
                header_by_kg = [row[0], row[1], "Weight (kg)"]
                header_buffer = 0
                continue

            if row[1] == '': # to ignore last row
                continue
            
            if row[0] in Constant_vars.by_kg: # sorts data to 2 well names (ur welcome) lists
                data_by_kg.append((row[0], row[1], float(row[4].replace(',',''))))
            else:
                data.append((row[0], row[1], float(row[4].replace(',',''))))


            
        output = open(f'{file_path}.csv', 'w', newline="")
        writer = csv.writer(output)
        sorted_data = sorted(data, key = lambda x: x[2], reverse=True)
        sorted_data_by_kg = sorted(data_by_kg, key = lambda x: x[2], reverse=True)

        writer.writerow(header) # writing to the new csv
        for row in sorted_data:
            writer.writerow(row)
        writer.writerow("\n")
        writer.writerow(header_by_kg)
        for row in sorted_data_by_kg:
            writer.writerow(row)
        output.close()

        print(f"Cleaned {os.path.basename(file_path)}.csv")

def combiner(path_to_main, path_to_months):
    master_file_names = os.listdir(path_to_main)
    for i in master_file_names:
        if i.endswith(".csv"):
            master_name = i
    master_csv = f'{path_to_main}//{master_name}'
    output_path = os.path.splitext(f'{path_to_main[:-10]}output//{master_name}')[0]
    with open(master_csv,'r') as main:
        main = csv.reader(main)
        months_with_data = os.listdir(path_to_months)
        output = open(f"{output_path}_overall_report.csv",'w', newline='')
        writer = csv.writer(output)
        main_dict = {}
        main_dict_by_kg = {}
        counter = 0
        header_buffer = 1
        
        for row in main:
            row = tuple(row)
            if header_buffer == 1:
                header = list(row)
                header_buffer = 0
                continue

            if row == ('\n',):
                continue


            if row[2] == "Weight (kg)":
                header_in_kg = list(row)
                continue

                
            if row[0] in Constant_vars.by_kg:
                main_dict_by_kg[row] = []
            else:
                main_dict[row] = []
        
        for month in reversed(Constant_vars.months): #for all files
            if f'{month}.csv' in months_with_data:
                counter += 1
                header.insert(2, month)
                header_in_kg.insert(2, month)

                for item in main_dict:
                    month_csv = open(f'{path_to_months}//{month}.csv')
                    month_csv = csv.reader(month_csv)
                    for slave_row in month_csv:
                        if slave_row[0] == item[0]:
                            main_dict[item].insert(0, slave_row[2][:-1])
                            break

                for item in main_dict:
                    if len(main_dict[item]) < counter:
                        main_dict[item].insert(0,0.0)
                
                for item in main_dict_by_kg:
                    month_csv = open(f'{path_to_months}//{month}.csv')
                    month_csv = csv.reader(month_csv)
                    for slave_row in month_csv:
                        if slave_row[0] == item[0]:
                            main_dict_by_kg[item].insert(0, slave_row[2][:-1])
                            break

                for item in main_dict_by_kg:
                    if len(main_dict_by_kg[item]) < counter:
                        main_dict_by_kg[item].insert(0,0.0)
        
        writer.writerow(header)

        data = tuple(main_dict.items())
        for item in data:
            writer.writerow([item[0][0], item[0][1]] + item[1] + [item[0][2]])
        
        writer.writerow("\n")

        writer.writerow(header_in_kg)

        data_by_kg = tuple(main_dict_by_kg.items())
        for item in data_by_kg:
            writer.writerow([item[0][0], item[0][1]] + item[1] + [item[0][2]])
        
    print('combined, why did this take so long')

def main_func():
    master_file_name = os.listdir(main_path) #should have 1 item
    master_file_path = f'{main_path}//{master_file_name[0]}'

    convert_excel_to_csv(master_file_path)
    mass_insert_function_here(months_path, convert_excel_to_csv)
    cleaner(f'{os.path.splitext(master_file_path)[0]}.csv')
    mass_insert_function_here(months_path,cleaner)
    combiner(main_path, months_path)

    for i in to_delete:
        print(f'Deleted {i}')
        os.remove(i)


    print("This took me way too long")


main_func()