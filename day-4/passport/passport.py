import re

class Passport:
    requirements = {
        # field : data validation
        "byr" : re.compile(r"19[2-9]\d|200[0-2]"), # 1920-2002 inclusive
        "iyr" : re.compile(r"201\d|2020"), # 2010-2020 inclusive
        "eyr" : re.compile(r"202\d|2030"), # 2020-2030 inclusive
        "hgt" : re.compile(r"((1[5-8]\d|19[0-3])cm)|((59|6\d|7[0-6])in)"), # 150-193cm inclusive, or 59-76in inclusive
        "hcl" : re.compile(r"#[a-f\d]{6}"), # # followed by hex number (0-9, a-f)
        "ecl" : re.compile(r"amb|blu|brn|gry|grn|hzl|oth"),
        "pid" : re.compile(r"\d{9}") # 9 digits
    }
    required_fields = set(requirements.keys())
    optional_fields = {"cid"}
    all_fields = required_fields | optional_fields

    def __init__(self,**data):
        self.data = data
        self.fields = set(data.keys())

    def validate_fields(self):
        '''
        Checks if passport contains all required fields.
        '''

        return self.required_fields.issubset(self.fields)

    def validate_data(self):
        '''
        Checks if passport data is valid.
        '''

        return all(
            re.fullmatch(self.requirements[field],datum)
            for field, datum in self.data.items()
            if field in self.requirements)

    def validate(self):
        return self.validate_fields() and self.validate_data()

    @classmethod
    def parse_passports(cls,txt):
        # {field_name}:{data}
        # separated by space or newline, or end of string
        regex = re.compile(fr"""
        ({'|'.join(cls.all_fields)}):(.*?)(?:\ |\n|$)
        """,
        re.X)

        # passports are separated by an empty line
        passports_input = txt.split("\n\n")
        passports = []
        for passport in passports_input:
            fields = dict(re.findall(regex,passport))
            passports.append(cls(**fields))

        return passports
