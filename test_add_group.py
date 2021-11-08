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

    def test_add_group(self):
        wd = self.wd
        self.Open_Home_page(wd)
        self.Authorization(wd, user="admin", secret="secret")
        self.Open_Group(wd)
        self.Create_New_Group(wd, Group(group_name="NEW_GROUP", group_header="NEW_GROUP", group_footer="NEW_GROUP"))
        self.Create_New_Group(wd, Group(group_name="", group_header="", group_footer=""))
        self.Logout(wd)

    def Logout(self, wd):
        # Logout
        wd.find_element_by_link_text("Logout").click()

    def Create_New_Group(self, wd, group):
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.group_name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.group_header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.group_footer)
        # Submit Click
        wd.find_element_by_name("submit").click()
        # return Group Page
        wd.find_element_by_link_text("group page").click()


    def Authorization(self, wd, user, secret):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(secret)


    def Open_Group(self, wd):
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def Open_Home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
