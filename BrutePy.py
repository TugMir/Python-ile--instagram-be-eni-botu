# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium import webdriver

browser = webdriver.Firefox()

browser.get('https://www.instagram.com/')
time.sleep(2)

username = browser.find_element("xpath", "//*[@id='loginForm']/div/div[1]/div/label/input")
username.send_keys("İnstagram Kullanıcı Ado")
password = browser.find_element("xpath", "//*[@id='loginForm']/div/div[2]/div/label/input")
password.send_keys("İnstagram Şifre")
giris = browser.find_element("xpath", "//*[@id='loginForm']/div/div[3]")
giris.click()
time.sleep(5)
#bilgi_kaydetme = browser.find_elements(By.CLASS_NAME, "sqdOP")
browser.find_elements(By.TAG_NAME, "button")[0].click()
time.sleep(3)
var2 = browser.find_element("xpath","/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]")
var3 = browser.find_element("xpath","/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]")
var3.click()
browser.get("Gitmek İstediğiniz profil")
time.sleep(2)
fotosec=browser.find_element("xpath","/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/div[3]/article/div/div/div[1]/div[1]")
fotosec.click()
time.sleep(5)
fotobegen=browser.find_element("xpath","/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button")
fotobegen.click()
time.sleep(5)




