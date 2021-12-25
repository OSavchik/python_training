# -*- coding: utf-8 -*-
from fixture.db import DbFixture
from model.contact import Contact
from model.group import Group

def test_del_contact_db(app, db):
    db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    try:
        if len(db.get_group_list()) == 0:
                app.group.create(Group(name="NEW_GROUP", header="NEW_GROUP", footer="NEW_GROUP"))
        group_with_name = db.search_not_empty_group()
        if group_with_name == None:
            app.group.create(Group(name="NEW_GROUP", header="NEW_GROUP", footer="NEW_GROUP"))
        contact_with_group = db.get_first_contact_with_group()
        if contact_with_group == None:
            app.contact.create_contact(Contact(first_name="first_name", middle_name="middle_name", last_name="last_name"))
        contact_with_group = db.get_first_contact_with_group()
        app.contact.delete_contact_by_id(contact_with_group[0])
        find_contact = db.get_contact_by_index_db(contact_with_group[0])
        assert find_contact == None
        link_group_with_contact = db.delete_link_group_with_contact(contact_with_group[0])
        assert link_group_with_contact == None
        find_link_group_with_contact = db.find_link_group_with_contact(contact_with_group[0])
        assert find_link_group_with_contact == None
    finally:
        db.destroy()
