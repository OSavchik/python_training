from selenium.common.exceptions import NoSuchElementException

from model.contact import Contact
from selenium.webdriver.support.ui import Select
import re

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
        self.contact_cache = None

    def submit_create_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.middle_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("nickname", contact.nick_name)
        self.choice_group()

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

    def choice_group(self):
        wd = self.app.wd
        is_find_group = 0
        try:
            wd.find_element_by_name("new_group")
        except NoSuchElementException:
            return True
        wd.find_element_by_name("new_group").click()
        option_list = Select(wd.find_element_by_name("new_group")).options
        for element in option_list:
            text = element.text
            if (text != None) and (text != '[none]') and (text != ''):
                Select(wd.find_element_by_name("new_group")).select_by_visible_text(text)
                is_find_group = 1
                break

    def return_Home(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_elements_by_xpath("//*[contains(text(), 'Delete record')]")
        wd.find_element_by_css_selector("div.msgbox")
        self.return_Home()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_elements_by_xpath("//*[contains(text(), 'Delete record')]")
        wd.find_element_by_css_selector("div.msgbox")
        self.return_Home()
        self.contact_cache = None

    def edit_first_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        self.select_contact_by_index(0)
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(contact)
        self.return_Home()
        self.contact_cache = None

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[22]").click()
        self.return_Home()
        self.contact_cache = None

    def edit_contact_by_id(self, index, index_element, contact):
        wd = self.app.wd
        self.select_contact_by_id(index)
        wd.find_element_by_xpath(f"(//img[@alt='Edit'])[{index_element + 1}]").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[22]").click()
        self.return_Home()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath(f"(//img[@alt='Edit'])[{index + 1}]").click()

    def view_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def count(self):
        wd = self.app.wd
        self.return_Home()
        wd.find_element_by_name("searchstring")
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def count_elements_in_contact_list(self):
        wd = self.app.wd
        self.return_Home()
        count_elements = 0
        for row in wd.find_elements_by_name("entry"):
            count_elements = count_elements + 1
        return count_elements

    def get_contact_list(self):
            if self.contact_cache is None:
                wd = self.app.wd
                self.return_Home()
                self.contact_cache = []
                for row in wd.find_elements_by_name("entry"):
                    cells = row.find_elements_by_tag_name("td")
                    last_name = cells[1].text
                    first_name = cells[2].text
                    address_name = cells[3].text
                    all_email = cells[4].text
                    id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                    all_phones_from_home_page = cells[5].text
                    self.contact_cache.append(Contact(last_name=last_name, first_name=first_name, id=id, address_name = address_name,
                                                      all_email=all_email, all_phones_from_home_page=all_phones_from_home_page))
            return list(self.contact_cache)

    def get_contact_list_by_index(self, index):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_Home()
            self.contact_cache = []
            row = wd.find_elements_by_name("entry")[index]
            cell = row.find_elements_by_tag_name("td")
            last_name = cell[1].text
            first_name = cell[2].text
            address_name = cell[3].text
            all_email = cell[4].text
            id = cell[0].find_element_by_tag_name("input").get_attribute("value")
            all_phones_from_home_page = cell[5].text
           # self.contact_cache.append(Contact(last_name=last_name, first_name=first_name, id=id,
                                             # address_name=address_name, all_email=all_email,
                                             # all_phones_from_home_page=all_phones_from_home_page))
            return Contact(last_name=last_name, first_name=first_name, id=id,
                                              address_name=address_name, all_email=all_email,
                                              all_phones_from_home_page=all_phones_from_home_page)

      #  return self.contact_cache

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        middle_name = wd.find_element_by_name("middlename").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        nick_name = wd.find_element_by_name("nickname").get_attribute("value")
        company_name = wd.find_element_by_name("company").get_attribute("value")
        title_name = wd.find_element_by_name("title").get_attribute("value")
        address_name = wd.find_element_by_name("address").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        mobil_phone = wd.find_element_by_name("mobile").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        secondary_phone = wd.find_element_by_name("phone2").get_attribute("value")
        all_phones_from_home_page = home_phone + mobil_phone + work_phone + secondary_phone
        fax = wd.find_element_by_name("fax").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        self.return_Home()

        return Contact(first_name = first_name, middle_name = middle_name, last_name = last_name, nick_name = nick_name, id = id,
                       company_name = company_name, title_name = title_name, address_name = address_name,
                       home_phone = home_phone, mobil_phone = mobil_phone, work_phone = work_phone, secondary_phone = secondary_phone,
                       all_phones_from_home_page = all_phones_from_home_page,
                       fax = fax, email = email, email2 = email2, email3 = email3)

    def get_contact_from_view_Page(self, index):
        wd = self.app.wd
        self.view_contact_by_index(index)
        text = wd.find_element_by_id("content").text
        all_fields_on_view_form = text
        home_phone = re.search("H: (.*)", text).group(1)
        mobil_phone = re.search("M: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        secondary_phone = re.search("P: (.*)", text).group(1)
        return Contact(home_phone = home_phone, mobil_phone = mobil_phone, work_phone = work_phone, secondary_phone = secondary_phone, all_fields_on_view_form = all_fields_on_view_form)

    #def merge_emails_on_home_page(contact):
      #  return "\n".join(filter(lambda x: x != "",
      #                          filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))

   # def merge_phones_like_on_home_page(contact):
      #  return "\n".join(filter(lambda x: x != "",
           #                     filter(lambda x: x is not None,
           #                            [contact.home_phone, contact.mobil_phone, contact.work_phone,
            #                            contact.secondary_phone])))

















