from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



driver = webdriver.Chrome(executable_path='./chromedriver')



driver.get('https://front.dev.ibt.ru/')
#time.sleep(5) лучше так не делать)) Лучше делать после каждого клика

# переход к авторизации
logo_authorization = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/div/div/button')
time.sleep(2)
logo_authorization.click()

time.sleep(2)
#Переход на вкладку "Войти"
button_authorization = driver.find_element_by_xpath('//*[@id="v-tab-1"]/span')
button_authorization.click()

time.sleep(2)
#Ввод номера телефона
input_autorization_phone = driver.find_element_by_class_name('v-input__input')
input_autorization_phone.send_keys('999 999-99-60')

time.sleep(2)
#Ввод пароля
input_autorization_password = driver.find_element_by_class_name('v-password__input')
input_autorization_password.send_keys('123456Root')

time.sleep(2)
#Нажать на кнопку "Войти"
button_come = driver.find_element_by_xpath('//*[@id="v-tab--panel1"]/div/form/div[3]/button[1]')
button_come.click()

time.sleep(2)
#Проверка авторизации. Переход в личку
check_user = driver.find_element_by_xpath('//*[@id="app"]/main/section/section[1]/div/div[1]/a[2]/div/picture/img')
check_user.click()

time.sleep(2)
citi_selection = driver.find_element_by_xpath('//*[@id="app"]/header/div[4]/div/div/button[1]')
citi_selection.click()

time.sleep(2)
#Поиск товара
search = driver.find_element_by_id('upper-filter')
search.click()
time.sleep(1)
search.send_keys('Щетка круглая тон 13 73 мм')
time.sleep(2)
search.send_keys(Keys.ENTER)
time.sleep(2)



#Щетка круглая тон 13 73 мм

#prompt = driver.switch_to.alert
#prompt.send_keys('dev')
#time.sleep(5)

#prompt.send_keys(Keys.TAB)
#time.sleep(5)

#prompt.send_keys('12344')


#input_login = driver.find_element_by_name('search_query')
#input_login.send_keys('fasd1111111111')
#input_login.send_keys(Keys.RETURN)

#time.sleep(5)

#input_login.send_keys('777bem')

#alert.send_keys(Keys.ENTER)
