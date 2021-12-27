# -*- coding: utf-8 -*-
from model.group import Group


def test_add_contact_db(app, db, json_contacts):
    if len(db.get_group_list()) == 0:
            app.group.create(Group(name="NEW_GROUP", header="NEW_GROUP", footer="NEW_GROUP"))
    group_with_name = db.search_not_empty_group()
    if group_with_name == None:
        app.group.create(Group(name="NEW_GROUP", header="NEW_GROUP", footer="NEW_GROUP"))
    contact = json_contacts
    app.contact.create_contact(json_contacts)
    Max_contact_index = db.get_max_contact_index_db()
    find_contact = db.get_contact_by_index_db(str(Max_contact_index[0]))
    assert find_contact[1] == contact.first_name
    assert str(find_contact[2]) == contact.middle_name
    assert find_contact[3] == contact.last_name
    assert find_contact[4] == contact.nick_name


