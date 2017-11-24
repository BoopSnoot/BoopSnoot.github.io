#! /usr/bin/python

from wx import *


def caneval(string):
    try:
        eval(string)
        return True
    except NameError:
        return False
    except SyntaxError:
        return False


class MyApp:
    def canevalerr(self):
        print("You done goofed")
        self.field2.SetValue("Please input ONLY mathematical expressions!")

    def evaluate(self, event):
        test = self.field1.GetLineText(0)
        if caneval(test):
            self.field1.SetValue(str(eval(self.field1.GetLineText(0))))
        elif caneval(test) is False:
            self.canevalerr()

    def square(self, event):
        evalstr = self.field1.GetLineText(0)
        if caneval(evalstr):
            if event.GetId() == 16:
                self.field1.SetValue(str(eval(evalstr) ** 2))
            else:
                self.field1.SetValue(str(eval(evalstr) ** 0.5))
        else:
            self.canevalerr()

    def erase(self, event):
        if event.GetId() == 20:
            self.field1.SetValue(self.field1.GetLineText(0)[:-1])
        else:
            self.field1.SetValue("0")

    def enter(self, event):
        nos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        buttonid = event.GetId()
        if buttonid in nos:
            if self.field1.GetLineText(0) != "0":
                self.field1.SetValue(self.field1.GetLineText(0) + str(buttonid))
            else:
                self.field1.SetValue(str(buttonid))
        elif buttonid == 19:
            if self.field1.GetLineText(0) == "":
                self.field1.SetValue("0.")
            else:
                self.field1.SetValue(self.field1.GetLineText(0) + ".")
        elif buttonid == 12:
            self.field1.SetValue(self.field1.GetLineText(0) + "+")
        elif buttonid == 13:
            self.field1.SetValue(self.field1.GetLineText(0) + "-")
        elif buttonid == 14:
            self.field1.SetValue(self.field1.GetLineText(0) + "*")
        elif buttonid == 15:
            self.field1.SetValue(self.field1.GetLineText(0) + "/")

    def __init__(self):
        self.frame = Frame(None, 9, "Calculator++ Reborn", style=DEFAULT_FRAME_STYLE & ~(RESIZE_BORDER | MAXIMIZE_BOX))
        self.frame.SetSize(365, 420)
        self.frame.Show()

        self.field1 = TextCtrl(self.frame, 10, "0", size=(365, 60), style=TE_PROCESS_ENTER)
        font = Font(24, FONTFAMILY_SWISS, FONTSTYLE_NORMAL, FONTWEIGHT_NORMAL)
        self.field1.SetFont(font)
        self.field1.Bind(EVT_TEXT_ENTER, self.evaluate)

        self.field2 = TextCtrl(self.frame, 22, size=(365, 20), pos=(0, 60), style=TE_READONLY)
        font1 = Font(8, FONTFAMILY_SWISS, FONTSTYLE_NORMAL, FONTWEIGHT_NORMAL)
        self.field2.SetFont(font1)
        self.field2.SetDefaultStyle(TextAttr(RED))

        self.buttoneq = Button(self.frame, 11, "=", pos=(185, 335), size=(180, 85))
        self.buttoneq.SetFont(font)
        self.buttoneq.Bind(EVT_BUTTON, self.evaluate)

        self.buttonplus = Button(self.frame, 12, "+", pos=(185, 165), size=(60, 85))
        self.buttonplus.SetFont(font)
        self.buttonplus.Bind(EVT_BUTTON, self.enter)

        self.buttonminus = Button(self.frame, 13, "-", pos=(245, 165), size=(60, 85))
        self.buttonminus.SetFont(font)
        self.buttonminus.Bind(EVT_BUTTON, self.enter)

        self.buttontimes = Button(self.frame, 14, "\N{MULTIPLICATION SIGN}", pos=(185, 250), size=(60, 85))
        self.buttontimes.SetFont(font)
        self.buttontimes.Bind(EVT_BUTTON, self.enter)

        self.buttondivide = Button(self.frame, 15, "\N{DIVISION SIGN}", pos=(245, 250), size=(60, 85))
        self.buttondivide.SetFont(font)
        self.buttondivide.Bind(EVT_BUTTON, self.enter)

        self.buttonsq = Button(self.frame, 16, "x\N{SUPERSCRIPT TWO}", pos=(305, 165), size=(60, 85))
        self.buttonsq.SetFont(font)
        self.buttonsq.Bind(EVT_BUTTON, self.square)

        self.buttonsqrt = Button(self.frame, 17, "\N{SQUARE ROOT}", pos=(305, 250), size=(60, 85))
        self.buttonsqrt.SetFont(font)
        self.buttonsqrt.Bind(EVT_BUTTON, self.square)

        self.buttonerase = Button(self.frame, 20, "\N{ERASE TO THE LEFT}", pos=(185, 80), size=(120, 85))
        self.buttonerase.SetFont(font)
        self.buttonerase.Bind(EVT_BUTTON, self.erase)

        self.buttonclear = Button(self.frame, 21, "AC", pos=(305, 80), size=(60, 85))
        self.buttonclear.SetFont(font)
        self.buttonclear.Bind(EVT_BUTTON, self.erase)

        self.separator1 = StaticLine(self.frame, pos=(180, 80), size=(5, 340))

        self.button1 = Button(self.frame, 1, "1", pos=(0, 80), size=(60, 85))
        self.button1.SetFont(font)
        self.button1.Bind(EVT_BUTTON, self.enter)

        self.button2 = Button(self.frame, 2, "2", pos=(60, 80), size=(60, 85))
        self.button2.SetFont(font)
        self.button2.Bind(EVT_BUTTON, self.enter)

        self.button3 = Button(self.frame, 3, "3", pos=(120, 80), size=(60, 85))
        self.button3.SetFont(font)
        self.button3.Bind(EVT_BUTTON, self.enter)

        self.button4 = Button(self.frame, 4, "4", pos=(0, 165), size=(60, 85))
        self.button4.SetFont(font)
        self.button4.Bind(EVT_BUTTON, self.enter)

        self.button5 = Button(self.frame, 5, "5", pos=(60, 165), size=(60, 85))
        self.button5.SetFont(font)
        self.button5.Bind(EVT_BUTTON, self.enter)

        self.button6 = Button(self.frame, 6, "6", pos=(120, 165), size=(60, 85))
        self.button6.SetFont(font)
        self.button6.Bind(EVT_BUTTON, self.enter)

        self.button7 = Button(self.frame, 7, "7", pos=(0, 250), size=(60, 85))
        self.button7.SetFont(font)
        self.button7.Bind(EVT_BUTTON, self.enter)

        self.button8 = Button(self.frame, 8, "8", pos=(60, 250), size=(60, 85))
        self.button8.SetFont(font)
        self.button8.Bind(EVT_BUTTON, self.enter)

        self.button9 = Button(self.frame, 9, "9", pos=(120, 250), size=(60, 85))
        self.button9.SetFont(font)
        self.button9.Bind(EVT_BUTTON, self.enter)

        self.button0 = Button(self.frame, 0, "0", pos=(0, 335), size=(120, 85))
        self.button0.SetFont(font)
        self.button0.Bind(EVT_BUTTON, self.enter)

        self.buttondot = Button(self.frame, 19, ".", pos=(120, 335), size=(60, 85))
        self.buttondot.SetFont(font)
        self.buttondot.Bind(EVT_BUTTON, self.enter)


app = App()
myapp = MyApp()
app.MainLoop()
