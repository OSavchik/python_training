from model.contact import Contact

def test_edit_name_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(first_name="FirstName"))
    app.contact.edit_first_contact(Contact(first_name="EditName"))

def test_edit_middlename_contact1(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(first_name="FirstName"))
    app.contact.edit_first_contact(Contact(middle_name="EditMiddleName"))

def test_edit_lastname_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(first_name="FirstName"))
    app.contact.edit_first_contact(Contact(last_name="EditLastName"))

def test_edit_nickname_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(first_name="FirstName"))
    app.contact.edit_first_contact(Contact(nick_name="EditNickeName"))

