from selenium import webdriver

SmallWait = 5
commonPath = "E:\\12)DevOps\\SELENIUM\\Testing"

def createDriver():
    driverPath = commonPath + "\WebDrivers\chromedriver.exe"
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(executable_path=driverPath, options=chromeOptions)
    return driver

def deleteDriver(obj):
    if obj.driver != None:
        try:
            errStr = ""
            for val in obj.failures:
                errStr += "" + val
            obj.assertTrue(obj.failures == [], str(errStr))
            obj.driver.close()  # print('WebDriver closing .')
        except Exception as em:
            obj.driver.close()
            print('WebDriver closing ..')
            raise
    else:
        print('Driver found Null..')
