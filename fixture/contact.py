from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_contact(self, new_contact):
        wd = self.app.wd
        # add new contact
        wd.find_element_by_link_text("add new").click()
        # Fill form for contact
        self.fill_contact_form(new_contact)
        # Submit Click
        self.submit_create_contact()
        # return Home Page
        self.return_Home()

    def submit_create_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.middle_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("nickname", contact.nick_name)

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def return_Home(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.return_Home()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[22]").click()
        self.return_Home()

    def count(self):
        wd = self.app.wd
        self.return_Home()
        wd.find_element_by_name("searchstring")
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.return_Home()
        contacts = []
        countcontacts = int(wd.find_element_by_xpath("// *[ @ id = 'search_count']").text)
        for i in range(2, countcontacts + 2):
            css_str = "#maintable > tbody:nth-child(1) > tr:nth-child(" + str(i) + ")"
            css_child_str = "#maintable > tbody:nth-child(1) > tr:nth-child(" + str(i) + ")" + " > td:nth-child(2)"
            for element in wd.find_elements_by_css_selector(css_str):
                id = element.find_element_by_name("selected[]").get_attribute("value")
            for element in wd.find_elements_by_css_selector(css_child_str):
                text = element.text
            contacts.append(Contact(last_name=text, id=id))
        return contacts






