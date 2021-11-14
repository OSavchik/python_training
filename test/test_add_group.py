# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application



@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
        app.session.authorization(user="admin", secret="secret")
        app.group.create(Group(name="NEW_GROUP", header="NEW_GROUP", footer="NEW_GROUP"))
        app.session.logout()



def test_add_empty_group(app):
        app.session.authorization(user="admin", secret="secret")
        app.group.create(Group(name="name", header="header", footer="footer"))
        app.session.logout()

