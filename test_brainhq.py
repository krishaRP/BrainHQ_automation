from Auth import Authentication
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import random

# Test Case 1: Enter valid Email Id and Password and tap on "LOG IN" button
# Expected result : User should be able to log in successfully
def test_login_page(driver):
    form = Authentication(driver)
    form.navigate_to_login_page()
    sleep(5)
    form.enter_login_username("admin123@gmail.com")
    form.enter_login_password("Admin123")
    sleep(5)
    form.click_login_button()
    sleep(5)
    try:
        element_nav = form.check_login_status()
        assert element_nav is not None
    except NoSuchElementException:
        assert False, f"Element with XPath does not exist."
#
#
# # Test Case 2: Enter valid Email Id and Password and tap on "LOG IN" button
# # Expected result : User should be able to log in successfully, check if login text is present
#
def test_login_button_works(driver):
    form = Authentication(driver)
    form.navigate_to_login_page()
    sleep(10)
    try:
        element_login = form.check_login_function()
        sleep(15)
        assert element_login
    except NoSuchElementException:
        assert False
#
# # Test Case 3: Tap on Hamburgur(Menu) option from nav bar and tap on Logout option
# # Expected : User should be able to log out successfully, and redirect to homepage/login page
def test_logout(driver):
    form = Authentication(driver)
    form.navigate_to_login_page()
    sleep(5)
    form.enter_login_username("admin123@gmail.com")
    form.enter_login_password("Admin123")
    sleep(5)
    form.click_login_button()
    sleep(5)
    form.click_logout_button()
    sleep(10)
    element_logout = form.logout_check()
    assert element_logout is not None

# Test case 4: Verify sign up functionality is working or not
# Expected : user should be able to sign up successfully
def test_signup(driver):
    email_suffix = str(random.randint(10, 1000))
    email = 'abc' + email_suffix + '@gmail.com'
    form = Authentication(driver)
    form.navigate_to_sign_up_page(email, 'Admin123', 'KPpandyfga', 'tadfilorfdg')
    sleep(5)
    try:
        element_nav = form.check_login_status()
        assert element_nav is not None
    except NoSuchElementException:
        assert False, f"Element with XPath does not exist."