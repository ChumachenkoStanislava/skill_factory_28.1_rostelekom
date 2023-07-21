from time import sleep
from settings import *
from auth_page import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# тест EXP-001 - общий вид формы (сохранить скриншот)

def test_001_vision(browser):
    form = AuthForm(browser)
    form.driver.save_screenshot('screen.jpg')


# тест EXP-002 - проверка, что по-умолчанию выбрана форма авторизации по телефону
def test_002_by_phone(browser):
    form = AuthForm(browser)

    assert form.placeholder.text == 'Мобильный телефон'


# тест EXP-003 - проверка автосмены "таб ввода"
def test_003_change_placeholder(browser):
    form = AuthForm(browser)

    # ввод телефона
    form.username.send_keys(valid_phone)
    form.password.send_keys('_')
    sleep(5)

    assert form.placeholder.text == 'Мобильный телефон'

    # очистка поля логина
    form.username.send_keys(Keys.CONTROL, 'a')
    form.username.send_keys(Keys.DELETE)

    # ввод почты
    form.username.send_keys(valid_email)
    form.password.send_keys('_')
    sleep(5)

    assert form.placeholder.text == 'Электронная почта'

    # очистка поля логина
    form.username.send_keys(Keys.CONTROL, 'a')
    form.username.send_keys(Keys.DELETE)

    # ввод логина
    form.username.send_keys('MyLogin')
    form.password.send_keys('_')
    sleep(5)

    assert form.placeholder.text == 'Логин'


# тест EXP-004 - проверка позитивного сценария авторизации по телефону
def test_004_positive_by_phone(browser):
    form = AuthForm(browser)

    # ввод телефона
    form.username.send_keys(valid_phone)
    form.password.send_keys(valid_pass)
    sleep(5)
    form.btn_click()

    assert form.get_current_url() != '/account_b2c/page'


# тест EXP-005 - проверка негативного сценария авторизации по телефону
def test_005_negative_by_phone(browser):
    form = AuthForm(browser)

    # ввод телефона
    form.username.send_keys('+1234567890')
    form.password.send_keys('any_password')
    sleep(5)
    form.btn_click()

    err_mess = form.driver.find_element(By.ID, 'form-error-message')
    assert err_mess.text == 'Неверный логин или пароль'


# тест EXP-006 - проверка позитивного сценария авторизации по почте
def test_006_positive_by_email(browser):
    form = AuthForm(browser)

    # ввод почты
    form.username.send_keys(valid_email)
    form.password.send_keys(valid_pass)
    sleep(5)
    form.btn_click()

    assert form.get_current_url() != '/account_b2c/page'


# тест EXP-007 - проверка негативного сценария авторизации по почте
def test_007_negative_by_email(browser):
    form = AuthForm(browser)

    # ввод почты
    form.username.send_keys('aa@aa.aa')
    form.password.send_keys('any_password')
    sleep(5)
    form.btn_click()

    err_mess = form.driver.find_element(By.ID, 'form-error-message')
    assert err_mess.text == 'Неверный логин или пароль'


# тест EXP-008 - проверка получения временного кода на телефон и открытия формы для ввода кода
def test_008_get_code(browser):
    form = CodeForm(browser)

    # ввод телефона
    form.address.send_keys(valid_phone)

    # длительная пауза предназначена для ручного ввода капчи при необходимости
    sleep(30)
    form.get_click()

    rt_code = form.driver.find_element(By.ID, 'rt-code-0')

    assert rt_code


# тест EXP-009 - проверка перехода в форму восстановления пароля и её открытия
def test_009_forgot_pass(browser):
    form = AuthForm(browser)

    # клик по надписи "Забыл пароль"
    form.forgot.click()
    sleep(5)

    reset_pass = form.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')

    assert reset_pass.text == 'Восстановление пароля'


# тест EXP-010 - проверка перехода в форму регистрации и её открытия
def test_010_register(browser):
    form = AuthForm(browser)

    # клик по надписи "Зарегистрироваться"
    form.register.click()
    sleep(5)

    reset_pass = form.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')

    assert reset_pass.text == 'Регистрация'


# тест EXP-011 - проверка открытия пользовательского соглашения
def test_011_agreement(browser):
    form = AuthForm(browser)

    original_window = form.driver.current_window_handle
    # клик по надписи "Пользовательским соглашением" в подвале страницы
    form.agree.click()
    sleep(5)
    WebDriverWait(form.driver, 5).until(EC.number_of_windows_to_be(2))
    for window_handle in form.driver.window_handles:
        if window_handle != original_window:
            form.driver.switch_to.window(window_handle)
            break
    win_title = form.driver.execute_script("return window.document.title")

    assert win_title == 'User agreement'


# тест EXP-012 - проверка перехода по ссылке авторизации пользователя через вконтакте
def test_012_auth_vk(browser):
    form = AuthForm(browser)
    form.vk_btn.click()
    sleep(5)

    assert form.get_base_url() == 'oauth.vk.com'


# тест EXP-013 - проверка перехода по ссылке авторизации пользователя через одноклассники
def test_013_auth_ok(browser):
    form = AuthForm(browser)
    form.ok_btn.click()
    sleep(5)

    assert form.get_base_url() == 'connect.ok.ru'


# тест EXP-014 - проверка перехода по ссылке авторизации пользователя через майлру
def test_014_auth_mailru(browser):
    form = RegistrPage(browser)
    form.mailru_btn.click()
    sleep(5)

    assert form.get_base_url() == 'connect.mail.ru'


### тест EXP-015 - проверка перехода по ссылке авторизации пользователя через google
def test_015_auth_google(browser):
    form = AuthForm(browser)
    form.google_btn.click()
    sleep(5)

    assert form.get_base_url() == 'accounts.google.com'


### тест EXP-016 - проверка перехода по ссылке авторизации пользователя через яндекс
def test_016_auth_ya(browser):
    form = AuthForm(browser)
    form.ya_btn.click()
    sleep(5)

    assert form.get_base_url() == 'passport.yandex.ru'