# -*- coding: utf-8 -*-
import  random
import  wx

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,u'猜数字',size=(400,300))
        wx.StaticText(self, -1,u'猜一猜数字1~99',pos=(30,50))

        self.input=wx.TextCtrl(self,-1,'',pos=(50,100),style=wx.TE_PROCESS_ENTER)
        self.Bind(wx.EVT_TEXT_ENTER,self.OnEnter,self.input)

        self.text=wx.TextCtrl(self,-1,'',pos=(200,0),size=(200,300),style=wx.TE_MULTILINE)
        self.text.Enable(False)

        self.button=wx.Button(self,-1,u'再来一次',pos=(50,150))
        self.Bind(wx.EVT_BUTTON,self.OnClick,self.button)
        self.button.Show(False)
        self.num=random.randint(1,99)

    def OnEnter(self,event):
        answer_str=self.input.GetValue()
        try:
            answer=eval(answer_str)
        except:
            self.text.AppendText(u'不对，再猜\n')
            return
        self.input.Clear()

        if answer< self.num:
            self.text.AppendText(answer_str+u'太小了\n')
        elif answer>self.num:
            self.text.AppendText(answer_str+u'太大了\n')
        else:
            self.text.AppendText(answer_str+u'对了\n')
            self.button.Show(True)

    def OnClick(self,event):
        self.text.SetValue('')
        self.button.Show(False)
        self.num=random.randint(1,99)

if __name__ == '__main__':
    app=wx.App()
    frame=MainFrame()
    frame.Show()
    app.MainLoop()

