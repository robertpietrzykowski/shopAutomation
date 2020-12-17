from random import randint, choice
import re
import string
import rstr


class DataGenerator:
    phone_number_reg = r'^[1-9][0-9]{8,12}(#[0-9]{1,6}?$)'
    mobile_number_reg = r'^[1-9][0-9]{8,12}$'
    improper_phone_number_regs = [r'^\+[1-9][0-9]{0,2} 0[0-9]{8,12}(#[0-9]{1,6}?$)',
                               r'^[0-9]{8,12}(#[0-9]{1,6}?$)',
                               r'^\+[1-9][0-9]{3,4} [1-9][0-9]{8,12}(#[0-9]{1,6}?$)',
                               r'^\+[1-9][0-9]{0,2} [1-9][0-9]{13,15}(#[0-9]{1,6}?$)']
    improper_mobile_number_regs = [r'^\+[1-9][0-9]{0,2} 0[0-9]{8,12}$',
                                r'^\+[1-9][0-9]{3,5} [1-9][0-9]{8,12}$',
                                r'^\+[1-9][0-9]{0,2} [1-9][0-9]{13,15}$']

    @staticmethod
    def generate_proper_name(min_length=1, max_length=35):
        return rstr.rstr(string.ascii_letters, min_length, max_length).strip().replace('  ', '')

    def generate_wrong_name(self, max_length=35):
        case = randint(1, 2)
        if case == 1:
            improper_characters = '!@#$%^&*()_+=[]{}\|/?;:.,><`~'
            return 'chars', \
                   rstr.rstr(string.ascii_letters + " '-" + string.digits, 1, max_length,
                             include=choice(improper_characters)).strip()
        else:
            return 'length', \
                   self.generate_proper_name(min_length=max_length + 1, max_length=max_length + 5)

    @staticmethod
    def generate_proper_email():
        improper_dot_pattern = re.compile('^\.')  # to verify if dot is not on beginning of returned string
        while True:
            email = '{0}{1}@{2}.{3}'.format(choice(string.ascii_letters),
                                            rstr.rstr(string.ascii_letters + string.digits + '-_.', 2, 20),
                                            rstr.rstr(string.ascii_letters + string.digits),
                                            choice(['pl', 'com', 'net', 'uk', 'gov', 'us']))
            if not improper_dot_pattern.match(email):
                return email

    @staticmethod
    def generate_wrong_email():
        improper_characters = '\():;"><[]@~ \t\n\r\x0b\x0c'
        case = randint(1, 2)
        if case == 1:
            return '{0}@{1}.{2}'.format(rstr.rstr(string.printable, include=choice(improper_characters),
                                                  exclude='\n\t\r"'),
                                        rstr.rstr(string.printable, include=choice(improper_characters),
                                                  exclude='\n\t\r"'),
                                        choice(['pl', 'com', 'net', 'uk', 'gov', 'us']))
        else:
            return rstr.rstr(string.printable, exclude='\n\t\r"')

    def generate_proper_phone_number(self):
        return rstr.xeger(self.phone_number_reg)

    def generate_wrong_phone_number(self):
        case = randint(1, 2)
        if case == 1:
            return rstr.xeger(choice(self.improper_phone_number_regs))
        else:
            return rstr.rstr(string.printable, include=choice(string.ascii_letters), exclude='\n\t\r"')

    def generate_proper_mobile_number(self):
        return rstr.xeger(self.mobile_number_reg)

    def generate_wrong_mobile_number(self):
        case = randint(1, 2)
        if case == 1:
            return rstr.xeger(choice(self.improper_mobile_number_regs))
        else:
            return rstr.rstr(string.printable, include=choice(string.ascii_letters), exclude='\n\t\r"')
