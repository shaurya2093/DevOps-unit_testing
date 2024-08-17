from shared import config
import unittest
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

class TC_AddToCart(unittest.TestCase):
    failures = []    #Failure list

    # Opening browser.
    def setUp(self):
        driverPath = config.commonPath + "\WebDrivers\chromedriver.exe"
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(executable_path=driverPath, options=chromeOptions)

    def test_executeAddProduct(self):
        driver = self.driver
        if driver != None:
            driver.get("http://127.0.0.1:5000/")
        try:
            driver.switch_to.default_content()

            WebDriverWait(driver, config.SmallWait).until(ec.visibility_of_element_located((By.ID, "product-form")))

            pList = driver.find_element_by_id("product-list")
            products = pList.find_elements_by_tag_name("li")
            productCount = 0
            prodFound = False
            if len(products) != 0:
                while len(products) != productCount:
                    productCount += 1
                    if "Product 1" in products[productCount-1].text:
                        print("Product found in list, now adding to cart")

                        btnsAddtoCart = driver.find_elements_by_tag_name('button')
                        btnsAddtoCart[productCount].click()

                        WebDriverWait(driver, config.SmallWait).until(ec.element_to_be_clickable((By.ID, "view-cart-btn")))
                        driver.find_element_by_id("view-cart-btn").click()

                        WebDriverWait(driver, config.SmallWait).until(ec.visibility_of_element_located((By.ID, "cart-list")))
                        prodName = driver.find_element_by_id("cart-list").text
                        print(prodName)

                        prodFound = True

            if prodFound == False:
                print("Product not found..")

        except TimeoutException as e:
            self.failures.append("\n\n Timeout Error...")
        except NoSuchElementException as es:
            self.failures.append("\n\n No Such Element Exception " + es.msg)
        except Exception as ex:
            self.failures.append("\n\n Exception is " + str(ex))

    def tearDown(self):
        config.deleteDriver(self)
        '''if self.driver != None:
            try:
                errStr = ""
                for val in self.failures:
                    errStr += "" + val
                self.assertTrue(self.failures == [], str(errStr))
                self.driver.close() # print('WebDriver closing .')
            except Exception as em:
                self.driver.close()
                print('WebDriver closing ..')
                raise
        else:
            print('Driver found Null..')'''

if __name__ == "__main__":
    unittest.main()