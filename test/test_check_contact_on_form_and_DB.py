from model.contact import Contact

def test_check_contact_on_form_and_DB(app, db):
    form_contacts = app.contact.get_contact_list()
    db_contacts = db.get_contact_list()
    assert sorted(form_contacts, key=Contact.id_or_max) == sorted(db_contacts, key=Contact.id_or_max)
