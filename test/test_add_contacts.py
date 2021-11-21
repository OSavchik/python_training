# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.contact.create_contact(Contact(first_name="FirstName", middle_name="MiddleName", last_name="LastName", nick_name="NickeName"))

def test_add_empty_contact(app):
    app.contact.create_contact(Contact(first_name=" ", middle_name=" ", last_name=" ", nick_name=" "))


