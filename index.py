import tkinter as tk
from tkinter import ttk
from lignes import bus_lines

def filter_lines(event=None):
    search_term = search_entry.get().strip().lower()
    for widget in canvas_frame.winfo_children():
        widget.destroy()
    if not search_term:  
        display_lines(bus_lines)
    else:
        filtered_lines = [
            line for line in bus_lines if search_term in line[0].lower() or search_term in line[1].lower()
        ]
        if filtered_lines:
            display_lines(filtered_lines)
        else:
            message_label = tk.Label(canvas_frame, text="Aucune ligne correspond à votre recherche",
                                      bg="#ffffff", fg="red", font=("Arial", 12, "bold"))
            message_label.pack(pady=10)

def display_lines(lines):
    for line in lines:
        line_frame = tk.Frame(canvas_frame, bg="#e0f7fa", bd=1, relief="solid")
        line_frame.pack(fill="x", pady=5, padx=10)

        line_number_label = tk.Label(line_frame, text=line[0], bg="#00796b", fg="white",
                                     font=("Arial", 12, "bold"), width=8)
        line_number_label.pack(side="left", padx=5, pady=5)

        line_desc_label = tk.Label(line_frame, text=line[1], bg="#e0f7fa", fg="#004d40",
                                   font=("Arial", 10), anchor="w", justify="left")
        line_desc_label.pack(side="left", fill="x", padx=5, pady=5, expand=True)

        line_price_label = tk.Label(line_frame, text=f"Tarif: {line[2]}", bg="#e0f7fa", fg="#388e3c",
                                    font=("Arial", 10, "bold"))
        line_price_label.pack(side="right", padx=5, pady=5)

root = tk.Tk()
root.title("Recherche de lignes de bus")
root.geometry("600x600")
root.configure(bg="#e0f7fa")

search_frame = tk.Frame(root, bg="#e0f7fa")
search_frame.pack(fill="x", padx=10, pady=10)

search_label = tk.Label(search_frame, text="Recherche:", bg="#e0f7fa", fg="#00796b", font=("Arial", 12, "bold"))
search_label.pack(side="left", padx=5)

search_entry = tk.Entry(search_frame, font=("Arial", 12), width=40)
search_entry.pack(side="left", padx=5)
search_entry.bind("<KeyRelease>", filter_lines)  # Appeler filter_lines à chaque modification du texte

search_icon = tk.Label(search_frame, text="🔍", bg="#e0f7fa", font=("Arial", 14))
search_icon.pack(side="left", padx=5)

main_frame = tk.Frame(root, bg="#ffffff")
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

canvas = tk.Canvas(main_frame, bg="#ffffff")
canvas.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas_frame = tk.Frame(canvas, bg="#ffffff")
canvas.create_window((0, 0), window=canvas_frame, anchor="nw")

display_lines(bus_lines)

root.mainloop()
