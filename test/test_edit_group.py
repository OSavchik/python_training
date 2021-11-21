from model.group import Group

def test_edit_group(app):
        app.group.edit_first_group(Group(name="EDIT_GROUP"))

def test_edit_group1(app):
        app.group.edit_first_group(Group(header="EDIT_header"))

def test_edit_group2(app):
        app.group.edit_first_group(Group(footer="EDIT_footer"))

