# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application



@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
        app.authorization(user="admin", secret="secret")
        app.create_new_group(Group(name="NEW_GROUP", header="NEW_GROUP", footer="NEW_GROUP"))
        app.logout()



def test_add_empty_group(app):
        app.authorization(user="admin", secret="secret")
        app.create_new_group(Group(name="name", header="header", footer="footer"))
        app.logout()

