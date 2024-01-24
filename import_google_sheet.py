import pandas as pd

def convert_google_sheet_to_xlsx(url,sheet_name):
    """
    This function created based on this code:
    https://gist.github.com/ivansaul/28257e793ae9b8575bb5c0f1b3906dad

    Args:
        url (string): the original Google Sheet Url

    Returns:
        A xlsx file from the google sheet
    """
    #Challenge URL: https://docs.google.com/spreadsheets/d/1m94pt5eNXwKS2uzFNsEODeNd8a8JPY42vJ53yks6gh0/edit#gid=0

    #get spreadsheets key from url
    gsheetkey = url.split("/")[-2]

    export_url=f'https://docs.google.com/spreadsheet/ccc?key={gsheetkey}&output=xlsx'
    df = pd.read_excel(export_url,sheet_name=sheet_name)
    return df