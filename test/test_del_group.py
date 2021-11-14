def test_delete_first_group(app):
    app.session.authorization(user="admin", secret="secret")
    app.group.delete_first_group()
    app.session.logout()