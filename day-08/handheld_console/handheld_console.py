class HandheldConsole:
    allowed_instructions = ("acc", "jmp", "nop")

    def __init__(self,instructions):
        '''
        Creates a Handheld Console™ object from an iterable of instructions. Each element of the iterable should be an iterable with two elements: command and parameter.

        To create a Handheld Console™ object from a file handle, use HandheldConsole.from_file() method.
        '''

        code = []
        for ins in instructions:
            cmd, param = ins

            if cmd not in self.allowed_instructions:
                raise ValueError(f"Command must be one of {self.allowed_instructions}.")
            
            try:
                param = int(param)
            except ValueError:
                raise ValueError("Parameter must be a signed integer.") from None

            code.append([cmd,param])

        self.code = code
        self.accumulator = None

    def execute(self):
        self.accumulator = 0
        already_executed = set()
        i=0

        while True:
            if i in already_executed:
                # print("Handheld Console™ got stuck in infinite loop!")
                return False
            if i==len(self.code):
                # print("Handheld Console™ executed instructions properly!")
                return True

            already_executed.add(i)

            ins = self.code[i]

            if ins[0]=="acc":
                self.accumulator += ins[1]
            elif ins[0]=="jmp":
                i += ins[1]
                continue

            i += 1

    def fix(self):
        for i, line in enumerate(self.code):
            tmp = line[0]

            if tmp!="acc":
                self.code[i][0] = "jmp" if tmp=="nop" else "nop"
            
            if self.execute():
                return f"faulty command = {tmp} at line {i}"

            self.code[i][0] = tmp

    @classmethod
    def from_file(cls,fh):
        instructions = (line.strip().split() for line in fh.readlines())

        return cls(instructions)
