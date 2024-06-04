from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    driver = webdriver.Chrome()
    driver.get("http://localhost")
    wait = WebDriverWait(driver, 100)


    product_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='product']")))
    product_element.click()

    screenshot_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='screenshot']")))
    screenshot_element.click()

    currency_select = Select(driver.find_element(By.ID, "currency-select"))
    currency_select.select_by_value("EUR")



    pc_menu_item = driver.find_element(By.XPATH, "//li[@class='menu-item']/a[contains(text(), 'PC')]")
    pc_menu_item.click()



    registration_link = driver.find_element(By.XPATH, "//a[@href='/registration']")
    registration_link.click()



    search_input = driver.find_element(By.ID, "search-input")
    search_input.send_keys("search_keyword")

    search_button = driver.find_element(By.ID, "search-button")
    search_button.click()

    driver.quit()

if __name__ == "__main__":
    main()
