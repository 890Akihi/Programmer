#戦争ゲームを作ろう！

from random import shuffle
import tkinter as tk
from tkinter.constants import CENTER

class App:
    def __init__(self):
        #ゲーム開始時に名前を入力させる。
        self.app = tk.Tk()
        self.app.title("戦争ゲーム")
        self.app.geometry("300x200")
        self.first_frame = tk.LabelFrame(self.app,
                                text="名前を入力してね")
        self.first_frame1= tk.LabelFrame(self.first_frame,
                                text="プレイヤー１")
        self.first_frame2= tk.LabelFrame(self.first_frame,
                                text="プレイヤー２")
        self.first_frame.pack(anchor=tk.CENTER)
        self.first_frame1.grid(row=0,column=0)
        self.first_frame2.grid(row=0,column=1)
        self.player_name1 = ""
        self.player_name2 = ""
        self.name1_entry = tk.Entry(self.first_frame1,
                                textvariable=self.player_name1,
                                width=8)
        self.name2_entry = tk.Entry(self.first_frame2,
                                textvariable=self.player_name2,
                                width=8)
        self.name1_entry.grid()
        self.name2_entry.grid()
        entry_btn = tk.Button(self.first_frame,
                                text="OK",
                                command=lambda:[self.game_state(),
                                                self.game_disp()])
        entry_btn.grid(row=0,column=2)
        self.app.mainloop()

    def game_state(self):
        name1 = self.player_name1
        name2 = self.player_name2
        self.game = Game(name1,name2)

    def game_disp(self):
        self.first_frame.destroy()
        
        #ゲームの続行と中止ボタン
        self.new_frame = tk.LabelFrame(self.app)
        self.name_frame1 = tk.LabelFrame(self.new_frame,
        text=self.game.name1)
        self.name_frame2 = tk.LabelFrame(self.new_frame,
        text=self.game.name2)
        self.game_frame1 = tk.LabelFrame(self.new_frame,
                                        text="")
        self.game_frame2 = tk.LabelFrame(self.new_frame,
                                        text="")
        self.new_frame.pack(anchor=tk.CENTER)
        btn = tk.Button(self.app)
        btn.pack()
        
        """
        btn_n = tk.Button(self.app,
                  text=("next"),
                  command=Game.next_loop)
        btn_q = tk.Button(self.app,
                  text="quit",
                  command=Game.quit)
        name1_frame = tk.Frame(self.app,
                                text=Game)
        name2_frame = 1
        """






class Card:
    suits = ["♠","♥","♦","♣","Joker"]

    values = [None,None,
              "2","3","4","5","6","7","8","9",
              "10","Jack","Queen","King","Ace",
              "Joker"
              ]
    
    def __init__(self,v,s):
        #スートもバリューも整数を持たせてあげます
        self.suit = s
        self.value = v

    
    def __it__(self,c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False
    
    def __gt__(self,c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False
    
    def __repr__(self):
        """
        #カードを文字で表示させる
        v =self.suits[self.suit]  +"の"+ self.values[self.value]
        return v
        """
        #カードグラフィックを表示させる
        if self.value in [11,12,13,14]:
            suit = [None,"J","Q","K","A"]
            v = self.value - 10
            v = suit[v]
        else:
            v =self.values[self.value]
        s =self.suits[self.suit]
        if self.values[self.value] == "Joker":
            v = "⋆"
            s = "J"
            print("Joker!")
        c= ("\n"+
            "_____\n"+
            "|{}   |\n".format(v)+
            "| {}  |\n".format(s)+
            "|   {}|\n".format(v)+
            "‾‾‾‾‾\n"
            )
        return c

class Deck:
    def __init__(self):
        self.cards = []
        self.cards.append(Card(15,4))
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)
    
    def rm_card(self):
        if len(self.cards) ==0:
            return
        return self.cards.pop()

class Player:
    def __init__(self,name):
        self.wins = 0
        self.card = None
        self.name = name

class Game(App):
    def __init__(self,name1,name2):
        self.name1 = name1
        self.name2 = name2
        self.deck = Deck()
        self.p1 = Player(self.name1)
        self.p2 = Player(self.name2)

    def wins(self,winner):
        w = "この勝負は{}が勝ちました"
        w = w.format(winner)
        print(w)

    def drow(self,n1,n2,c1,c2):
        d = "{}は\n{}をひきました。\n{}は\n{}をひきました。"
        d = d.format(n1,c1,n2,c2)
        print(d)
    
    def play_game(self):
        cards = self.deck.cards
        while len(cards) > 2:
            #response = input("ゲームを始めるには何か入力してください（qでゲームを終了します)")
            #if response == "q":
            #    break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.drow(p1n,p2n,p1c,p2c)
            if p1c == (15,5):
                self.p1.wins += 1
                self.wins(p1n)
            elif  p2c == (15,5):
                self.p2.wins += 1
                self.wins(p2n)
            else:
                if p1c > p2c:
                    self.p1.wins += 1
                    self.wins(p1n)
                else:
                    self.p2.wins += 1
                    self.wins(p2n)
            break
        win = self.winner(self.p1,self.p2)
        print("ゲームを終了します。勝者は{}です！".format(win))
    
    def winner(self,p1,p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "いませんでした。引き分け"

    def quit(self):
        self.app.destroy()
    
    def next_loop(self):
        self.play_game()


app = App()