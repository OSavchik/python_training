import re
from random import randrange

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list(0)[0]
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
    index = 0
    contact_from_view_page_by_index = app.contact.get_contact_list(index)[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    fields_view_form = [contact_from_view_page_by_index.last_name, contact_from_view_page_by_index.first_name, contact_from_view_page_by_index.address_name,
                        contact_from_view_page_by_index.all_email, contact_from_view_page_by_index.all_phones_from_home_page ]
    str_fields_view_form = merge_all_fields_on_home_page_test(fields_view_form)
    str_fields_view_form = re.sub(r'\s+', '', str_fields_view_form).replace(' ', '')
    fields_edit_form = [contact_from_edit_page.last_name, contact_from_edit_page.first_name, contact_from_edit_page.address_name,
                        contact_from_edit_page.email+contact_from_edit_page.email2+contact_from_edit_page.email3,
                        contact_from_edit_page.all_phones_from_home_page]
    str_fields_edit_form = merge_all_fields_on_home_page_test(fields_edit_form)
    str_fields_edit_form = re.sub(r'\s+', '', str_fields_edit_form).replace(' ', '')
    assert str_fields_view_form == str_fields_edit_form


def clear(s):
    return re.sub("[() -]", "", s)

def merge_all_fields_on_home_page_test(fiels_by_contact):
    return "".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       fiels_by_contact))))




