from model.group import Group

def test_edit_group(app):
        if app.group.count() == 0:
                app.group.create(Group(name="NEW_GROUP", header="NEW_GROUP", footer="NEW_GROUP"))
        app.group.edit_first_group(Group(name="EDIT_GROUP"))

def test_edit_group1(app):
        if app.group.count() == 0:
                app.group.create(Group(name="NEW_GROUP", header="NEW_GROUP", footer="NEW_GROUP"))
        app.group.edit_first_group(Group(header="EDIT_header"))

def test_edit_group2(app):
        if app.group.count() == 0:
                app.group.create(Group(name="NEW_GROUP", header="NEW_GROUP", footer="NEW_GROUP"))
        app.group.edit_first_group(Group(footer="EDIT_footer"))

