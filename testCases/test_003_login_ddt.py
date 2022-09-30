import time
import pytest

from pageObjects.Homepage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccountPage import MyAccountPage
from utilities import XLUtiles
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os

class Test_Login_DDT():
    baseURL=ReadConfig.getApplicationURL()
    logger=LogGen.loggen()  #Logger

    path=os.path.abspath(os.curdir)+"\\testdata\\Opencart\\LoginData.xlsx"

    def test_login_ddt(self,setup):
        self.logger.info("*******starting test_003_login_Datadriven******")
        self.rows=XLUtiles.getRowCount(self.path,'Sheet1')
        lst_status=[]

        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)   # HomePage Pageobject Class
        self.lp=LoginPage(self.driver)  #LoginPage Pageobject Class
        self.ma=MyAccountPage(self.driver) #MyAccountPage Pageobject Class

        for r in range(2,self.rows+1):
            self.hp.clickMyAccount()
            self.hp.clickLogin()

            self.email=XLUtiles.readData(self.path,"Sheet1",r,1)
            self.password=XLUtiles.readData(self.path,"Sheet1",r,2)
            self.exp = XLUtiles.readData(self.path, "Sheet1", r, 3)
            self.lp.setEmail(self.email)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(3)
            self.targetpage=self.lp.isMyAccountPageExist()

            if self.exp=='valid':
                if self.targetpage==True:
                    lst_status.append('Pass')
                    self.ma.clickLogout()
                else:
                    lst_status.append('Fail')
            elif self.exp=='Invalid':
                if self.targetpage==True:
                    lst_status.append('Fail')
                    self.ma.clickLogout()
                else:
                    lst_status.append('Pass')
        self.driver.close()
        # final validation
        if "Fail" not in lst_status:
            assert True
        else:
            assert False
        self.logger.info("*****End of test_003_login_Datadriven******")



