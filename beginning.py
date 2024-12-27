import tkinter as tk
from lignes import bus_lines

def display_lines(lines):
    for widget in scrollable_frame.winfo_children():
        widget.destroy()
    if not lines:
        error_label = tk.Label(scrollable_frame, text="Cette ligne n'existe pas", font=("Arial", 12, "bold"), fg="red")
        error_label.pack(pady=10)
    for number, description in lines:
        tk.Label(scrollable_frame, text=number, font=("Arial", 12, "bold"), bg="lightgray").pack(fill="x", pady=2)
        tk.Label(scrollable_frame, text=description, font=("Arial", 10), wraplength=600, bg="white").pack(fill="x", pady=2)

def search_lines(event=None):
    query = search_entry.get().lower()
    filtered = [line for line in bus_lines if query in line[0].lower() or query in line[1].lower()]
    display_lines(filtered)

root = tk.Tk()
root.title("Lignes de Bus")
root.geometry("900x600")

# Barre de recherche
search_frame = tk.Frame(root)
search_frame.pack(fill="x", pady=10)
tk.Label(search_frame, text="Rechercher :", font=("Arial", 12)).pack(side="left", padx=10)
search_entry = tk.Entry(search_frame, font=("Arial", 12), width=50)
search_entry.pack(side="left", padx=5)
search_entry.bind("<KeyRelease>", search_lines)

canvas = tk.Canvas(root)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

display_lines(bus_lines)

root.mainloop()
