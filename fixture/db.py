import  pymysql.connections
from model.group import Group
from model.contact import Contact

class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.Connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor =  self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor =  self.connection.cursor()
        try:
            cursor.execute(f"select id, firstname, middlename, lastname, nickname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, first_name, middle_name, last_name, nick_name) = row
                list.append(Contact(id=str(id), first_name=first_name, middle_name=middle_name, last_name=last_name, nick_name=nick_name))
        finally:
            cursor.close()
        return list

    def get_max_contact_index_db(self):
        cursor =  self.connection.cursor()
        try:
            cursor.execute("select MAX(a.id) from addressbook a")
            contact_id = cursor.fetchone()
        finally:
            cursor.close()
        return contact_id

    def get_contact_by_index_db(self, index):
        cursor =  self.connection.cursor()
        try:
            cursor.execute(f"select addressbook.id, addressbook.firstname, addressbook.middlename, addressbook.lastname, addressbook.nickname from addressbook\
                             join address_in_groups on addressbook.id = address_in_groups.id and addressbook.id = {index}")
            find_contact_by_index = cursor.fetchone()
        finally:
            cursor.close()
        return find_contact_by_index

    def get_first_contact_with_group(self):
        cursor =  self.connection.cursor()
        try:
            cursor.execute("select addressbook.id, address_in_groups.group_id from addressbook\
                             join address_in_groups on addressbook.id = address_in_groups.id ")
            find_contact_with_group = cursor.fetchone()
        finally:
            cursor.close()
        return find_contact_with_group

    def destroy(self):
        self.connection.close()

