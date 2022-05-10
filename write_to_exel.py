def write_to_exel(body):
    from oauth2client.service_account import ServiceAccountCredentials
    import gspread
    scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
    ]
    credentials = ServiceAccountCredentials.from_json_keyfile_name("just.json", scopes) #access the json key you downloaded earlier 
    file = gspread.authorize(credentials) # authenticate the JSON key with gspread
    sheet = file.open("just")  #open sheet
    wk_sheet = sheet.worksheet(body[-1])
    i = 1
    while True:
        val = wk_sheet.acell(f'A{i}').value
        if val != None:
            i += 1
        else:
            break
    sheet.values_update(
                    f'{body[-1]}!A{i}',
                    params={
                        'valueInputOption': 'USER_ENTERED'
                    },
                    body={
                        'values': [body[:-1]]
                    }
                )


if '__main__' == __name__:
    write_to_exel(['Элдияр', 'Три в одном', '15', '2022-5-10 9:50', 'Цех 6'])