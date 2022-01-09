# -*- coding: utf-8 -*-
import allure

from model.contact import Contact

@allure.epic('Действия с контактами')
@allure.feature('Создание контакта')
@allure.description('Создание контакта и сравнение списков контактов перед созданием нового контакта и после его создания')
def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    with allure.step("Получение списка контактов перед созданием нового контакта"):
        old_contacts = db.get_contact_list()
    with allure.step("Создание нового контакта %s" % contact):
        app.contact.create_contact(contact)
    with allure.step("Сравнение списков контактов"):
        assert len(old_contacts) + 1 == app.contact.count()
        new_contacts = db.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)



