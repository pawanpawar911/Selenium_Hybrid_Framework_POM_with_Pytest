from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        
        self.homepage_logo = (By.XPATH, "//img[@alt='company-branding']")        
        self.username_textbox = (By.NAME, "username")
        self.password_textbox = (By.NAME, "password")
        self.cred_msg = (By.CSS_SELECTOR, "p.oxd-text.oxd-text--p.oxd-alert-content-text")
        self.login_button = (By.XPATH, "//button[normalize-space()='Login']")
        
        self.dashboard = (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='Dashboard']")
        self.common_title = (By.XPATH, "//div[@class='oxd-topbar-header-title']")
        
        self.admin = (By.XPATH, "//li[1]//a[1]//span[1]")
        self.adminTitle = (By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")
        
        self.directory = (By.XPATH, "//span[normalize-space()='Directory']")
        self.pim = (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='PIM']")
        self.leave = (By.XPATH, "//span[normalize-space()='Leave']")
        
        self.add_button = (By.XPATH, "//button[normalize-space()='Add']")
        self.first_name = (By.XPATH, "//input[@placeholder='First Name']") 
        self.last_name = (By.XPATH, "//input[@placeholder='Last Name']")
        self.emp_id = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.submit = (By.XPATH, "//button[@type='submit']")
        
    def open_page(self, url):
        self.driver.get(url)
        
    def logo(self):
        wait = WebDriverWait(self.driver, 10)  # Wait up to 10 seconds
        return wait.until(EC.presence_of_element_located(self.homepage_logo))
        
    def enter_usrname(self, username):
        self.driver.find_element(*self.username_textbox).send_keys(username)
        
    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)
        
    def login_msg(self):
        msg = self.driver.find_element(*self.cred_msg)
        return msg.text
        
    def click_login(self):
        self.driver.find_element(*self.login_button).click()
        
    def dashBoard_click(self):
        self.driver.find_element(*self.dashboard).click()

    def text_title(self):        
        title = self.driver.find_element(*self.common_title)
        return title.text
    
    def admin_click(self):
        self.driver.find_element(*self.admin).click()
        
    def admin_title(self):        
        title = self.driver.find_element(*self.adminTitle)
        return title.text
    
    def directory_click(self):
        self.driver.find_element(*self.directory).click()
        
    def pim_click(self):
        self.driver.find_element(*self.pim).click()

    def leave_click(self):
        self.driver.find_element(*self.leave).click()
        
    def pim_tab_add_button(self):
        self.driver.find_element(*self.add_button).click()
         
    def pim_tab_first_name(self, FirstName):
        fn = self.driver.find_element(*self.first_name)
        fn.clear()
        fn.send_keys(FirstName)
            
    def pim_tab_last_name(self, lastName):
        ln = self.driver.find_element(*self.last_name)
        ln.clear()
        ln.send_keys(lastName)
            
    def pim_tab_EmpId(self, EmpId):
        empId = self.driver.find_element(*self.emp_id)
        empId.clear()
        empId.send_keys(EmpId)
            
    def pim_tab_submit_button(self):
        self.driver.find_element(*self.submit).click()

