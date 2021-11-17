class SessionHelper:

    def __init__(self, app):
        self.app = app

    def authorization(self, user, secret):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(secret)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        # Logout
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user")