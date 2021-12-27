from model.contact import Contact
import re

def test_check_contact_on_form_and_DB(app, db):
    form_contacts = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    db_contacts = sorted(db.get_contact_list(), key=Contact.id_or_max)
    assert sorted(form_contacts, key=Contact.id_or_max) == sorted(db_contacts, key=Contact.id_or_max)
    count_elements = len(form_contacts)
    element=0
    while element < count_elements:
        contact_from_form = form_contacts[element]
        contact_from_DB = db_contacts[element]
        assert str(contact_from_form.first_name).strip() == str(contact_from_DB.first_name).strip()
        assert str(contact_from_form.last_name).strip() == str(contact_from_DB.last_name).strip()
        assert str(contact_from_form.address_name).strip() == str(contact_from_DB.address_name).strip()
        email_db_form = [contact_from_DB.email, contact_from_DB.email2, contact_from_DB.email3]
        assert contact_from_form.all_email == app.contact.merge_fields_on_home_page(email_db_form)
        all_phones_db_form = [contact_from_DB.home_phone, contact_from_DB.mobil_phone,
                                contact_from_DB.work_phone, contact_from_DB.secondary_phone]
        assert contact_from_form.all_phones_from_home_page == app.contact.merge_fields_on_home_page(all_phones_db_form)
        element = element + 1







