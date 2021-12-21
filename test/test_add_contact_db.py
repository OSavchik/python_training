# -*- coding: utf-8 -*-
from fixture.db import DbFixture


def test_add_contact_db(app, db, json_contacts):
    db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    try:
        Max_contact_index = db.get_max_contact_index_db()
        contact = json_contacts
        app.contact.create_contact(json_contacts)
        find_contact = db.get_contact_by_index_db(str(Max_contact_index[0] + 1))
        assert find_contact[1] == contact.first_name
        assert str(find_contact[2]) == contact.middle_name
        assert find_contact[3] == contact.last_name
        assert find_contact[4] == contact.nick_name
    finally:
        db.destroy()

