import os
from selenium import webdriver
from selenium.webdriver.common.by import By

cwd = os.getcwd()
path = os.path.join(cwd, "chromedriver.exe")

username = "Your_Username"
password = "Your_Password"
exp = [
    "169623",
    "168234",
    "168236",
    "190218",
]

def grind():
    driver = webdriver.Chrome(path)
    driver.get('https://elok.ugm.ac.id/')
    
    driver.find_element(By.CLASS_NAME,'link-sso').click()
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.NAME,"submit").click()
    driver.find_element(By.ID, "expandable_branch_20_7316").click()
    
    for n in exp :
        driver.get("https://elok.ugm.ac.id/mod/page/view.php?id=" + n)
    driver.quit()
    
i = 0
while i < 20 :
    i = i + 1
    grind()
    
