import re


class Phones:
    def __init__(self, phone):
        if self.valid_phone(phone):
            self.number = phone
        else:
            raise ValueError("O Número está incorreto!")

    def valid_phone(self, phone):
        pattern = "([0-9]{2,3})([0-9]{2})([0-9]{4,5})([0-9]{4})"
        answer = re.findall(pattern, phone)
        if answer:
            return True
        else:
            return False

    def formating_phone(self):
        pattern = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        answer = re.search(pattern, self.phone)
        phone_formated = "+{}({}){}-{}".format(
            answer.group(1),
            answer.group(2),
            answer.group(3),
            answer.group(4)
        )
        return phone_formated