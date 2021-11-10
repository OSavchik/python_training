# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from contact import Contact

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class TestAddContacts(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, user, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").send_keys(user)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys(password)
        # click button Login
        wd.find_element_by_xpath("//input[@value='Login']").click()


    def create_contact(self, wd, Contact):
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(Contact.first_name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(Contact.middle_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(Contact.last_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(Contact.nick_name)


    def submit_create_contact(self, wd):
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def return_Home(self, wd):
        wd.find_element_by_link_text("home").click()


    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()


    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, user="admin", password="secret")
        self.create_contact(wd, Contact(first_name="FirstName", middle_name="MiddleName", last_name="LastName", nick_name="NickeName"))
        self.submit_create_contact(wd)
        self.return_Home(wd)
        self.logout(wd)

    def test_add_empty_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, user="admin", password="secret")
        self.create_contact(wd, Contact(first_name=" ", middle_name=" ", last_name=" ", nick_name=" "))
        self.submit_create_contact(wd)
        self.return_Home(wd)
        self.logout(wd)


    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
