from model.contact import Contact
import random

def test_edit_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(last_name="last_name333"))
    old_contacts = app.contact.get_contact_list()
    index = random.choice(old_contacts)
    i = app.get_serial_number_element_by_id(old_contacts, index.id)
    contact = Contact(last_name="last_name444")
    contact.id = old_contacts[i].id
    app.contact.edit_contact_by_id(index.id,  i, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts[i] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)



