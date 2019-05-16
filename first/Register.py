from selenium.webdriver.support.ui import Select

class Register():
    def __init__(self, driver):
        self.driver = driver

        # These are the three locators on this page
        self.input_email_xpath = "//input[@id='email']"
        self.press_button_xpath = "//img[@id='enterimg']"
        self.firstname_xpath = "//input[@placeholder='First Name']"
        self.lastname_xpath = "//input[@placeholder='Last Name']"
        self.Address_xpath = "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/textarea[1]"
        self.Email_xpath = "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[3]/div[1]/input[1]"
        self.PhoneNumber_xpath = "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[4]/div[1]/input[1]"
        self.Gender_xpath = "//label[1]//input[1]"
        self.Hobby_xpath = "//input[@id='checkbox2']"
        self.Language_click_xpath = "//div[@id='msdd']"
        self.select_Language_xpath = "//a[contains(text(),'English')]"
        self.skills_xpath = "//select[@id='Skills']"
        self.Countries_xpath = "//select[@id='countries']"
        self.year_xpath = "//select[@id='yearbox']"
        self.month_xpath = "//select[@placeholder='Month']"
        self.day_xpath = "//select[@id='daybox']"
        self.Password_xpath = "//input[@id='firstpassword']"
        self.Confirm_Password_xpath = "//input[@id='secondpassword']"
        self.Submit_button_xpath = "//button[@id='submitbtn']"

    def enter_email(self, email):

        self.driver.find_element_by_xpath(self.input_email_xpath).send_keys(email)
        self.driver.find_element_by_xpath(self.press_button_xpath).click()

    def enter_details1(self, firstname, lastname, address, email, phonenumber):

        self.driver.find_element_by_xpath(self.firstname_xpath).clear()
        self.driver.find_element_by_xpath(self.firstname_xpath).send_keys(firstname)
        self.driver.find_element_by_xpath(self.lastname_xpath).clear()
        self.driver.find_element_by_xpath(self.lastname_xpath).send_keys(lastname)
        self.driver.find_element_by_xpath(self.Address_xpath).clear()
        self.driver.find_element_by_xpath(self.Address_xpath).send_keys(address)
        self.driver.find_element_by_xpath(self.Email_xpath).clear()
        self.driver.find_element_by_xpath(self.Email_xpath).send_keys(email)
        self.driver.find_element_by_xpath(self.PhoneNumber_xpath).clear()
        self.driver.find_element_by_xpath(self.PhoneNumber_xpath).send_keys(phonenumber)

    def enter_details2(self, Skill, country, year, month, day):
        self.driver.find_element_by_xpath(self.Gender_xpath).click()
        self.driver.find_element_by_xpath(self.Hobby_xpath).click()
        self.driver.find_element_by_xpath(self.Language_click_xpath).click()
        self.driver.find_element_by_xpath(self.select_Language_xpath).click()

        Select(self.driver.find_element_by_xpath(self.skills_xpath)).select_by_value(Skill)
        Select(self.driver.find_element_by_xpath(self.Countries_xpath)).select_by_value(country)
        Select(self.driver.find_element_by_xpath(self.year_xpath)).select_by_value(year)
        Select(self.driver.find_element_by_xpath(self.month_xpath)).select_by_value(month)
        Select(self.driver.find_element_by_xpath(self.day_xpath)).select_by_value(day)

    def enter_password(self, password, confirm_password):

        self.driver.find_element_by_xpath(self.Password_xpath).clear()
        self.driver.find_element_by_xpath(self.Password_xpath).send_keys(password)

        self.driver.find_element_by_xpath(self.Confirm_Password_xpath).clear()
        self.driver.find_element_by_xpath(self.Confirm_Password_xpath).send_keys(confirm_password)


    def submit(self):

        self.driver.find_element_by_xpath(self.Submit_button_xpath).click()