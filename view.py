from tkinter import *
from Lingo import Lingo
import time 
from my_timer import *
from my_timer import MyTimer


cells = {}
# Listener bij het verlaten van een entry
def focus_out(event):

    invoer = ""
    for c in range(5):
        if (cells[(lingo.beurt,c)].get()!=""):
            cells[(lingo.beurt,c)].config(state ="disabled", disabledbackground="blue", disabledforeground="white")
            invoer += cells[(lingo.beurt,c)].get()
        
        if (len(invoer) == 5):
            print("De rij is ingevuld!")

            # Check het woord 
            uitvoer = lingo.validate_input(invoer, naam_veld.get())

            # Toon de feedback
            show_result(uitvoer)


# Listener als er karakter wordt ingevoerd in de entry widget
def key_pressed(event):
    event.widget.tk_focusNext().focus()

# Functie om de uitvoer weer te geven
def show_result(uitvoer):

    # Update aantal beurten
    beurten_label.config(text= str(lingo.beurt+1) + "/5")

    # Toon het resultaat in het status label als het niet meer het woord is
    if (len(uitvoer) != 5):
        status_label.config(text = uitvoer)
        
    # Tonn het resultaat in het raster
    else:
        for i in range(5):
            # Als de letter op de juiste plek staat > rode achtergrond
            if (uitvoer[i].isupper()):
                cells[lingo.beurt-1, i].config(disabledbackground="red")
            elif (uitvoer[i].islower()):
                cells[lingo.beurt-1, i].config(disabledbackground="orange")

    
# Lingo object
lingo = Lingo()


# Lijst met invoervelden
invoervelden = {}
# Valideer de invoer, event listener 
def validate(event):
    print("beurt: " + str(lingo.beurt))
    print("woord: " + lingo.woord)
    
    invoer = invoervelden[lingo.beurt-1].get()
    print("ingevoerd: " + invoer)

    uitvoer = lingo.validate_input(invoer, naam_veld.get())
    print("Resultaat: " + uitvoer)

    # Toon de uitvoer
    invoervelden[lingo.beurt-2].insert(END, " > " + uitvoer)

    # Update de status
    status_label.config(text = uitvoer)

    


# Main
app = Tk()
app.title("Lingo")
app.geometry("300x400")
app.resizable(False, False)

# Frame voor de info
info_frame = Frame(app)
info_frame.pack()

# Titel 
titel_label = Label(app, text = "Welkom bij Lingo!", font=("Arial", 18, "bold"))
titel_label.pack()

# Uitleg
intro_label = Label(app, text = "Raad het woord van 5 letters in 5 beurten")
intro_label.pack()

# Status
status_label = Label(app, text = "Succes", font=("Arial", 12, "bold"), fg = 'red')
status_label.pack()

# Naam van speler
naam_veld = Entry(app, font=("Arial", 18, "bold"))
naam_veld.insert(0, "type hier uw naam in!")
naam_veld.pack()

# Timer

timer_label = Label(info_frame, text = "100", font =("Arial", 20, "bold"))

timer_label.grid(row=3, column=1, sticky='e' )

mytimer = MyTimer(timer_label)

mytimer.start()

# Aantal beurten
beurten_label = Label(app, text = "1/5", font=("Arial", 20, "bold"))
beurten_label.pack()



# Frame voor het raster van invoervelden 
raster_frame = Frame(app, padx=10, pady=10)
raster_frame.pack(side= LEFT, pady=15)

for r in range (5):
    Grid.rowconfigure(raster_frame, r, weight=1)
    for c in range(5):
        Grid.columnconfigure(raster_frame, c, weight=1)

        cell=Entry(raster_frame, bg='#3366cc', justify=CENTER, font=("Arial", 24, "bold"), fg = 'white')
        cell.grid(row=r, column=c, sticky='', ipady=10)
        cell.bind('<Key>', key_pressed)
        cell.bind('<FocusOut>', focus_out)
        cells[(r,c)] = cell 

    # Focus op de eerte cell
    cells[0,0].focus()




# Run
app.mainloop()