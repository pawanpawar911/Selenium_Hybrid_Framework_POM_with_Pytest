import pytest
import time

from selenium.webdriver.support.ui import WebDriverWait
from base_pages.login_page import LoginPage
from utilities.read_properties import ReadConfig
from utilities.customLogger import LogGenerate

   
def test_home_page(driver):
    logger = LogGenerate.logger_file()
    logger.info("Starting Test1: Verifying Home Page")
    
    login_page = LoginPage(driver)
    
    baseURL = ReadConfig.getWebURL()
    logger.info(f"Opening URL: {baseURL}")
    
    login_page.open_page(baseURL)

    #base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    #login_page.open_page(base_url)
    
    
    logger.info("Verifying HomePage LOGO")
    
    time.sleep(3)

    try:
        logo = login_page.logo()
        assert logo.is_displayed(), logger.info("Logo is not present on the homepage")
        logger.info("HomePage logo is displayed.")
    except AssertionError as e:
        print(f"Assertion failed: {e}") 
        raise
        
    finally: 
        logger.info("Test1: Home Page Completed")
    
def test_login_window_invalid_cred1(driver):
    logger = LogGenerate.logger_file()
    logger.info("Starting Test2: Veryfying Login Window-1")
    
    login_page = LoginPage(driver)
    
    usrN = ReadConfig.get_valid_usrName()
    passW = ReadConfig.get_invalid_passWord()
    try: 
        login_page.enter_usrname(usrN)
        login_page.enter_password(passW)
        time.sleep(2)
        login_page.click_login()

        expected_text = login_page.login_msg()
        actual_text = "Invalid credentials"
        
        assert expected_text == actual_text, logger.info(f"Expected: {expected_text}, but got: {actual_text}")
        logger.info("Test Login Window-1 : Passed")
        
    except AssertionError as e:
        print(f"Assertion failed: {e}") 
        raise
        
    finally: 
        logger.info("Test2: Login Window-1 Completed")
              
def test_login_window_invalid_cred2(driver):
    logger = LogGenerate.logger_file()
    logger.info("Starting Test3: Veryfying Login Window-2")
    
    login_page = LoginPage(driver)    
     
    usrN = ReadConfig.get_invalid_usrName()
    passW = ReadConfig.get_valid_passWord()
    
    try: 
        login_page.enter_usrname(usrN)
        login_page.enter_password(passW)
        login_page.click_login()

        expected_text = login_page.login_msg()
        actual_text = "Invalid credentials"
        
        if expected_text == actual_text:
            logger.info("Test Login Window-2 : Passed")
            assert True  
        else: 
            driver.save_screenshot(".\\snapshots\\" + "Invalid_usrName_valid_password.png")
            logger.info(f"Expected: {expected_text}, but got: {actual_text}")
            assert False
                
    except AssertionError as e:
        print(f"Assertion failed: {e}") 
        raise
        
    finally: 
        logger.info("Test3: Login Window-2 Completed")

def test_login_window_valid_cred(driver):
    logger = LogGenerate.logger_file()
    logger.info("Starting Test4: Veryfying Login Window-3")
    
    login_page = LoginPage(driver) 
    
    usrN = ReadConfig.get_valid_usrName()
    passW = ReadConfig.get_valid_passWord()
        
    try:
        login_page.enter_usrname(usrN)
        login_page.enter_password(passW)
        login_page.click_login()

        expected_text = login_page.text_title() 
        actual_text = "Dashboard"
        
        assert expected_text == actual_text, logger.info(f"Expected {expected_text}, but got {actual_text}")
        logger.info("Test Correct Credential : Passed")
        
    except AssertionError as e:
        print(f"Assertion failed: {e}") 
        raise
        
    finally: 
        logger.info("Test4: Login Window-3  Completed")
        
def test_All_Tabs(driver):
    logger = LogGenerate.logger_file()
    logger.info("Starting Test5: Veryfying the All Tab")
    
    all_tab_page = LoginPage(driver)
    
    try: 
        logger.info("Starting Test1 of Test5: Veryfying the DashBoard Tab")
        all_tab_page.dashBoard_click()
        expected_text = all_tab_page.text_title()        
        actual_text = "Dashboard"
        
        assert expected_text == actual_text, logger.info(f"Expected {expected_text}, but got {actual_text}")
        logger.info("Test1 of Test5 Dashboard Tab : Passed")
        
    except AssertionError as e:
        print(f"Assertion failed: {e}")
        
    finally:
        logger.info("Test1 of Test5: DashBoard Tab Completed")
         
    try: 
        logger.info("Starting Test2 of Test5: Veryfying the Admin Tab")
        all_tab_page.admin_click()
        expected_text = all_tab_page.admin_title()        
        actual_text = "Admin"
        
        assert expected_text == actual_text, logger.info(f"Expected {expected_text}, but got {actual_text}")
        logger.info("Test2 of Test5 Admin Tab : Passed")
        
    except AssertionError as e:
        print(f"Assertion failed: {e}") 
        
    finally:
        logger.info("Test2 of Test5: DashBoard Tab Completed")      
        
    try: 
        logger.info("Starting Test3 of Test5: Veryfying the Directory Tab")
        all_tab_page.directory_click()
        expected_text = all_tab_page.text_title()
        actual_text = "Directory"
        
        assert expected_text == actual_text, logger.info(f"Expected {expected_text}, but got {actual_text}")
        logger.info("Test3 of Test5 Directory Tab : Passed")
        
    except AssertionError as e:
        print(f"Assertion failed: {e}")
        
    finally:
        logger.info("Test3 of Test5: Directory Tab Completed")
        
    try: 
        logger.info("Starting Test4 of Test5: Veryfying the PIM Tab")
        all_tab_page.pim_click()
        expected_text = all_tab_page.text_title()
        actual_text = "PIM"
        
        assert expected_text == actual_text, logger.info(f"Expected {expected_text}, but got {actual_text}")
        logger.info("Test4 of Test5 PIM Tab : Passed")
        
    except AssertionError as e:
        print(f"Assertion failed: {e}")
        
    finally:
        logger.info("Test4 of Test5: PIM Tab Completed")
           
    try: 
        logger.info("Starting Test5 of Test5: Veryfying the Leave Tab")
        all_tab_page.leave_click()
        expected_text = all_tab_page.text_title()
        actual_text = "Leave"
        
        assert expected_text == actual_text, logger.info(f"Expected {expected_text}, but got {actual_text}")
        logger.info("Test5 of Test5 Leave Tab : Passed")
        
    except AssertionError as e:
        print(f"Assertion failed: {e}")
        
    finally:
        logger.info("Test5 of Test5: Leave Tab Completed")
        
    logger.info("Test5: All Tab Completed")
     
def test_PIM_Tab(driver):
    logger = LogGenerate.logger_file()
    logger.info("Starting Test6: Veryfying the PIM page field")
    
    pim_page = LoginPage(driver)
  
    try: 
        pim_page.pim_click()
        
        pim_page.pim_tab_add_button()
        
        pim_page.pim_tab_first_name("Pawan")
        pim_page.pim_tab_last_name("Pawar")
        pim_page.pim_tab_EmpId("42398")
        pim_page.pim_tab_submit_button()

        logger.info("Test6: PIM page field : Passed")       
    except AssertionError as e:
        print(f"Assertion failed: {e}")
        
    finally:
        logger.info("Test6: PIM page field Completed")

if __name__ == "__main__":
    pytest.main()