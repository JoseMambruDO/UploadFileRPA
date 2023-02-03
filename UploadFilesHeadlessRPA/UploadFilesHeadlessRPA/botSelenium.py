import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from time import sleep

options = webdriver.ChromeOptions() 
options.add_argument('--headless')
options.add_argument("start-maximized")
options.add_argument("--disable-gpu")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\dadtech\Downloads\chromedriver_win32\chromedriver.exe")

driver.get('http://127.0.0.1:5000/upload')
sleep(5)

for i in range(1,10):

    txt_name = f"Name::Field {i}"
    txt_last_name = f"Last Name::Field {i}"
    txt_file= f"C:\\tmp\\somefiles\\file{i}.txt"
    
    name= driver.find_element(By.ID, ("name"))
    sleep(1)
    name.send_keys(txt_name)

    last_name= driver.find_element(By.ID, ("last_name"))
    sleep(1)
    last_name.send_keys(txt_last_name)

    file=driver.find_element_by_xpath('//input[@type="file"]')
    sleep(1)
    file.send_keys(txt_file)

    submit = driver.find_element_by_xpath('/html/body/form/p[7]/input')
    sleep(1)
    submit.click()