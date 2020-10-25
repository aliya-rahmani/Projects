import pandas

excel_data_df = pandas.read_excel('records.xlsx', sheet_name='Employees')

# print whole sheet data
print(excel_data_df)