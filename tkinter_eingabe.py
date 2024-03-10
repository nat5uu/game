import tkinter as tk

def search():
    search_term = entry.get()
    print("Suche nach:", search_term)
    # Hier kannst du deine Suchlogik implementieren

# Tkinter Fenster erstellen
root = tk.Tk()
root.title("Suchfeld Beispiel")

# Suchfeld erstellen
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Suchbutton erstellen
search_button = tk.Button(root, text="Suchen", command=search)
search_button.pack()

root.mainloop()
