# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time, re
from group import Group

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_Home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def authorization(self, wd, user, secret):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(secret)

    def open_Group(self, wd):
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def create_New_Group(self, wd, group):
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Submit Click
        wd.find_element_by_name("submit").click()
        # return Group Page
        wd.find_element_by_link_text("group page").click()

    def logout(self, wd):
        # Logout
        wd.find_element_by_link_text("Logout").click()


    def test_add_group(self):
        wd = self.wd
        self.open_Home_page(wd)
        self.authorization(wd, user="admin", secret="secret")
        self.open_Group(wd)
        self.create_New_Group(wd, Group(name="NEW_GROUP", header="NEW_GROUP", footer="NEW_GROUP"))
        self.logout(wd)


    def test_add_empty_group(self):
        wd = self.wd
        self.open_Home_page(wd)
        self.authorization(wd, user="admin", secret="secret")
        self.open_Group(wd)
        self.create_New_Group(wd, Group(name="name", header="header", footer="footer"))
        self.logout(wd)


    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
