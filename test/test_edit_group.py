from model.group import Group
from random import randrange
import random

#def test_edit_group(app):
      #  if app.group.count() == 0:
       #         app.group.create(Group(name="NEW_GROUP", header="NEW_GROUP", footer="NEW_GROUP"))
      #  old_groups = app.group.get_group_list()
       # group = Group(name="EDIT_GROUP")
      #  group.id = old_groups[0].id
       # app.group.edit_first_group(group)
       # assert len(old_groups) == app.group.count()
       # new_groups = app.group.get_group_list()
       # old_groups[0] = group
       # assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_edit_some_group(app, db, check_ui):
        if len(db.get_group_list()) == 0:
                app.group.create(Group(name="NEW_GROUP", header="NEW_GROUP", footer="NEW_GROUP"))
        old_groups = db.get_group_list()
        index = random.choice(old_groups)
        i = 0
        for index_element in old_groups:
                if index_element.id == index.id:
                        break
                else:
                    i = i + 1
        group = Group(name="EDIT_GROUP")
        group.id = old_groups[i].id
        app.group.edit_group_by_id(index.id, group)
        assert len(old_groups) == app.group.count()
        new_groups = db.get_group_list()
        old_groups[i] = group
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)






