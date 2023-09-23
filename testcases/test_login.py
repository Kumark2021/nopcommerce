import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from utilities.ReadProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseurl =ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()

    def test_homePage(self,setup):
        self.logger.info(" ****Test_001_Login***")
        self.logger.info("**Verifying the tile ****")
        self.driver=setup
        self.driver.get(self.baseurl)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**** Home Page title is Verifies****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePage.png")
            self.driver.close()
            assert False

    def test_login(self,setup):
        self.logger.info(" ****Veifying the login test***")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp=LoginPage(self.driver);
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
           assert True
           self.driver.close()
           self.logger.info("***Passes***")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("***Failed***")
            assert False






