class Artificial_Input:

    def __init__(self):

        self.Holding = [];
        self.Reading = 0;

    def add_input(self, new_input, split_lines=True):

        Appending = None;

        if type(new_input) is str and split_lines:

            Appending = new_input.split("\n");

        elif type(new_input) is list:

            Appending = new_input;

        else:

            raise Exception("Given value is not a string or list!")

        self.Holding += Appending;

        print(self.Holding);

    def read(self):

        Returning = self.Holding[self.Reading];
        self.Reading += 1;

        return Returning;

Custom_Input = Artificial_Input();

Custom_Input.add_input('''
''')