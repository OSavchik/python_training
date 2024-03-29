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
        wd.find_element_by_css_selector('input[type="submit"]').click()
       # wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        # Logout
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user")

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, user):
        wd = self.app.wd
        return self.get_logged_user() == user

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div/div[1]/form/b").text[1:-1]

    def ensure_authorization(self, user, secret):
        wd = self.app.wd
        if self.is_logged_in():
             if self.is_logged_in_as(user):
                 return
             else:
                 self.logout()
        self.authorization(user, secret)

