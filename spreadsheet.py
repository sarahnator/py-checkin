import myfitnesspal as pal
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

def update_row(dict):
    #TODO make update work with dictionary values
    #TODO test single entry --> mutltiple entries
    #TODO increment input range
    #TODO logic based on day of week? su = 40, mo = 41, tu = 42, etc?

    # break dictionary into list of values
    val_list = [*[list(idx.values()) for idx in dict]]
    #                       [day 1]                                               [day 2]                                [day 3]
    #func: [['123.3', '05-18', 2347, 153, 301, 65, 62], ['123.2', '05-19', 2324, 154, 298, 63, 63], ['123.4', '05-20', 2316, 152, 295, 63, 67]]

    print("func: " + str(val_list))

def update_col(dict):
    #func: [['122.5', '123.3', '123.2', '123.4'], --> weight
    # ['05-17', '05-18', '05-19', '05-20'],  --> date
    # [2321, 2347, 2324, 2316], --> cals
    # [298, 301, 298, 295], --> pro
    # [63, 65, 63, 63], --> fat
    # [154, 153, 154, 152], --> pro
    # [62, 62, 63, 67]] --> fiber
    val_list = [list(col) for col in zip(*[d.values() for d in dict])]
    print("func: " + str(val_list))
    update_weights(val_list, 0)

# TODO variable number of args?
def update_weights(val_list, num):
    # weight cells: B40:B46
    # num = day of week data starts
    rng = str('B' + str(40 + num) + ':B' + str(40 + len(val_list[0]) - 1))
    print(rng)
    cell_range = sheet.range(rng)
    for i, cell in enumerate(cell_range):
        cell.value = val_list[0][i]
        print("cell val: " + str(cell.value))
    sheet.update_cells(cell_range)

def update_dates(val_list, num):
    pass

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('../json/client_secret.json', scope)
client = gspread.authorize(creds)

# extract json information @sheetName
with open('../json/creds.json') as src:
    data = json.load(src)

# Find workbook by name and open the first sheet
sheet = client.open(data['sheetName']).sheet1

# sheet.batch_update([{
#     #update weight, date
#     'range': 'B40:C40',
#     'values': [['800', '0/2']],
# }, {
#     #update mfp cals, protein, carbs, fat
#     'range': 'E40:I40',
#     'values': [['a', 'b', 'c', 'd', 'e']],
# }])


