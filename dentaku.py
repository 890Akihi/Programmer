#簡易な電卓アプリ
#失敗しました。。。

import tkinter as tk
from functools import partial
from tkinter.constants import E, N
#パーちゃる？敵なのが必要そう？必要なかったら勝ち
app = tk.Tk()
app.title("計算機")
app.geometry("200x300")

def changeText(next):
    label.configure(text=next)

#計算機に数値や演算子を入力させる処理をするよ

class Keisanki:
    def __init__(self):
        self.number = "0"
        self.keisan_number = None
        self.keisan_shiki = None
    
    def operand(self,x):
        if self.number == None or self.number == "0" or type(self.number) == int:
            self.number = x
        else:
            self.number = self.number + x
        txt = self.number
        label.configure(text=txt)
    
    def operater(self,e):
        if self.keisan_number == None:
            txt = self.number + e
            self.keisan_number = self.number
            self.keisan_shiki = txt
            label0.configure(text=txt)
            self.number = None
        elif self.number == None:
            txt = self.keisan_number + e
            self.keisan_shiki = txt
            label0.configure(text=txt)
        else:
            txt = self.keisan_shiki + str(self.number)
            kekka = eval(txt)
            self.numder = None
            txt = str(kekka) + e
            self.keisan_number = txt
            label0.configure(text=self.keisan_number)
            label.configure(text=kekka)

    def clear(self):
        self.number = "0"
        self.keisan_number = None
        self.keisan_shiki = None
        label0.configure(text=self.keisan_number)
        label.configure(text=self.number)

keisanki = Keisanki()
def keisan():
    pass



label0 = tk.Label(
    app,
    text= None
)
frame = tk.LabelFrame(app,text="数字",foreground="red")
f2 = tk.LabelFrame()
label = tk.Label(
    frame,
    text = "0"
)

frame.pack()
label0.pack()
label.pack(anchor=N)

#ボタンの作成
btn1 = tk.Button(width=3,height=2,text="1", command= partial(keisanki.operand,"1"))
btn2 = tk.Button(width=3,height=2,text="2", command= partial(keisanki.operand,"2"))
btn3 = tk.Button(width=3,height=2,text="3", command= partial(keisanki.operand,"3"))
btn4 = tk.Button(width=3,height=2,text="4", command= partial(keisanki.operand,"4"))
btn5 = tk.Button(width=3,height=2,text="5", command= partial(keisanki.operand,"5"))
btn6 = tk.Button(width=3,height=2,text="6", command= partial(keisanki.operand,"6"))
btn7 = tk.Button(width=3,height=2,text="7", command= partial(keisanki.operand,"7"))
btn8 = tk.Button(width=3,height=2,text="8", command= partial(keisanki.operand,"8"))
btn9 = tk.Button(width=3,height=2,text="9", command= partial(keisanki.operand,"9"))
btn0 = tk.Button(width=3,height=2,text="0", command= partial(keisanki.operand,"0"))
btni = tk.Button(width=3,height=2,text="=", command= keisan())
btnc = tk.Button(width=3,height=2,text="C", command= keisanki.clear())
btnp = tk.Button(width=3,height=2,text="+", command= partial(keisanki.operater,"+"))
btnm = tk.Button(width=3,height=2,text="-", command= partial(keisanki.operater,"-"))
btnk = tk.Button(width=3,height=2,text="x", command= partial(keisanki.operater,"*"))
btnw = tk.Button(width=3,height=2,text="÷", command= partial(keisanki.operater,"/"))
#ボタンの配置
f2.pack()
btn1.grid(in_ = f2,column=0,row=0)
btn2.grid(in_ = f2,column=1,row=0)
btn3.grid(in_ = f2,column=2,row=0)
btn4.grid(in_ = f2,column=0,row=1)
btn5.grid(in_ = f2,column=1,row=1)
btn6.grid(in_ = f2,column=2,row=1)
btn7.grid(in_ = f2,column=0,row=2)
btn8.grid(in_ = f2,column=1,row=2)
btn9.grid(in_ = f2,column=2,row=2)
btn0.grid(in_ = f2,column=1,row=3)
btni.grid(in_ = f2,column=2,row=3)
btnc.grid(in_ = f2,column=0,row=3)
btnp.grid(in_ = f2,column=4,row=0)
btnm.grid(in_ = f2,column=4,row=1)
btnk.grid(in_ = f2,column=4,row=2)
btnw.grid(in_ = f2,column=4,row=3)

app.mainloop()