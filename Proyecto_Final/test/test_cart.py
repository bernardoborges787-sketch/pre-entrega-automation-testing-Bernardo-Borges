from selenium import webdriver
from selenium.webdriver.common.by import By     
import pytest


@pytest.mark.smoke
def test_cart(driver_logged):
        driver = driver_logged
                
               
        # Agregar un producto al carrito
        driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click()
        
        # Verificar que el contador del carrito se actualice correctamente
        contador_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        
        assert contador_cart.text == "1", "El contador del carrito no se actualizó correctamente"
                
        #Obetener nombre del primer producto agregado
        product_name = driver.find_elements(By.CLASS_NAME, "inventory_item_name")[0].text
        
        # Ir al carrito de compras
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        
        # Obtener el nombre del producto en el carrito de compras
        cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        
        #Verficar que el producto en el carrito coincide con el producto agregado
        assert cart_item == product_name, "El producto en el carrito no coincide"
        
        