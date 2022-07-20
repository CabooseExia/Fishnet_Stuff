import pdb
import os
import csv
import pandas as pd
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

    ic_header = ['Internal Code', 'NTUC name', 'Redmart name', 'NTUC barcode', 'Redmart barcode', 'NTUC SKU', 'Redmart RPC']
    ic_body = []

    for ntuc_row in ntuc_list:
        for redmart_row in redmart_list:
            if ntuc_row[1] == redmart_row[2]:
                print(f'ntuc = {ntuc_row[1]}, redmart = {redmart_row[2]}')
                if ntuc_row[3] == redmart_row[3]:
                    ntuc_row.append('no ic problem')
                    redmart_row.append('no ic problem')
                else:
                    ntuc_row.append('ic problem') #for debugging purposes
                    redmart_row.append('ic problem')
                    ic_body.append((ntuc_row[1], ntuc_row[2], redmart_row[0], ntuc_row[3], redmart_row[3], ntuc_row[0], redmart_row[1]))

    barcode_header = ['Barcode', 'NTUC name', 'Redmart name', 'NTUC internal code', 'Redmart internal code', 'NTUC SKU', 'Redmart RPC']
    barcode_body = []

    for ntuc_row in ntuc_list:
        for redmart_row in redmart_list:
            if ntuc_row[3] == redmart_row[3]:
                print(f'ntuc = {ntuc_row[3]}, redmart = {redmart_row[3]}')
                if ntuc_row[1] == redmart_row[2]:
                    ntuc_row.append('no barcode problem')
                    redmart_row.append('no barcode problem')
                else:
                    ntuc_row.append('barcode problem') #for debugging purposes
                    redmart_row.append('barcode problem')
                    barcode_body.append((ntuc_row[3], ntuc_row[2], redmart_row[0], ntuc_row[1], redmart_row[2], ntuc_row[0], redmart_row[1]))

    ic_path = 'C://Users//User//Desktop//Ethan//Barcode_checker//Same internal code.csv'
    ic = open(ic_path, 'w', newline='')
    ic_writer = csv.writer(ic)

    barcode_path = 'C://Users//User//Desktop//Ethan//Barcode_checker//Same barcode.csv'
    barcode = open(barcode_path, 'w', newline='')
    barcode_writer = csv.writer(barcode)

    # ntuc_issue_path = 'C://Users//User//Desktop//Ethan//Barcode_checker//ntuc issues.csv'
    # ntuc_issue = open(ntuc_issue_path, 'w', newline='')
    # ntuc_issue_writer = csv.writer(ntuc_issue)

    # redmart_issue_path = 'C://Users//User//Desktop//Ethan//Barcode_checker//redmart issues.csv'
    # redmart_issue = open(redmart_issue_path, 'w', newline='')
    # redmart_issue_writer = csv.writer(redmart_issue)

    ic_writer.writerow(ic_header)
    for row in ic_body:
        ic_writer.writerow(row)
    ic.close()

    barcode_writer.writerow(barcode_header)
    for row in barcode_body:
        barcode_writer.writerow(row)
    barcode.close()

    # writer.writerow('\n')
    # writer.writerow(('ntuc unused',))
    # for item in ntuc_list:
    #     if len(item) == 6:
    #         writer.writerow(item)
    # writer.writerow('\n')
    # writer.writerow(('redmart unused',))
    # for item in redmart_list:
    #     if len(item) == 9:
    #         writer.writerow(item)
   
    Constant_vars.convert_csv_to_excel(ic_path)
    Constant_vars.convert_csv_to_excel(barcode_path)
    os.remove(ic_path)
    os.remove(barcode_path)

    ntuc_file.close()
    redmart_file.close()
    os.remove(ntuc_csv)
    os.remove(redmart_csv)
   





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