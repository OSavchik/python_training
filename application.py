from selenium import webdriver


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")


    def authorization(self, user, secret):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(secret)


    def open_group(self):
        wd = self.wd
        wd.find_element_by_xpath("//input[@value='Login']").click()


    def create_new_group(self, group):
        wd = self.wd
        self.open_group()
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


    def create_contact(self, Contact):
        wd = self.wd
        # click button Login
        wd.find_element_by_xpath("//input[@value='Login']").click()
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
        # Submit Click
        self.submit_create_contact()
        # return Home Page
        self.return_Home()


    def submit_create_contact(self):
        wd = self.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()


    def return_Home(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()


    def logout(self):
        # Logout
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()


    def destroy(self):
        self.wd.quit()
