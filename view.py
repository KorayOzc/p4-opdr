import tkinter as tk
from Lingo import Lingo
from my_timer import MyTimer

cells = {}

def focus_out(event):
    invoer = ""
    for c in range(5):
        if cells[(lingo.beurt,c)].get()!="":
            cells[(lingo.beurt,c)].config(state ="disabled", disabledbackground="blue", disabledforeground="white")
            invoer += cells[(lingo.beurt,c)].get()
        
        if len(invoer) == 5:
            print("De rij is ingevuld!")
            uitvoer = lingo.validate_input(invoer, naam_veld.get())
            show_result(uitvoer)

def key_pressed(event):
    event.widget.tk_focusNext().focus()

def show_result(uitvoer):
    beurten_label.config(text= str(lingo.beurt+1) + "/5")

    if len(uitvoer) != 5:
        status_label.config(text=uitvoer)
    else:
        for i in range(5):
            if uitvoer[i].isupper():
                cells[lingo.beurt-1, i].config(disabledbackground="red")
            elif uitvoer[i].islower():
                cells[lingo.beurt-1, i].config(disabledbackground="orange")

lingo = Lingo()

def validate(event):
    print("beurt: " + str(lingo.beurt))
    print("woord: " + lingo.woord)
    
    invoer = invoervelden[lingo.beurt-1].get()
    print("ingevoerd: " + invoer)

    uitvoer = lingo.validate_input(invoer, naam_veld.get())
    print("Resultaat: " + uitvoer)

    invoervelden[lingo.beurt-2].insert(tk.END, " > " + uitvoer)

    status_label.config(text=uitvoer)

app = tk.Tk()
app.title("Lingo")
app.geometry("300x400")
app.resizable(False, False)

info_frame = tk.Frame(app)
info_frame.pack()

titel_label = tk.Label(app, text="Welkom bij Lingo!", font=("Courier", 18, "bold"))
titel_label.pack()

intro_label = tk.Label(app, text="Raad het woord van 5 letters in 5 beurten")
intro_label.pack()

status_label = tk.Label(app, text="Succes", font=("Courier", 12, "bold"), fg='blue')
status_label.pack()

naam_veld = tk.Entry(app, font=("Courier", 18, "bold"))
naam_veld.insert(0, "type hier uw naam in!")
naam_veld.pack()

timer_label = tk.Label(info_frame, text="100", font=("Courier", 20, "bold"))
timer_label.grid(row=3, column=1, sticky='e')

mytimer = MyTimer(timer_label)
mytimer.start()

beurten_label = tk.Label(app, text="1/5", font=("Courier", 20, "bold"))
beurten_label.pack()

raster_frame = tk.Frame(app, padx=10, pady=10)
raster_frame.pack(side=tk.LEFT, pady=15)

for r in range(5):
    tk.Grid.rowconfigure(raster_frame, r, weight=1)
    for c in range(5):
        tk.Grid.columnconfigure(raster_frame, c, weight=1)

        cell = tk.Entry(raster_frame, bg='#FFD700', justify=tk.CENTER, font=("Courier", 24, "bold"), fg='black')
        cell.grid(row=r, column=c, sticky='', ipady=10)
        cell.bind('<Key>', key_pressed)
        cell.bind('<FocusOut>', focus_out)
        cells[(r,c)] = cell 

    cells[0,0].focus()

app.mainloop()
