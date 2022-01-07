import re
from random import randrange

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_by_index(0)
    str_phones_view_form = re.sub(r'\s+', '', contact_from_home_page.all_phones_from_home_page).replace(' ', '')
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    phones_edit_form = [contact_from_edit_page.all_phones_from_home_page]
    str_phones_edit_form = merge_all_fields_on_home_page_test(phones_edit_form)
    str_phones_edit_form = re.sub(r'\s+', '', str_phones_edit_form).replace(' ', '')
    assert str_phones_view_form == str_phones_edit_form

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_Page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
    assert contact_from_view_page.mobil_phone == contact_from_edit_page.mobil_phone
    assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
    assert contact_from_view_page.secondary_phone == contact_from_edit_page.secondary_phone

def test_data_on_contact_view_page_by_index(app):
    all_contacts = app.contact.count_elements_in_contact_list()
    index = randrange(all_contacts)
    contact_from_view_page_by_index = app.contact.get_contact_by_index(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert str(contact_from_view_page_by_index.last_name).strip() == str(contact_from_edit_page.last_name).strip()
    assert str(contact_from_view_page_by_index.first_name).strip() == str(contact_from_edit_page.first_name).strip()
    assert str(contact_from_view_page_by_index.address_name).strip() == str(contact_from_edit_page.address_name).strip()
    assert contact_from_view_page_by_index.all_email.replace(' ', '') == merge_emails_like_on_home_page(contact_from_edit_page).replace(' ', '')
    assert contact_from_view_page_by_index.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_all_fields_on_home_page_test(fiels_by_contact):
    return "".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       fiels_by_contact))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3])))

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobil_phone, contact.work_phone, contact.secondary_phone]))))










