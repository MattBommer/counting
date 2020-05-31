import tkinter as tk
import counting as ct
from tkinter import StringVar

def main():
    card_counter = DegeneracyLite()
    card_counter.mainloop()

class DegeneracyLite (tk.Tk):
    def __init__(self):
        super(DegeneracyLite, self).__init__()
        self.pages = []
        self.counting_obj = None
        self.title("DegeneracyLite")
        mainframe = tk.Frame(self)
        mainframe.pack(fill="both", expand=True)
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        for page in [HomePage, GamePage]:
            p_obj = page(mainframe, self)
            p_obj.grid(row=0,column=0,sticky="nwes")
            self.pages.append(p_obj)
        self.raise_page(0)

    def raise_page(self, idx):
        self.pages[idx].tkraise()

    def backend_obj(self, obj):
        self.counting_obj = obj
        self.pages[1].set_backend(obj)
    
    def pass_backend(self):
        return self.counting_obj


class HomePage(tk.Frame):
    
    def __init__(self, parent_frame, parent_obj):
        super(HomePage, self).__init__(parent_frame)
        self.parent = parent_obj
        tk.Label(self, text="Welcome to the DegeneracyLite Blackjack card counter!").pack(fill="both", padx=5, pady=5)
        
        #String variables
        num_deck = StringVar()
        error_message = StringVar()

        #Label for number of decks left in shoe
        tk.Label(self, text="Number of decks left in the shoe? (Enter a number)").pack()
        deck_entry = tk.Entry(self, width=3, textvariable=num_deck)
        deck_entry.pack()
        
        #Error label if the user inputs a value that isn't a number
        tk.Label(self, textvariable=error_message).pack(side="bottom", fill="both")

        #Button to run the program
        button = tk.Button(self, text="Start", command=lambda: self.init_count(num_deck.get(), error_message))
        button.pack()
        
        #Writing cursor defaults to the only text box available and we bind enter key to running the program
        deck_entry.focus()
        parent_obj.bind('<Return>', lambda event: self.init_count(num_deck.get(), error_message))


    def init_count(self, decks, error_reply):
        try:
            dnum = int(decks)
            error_reply.set("")
        except:
            error_reply.set("The entry " + str(decks) + " is not an integer or in int form, try again...")
        else:
            self.parent.backend_obj(ct.main(dnum))
            self.parent.geometry("612x362")
            self.parent.resizable(height=False, width=False)
            self.parent.raise_page(1)
            

class GamePage(tk.Frame):

    def __init__(self, parent_frame, parent_obj):
        super(GamePage, self).__init__(parent_frame)
        self.parent = parent_obj
        self.count_obj = None
        
        #Random page label for the time being
        background = tk.PhotoImage(file="table.png")
        bg_label = tk.Label(self, image=background)
        bg_label.image = background
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        
        #Button for reseting the program (used when the cards are shuffled and a new shoe is in play)
        img = tk.PhotoImage(file="plusbutton.png")
        
          
        button7 = tk.Button(self, image=img, borderwidth=0, highlightthickness=0, command=lambda: self.new_player(7))
        button7.image = img
        button7.place(relx=.0735, rely=.3)

        button6 = tk.Button(self, image=img, borderwidth=0, highlightthickness=0, command=lambda: self.new_player(6))
        button6.image = img
        button6.place(relx=.175, rely=.493)

        button5 = tk.Button(self, image=img, borderwidth=0, highlightthickness=0, command=lambda: self.new_player(5))
        button5.image = img
        button5.place(relx=.311, rely=.63)

        button4 = tk.Button(self, image=img, borderwidth=0, highlightthickness=0, command=lambda: self.new_player(4))
        button4.image = img
        button4.place(relx=.475, rely=.67)

        button3 = tk.Button(self, image=img, borderwidth=0, highlightthickness=0, command=lambda: self.new_player(3))
        button3.image = img
        button3.place(relx=.639, rely=.63)

        button2 = tk.Button(self, image=img, borderwidth=0, highlightthickness=0, command=lambda: self.new_player(2))
        button2.image = img
        button2.place(relx=.775, rely=.493)

        button1 = tk.Button(self, image=img, borderwidth=0, highlightthickness=0, command=lambda: self.new_player(1))
        button1.image = img
        button1.place(relx=.8765, rely=.3)

        # tk.Button(self, text="Remove Player", command=lambda: self.remove_player(1)).pack(side="bottom", fill="both", padx=5, pady=5)
        tk.Button(self, text="Reset", command=self.reset_count).place(relx=0.0, rely=.925)
        tk.Button(self, text="Calculate Count", command=self.run_count).place(relx=.845, rely=.925)

    def new_player(self, location):
        self.count_obj.add_player(location)

    def remove_player(self, location):


        self.count_obj.remove_player(location)

    def reset_count(self):
        self.parent.geometry("")
        self.parent.raise_page(0)

    def set_backend (self, obj):
        self.count_obj = obj

    def run_count(self):
        #run a round of count
        pass
        
if __name__ == "__main__":
    main()