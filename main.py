import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
def scrape():

    # user=input("Who do you want to scrape : ")
    # user='dostiyorov__m'
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

    time.sleep(2)

    driver.get(f'https://www.instagram.com/{"cristiano"}/')
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 4000)") 
    
    time.sleep(3)
    
    elements=driver.find_elements(By.XPATH,'//ul/li')
    
    for i in elements[0:3]:
        print(i.text)
 

    time.sleep(2)
        
    driver.quit()
    

if __name__=="__main__":
    scrape()