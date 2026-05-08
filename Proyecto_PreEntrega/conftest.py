import pytest
from selenium import webdriver
from utils.LoginPage import login


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incongnito")
    
    driver = webdriver.Chrome(options=options)

#Yield funciona como un return(se pausa y se mete toda la prueba,para no estar retornando cada set con la prueba)
    yield driver

    driver.quit()
    
@pytest.fixture
def login_in_driver(driver):
    login(driver)
    return driver
