from tkinter import *
from tkinter import ttk
import counting as ct

def start(*args):
    try:
        deck = int(deck_num.get())
        players = int(num_players.get())
        prg_args = [deck, players, 0]
        error_message.set("")
        frame = Toplevel(root).grid(column=0, row=0, sticky=(N, W, E, S))
        frame.tkraise()
    except ValueError:
        error_message.set("One or more of the arguments given wasn't a number, try again...")

root = Tk()
root.title("Degeneracy Lite")

# mainframe = ttk.Frame(root, padding="20 20 20 20", width=400, height=1300)
# mainframe.grid(row=0, column=0, sticky=(N, W, E, S))
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

# deck_num = StringVar()
# num_players = StringVar()
# error_message = StringVar()

# ttk.Label(mainframe, text="Number of decks left in the shoe?").grid(column=7,row=1,sticky=W)
# deck_entry = ttk.Entry(mainframe, textvariable=deck_num)
# deck_entry.grid(column=7, row=2, sticky=W)

# ttk.Label(mainframe, text="Number of players at the table?").grid(column=7,row=3,sticky=W)
# player_entry = ttk.Entry(mainframe, textvariable=num_players)
# player_entry.grid(column=7, row=4, sticky=W)

# error_label = ttk.Label(mainframe, textvariable=error_message).grid(column=7, row=10, sticky=W)

# ttk.Button(mainframe, text="Start Counting", command=start).grid(column=20, row=20, sticky=E)

# for child in mainframe.winfo_children(): child.grid_configure(padx=10, pady=10)

# deck_entry.focus()
# root.bind('<Return>', start)

root.mainloop()