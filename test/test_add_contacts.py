# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits #+ string.punctuation + " "*2
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
        Contact(first_name=first_name, middle_name=middle_name, last_name=last_name, nick_name=nick_name)
        for first_name in ["", random_string("first_name", 10)]
        for middle_name in ["", random_string("middle_name", 20)]
        for last_name in ["", random_string("last_name", 20)]
        for nick_name in ["", random_string("nick_name", 20)]
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])

def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_add_empty_contact(app):
  #  old_contacts = app.contact.get_contact_list()
  #  contact = Contact(first_name="", middle_name="", last_name="", nick_name="")
  #  app.contact.create_contact(contact)
  #  new_contacts = app.contact.get_contact_list()
  #  assert len(old_contacts) + 1 == len(new_contacts)
  #  old_contacts.append(contact)
  #  assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




