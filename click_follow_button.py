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

    user=input("Who do you want to scrape : ")
   
    counts=int(input("how many : "))
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.get("https://www.instagram.com/")
    

    user_element=WebDriverWait(driver,timeout=10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input")))
    
    passwordelement=WebDriverWait(driver,timeout=10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')))
  
    loginbutton=driver.find_element(By.XPATH,"//button")

    USERNAME = "username"
    PASSWORD = "password"

    user_element.send_keys(USERNAME)
    passwordelement.send_keys(PASSWORD)

    loginbutton.click()

    time.sleep(10)

    driver.get(f'https://www.instagram.com/{user}/')
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, 4000)") 
    
    time.sleep(5)
    
    WebDriverWait(driver,timeout=10).until(EC.presence_of_element_located((By.XPATH,"//a[contains(@href, '/followers')]"))).click()
   
    

    time.sleep(10)
    
   

    followers_list = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='_aano']")))
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_list)
    time.sleep(2)
    for _ in range(round(counts//10)):
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_list)
        time.sleep(2)
    
    for i in range(counts):
        follow_button = WebDriverWait(followers_list, 10).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[{i+1}]/div[3]/button")))
        follow_button.click()                                                                          
   
   
  
    time.sleep(5)
   

if __name__=="__main__":
    scrape()