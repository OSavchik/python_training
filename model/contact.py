from sys import maxsize

class Contact:


    def __init__(self, first_name=None, middle_name=None, last_name=None, nick_name=None,
                 company_name=None, title_name=None, address_name=None,
                 home_phone = None, mobil_phone = None, work_phone = None, secondary_phone = None,
                 fax=None, email=None, email2=None, email3=None,
                 all_phones_from_home_page=None, id=None,
                 all_fields_on_view_form = None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nick_name = nick_name
        self.company_name = company_name
        self.title_name = title_name
        self.address_name = address_name
        self.home_phone = home_phone
        self.mobil_phone = mobil_phone
        self.work_phone = work_phone
        self.secondary_phone = secondary_phone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.id = id
        self.all_fields_on_view_form = all_fields_on_view_form

    def __repr__(self):
        return "%s:%s:%s:%s:%s" % (self.id, self.first_name, self.middle_name,  self.last_name, self.nick_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
