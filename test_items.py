from time import sleep


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_button_add_to_basket_pass(browser):
    browser.get(link)
    sleep(30)
    result = browser.find_elements_by_css_selector(".btn-add-to-basket")
    assert len(result) == 1, "CSS selector not unique or missing."
