from model.group import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="NEW_GROUP", header="NEW_GROUP", footer="NEW_GROUP"))
    app.group.delete_first_group()
