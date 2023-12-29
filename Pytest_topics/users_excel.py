import openpyxl
from pathlib import Path

excel_file = "users.xlsx"
directory = "assets"
base_dir = Path(__file__).resolve().parent.parent
data_file = base_dir.joinpath(directory).joinpath(excel_file)

book = openpyxl.load_workbook(data_file)
sheet = book.active


def get_usernames():
    username_list = []
    for i in range(2, sheet.max_row + 1):
        username = sheet.cell(row=i, column=1).value
        username_list.append(username)
    return username_list


def parse_excel_to_dict(username):
    Dict1 = {}
    for i in range(2, sheet.max_row + 1):
        if sheet.cell(row=i, column=1).value == username:
            for j in range(1, sheet.max_column + 1):
                Dict1[sheet.cell(row=1, column=j).value] = sheet.cell(row=i, column=j).value
    return Dict1


selected_username = sheet['A6'].value;

print(get_usernames())
print(parse_excel_to_dict(selected_username))
