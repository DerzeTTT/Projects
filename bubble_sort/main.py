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
Julia Soska 5 5 5 5 5 5 5 5''');

Reading = int(Custom_Input.read());
Students_Info = [];

for i in range(Reading):

    Students_Info.append(Custom_Input.read());

class Student_Factory:

    def __init__(self):

        self.Grades = [];
        self.Full_Name = "";

    def Parse(self, T_Str):

        Split_Info = T_Str.split(" ");

        #Parsing full name
        self.Full_Name = f"{Split_Info[0]} {Split_Info[1]}"

        #Parsing grades
        for i in range(2, len(Split_Info)):

            self.Grades.append(int(Split_Info[i]));

    def Get_Average(self):

        Total = 0;

        for v in self.Grades:

            Total += v;

        Final_Product = Total/len(self.Grades);

        return Final_Product;

    def __str__(self):

        return f"{self.Full_Name} {round(self.Get_Average(), 2)}"

Students = [];

for v in Students_Info:

    New_Student = Student_Factory();
    New_Student.Parse(v);

    New_Student.Get_Average();

    Students.append(New_Student);

def Bubble_Sort(T_Arr):

    Arr = T_Arr;

    n = len(Arr);

    for i in range(0,n):

        Swapped = False;

        for element in range(0,n-i-1):

            if Arr[element].Get_Average() > Arr[element+1].Get_Average():

                hold = Arr[element+1];

                Arr[element+1]=Arr[element];
                Arr[element] = hold;
                
                Swapped = True;
            
            if not Swapped: break;

    return Arr;

Ordered_Students = Bubble_Sort(Students);

for i in range(len(Ordered_Students)-1, -1, -1):

    print(Ordered_Students[i]);