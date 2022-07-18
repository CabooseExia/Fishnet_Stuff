import pdb
import os
import csv
import Constant_vars

def the_func(path_to_ntuc_file, path_to_remart_file):
    ntuc_csv = Constant_vars.convert_excel_to_csv(path_to_ntuc_file)
    redmart_csv = Constant_vars.convert_excel_to_csv(path_to_remart_file)

    ntuc_file = open(ntuc_csv, 'r')
    redmart_file = open(redmart_csv)
    ntuc_readfile = csv.reader(ntuc_file) #the readers are trash wtf
    redmart_readfile = csv.reader(redmart_file)

    ntuc_list = []
    for row in ntuc_readfile:
        ntuc_list.append(row)
    redmart_list = []
    for row in redmart_readfile:
        redmart_list.append(row)

    output_header = ['Internal Code', 'NTUC name', 'Redmart name', 'NTUC barcode', 'Redmart barcode', 'NTUC SKU', 'Redmart RPC']
    output_body = []

    for ntuc_row in ntuc_list:
        for redmart_row in redmart_list:
            if ntuc_row[1] == redmart_row[2]:
                print(f'ntuc = {ntuc_row[1]}, redmart = {redmart_row[2]}')
                if ntuc_row[3] == redmart_row[3]:
                    ntuc_row.append('no problem')
                    redmart_row.append('no problem')
                else:
                    ntuc_row.append('problem') #for debugging purposes
                    redmart_row.append('problem')
                    output_body.append(ntuc_row[1], ntuc_row[2], redmart_row[0], ntuc_row[3], redmart_row[3], ntuc_row[0], redmart_row[1])

    
                



    # for ntuc_row in ntuc_readfile: 
    #     pdb.set_trace()
    #     for redmart_row in redmart_readfile:
    #         print(f'ntuc = {ntuc_row[1]}, redmart = {redmart_row[2]}')
    #         if ntuc_row[1] == redmart_row[2]:
    #             print("yes")

    

    ntuc_file.close()
    redmart_file.close()



if __name__ == '__main__':

    ntuc_path = 'C://Users//User//Desktop//Ethan//Barcode_checker//Ntuc'
    redmart_path = 'C://Users//User//Desktop//Ethan//Barcode_checker//Redmart'

    ntuc_files = os.listdir(ntuc_path)
    redmart_files = os.listdir(redmart_path)


    if len(ntuc_files) == 1 and len(redmart_files) == 1:
        the_func(f'{ntuc_path}//{ntuc_files[0]}', f'{redmart_path}//{redmart_files[0]}')

    else:
        for i in ntuc_files:
            if i.endswith('csv'):
                os.remove(f'{ntuc_path}//{i}')
        for i in redmart_files:
            if i.endswith('csv'):
                os.remove(f'{redmart_path}//{i}')