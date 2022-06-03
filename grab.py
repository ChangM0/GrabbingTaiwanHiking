from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome("/Users/m0chang/Downloads/chromedriver")

url = "https://npm.cpami.gov.tw/apply_1_2.aspx?unit=e6dd4652-2d37-4346-8f5d-6e538353e0c2"
driver.get(url)

driver.find_element(By.ID, "chk[]0").click()
driver.find_element(By.ID, "chk[]2").click()
driver.find_element(By.ID, "chk[]10").click()
driver.find_element(By.ID, "chk[]11").click()
driver.find_element(By.ID, "chk[]12").click()
driver.find_element(By.ID, "chk[]").click()




agree_btn = driver.find_element(By.ID, "ContentPlaceHolder1_btnagree")
agree_btn.click()


# switch to second window
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)




driver.close()
