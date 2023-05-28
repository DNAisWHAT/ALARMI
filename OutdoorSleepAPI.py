import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

def Login(ID, PW, SD, ED)
  LOGIN_URL = "https://eais.af.ac.kr/js/jqm/login.jsp"
  # ID = '23250275'
  # PW = 'zxcx!!8520'
  # SD = '2023-05-30'
  # ED = '2023-06-01'
  
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  driver.get(LOGIN_URL)
  
  ID_BOX = driver.find_element(By.ID, "input-id")
  PW_BOX = driver.find_element(By.ID, "input-pw")
  ID_BOX.send_keys(ID)
  PW_BOX.send_keys(PW)
  INPUT_BOX = driver.find_element(By.ID, "login_button")
  INPUT_BOX.click()
  time.sleep(0.1)
  driver.get(
    "https://eais.af.ac.kr/js/jqm/DM/DM0406H01.jsp?appl_no=2023-00660&status=I")
  
  #destination = driver.find_element(By.CLASS_NAME,"ui-block-a")
  #destination.click()
  
  #time.sleep(1)
  
  # application_btn = driver.find_element(By.XPATH,'//*[@id="btn_new"]')
  # application_btn.click()
  
  #time.sleep(0.5)
  
  # start_date = driver.find_element(By.ID, "cal_inp1_act_dt")
  # driver.find_element(By.XPATH, '//*[@id="cal_inp1_act_dt"]//div/div/div[1]').send_keys('2023')
  # driver.find_element(By.XPATH, '//*[@id="cal_inp1_act_dt"]//div/div/div[3]').send_keys('05')
  # driver.find_element(By.XPATH, '//*[@id="cal_inp1_act_dt"]//div/div/div[5]').send_keys('29')
  
  # driver.find_element(By.XPATH, '//*[@id="cal_inp1_act_dt_end"]//div/div/div[1]').send_keys('2023')
  # driver.find_element(By.XPATH, '//*[@id="cal_inp1_act_dt_end"]//div/div/div[3]').send_keys('05')
  # driver.find_element(By.XPATH, '//*[@id="cal_inp1_act_dt_end"]//div/div/div[5]').send_keys('30')
  time.sleep(0.2)
  # end_date = driver.find_element(By.ID, "cal_inp1_act_dt_end")
  driver.execute_script(
    "document.getElementById('cal_inp1_act_dt').value = '{0}'".format(SD))
  driver.execute_script(
    "document.getElementById('cal_inp1_act_dt_end').value = '{0}'".format(ED))
  
  # start_date.send_keys(START_DATE)
  # end_date.send_keys(END_DATE)
  
  reason_box = driver.find_element(By.ID, "txt_inp1_act_rsn")
  reason_box.send_keys("TEST")
  
  save_btn = driver.find_element(By.ID, "btn_save")
  save_btn.click()
  time.sleep(0.1)
  # keyboard.press('enter')
  # save_btn.send_keys("ENTER")
  da = Alert(driver)
  # da.accept()
  time.sleep(0.1) # 필수 
  da.accept()
  da.accept()
  # save_btn.send_keys("ENTER")
  # keyboard.press('enter')
  
