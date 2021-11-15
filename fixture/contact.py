class ContactHelper:


    def __init__(self, app):
        self.app = app


    def create_contact(self, contact):
        wd = self.app.wd
        # click button Login
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nick_name)
        # Submit Click
        self.submit_create_contact()
        # return Home Page
        self.return_Home()


    def submit_create_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()


    def return_Home(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()


    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("Delete").click()
        wd.switch_to.alert.accept()
        wd.find_element_by_link_text("home").click()


    def edit_first_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nick_name)
        wd.find_element_by_xpath("//div[@id='content']/form/input[22]").click()
        wd.find_element_by_link_text("home").click()






