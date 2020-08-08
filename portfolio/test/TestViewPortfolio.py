import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class TestViewPortfolio(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_add_stock(self):
        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.get("https://efs-development.herokuapp.com/")
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[2]/li/a').click()
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="id_username"]').send_keys('instructor')
        driver.find_element_by_xpath('//*[@id="id_password"]').send_keys('maverick1a')
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/form/input[2]').click()
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[2]/div/div/div/div/div[1]/div/div/p[2]/a').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[2]/table/tbody/tr[1]/td[11]/a').click()
        time.sleep(2)

        try:
            if (driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[1]/h1').text == 'Katherine McClusky Portfolio'):
                assert True
            assert False
        except NoSuchElementException:
            assert False


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
