#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys

from page.login_page import LoginPage

def test_login_validation(driver):
    login_page = LoginPage(driver)
    
    login_page.login("standard_user", "secret_sauce")
    
    assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
    
def test_login_invalid_credentials(driver):
    login_page = LoginPage(driver)
    
    login_page.login("invalid_user", "invalid_password")
    
    error_message = login_page.get_error_message()
    assert error_message == "Epic sadface: Username and password do not match any user in this service", "No se mostró el mensaje de error esperado"   
    
     