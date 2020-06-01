class SQLite_Secure():

    def __init__(self):
        pass

    def Check(self,Check_String):

        if('--' in Check_String):
            Check_String=Check_String.replace('--','')

        if('\'' in Check_String):
            Check_String = Check_String.replace('\'', '"')

        return Check_String




