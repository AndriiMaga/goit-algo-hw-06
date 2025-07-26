from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError('Name cannot be empty')
        self.value = value

class Phone(Field):
    def __init__(self, value):
        if value.isdigit() and len(value) == 10:
            self.value = value
        else:
            raise ValueError("Phone number must be 10 digits")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        new_phone = Phone(phone)
        self.phones.append(new_phone)

    def remove_phone(self, phone):
        for phone_obj in self.phones:
            if phone_obj.value == phone:
                self.phones.remove(phone_obj)
                break

    def edit_phone(self, old_phone, new_phone):
        new_phone_digits = Phone(new_phone)
        for phone_obj in self.phones:
            if phone_obj.value == old_phone:
                phone_obj.value = new_phone_digits.value
                return
        raise ValueError("Old phone number not found")

    def find_phone(self, phone):
        for phone_obj in self.phones:
            if phone_obj.value == phone:
                return phone_obj
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            return self.data.pop(name)
        else:
            raise KeyError(f"Contact: '{name}' not found")

    def __str__(self):
        if not self.data:
            return "Address book is empty"
        return "\n".join(map(str, self.data.values()))
