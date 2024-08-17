from shared import config
import unittest
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

class TC_AddProduct(unittest.TestCase):
    failures = []    #Failure list

    # Opening browser.
    def setUp(self):
        self.driver = config.createDriver()
        '''driverPath = config.commonPath + "\WebDrivers\chromedriver.exe"
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(executable_path=driverPath, options=chromeOptions)'''

    def test_executeAddProduct(self):
        driver = self.driver
        if driver != None:
            #driver.maximize_window()
            driver.get("http://127.0.0.1:5000/")
        try:
            driver.switch_to.default_content()

            WebDriverWait(driver, config.SmallWait).until(ec.visibility_of_element_located((By.ID, "product-form")))

            WebDriverWait(driver, config.SmallWait).until(ec.element_to_be_clickable((By.ID, "name")))
            name = driver.find_element_by_id("name")
            name.send_keys("Product : Watch")
            WebDriverWait(driver, config.SmallWait).until(ec.element_to_be_clickable((By.ID, "price")))
            price = driver.find_element_by_id("price")
            price.send_keys("1000")
            WebDriverWait(driver, config.SmallWait).until(ec.element_to_be_clickable((By.ID, "description")))
            desc = driver.find_element_by_id("description")
            desc.send_keys("Brand Fastrack")

            btnList = driver.find_elements_by_tag_name('button')
            if len(btnList) != 0:
                if btnList[0].text == "Add Product":
                    btnList[0].click()

            driver.get("http://127.0.0.1:5000/")

            productList = []
            pList = driver.find_element_by_id("product-list")
            products = pList.find_elements_by_tag_name("li")
            if products != "":
                for p in products:
                    productList.append(p.text)
            print(productList)

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