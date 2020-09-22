import os
import pandas as pd
import openpyxl as xl

cwd = os.path.abspath('../')
files = os.listdir(cwd)


# delete first columns from the excel file
# def delete_columns(file_name, col_num):
#     wb = xl.load_workbook(file_name)
#     sheet = wb.get_sheet_by_name('Sheet1')
#     sheet.delete_cols(col_num)
#     wb.save(file_name)
#     print('deleted columns' + col_num)


# delete first rows of the excel file
# def delete_rows(file_name, amount):
#     # if file_name.endswith('.xlsx'):
#     wb = xl.load_workbook(file_name)
#     sheet = wb.get_sheet_by_name('Sheet1')
#     sheet.delete_rows(1, amount=amount)
#     wb.save(file_name)
#     print('deleted rows from ' + file_name)


# Merge the first sheet of a given files
# def merge_excel():
#     df = pd.DataFrame()
#     for file in files:
#         if file.endswith('.xlsx'):
#             df = df.append(pd.read_excel(file), ignore_index=True)
#     df.head()
#     df.to_excel('total_stat.xlsx')

# # convert excel files to csv
# read_file = pd.read_excel(r'month122018_statistic.xlsx')
# read_file.to_csv(r'new_statistic.csv', index=None, header=True)
# read_data_from_csv()
