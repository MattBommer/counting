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

class HomePage(tk.Frame):
    
    def __init__(self, parent_frame, parent_obj):
        super(HomePage, self).__init__(parent_frame)
        self.parent = parent_obj

        tk.Label(self, text="Welcome to the DegeneracyLite Blackjack card counter!").pack(fill="both", padx=5, pady=5)
        
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
            #Run count.py
            self.parent.raise_page(1)
            

class GamePage(tk.Frame):

    def __init__(self, parent_frame, parent_obj):
        super(GamePage, self).__init__(parent_frame)
        self.parent = parent_obj
        
        #Random page label for the time being
        tk.Label(self, text="This is the GamePage").pack()
        
        #Button for reseting the program (used when the cards are shuffled and a new shoe is in play)
        tk.Button(self, text="Reset", command=self.reset_count).pack()
        tk.Button(self, text="Calculate Count", command=self.run_count).pack()

    def reset_count(self):
        self.parent.raise_page(0)

    def run_count(self):
        #run a round of count
        print("running a round of count")
        pass
        
if __name__ == "__main__":
    main()