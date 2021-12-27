# -*- coding: utf-8 -*-
from fixture.db import DbFixture
from model.contact import Contact
from model.group import Group
import random

def test_del_contact_db(app, db):
    if len(db.get_group_list()) == 0:
            app.group.create(Group(name="NEW_GROUP", header="NEW_GROUP", footer="NEW_GROUP"))
    group_with_name = db.search_not_empty_group()
    if group_with_name == None or group_with_name == '':
        app.group.create(Group(name="NEW_GROUP", header="NEW_GROUP", footer="NEW_GROUP"))
    contact_with_group = db.get_first_contact_with_group()
    if len(contact_with_group) == 0:
        app.contact.create_contact(Contact(first_name="first_name", middle_name="middle_name", last_name="last_name"))
        contact_with_group = db.get_first_contact_with_group()
    index = random.choice(contact_with_group)
    id_contact = index[0]
    id_group = index[1]
    name_group = index[2]
    app.contact.delete_contact_from_group(id_contact, id_group, name_group)
    find_contact = db.get_contact_by_index_db(id_contact)
    assert find_contact == None
