import Utilities

def Handle_Operator(Operator, First, Second):

    return eval(f"{First.Decimal}{Operator}{Second.Decimal}");

class RSys:

    def __init__(self, R_Num):

        self.Roman = R_Num;
        self.Decimal = Utilities.Convert("Arabic", R_Num);

    def __str__(self):

        return f"{self.Roman} ({str(self.Decimal)})";

    def __gt__(self, Comparing):

        return Handle_Operator(">", self, Comparing);

    def __lt__(self, Comparing):

        return Handle_Operator("<", self, Comparing);

    def __eq__(self, Comparing):

        return Handle_Operator("==", self, Comparing);

    def __add__(self, Comparing):

        return Handle_Operator("+", self, Comparing);
    
    def __sub__(self, Comparing):

        return Handle_Operator("-", self, Comparing);

    def __mul__(self, Comparing):

        return Handle_Operator("*", self, Comparing);

    def __truediv__(self, Comparing):

        return Handle_Operator("/", self, Comparing);

R1 = RSys("XV");
R2 = RSys("XVI");

print(R2);
print(R2 > R1, R1 < R2, R2 * R1, R2 / R1, R2 + R1, R2 - R1);
#ok