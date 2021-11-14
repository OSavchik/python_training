# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.authorization(user="admin", secret="secret")
    app.create_contact(Contact(first_name="FirstName", middle_name="MiddleName", last_name="LastName", nick_name="NickeName"))
    app.logout()


def test_add_empty_contact(app):
    app.authorization(user="admin", secret="secret")
    app.create_contact(Contact(first_name=" ", middle_name=" ", last_name=" ", nick_name=" "))
    app.logout()


