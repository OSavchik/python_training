from model.contact import Contact

def test_edit_contact(app):
    app.session.authorization(user="admin", secret="secret")
    app.contact.edit_first_contact(Contact(first_name="EditName", middle_name="EditMiddleName", last_name="EditLastName", nick_name="EditNickeName"))
    app.session.logout()

