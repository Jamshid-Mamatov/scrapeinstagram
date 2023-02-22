import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape():

    # user=input("Who do you want to scrape : ")
    # counts=int(input("how many : "))
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # options=Options()
    # # options.add_argument("--headless")

    # driver=webdriver.Chrome(options=options)
    driver.get("https://www.instagram.com/")
    

    user_element=WebDriverWait(driver,timeout=10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input")))
    
    passwordelement=WebDriverWait(driver,timeout=10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')))
  
    loginbutton=driver.find_element(By.XPATH,"//button")

    USERNAME = "olimjon_sn"
    PASSWORD = "Olimjon200228"

    user_element.send_keys(USERNAME)
    passwordelement.send_keys(PASSWORD)

    loginbutton.click()

    time.sleep(10)



if __name__=="__main__":
    scrape()