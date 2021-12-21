# -*- coding: utf-8 -*-
from fixture.db import DbFixture

def test_del_contact_db(app, db):
    db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    try:
        contact_with_group = db.get_first_contact_with_group()
        if len(contact_with_group) == 0:
            print("Нет контактов связанных с группами")
        else:
            app.contact.delete_contact_by_id(contact_with_group[0])
            find_contact = db.get_contact_by_index_db(contact_with_group[0])
            assert find_contact == None

    finally:
        db.destroy()