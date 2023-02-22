class Artificial_Input:

    def __init__(self):

        self.Holding = [];
        self.Reading = 0;

        self.Production = False;

    def add_input(self, new_input, split_lines=True):

        Appending = None;

        if type(new_input) is str and split_lines:

            Appending = new_input.split("\n");

        elif type(new_input) is list:

            Appending = new_input;

        else:

            raise Exception("Given value is not a string or list!")

        self.Holding += Appending;

    def read(self):

        if not self.Production:

            Returning = self.Holding[self.Reading];
            self.Reading += 1;

            return Returning;
        
        else:

            return input();

Custom_Input = Artificial_Input();

Custom_Input.Production = False;

Custom_Input.add_input('''4
Jan Kowalski 5 6 5 4 6 5
Anna Nowak 3 4 2 5 3 4
Piotr Testowski 1 1 3 1 5
Julia Soska 5 5 5 5 5 5 5 5
''')

Reading = int(Custom_Input.read());

for i in range(Reading):

    print("Lol", Custom_Input.read());