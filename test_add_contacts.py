# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from contacts import Contacts

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
    def test_add_contact(self):
        wd = self.wd
        self.Open_Home_Page(wd)
        self.Login(wd, user="admin", password="secret")
        self.Create_Contacts(wd, Contacts(FirstName="FirstName", MiddleName="MiddleName", LastName="LastName", NickName="NickeName"))
        self.Submit_Create_Contacts(wd)
        self.Return_Home(wd)
        self.Logout(wd)

    def Logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def Return_Home(self, wd):
        wd.find_element_by_link_text("home").click()

    def Submit_Create_Contacts(self, wd):
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def Create_Contacts(self, wd, Contacts):
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(Contacts.FirstName)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(Contacts.MiddleName)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(Contacts.LastName)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(Contacts.NickName)


    def Login(self, wd, user, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").send_keys(user)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys(password)
        # click button Login
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def Open_Home_Page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
