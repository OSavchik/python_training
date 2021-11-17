from model.group import Group

def test_edit_group(app):
        app.session.authorization(user="admin", secret="secret")
        app.group.edit_first_group(Group(name="EDIT_GROUP", header="EDIT_GROUP", footer="EDIT_GROUP"))
        app.session.logout()

def test_edit_group1(app):
        app.session.authorization(user="admin", secret="secret")
        app.group.edit_first_group(Group(name="EDIT_GROUP1", header="EDIT_GROUP1", footer="EDIT_GROUP1"))
        app.session.logout()