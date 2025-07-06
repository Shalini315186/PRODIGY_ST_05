from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# ✅ Setup WebDriver
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

try:
    # ✅ 1. Open Website
    driver.get("https://www.saucedemo.com")
    time.sleep(2)

    # ✅ 2. Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    # ✅ 3. Add Items to Cart
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    time.sleep(1)

    # ✅ 4. Go to Cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(1)

    # ✅ 5. Proceed to Checkout
    driver.find_element(By.ID, "checkout").click()
    time.sleep(1)

    # ✅ 6. Fill Checkout Form
    driver.find_element(By.ID, "first-name").send_keys("Shalini")
    driver.find_element(By.ID, "last-name").send_keys("Murugan")
    driver.find_element(By.ID, "postal-code").send_keys("600001")
    driver.find_element(By.ID, "continue").click()
    time.sleep(1)

    # ✅ 7. Finish Checkout
    driver.find_element(By.ID, "finish").click()
    time.sleep(2)

    # ✅ 8. Validate Confirmation
    message = driver.find_element(By.CLASS_NAME, "complete-header").text
    if "THANK YOU" in message.upper():
        print("✅ Checkout Completed Successfully!")
    else:
        print("❌ Checkout Failed!")

except Exception as e:
    print("❌ Test Failed:", e)

finally:
    time.sleep(3)
    driver.quit()
