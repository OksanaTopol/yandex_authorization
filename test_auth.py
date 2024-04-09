from selenium.webdriver import Chrome, ChromeOptions, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def test_auth():
    url = "https://360.yandex.ru/disk/"
    browser_options = ChromeOptions()
    browser_options.headless = True
    user_name = "unknown503@yandex.ru"
    password = "123Password!!!!"

    driver = Chrome(options=browser_options)
    driver.maximize_window()
    driver.get(url)

    driver.implicitly_wait(5000)
    # When - user clicks on the 'Войти' button
    driver.find_element(By.ID, "header-login-button").click()
    # When - user inserts login
    driver.find_element(By.ID,"passp-field-login").send_keys(user_name)
    # When - user click son the 'Продолжить' button
    driver.find_element(By.ID, "passp:sign-in").click()
    # When - user inserts password
    driver.find_element(By.ID, "passp-field-passwd").send_keys(password)
    # When - user clicks on the 'Продолжить' button
    driver.find_element(By.ID, "passp:sign-in").click()
    # When user clicks on the 'Создать' button
    driver.find_element(By.CLASS_NAME, "create-resource-popup-with-anchor").click()
    # When user clicks on the 'Папку' element
    driver.find_element(By.CLASS_NAME, "create-resource-button__text").click()
    # When user clicks on the 'Сохранить' button
    driver.find_element(By.CSS_SELECTOR, '.confirmation-dialog__button_submit').click()
    # When - user clicks on the 'Новая папка'
    element = driver.find_element(By.XPATH, "//div[@class='listing-item__title listing-item__title_overflow_clamp' and @aria-label='Новая папка']/span[@class='clamped-text']")
    action = ActionChains(driver)
    action.double_click(on_element = element)
    action.perform()
    # When user clicks on the 'Создать' button
    driver.find_element(By.CLASS_NAME, "create-resource-popup-with-anchor").click()
    # When user clicks on the 'Текстовый документ' element
    driver.find_element(By.XPATH, "//span[@class='create-resource-button__text' and text()='Текстовый документ']").click()
    # When user clicks on the 'Создать' button
    driver.find_element(By.CSS_SELECTOR, '.confirmation-dialog__button_submit').click()
    driver.implicitly_wait(5000)
    # When user closes tab
    driver.close()
    # When - user swiches to the old tab
    driver.switch_to.window(url)
    driver.quit()




