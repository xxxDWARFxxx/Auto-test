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
time.sleep(6)


open_product = driver.find_element_by_css_selector('#app > main > section > section > div > div.catalog-view__main > div.catalog-product-list.catalog-view__main-grid > ul > a.catalog-product-list-card.catalog-product-list__item.catalog-product-list__item--order-1 > div > div.catalog-product-list-card__img > div > button.btn.btn--outline.catalog-product-list-card__controls-btn')
open_product.click()
time.sleep(4)

continue_shopping = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[1]/div[2]/button')
continue_shopping.click()
time.sleep(2)

search.click()
time.sleep(1)
search.send_keys('Щетка круглая цвет №15 74 мм')
time.sleep(2)
search.send_keys(Keys.ENTER)
time.sleep(6)

# открываем второй товар
open_product_2 = driver.find_element_by_css_selector('#app > main > section > section > div > div.catalog-view__main > div.catalog-product-list.catalog-view__main-grid > ul > a.catalog-product-list-card.catalog-product-list__item.catalog-product-list__item--order-1 > div > div.catalog-product-list-card__img > div > button.btn.btn--outline.catalog-product-list-card__controls-btn')
open_product_2.click()

time.sleep(4)
continue_shopping_2 = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[1]/div[2]/button')
continue_shopping_2.click()

time.sleep(2)
basket = driver.find_element_by_xpath('//*[@id="app"]/header/div[2]/div/div[3]/div[2]/div/div/button/span')
basket.click()

time.sleep(3)
checkout_button = driver.find_element_by_xpath('//*[@id="app"]/main/section/section[1]/div/div[2]/div/div/button')
checkout_button.click()

time.sleep(16)
gift_certificate_button = driver.find_element_by_xpath('//*[@id="app"]/main/section/section/div/div[1]/div/div[5]/div[2]/div[1]/div/label/h3')
gift_certificate_button.click()

time.sleep(10)
change_gift_certificate = driver.find_element_by_xpath('//*[@id="app"]/main/section/section/div/div[1]/div/div[5]/div[2]/div[2]/div/div/button')
change_gift_certificate.click()

time.sleep(4)
change_gift_certificate_input = driver.find_element_by_id('v-input-id-1648')
change_gift_certificate_input.send_keys(Keys.BACKSPACE)
change_gift_certificate_input.send_keys(Keys.BACKSPACE)
change_gift_certificate_input.send_keys(Keys.BACKSPACE)
change_gift_certificate_input.send_keys(Keys.BACKSPACE)
change_gift_certificate_input.send_keys(Keys.BACKSPACE)
change_gift_certificate_input.send_keys('159')

time.sleep(2)
change_gift_certificate_button = driver.find_element_by_xpath('//*[@id="app"]/main/section/section/div/div[1]/div/div[5]/div[2]/div[2]/button')
change_gift_certificate_button.click()

time.sleep(17)
go_payment = driver.find_element_by_xpath('//*[@id="app"]/main/section/section/div/div[2]/div/div/button')
go_payment.click()

time.sleep(21)
card_number = driver.find_element_by_id('cardNumber')
card_number.send_keys('4111 1111 1111 1111')

time.sleep(2)
card_number_date = driver.find_element_by_name('skr_month')
card_number_date.send_keys('12')

time.sleep(2)
card_number_date2 = driver.find_element_by_name('skr_year')
card_number_date2.send_keys('23')

time.sleep(2)
card_number_cvc = driver.find_element_by_name('skr_cardCvc')
card_number_cvc.send_keys('123')

time.sleep(2)
card_number_button_pay = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[2]/div[3]/div/div/div[1]/div[3]/div/div/div[1]/button/span')
card_number_button_pay.click()


time.sleep(6)
back_store = driver.find_element_by_xpath('/html/body/div[1]/div/a')
back_store.click()

time.sleep(7)
back_orders = driver.find_element_by_xpath('//*[@id="app"]/main/section/div[3]/div/div/div/div[2]/div/div/a')
back_orders.click()


#Добавление товара - нажать купить
#buy_button = driver.find_element_by_xpath('//*[@id="app"]/main/section/section/div/div[2]/div[2]/ul/a[1]/div/div[1]/div/button[1]')
#time.sleep(2)
#buy_button.click()


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
