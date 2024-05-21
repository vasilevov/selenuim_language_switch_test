from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_basket_button(browser):
    browser.get(link)
    try:
        browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    except Exception:
        assert False, "Кнопка не найдена"