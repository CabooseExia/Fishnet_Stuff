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
for_top_few = ''
final_path = ''

# def convert_excel_to_csv(excel_file):
#     output_file_name = f'{os.path.splitext(excel_file)[0]}.csv'
#     read_file = pd.read_excel(excel_file)
#     read_file.to_csv(output_file_name, index=None)
#     to_delete.append(output_file_name)
#     print(f'converted {os.path.basename(excel_file)} to a csv_file')

def mass_insert_function_here(input_path,  function): 
    files = os.listdir(input_path)

    if function == cleaner: #lol this is trash
        file_type = '.csv'
    else:
        file_type = '.xls'
        for file in files:
            file_path = os.path.splitext(f'{input_path}//{file}')[0]
            to_delete.append(f'{file_path}.csv')
    
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
    global for_top_few
    global final_path
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

    for_top_few = f"{output_path}_overall_report.csv"
    final_path = f"{output_path}_overall_report.csv"

    print('combined, why did this take so long')


def top_few(csv_file, top_number):
    global final_path
 
    data = []
    with open(csv_file,'r',) as csv_file:
        csv_file = csv.reader(csv_file)
        header_buffer = 1
        for row in csv_file:
            if header_buffer == 1:
                header = row
                header_buffer = 0
                continue
            if row[0] in Constant_vars.internal_code_list and row[0] not in Constant_vars.by_kg:
                monthly_output = list(float(x) for x in row[2:])
                data.append((row[0:2]) + monthly_output)
        sorted_data = sorted(data, key = lambda x: int(x[-1]), reverse = True)

    output = open(for_top_few, 'w', newline='')
    writer = csv.writer(output)

    writer.writerow(header)
    for rows in range(int(top_number)):
        writer.writerow(sorted_data[rows])
    

    final_path = for_top_few
    print(f'Done calculating top {top_number}')

if __name__ == "__main__":
    master_file_name = os.listdir(main_path) #should have 1 item
    master_file_path = f'{main_path}//{master_file_name[0]}'

    to_delete.append(Constant_vars.convert_excel_to_csv(master_file_path))
    mass_insert_function_here(months_path, Constant_vars.convert_excel_to_csv)
    cleaner(f'{os.path.splitext(master_file_path)[0]}.csv')
    mass_insert_function_here(months_path,cleaner)
    combiner(main_path, months_path)

    for i in to_delete:
        print(f'Deleted {i}')
        os.remove(i)
    
    while True:
        calc_top_few = input("Do you want the top few? y/n : ")
        if calc_top_few == 'y' or calc_top_few == 'Y':
            number = input("Top how many? : ")
            try:
                top_few(for_top_few, int(number))
                break
            except:
                print('That is not a number... try again')
                continue
        elif calc_top_few == 'n' or calc_top_few == 'N':
            print('ok can')
            break
        else:
            print('ding dong wrong input, y or n...')
        
    read_file = pd.read_csv(final_path)
    read_file.to_excel(f'{os.path.splitext(final_path)[0]}.xlsx', index=None, header=True)
    os.remove(final_path)
    print(f'Converted {os.path.basename(final_path)} to excel')




    print("This took me way too long")


