import pdb
import os
import csv
import pandas as pd
from datetime import datetime
import Constant_vars

idc = 'C://Users//User//Desktop//Ethan//20220726_purchaseOrderDetail_133894_133903_20220726124118.xlsx'

if __name__ == '__main__':
    to_delete = []

    idc_csv = Constant_vars.convert_excel_to_csv(idc)
    to_delete.append(idc_csv)

    with open(idc_csv, 'r') as main_csv:
        main_csv = csv.reader(main_csv)

        header_buffer = 1

        for row in main_csv:
            if header_buffer == 1:
                header = [row[19], row[18]]
                continue
                pdb.set_trace()
            
            if row[20] != row[21] or row[20] != row[22] or row[21] != row[22]:
                pdb.set_trace()
            
               

