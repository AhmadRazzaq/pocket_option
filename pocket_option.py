import time
import undetected_chromedriver as uc
from scrapy import Selector
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


class browsePocketOption:
    def __init__(self):
        self.driver = uc.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def switch_to_iframe_to_solve_captcha(self):
        iframe = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '[title="reCAPTCHA"]')))
        self.driver.switch_to.frame(iframe)
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '#recaptcha-anchor'))).click()
        time.sleep(5)
        self.driver.switch_to.default_content()

    def login(self):
        self.driver.get("https://affiliate.pocketoption.com/en/dashboard")
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '[name="email"]'))).send_keys("fasehfaizan0@gmail.com")
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '[name="password"]'))).send_keys("Faseh!@#1234")
        time.sleep(5)
        self.switch_to_iframe_to_solve_captcha()
        time.sleep(5)
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '[type="submit"]'))).click()

    def parse_data(self):
        time.sleep(15)
        response = Selector(text=self.driver.page_source)
        visitor = response.css('#partnerVisits::text').get('')
        Registrations = response.css('#partnerClients::text').get('')
        FTD = response.css('#partnerFTDs::text').get('')
        Deposits = response.css('#partnerDeposits::text').get('')
        ClientsWithdrawals = response.css('#partnerClientsWithdrawals::text').get('')
        HoldCommission = response.css('#partnerHoldCommission::text').get('')
        Commission = response.css('#partnerCommission::text').get('')
        Balance = response.css('#partnerBalance::text').get('')
        print(f"Visitor: {visitor}\n",
              f"Registrations: {Registrations}\n",
              f"FTD: {FTD}\n",
              f"Deposits: {Deposits}\n",
              f"Withdrawals: {ClientsWithdrawals}\n",
              f"Hold Commission: {HoldCommission}\n",
              f"Commission: {Commission}\n",
              f"Balance: {Balance}\n")
        self.driver.close()


if __name__ == "__main__":
    obj = browsePocketOption()
    obj.login()
    obj.parse_data()
pass
