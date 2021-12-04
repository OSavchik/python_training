import re
from random import randrange

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_Page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
    assert contact_from_view_page.mobil_phone == contact_from_edit_page.mobil_phone
    assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
    assert contact_from_view_page.secondary_phone == contact_from_edit_page.secondary_phone

def test_data_on_contact_view_page(app):
    all_contacts = app.contact.count_elements_in_contact_list()
    index = randrange(all_contacts)
    contact_from_view_page = app.contact.get_contact_from_view_Page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    contact_from_edit_page.home_phone = str("H:") + contact_from_edit_page.home_phone
    contact_from_edit_page.work_phone = str("W:") + contact_from_edit_page.work_phone
    contact_from_edit_page.mobil_phone = str("M:") + contact_from_edit_page.mobil_phone
    contact_from_edit_page.fax = str("F:") + contact_from_edit_page.fax
    contact_from_view_page.all_fields_on_view_form = re.sub("^\s+|\n|\r|\s+$", '', contact_from_view_page.all_fields_on_view_form)
    contact_from_view_page.all_fields_on_view_form = contact_from_view_page.all_fields_on_view_form.replace(' ', '')
    s = contact_from_view_page.all_fields_on_view_form
    s = s[:s.find('Homepage')].strip()
    s1 = merge_all_fields_on_home_page(contact_from_edit_page)
    s1 = re.sub("^\s+|\n|\r|\s+$", '', s1)
    assert s == s1

def clear(s):
    return re.sub("[() -]", "", s)

def merge_all_fields_on_home_page(Contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [Contact.first_name, Contact.middle_name, Contact.last_name, Contact.nick_name,
                                        Contact.title_name, Contact.company_name , Contact.address_name,
                                        Contact.home_phone, Contact.mobil_phone, Contact.work_phone, Contact.fax,
                                        Contact.email, Contact.email2, Contact.email3]))))

def merge_phones_like_on_home_page(Contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [Contact.first_name, Contact.middle_name, Contact.last_name]))))


