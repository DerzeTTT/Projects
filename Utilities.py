Roman_Numerals = {
    
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000

};

Roman_Order = {

    1:'I',
    2:'V',
    3:'X',
    4:'L',
    5:'C',
    6:'D',
    7:'M'

};

def Convert(New_Type, Val):

    if New_Type == "Roman":

        New_Str = '';
        Rest = Val;
        
        for Key in range(len(Roman_Order), 0, -1):

            Numeral = Roman_Order[Key];
            Div = Roman_Numerals.get(Numeral);

            while (Rest >= Div):

                Rest -= Div;
                New_Str += Numeral;

        return New_Str;

    elif New_Type == "Arabic":

         Chars = list(str(Val));
         Total = 0;

         for Key in range(len(Chars)):

            Current = Roman_Numerals.get(Chars[Key]);

            try:

                Next_Num = Roman_Numerals.get(Chars[Key+1]);

            except:

                Next_Num = False;

            Adding = True;

            if Next_Num and Current < Next_Num:

                Adding = False;

            if Adding:

                Total += Current;

            else:

                Total -= Current;

         return Total;