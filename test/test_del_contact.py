def test_delete_first_contact(app):
    app.session.authorization(user="admin", secret="secret")
    app.contact.delete_first_contact()
    app.session.logout()