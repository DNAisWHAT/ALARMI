from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

try:
  LOGIN_URL = "https://eais.af.ac.kr/js/jqm/login.jsp"
  ID = '23250275'
  PW = 'zxcx!!8520'
  
  START_DATE = '2023-05-28'
  END_DATE = '2023-05-29'
  
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  driver.get(LOGIN_URL)
  
  ID_BOX = driver.find_element(By.ID, "input-id")
  PW_BOX = driver.find_element(By.ID, "input-id")
  ID_BOX.send_keys(ID)
  PW_BOX.send_keys(PW)
  INPUT_BOX = driver.find_element(By.ID, "login_button")
  INPUT_BOX.click()
  
  destination = driver.find_element(By.CLASS_NAME,"ui-block-a")
  destination.click()
  application_btn = driver.find_element(By.ID,"btn_new")
  application_btn.click()
  
  start_date = driver.find_element(By.ID, "cal_inp1_act_dt")
  end_date = driver.find_element(By.ID, "cal_inp1_act_dt_end")
  start_date.send_keys(START_DATE)
  end_date.send_keys(END_DATE)
  save_btn = driver.find_element(By.ID, "btn_save")
  save_btn.click()
except:
  print("Err found.")






