import os
import pandas as pd
import openpyxl as xl

from src.DB import db

cwd = os.path.abspath('')
files = os.listdir(cwd)


# convert excel to csv
def convert_excel_to_csv(xl_file_name, csv_file_name):
    read_file = pd.read_excel(xl_file_name)
    read_file.to_csv(csv_file_name, index=True, header=True)


# delete first columns from the excel file
def delete_columns(file_name, col_num):
    wb = xl.load_workbook(file_name)
    sheet = wb.get_sheet_by_name('Sheet1')
    sheet.delete_cols(col_num)
    wb.save(file_name)
    print('deleted columns' + col_num)


# delete first rows of the excel file
def delete_rows(file_name, amount):
    # if file_name.endswith('.xlsx'):
    wb = xl.load_workbook(file_name)
    sheet = wb.get_sheet_by_name('Sheet1')
    sheet.delete_rows(1, amount=amount)
    wb.save(file_name)
    print('deleted rows from ' + file_name)


# Merge the first sheet of a given files
def merge_excel():
    df = pd.DataFrame()
    for file in files:
        if file.endswith('.xlsx'):
            df = df.append(pd.read_excel(file), ignore_index=True)
    df.head()
    df.to_excel('total_stat.xlsx')


# update new excel
def update_excel():
    df = pd.DataFrame()
    for file in files:
        if file.endswith('.xlsx'):
            delete_rows(file, 9)
            convert_excel_to_csv(file, 'new_file.csv')  # TODO fix convert_excel_to_csv


# df = pd.DataFrame()
# # delete_columns('02.2018.xlsx', 2)
# delete_columns('01.2018.xlsx', 7)
# delete_columns('01.2018.xlsx', 7)
# # df.to_excel('new_01.2018.xlsx')
# df = pd.read_excel('02.2018.xlsx')
# print(df.head(15))


# make changes in the csv so the json will be good
# df = pd.DataFrame()
# df = pd.read_csv('new_month_statistic.csv')
# # df.drop(['Unnamed: 2', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 11', 'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 23', 'Unnamed: 27', "מס' זיהוי",'שם'], axis=1, inplace=True)
# df.drop(['Unnamed: 0', 'Unnamed: 10', 'Unnamed: 16'], axis=1, inplace=True)
# df.to_csv('new_month_statistic.csv', index=False)
# df = pd.read_csv('new_month_statistic.csv')
# # print(df.head(2))


# convert excel files to csv
# convert_excel_to_csv(r'01.2018.xlsx', r'month012018_statistic.csv')
