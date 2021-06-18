import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        # wx.Frame.__init__(self, parent, id, title="Log in", pos=(700, 200), size=(800, 500))
        # # 创建画板
        # panel = wx.Panel(self)
        # # 创建标题并设置字体
        # self.title = wx.StaticText(panel, label='Please input username and password', pos=(300, 20))
        # # font = wx.Font(10, wx.DEFAULT, wx.FONTSTYLE_MAX, wx.NORMAL)
        # # title.SetFont(font)
        # # 创建输入
        # self.label_user = wx.StaticText(panel, label='user: ', pos=(250, 50))
        # self.text_user = wx.TextCtrl(panel, pos=(300, 50), size=(235, 25), style=wx.TE_LEFT)
        # self.label_password = wx.StaticText(panel, label='password: ', pos=(250, 90))
        # self.text_password = wx.TextCtrl(panel, pos=(300, 90), size=(235, 25), style=wx.TE_PASSWORD)
        # # 创建“确定”和”取消“按钮
        # self.bt_confirm = wx.Button(panel,label='OK',pos=(300,120))
        # self.bt_cancel = wx.Button(panel, label='Cancel', pos=(450, 120))

        # 使用布局
        wx.Frame.__init__(self, parent, id, title="Log in", size=(400, 300))
        panel = wx.Panel(self)
        self.bt_confirm = wx.Button(panel, label='OK')
        self.bt_confirm.Bind(wx.EVT_BUTTON, self.OnclickSubmit)  # 添加事件处理
        self.bt_cancel = wx.Button(panel, label='Cancel')
        self.bt_cancel.Bind(wx.EVT_BUTTON, self.OnclickSCancel)  # 添加事件处理
        # 创建文本、左对齐
        self.title = wx.StaticText(panel, label='Please input username and password')
        self.label_user = wx.StaticText(panel, label='user: ')
        self.text_user = wx.TextCtrl(panel, style=wx.TE_LEFT)
        self.label_password = wx.StaticText(panel, label='password: ')
        self.text_password = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        # 添加容器、容器中控件横向排列
        hsizer_user = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_user.Add(self.label_user, proportion=0, flag=wx.ALL, border=5)
        hsizer_user.Add(self.text_user, proportion=1, flag=wx.ALL, border=5)
        hsizer_password = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_password.Add(self.label_password, proportion=0, flag=wx.ALL, border=5)
        hsizer_password.Add(self.text_password, proportion=1, flag=wx.ALL, border=5)
        hsizer_button = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button.Add(self.bt_confirm, proportion=0, flag=wx.ALL, border=5)
        hsizer_button.Add(self.bt_cancel, proportion=0, flag=wx.ALL, border=5)
        # 添加容器、容器中控件纵向排列
        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(self.title, proportion=0, flag=wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER, border=15)
        vsizer_all.Add(hsizer_user, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=45)
        vsizer_all.Add(hsizer_password, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=45)
        vsizer_all.Add(hsizer_button, proportion=0, flag=wx.ALIGN_CENTER | wx.TOP, border=45)

        panel.SetSizer(vsizer_all)

    def OnclickSubmit(self,event):
        message = ""
        username = self.text_user.GetValue()
        password = self.text_password.GetValue()
        if username=="" or password=="":
            message = "user or password can't be empty"
        elif username=="xrf" or password=="1998312":
            message = "Login successfully"
        else:
            message = "Username and password do not match"
        wx.MessageBox(message)

    def OnclickSCancel(self,event):
        self.text_user.SetValue("")
        self.text_password.SetValue("")


if __name__ == '__main__':
    # 实例化一个wx.App类
    app = wx.App()
    # 定义一个顶级窗口
    frame = MyFrame(parent=None, id=-1)
    # 显示窗口
    frame.Show()
    # 调用wx.App类的MainLoop()主循环方法
    app.MainLoop()
