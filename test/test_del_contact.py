from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(first_name="FirstName"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts

#def test_delete_first_contact1(app):
   # if app.contact.count() == 0:
    #    app.contact.create_contact(Contact(middle_name="middle_name"))
    #old_contacts = app.contact.get_contact_list()
    #app.contact.delete_first_contact()
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) - 1 == len(new_contacts)
    #old_contacts[0:1] = []
    #assert old_contacts == new_contacts






