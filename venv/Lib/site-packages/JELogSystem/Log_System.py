import datetime


class Log_System():
    '''
    預設廣播等級 : 3
    預設紀錄時間
    Normal : 0
    Debug : Debug 1
    Info : Info 2
    Warning : 3
    Error : 4
    Critical : 5
    '''

    def __init__(self):

        self.Normal_Lv = 0

        self.Debug_Lv = 1

        self.Info_Lv = 2

        self.Warning_Lv = 3

        self.Error_Lv = 4

        self.Critical_Lv = 5

        self.BoardCast_Lv = 3

        self.Time = True

    # ----------------------------------------------------------------------------------------------
    '''
    Log 種類
    Normal : 普通訊息
    Debug : Debug 用訊息
    Info : Info 特殊訊息
    Warning : 警告訊息
    Error : 錯誤訊息
    Critical : 嚴重錯誤訊息
    '''

    def Normal(self, *args, Except=False):
        self.State(self.Normal_Lv, self.BoardCast_Lv, "Log", 'Normal', Except, *args)

    def Debug(self, *args, Except=False):
        self.State(self.Debug_Lv, self.BoardCast_Lv, "Log", 'Debug', Except, *args)

    def Info(self, *args, Except=False):
        self.State(self.Info_Lv, self.BoardCast_Lv, "Log", 'Info', Except, *args)

    def Warning(self, *args, Except=False):
        self.State(self.Warning_Lv, self.BoardCast_Lv, "Log", 'Warning', Except, *args)

    def Error(self, *args, Except=False):
        self.State(self.Error_Lv, self.BoardCast_Lv, "Log", 'Error', Except, *args)

    def Critical(self, *args, Except=False):
        self.State(self.Critical_Lv, self.BoardCast_Lv, "Log", 'Critical', Except, *args)

    # ----------------------------------------------------------------------------------------------
    # 設置需要廣播的等級
    def Set_BoardCast_Lv(self, Lv):
        if (Lv <= -1):
            self.BoardCast_Lv = 3
        else:
            self.BoardCast_Lv = Lv

    # 設置是否顯示時間
    def Set_Time_Able(self, Time_Able):
        self.Time = Time_Able

    # ----------------------------------------------------------------------------------------------
    # 用來印出消息
    def State(self, LV1, LV2, LogFileName, Error, Except=False, *args):
        try:
            if (LV1 >= LV2 and self.Time == True):
                Text = ''
                Text += (datetime.datetime.now().strftime('%Y:%m:%d:%H:%M:%S') + '\t')
                Text += ('\t' + str(Error) + ': ' + str(args))
                print("Log in file "+Text)
                self.Save_Log(Text, LogFileName)
            elif (self.Critical_Lv >= self.BoardCast_Lv):
                print("Not log in file ",str(Error) + ': ' + str(args))
        except Exception as e:
            if (Except and LV1 >= LV2):
                print(e)

    # ----------------------------------------------------------------------------------------------
    '''
    Log出消息
    '''

    def Save_Log(self, Error_Text, LogName):
        with open(LogName, 'a')as File:
            File.write(Error_Text + '\n')

    def Clean_Log(self, LogName):
        with open(LogName, 'w')as File:
            File.write('')
