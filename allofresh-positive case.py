from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inisialisasi WebDriver (menggunakan Chrome)
driver = webdriver.Chrome()

# Test Case Positif
def test_positive_case():
    # Buka halaman https://www.saucedemo.com/
    driver.get("https://www.saucedemo.com/")

    # Input username dan password
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # Klik Login
    driver.find_element(By.ID, "login-button").click()

    # Redirect ke halaman https://www.saucedemo.com/inventory.html
    WebDriverWait(driver, 10).until(EC.url_to_be("https://www.saucedemo.com/inventory.html"))

    # Pilih item "Sauce Labs Backpack"
    driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']").click()

    # Klik Add to Cart
    driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click()

    # Pilih icon keranjang di pojok kanan atas
    driver.find_element(By.CLASS_NAME, "shopping_cart_container").click()

    # Redirect ke halaman "https://www.saucedemo.com/cart.html"
    WebDriverWait(driver, 10).until(EC.url_to_be("https://www.saucedemo.com/cart.html"))

    # Klik button checkout
    driver.find_element(By.ID, "checkout").click()

    # Redirect ke halaman https://www.saucedemo.com/checkout-step-one.html
    WebDriverWait(driver, 10).until(EC.url_to_be("https://www.saucedemo.com/checkout-step-one.html"))

    # Input First Name, Last Name, dan Zip/Postal Code
    driver.find_element(By.ID, "first-name").send_keys("Fitria")
    driver.find_element(By.ID, "last-name").send_keys("Agista")
    driver.find_element(By.ID, "postal-code").send_keys("16610")

    # Klik continue
    driver.find_element(By.ID, "continue").click()

    # Redirect ke halaman "https://www.saucedemo.com/checkout-step-two.html"
    WebDriverWait(driver, 10).until(EC.url_to_be("https://www.saucedemo.com/checkout-step-two.html"))

    # Klik button finish
    driver.find_element(By.ID, "finish").click()

    # Redirect ke halaman https://www.saucedemo.com/checkout-complete.html
    WebDriverWait(driver, 10).until(EC.url_to_be("https://www.saucedemo.com/checkout-complete.html"))

    # Pastikan ada kalimat Checkout: Complete!
    checkout_complete_message = driver.find_element(By.XPATH, "//h2[text()='Checkout: Complete!']").text
    assert "Checkout: Complete!" in checkout_complete_message, "Positive test failed"

    # Print informasi di console atau masukkan ke dalam report
    print("Test Case 1 passed!")

# Menjalankan Test Case Positif
test_positive_case()

# Menutup browser setelah selesai
driver.quit()
