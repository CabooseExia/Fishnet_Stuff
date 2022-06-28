import csv
import os
import pdb

input_path = 'C://Users//User//Desktop//Data_analytics//Amazon'

# def convert_str_to_tpl(string): #helps convert strings to tuples
#     li = tuple(string.split(','))
#     return li

# def find_no_sale(file):
#     with open(file, 'r') as csv_file:
#         output = open(output_csv, 'w', newline="")
#         writer = csv.writer(output)
#         header_buffer = 1
#         food_dict = {}

#         for row in csv_file: 
#             row = convert_str_to_tpl(row)
#             new_row = []

#             for item in row: # to remove some extra quotation marks
#                 new_row.append(item.strip('\"'))
 
#             if header_buffer == 1:
#                 header = [new_row[5], new_row[6], "Cartons that did not sell (quantity requested - accepted quantity)"]
#                 header_buffer = 0
#                 continue

#             ###   The following is to deal with the extra commas in the name of the products   ###
#             if len(row) == 19: # No extra comma

#                 if food_dict == {} or (row[5], row[6]) not in food_dict:  
#                     food_dict[new_row[5], new_row[6]] = int(new_row[13]) - int(new_row[14])
#                 else: 
#                     food_dict[new_row[5], new_row[6]] += int(new_row[13]) - int(new_row[14])

#             elif len(row) == 20: # one extra comma

#                 if food_dict == {} or (row[5], row[6] + "," + row[7]) not in food_dict:  
#                     food_dict[row[5], row[6] + "," + row[7]] = int(new_row[14]) - int(new_row[15])
#                 else: 
#                     food_dict[row[5], row[6] + "," + row[7]] += int(new_row[14]) - int(new_row[15])
            
#             else: #to specifically deal with salmon 3 pc with 2 extra commas

#                 if food_dict == {} or (row[5], row[6] + "," + row[7] + "," + row[8]) not in food_dict:  
#                     food_dict[row[5], row[6] + "," + row[7] + "," + row[8]] = int(new_row[15]) - int(new_row[16])
#                 else: 
#                     food_dict[row[5], row[6] + "," + row[7] + "," + row[8]] += int(new_row[15]) - int(new_row[16])

#     #turning the food dictionary to a list and sorting it
#     data = tuple(food_dict.items())
#     sorted_data = sorted(data, key = lambda x : x[1], reverse=True)
    
#     # to write to a new csv
#     writer.writerow(header)
#     for row in sorted_data:
#         writer.writerow((row[0][0], row[0][1], row[1]))

#     print("Amazon Donzo")

#     output.close()


def sort(path):
    files = os.listdir(path)
    header_buffer = 1
    data = []
    for file in files:
        if file.endswith('csv'):
            raw = open(f'{input_path}//{file}','r')
            raw = csv.reader(raw)
            next(raw,None)
            for row in raw:

                if header_buffer == 1:
                    header = ([row[0], row[1], row[5]])
                    header_buffer = 0
                    continue
                data.append(([row[0], row[1], int(row[5].replace(',',''))]))
    
            sorted_data = sorted(data, key = lambda x: x[2], reverse=True)
            file_name = os.path.splitext(file)[0]
            output = open(f'{input_path}//output//{file_name}_report.csv','w', newline='')
            writer = csv.writer(output)

            writer.writerow(header)
            for row in sorted_data:
                writer.writerow(row)
            
            print(f'sorted {file}')
            
sort(input_path)