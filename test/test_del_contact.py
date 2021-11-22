from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(first_name="FirstName"))
    app.contact.delete_first_contact()

def test_delete_first_contact1(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(middle_name="middle_name"))
    app.contact.delete_first_contact()



