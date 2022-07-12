import pdb
import os
import csv
import pandas as pd
import Constant_vars
from datetime import datetime

input_path = 'C://Users//User//Desktop//Data_analytics//Madsoft_sales'
files_to_go_through = []
csv_files = []

def sorter(path):
    files = os.listdir(path)

    header_buffer = 1
    for file in files: #this creates a copy of the excel file but as a csv
        if file.endswith('xls'):
            name = os.path.splitext(file)[0]
            temp = f'{path}//{name}.csv'
            read_excel = pd.read_excel(f'{path}//{file}')
            read_excel.to_csv(temp, index=None)
            files_to_go_through.append(temp)
    
    if not files_to_go_through:
        print('No files')
        return
            
    data_type = input('Order by Stock code(1) or Quantity sold(2) : ')

    for file in files_to_go_through: # goes through each file and creates a sorted csv, aka smth_report.csv
        data = []
        data_by_kg = []
        data_row = []
        current_row = 0
        with open(file, 'r') as csv_file:
            csv_file = csv.reader(csv_file)
            for row in csv_file:
                current_row += 1
                if header_buffer == 1: #to create header
                    header = ["Stock code", "Name"] + row[3:]
                    header_buffer = 0
                    continue
            
                if "STOCK CODE" in row[1]: #this is to get the code and name of the product
                    code = row[1].split(":")[1].removeprefix(" ")
                    data_row.append(code)
                    try:
                        data_row.append(Constant_vars.Madsoft_dict[code]) #finds the name in the dict
                    except:
                        data_row.append("The code here in inconsistant with 'storebest stocks' google sheets") #can't find the name

                elif row[1] == '' and row[2] == '': # only need the row with the final data of the month
                    data_row += [float(x.replace(",",'')) for x in row[3:]] #this adds the data for the month to the name of the month
                    if len(data_row) == 2 + len(row[3:]): # This is to deal with the last row as it does not have a code or name
                        if data_row[0] not in Constant_vars.by_kg:
                            data.append(data_row)
                        else:
                            data_by_kg.append(data_row)
                        data_row = []
                    else:
                        continue

        while True:
            if data_type == '1':
                sorted_data = sorted(data, key = lambda x: x[0], reverse=False)
                sorted_data_by_kg = sorted(data_by_kg, key = lambda x: x[0], reverse=False)
                output_file = f'{os.path.dirname(file)}//Output//{os.path.splitext(os.path.basename(file))[0]}_by_stockcode_report.csv' #this is for Hazlan
                break
            elif data_type == '2':
                sorted_data = sorted(data, key = lambda x: x[-1], reverse=True)
                sorted_data_by_kg = sorted(data_by_kg, key = lambda x: x[-1], reverse=True)
                output_file = f'{os.path.dirname(file)}//Output//{os.path.splitext(os.path.basename(file))[0]}_by_sold_report.csv' #this is for weekly(?) reports
                break
            elif data_type == 'ethan': #this is now a hidden feature :)
                sorted_data = sorted(data, key = lambda x: x[-1], reverse=True)
                sorted_data_by_kg = sorted(data_by_kg, key = lambda x: x[0], reverse=True)
                output_file = f'{os.path.dirname(file)}//Output//{os.path.splitext(os.path.basename(file))[0]}_PowerBi_report.csv' #this is for Ethan... though i dont think this was needed...
                break
            else:
                print('Try again, I know its hard to press "1" or "2". You can do it')
                data_type = input('"1" for Stock code, "2" for Quantity sold')
            
        output = open(output_file, 'w', newline = '')
        writer = csv.writer(output)
     
        writer.writerow(header)
        for row in sorted_data:
            writer.writerow(row)
        if data_by_kg:
            if data_type != '3':
                writer.writerow('\n')
                writer.writerow(["By weight",])
                writer.writerow(header)
            for row in sorted_data_by_kg:
                writer.writerow(row)
        csv_files.append(output_file)

        print(f'Done with {output_file}')
        
        os.remove(file)


def combine(): #for foodpanda bulk for now. need to combine 3 reports
    global csv_files
    csv_delete = csv_files.copy()
    
    food_dict = {}
    food_dict_by_kg = {}
    header_buffer = 1
    for item in csv_files: # opens each file one by one to get all the data
        with open(item, 'r') as file:
            file = csv.reader(file)
            for row in file:
                if header_buffer == 1: #to get header. should only use the first file to get it
                    header = row ### header may need to be updated. (rank, header, average)
                    header_buffer = 0
                    continue

                if row[-1] == 'TOTAL' or row[0] == '\n' or row[0] == 'By weight': #to ignore the next few headers for the remianing files and the space between by ea and weight
                    continue
                
                if row[0] not in Constant_vars.by_kg:
                    if (row[0], row[1]) in food_dict: #checks if item in in the dict
                        prev = food_dict[(row[0], row[1])]
                        new = row[2:]
                        total = []
                        for i in range(len(new)):
                            total.append(prev[i] + float(new[i])) #vector adding baby. numpy didnt work
                        food_dict[(row[0], row[1])] = total
                    else:
                        food_dict[(row[0], row[1])] = [float(x) for x in row[2:]]

                else:
                    if (row[0], row[1]) in food_dict_by_kg: #checks if item in in the dict
                        prev = food_dict_by_kg[(row[0], row[1])]
                        new = row[2:]
                        total = []
                        for i in range(len(new)):
                            total.append(prev[i] + float(new[i])) #vector adding baby. numpy didnt work
                        food_dict_by_kg[(row[0], row[1])] = total
                    else:
                        food_dict_by_kg[(row[0], row[1])] = [float(x) for x in row[2:]]

                    
    data = tuple(food_dict.items())
    sorted_data = sorted(data, key = lambda x: x[1][-1], reverse=True)
    data_by_kg = tuple(food_dict_by_kg.items())
    sorted_data_by_kg = sorted(data_by_kg, key = lambda x: x[1][-1], reverse=True)

    file_name = f'{input_path}//output//Pandamart_report_{datetime.today().strftime("%d-%m-%Y")}.csv' #so it would give a diff file name for diff days, easier to collate over time
    output = open(file_name,'w', newline='')
    writer = csv.writer(output)

    # This helps make the csv, if we want to re-order the file it is here
    writer.writerow(header)
    for row in sorted_data:
        writer.writerow(list(row[0]) + list(row[1]))
    if data_by_kg: #does not print if it does not exist
        writer.writerow('\n')
        writer.writerow(["By weight",])
        writer.writerow(header)
        for row in sorted_data_by_kg:
            writer.writerow(list(row[0]) + list(row[1]))
    csv_files.append(file_name)

    for i in csv_delete:
        csv_files.remove(i)
        os.remove(i)
        print(f"Deleted {os.path.basename(i)}")    
    print(f'Doned Pandamart {file_name}')
    

if __name__ == '__main__':

    sorter(input_path) #main sorter
    if files_to_go_through:

        while True: #purely for pandamart rn...
            pandamart = input("Combine for pandamart? y/n : ")
            if pandamart == "y" or pandamart == "Y":
                combine()
                break
            elif pandamart == "n" or pandamart == "N":
                print('ok can')
                break
            else:
                print('ding dong wrong input, y or n...')

        for file in csv_files: #to clean up csv files made
            read_file = pd.read_csv(file)
            read_file.to_excel(f'{os.path.splitext(file)[0]}.xlsx', index=None, header=True)
            os.remove(file)

            print(f'Converted {os.path.basename(file)} to an excel file')
            


