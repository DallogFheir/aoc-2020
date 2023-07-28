class CustomsForm:
    def __init__(self,forms):
        self.forms = [set(form) for form in forms.split("\n")]
        self.group_size = len(self.forms)

        self.questions_anyone_answered = set.union(*self.forms)

        self.questions_everyone_answered = set.intersection(*self.forms)

    @classmethod
    def parse_forms(cls,file_handle):
        groups = file_handle.read().split("\n\n")

        return [cls(group) for group in groups]
