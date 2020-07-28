class SQLite_Secure():

    def __init__(self):
        pass

    def Check(self,Check_String):

        try:

            if '--' in Check_String:
                Check_String=Check_String.replace('--','')

            if '\'' in Check_String:
                Check_String = Check_String.replace('\'', '"')

            if ';' in Check_String:
                Check_String = Check_String.replace(';', '')

            Check_String=Check_String+';'

        except Exception as Errr:
            raise Errr

        return Check_String




