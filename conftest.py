import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language',
                     action='store',
                     default="en",
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    print(f"{user_language}")
    # browser = None
    if browser_name == "chrome":
        from selenium.webdriver.chrome.options import Options

        print("\nstart chrome browser for test..")

        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")

        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(
            firefox_binary='c:/from_C/Program Files/Mozilla Firefox/firefox.exe',
            firefox_profile=fp)

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    browser.implicitly_wait(5)

    yield browser
    print("\nquit browser..")
    browser.quit()
