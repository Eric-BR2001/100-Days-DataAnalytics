from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_dollar_value():
    # Set up the Chrome WebDriver
    driver = webdriver.Chrome()

    try:
        # Open Google
        driver.get("https://www.google.com")

        # Wait for the page to load
        time.sleep(2)

        # Search for the dollar value
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("USD to BRL")  # or "Dólar hoje" for Portuguese results
        search_box.submit()

        # Wait for results to load
        time.sleep(2)

        # Get the exchange rate from the result page
        exchange_rate_element = driver.find_element(By.XPATH, '//span[@class="DFlfde SwHCTb"]')
        dollar_value = exchange_rate_element.text

        print(f"Current USD to BRL exchange rate: R$ {dollar_value}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser
        time.sleep(3)
        driver.quit()

if __name__ == "__main__":
    get_dollar_value()
