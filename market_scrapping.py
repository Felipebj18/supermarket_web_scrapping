from time import sleep
from selenium import webdriver
import pandas as pd
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


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


#ean=convert_google_sheet_to_xlsx("https://docs.google.com/spreadsheets/d/1m94pt5eNXwKS2uzFNsEODeNd8a8JPY42vJ53yks6gh0/edit#gid=0","Sheet1")

driver = webdriver.Chrome()

driver.get("https://mercadomadrid.com.co/?sede=1")
sleep(10)

menu_categorias = driver.find_elements(By.CLASS_NAME,"lname-cat-12")

print_names=lambda t:print(t.text)

map(print_names,menu_categorias)

#categorias = driver.find_elements(By.XPATH,'//li[class="root-item menu_item_children"]')
sleep(2)
# for categoria in categorias:
#     print(categoria.text)
sleep(10)




# sleep(10)
# WebDriverWait(driver,5).until(
#     (expected_conditions.presence_of_element_located,
#      By.XPATH,"//span[@class=cross][@]"))
# cerrar=driver.find_element(By.,"iqit-close-popup")

# cerrar.click()

# sleep(100)



# tx=lambda t:t.text

# precios=map(tx,precios)

# print(precios)

# sleep(3)


