from selenium.webdriver.common.by import By


class AccountRegistrationPage():
    txt_firstname_name = "firstname"
    txt_lastname_name = "lastname"
    txt_email_name = "email"
    txt_password_name = "password"
    chk_policy_xpath = "//input[@type='checkbox']"
    btn_cont_xpath="//button[normalize-space()='Continue']"
    text_msg_conf_xpath="//h1[normalize-space()='Your Account Has Been Created!']"

    def __init__(self, driver):
        self.driver = driver

    def setFirstName(self,fname):
      self.driver.find_element(By.NAME,self.txt_firstname_name).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.NAME,self.txt_lastname_name).send_keys(lname)

    def setEmail(self,email):
        self.driver.find_element(By.NAME,self.txt_email_name).send_keys(email)

    def setPassword(self,pwd):
        self.driver.find_element(By.NAME,self.txt_password_name).send_keys(pwd)

    def setPrivacyPolicy(self):
        self.element=self.driver.find_element(By.XPATH,self.chk_policy_xpath)
        self.driver.execute_script("arguments[0].click();",self.element)

    def clickContinue(self):
        self.conts=self.driver.find_element(By.XPATH,self.btn_cont_xpath)
        self.driver.execute_script("arguments[0].click();",self.conts)

    def getconfirmationmsg(self):
        try:
            return  self.driver.find_element(By.XPATH,self.text_msg_conf_xpath).text
        except:
            None
