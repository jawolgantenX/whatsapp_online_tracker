#Importing packages
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time

#Install Driver
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome('chromedriver.exe',chrome_options=chrome_options)

#Specify Search URL
search_url="https://whatsapptools.net/check-online-status"

driver.get(search_url)

contryCode = driver.find_element_by_class_name('form-control')
time.sleep(5)
select = Select(contryCode)
select.select_by_visible_text("COUNTRY_CODE_AS_MENTIONED_IN_README")

number = driver.find_element_by_css_selector("input[type='text']")
number.click()
no = "WHATSAPP_NUMBER_YOU_WANT_TRACK"
number.send_keys(no)
button = driver.find_element_by_class_name('btn')

while(1):
    time.sleep(10)
    driver.execute_script("arguments[0].click();", button)
    time.sleep(5)
    alert = driver.find_element_by_class_name('alert')
    # Append-adds at last
    file1 = open("result_"+no+".txt" , "a")  # append mode
    file1.write(no+" -  "+alert.text+"\n")
    file1.close()
