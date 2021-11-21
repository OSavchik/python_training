# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
        app.group.create(Group(name="NEW_GROUP", header="NEW_GROUP", footer="NEW_GROUP"))

def test_add_empty_group(app):
        app.group.create(Group(name="name", header="header", footer="footer"))

