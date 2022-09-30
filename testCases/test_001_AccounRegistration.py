from pageObjects.Homepage import HomePage
from pageObjects.AccountregistrationPage import AccountRegistrationPage
from pageObjects.Homepage import HomePage
from utilities import randomString
import os
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import pytest



class Test_001_AccountReg:
    baseURL = ReadConfig.getApplicationURL()
    logger=LogGen.loggen()  #for logging

    @pytest.mark.sanity
    def test_account_reg(self, setup):
        self.logger.info("*** test_001_AccountRegistration started ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Launching Application")
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.logger.info("Clicking on MyAccount--> register")
        self.hp.clickMyAccount()
        self.hp.clickRegister()

        self.logger.info("Proving customer details for registration")
        self.regpage = AccountRegistrationPage(self.driver)
        self.regpage.setFirstName("John")
        self.regpage.setLastName("Canedy")
        self.email = randomString.random_string_generator() + '@gmail.com'
        self.regpage.setEmail(self.email)
        # self.regpage.setEmail("abc0951776091@gmail.com")
        self.regpage.setPassword("abcxyz")
        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        self.confmsg = self.regpage.getconfirmationmsg()
        if self.confmsg == "Your Account Has Been Created!":
            self.logger.info("Account registration is passed..")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_account_reg.png")
            self.logger.error("Account registration is failed..")
            self.driver.close()
            assert False
        self.logger.info("*** test_001_AccountRegistration finished ***")