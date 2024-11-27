from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class FormFiller:
    def __init__(self ,form_url):
        self.driver = webdriver.Chrome()
        self.form_url = form_url
        self.spreadsheet_url = "https://docs.google.com/spreadsheets/d/1K_fzk55QuAqnkHWWJvFauBRKzDn-8eOWFltyJaZ6x7E/edit?usp=sharing"



    def fill_form(self, price, address, link):
        try:
            self.driver.get(self.form_url)
            time.sleep(2)
            price_field = self.driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")  
            address_field = self.driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input") 
            link_field = self.driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input") 
            submit_button = self.driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span/span")  
            
            # Fill in the form
            price_field.clear()
            price_field.send_keys(price)
            address_field.clear()
            address_field.send_keys(address)
            link_field.clear()
            link_field.send_keys(link)
            
            submit_button.click()
            
            
            time.sleep(2) 
        except Exception as e:
            print(f"Error filling the form: {e}")

    def fill_multiple_forms(self ,listings):
         
         for property_id , details in listings.items() :
            price = details["price"]
            address = details["address"]
            link =details["link"]
            self.fill_form(price ,address , link)

    def open_spreadsheet(self):
        
        try:
            print("Opening the Google Spreadsheet to view responses.")
            self.driver.get(self.spreadsheet_url)
            time.sleep(5) 
        except Exception as e:
            print(f"Error opening spreadsheet: {e}")
        
    def close_driver(self):
        self.driver.quit()
        