# -*- coding: utf-8 -*-
from model.group import Group
import allure

@allure.epic('Действия с группами')
@allure.feature('Создание групп')
@allure.description('Создание группы и сравнение списков групп перед созданием новой группы и после ее создания')
def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    with allure.step("Получение списка групп до создания новой группы" ):
        old_groups  = db.get_group_list()
    with allure.step("Создание группы %s " % group ):
        app.group.create(group)
    with allure.step("Получение нового списка групп после создания группы"):
        new_groups = db.get_group_list()
    with allure.step("Добавление новой группы в список, сформированный до создания группы"):
        old_groups.append(group)
    with allure.step("Сравнение полученных списков"):
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)



