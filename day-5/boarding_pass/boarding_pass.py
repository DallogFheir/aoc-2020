import re

class BoardingPass:
    bpass_string_pattern = re.compile(r"^[FB]{7}[LR]{3}$")
    seat_id_range = range(1024)

    correspondences = {
        "row" : ("FB","01"),
        "col" : ("LR","01")
    }
    letter_to_digit = {
        axis : str.maketrans(*trans)
        for axis, trans in correspondences.items()}
    digit_to_letter = {
        axis : str.maketrans(*reversed(trans))
        for axis, trans in correspondences.items()}

    def __init__(self,arg):
        '''
        Creates a BoardingPass object.

        Arg can either of the following:

        * boarding pass string in the format XXXXXXXYYY, where X is either "F" or "B", and Y is either "L" or "R"

        * seat ID as an integer in the range 0-1023 inclusive
        '''

        if isinstance(arg,str) and re.fullmatch(self.bpass_string_pattern,arg):
            self._from_bpass_string(arg)

        elif isinstance(arg,int) and arg in self.seat_id_range:
            self._from_seat_id(arg)
        
        else:
            raise ValueError("Invalid input.")

    def _from_bpass_string(self,bpass_string):
        # boarding pass string : FBFBBFFRLR
        # row spot : FBFBBFF
        # column spot : RLR
        self.bpass_string = bpass_string

        self.row_string = bpass_string[:7]
        self.row_number = self._string_to_number(self.row_string,"row")
        
        self.col_string = bpass_string[7:]
        self.col_number = self._string_to_number(self.col_string,"col")

        self.id = self.row_number * 8 + self.col_number

    def _from_seat_id(self,id):
        # id = 8 * row + col
        # col = id - 8 * row
        # 0 <= col <= 7
        # id/8 - 7/8 <= row <= id/8
        #
        # to prove:
        # id/8 - id//8 <= 0.875
        #
        # id/8 = id//8 + r/8
        # id//8 = id/8 - (id%8)/8
        # >
        # (id%8)/8 <= 0.875
        # id%8 <= 7
        # QED

        self.id = id

        self.row_number = id // 8
        self.row_string = self._number_to_string(self.row_number,"row")

        self.col_number = id - 8 * self.row_number
        self.col_string = self._number_to_string(self.col_number,"col")

        self.bpass_string = self.row_string + self.col_string

    def _number_to_string(self,num,axis):
        fillers = {
            "row" : 7,
            "col" : 3
        }

        return bin(num)[2:].zfill(fillers[axis]).translate(self.digit_to_letter[axis])

    def _string_to_number(self,string,axis):
        return int(
            string.translate(self.letter_to_digit[axis]),
            2
        )

    @classmethod
    def parse_bpasses(cls,txt):
        boarding_passes = []

        for line in txt.split("\n"):
            boarding_passes.append(cls(line.strip()))

        return boarding_passes
