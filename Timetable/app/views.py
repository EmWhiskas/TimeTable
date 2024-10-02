from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def smena1(request):
    import os.path
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
    mas = []
    # If modifying these scopes, delete the file token.json.
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

    # The ID and range of a sample spreadsheet.
    SAMPLE_SPREADSHEET_ID = "1O75BM0QxHI2l8n5rMewLm9LABKHeAUc1eKMeEtW7gEU"
    SAMPLE_RANGE_NAME = "Смена 1 на тв!A1:S35"

    def main():
        creds = None
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "app/credentials.json", SCOPES
                )
                creds = flow.run_local_server(port=0)
            with open("token.json", "w") as token:
                token.write(creds.to_json())

        try:
            service = build("sheets", "v4", credentials=creds)

            # Call the Sheets API
            sheet = service.spreadsheets()
            result = (
                sheet.values()
                .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
                .execute()
            )
            values = result.get("values", [])

            if not values:
                print("No data found.")
                return

            for row in values:
                if row != '':
                    mas.append(row)
                else:
                    mas.append('aaaaa')
        except HttpError as err:
            print(err)

    main()
    data = {'mas': mas}
    return render(request, 'smena1.html', data)

def smena2(request):
    import os.path
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
    mas = []
    # If modifying these scopes, delete the file token.json.
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

    # The ID and range of a sample spreadsheet.
    SAMPLE_SPREADSHEET_ID = "1O75BM0QxHI2l8n5rMewLm9LABKHeAUc1eKMeEtW7gEU"
    SAMPLE_RANGE_NAME = "Смена 2 на тв!A1:W33"

    def main():
        creds = None
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "app/credentials.json", SCOPES
                )
                creds = flow.run_local_server(port=0)
            with open("token.json", "w") as token:
                token.write(creds.to_json())

        try:
            service = build("sheets", "v4", credentials=creds)

            # Call the Sheets API
            sheet = service.spreadsheets()
            result = (
                sheet.values()
                .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
                .execute()
            )
            values = result.get("values", [])

            if not values:
                print("No data found.")
                return

            for row in values:
                if row != '':
                    mas.append(row)
                else:
                    mas.append('aaaaa')
        except HttpError as err:
            print(err)

    main()
    data = {'mas': mas}
    return render(request, 'smena2.html', data)