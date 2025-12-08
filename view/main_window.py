import tkinter as tk
from tkinter import ttk
from ui.car_table import CarTable
import json

class MainWindow:
    """ Hlavní okno aplikace """

    def __init__(self):
        self.root = tk.Tk()    
        self._configure_window()
        self._create_widgets()
        self._load_data()
    
    def _configure_window(self):
        """ Konfigurace hlavního okna """
        self.root.title("🚗 Správa Aut")
        self.root.geometry("900x500")
        self.root.minsize(600, 400)
    
    def _create_widgets(self):
        """ Vytvoření widgetů v hlavním okně """
        main_frame = ttk.Frame(self.root, padding=36)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Nadpis
        title = ttk.Label(
            main_frame,
            text="Správa autobazaru",
            font=("Segoe UI", 18, "bold")
        )
        title.pack(pady=(0, 24))

        # Tabulka aut
        table_frame = ttk.LabelFrame(main_frame, text="Seznam aut", padding=10)
        table_frame.pack(fill=tk.BOTH, expand=True)

        self.table = CarTable(table_frame)
        self.table.pack(fill=tk.BOTH, expand=True)

        #Informační text
        info = ttk.Label(
            main_frame,
            text="Vyberte auto pro zobrazení detailů nebo úpravu.",
            font=("Segoe UI", 10)
        )
        info.pack(pady=(8, 0))

    def _load_data(self):
        """ Načtení dat do tabulky (zatím prázdná metoda) """
        
        try:
            with open("data/cars.json", "r", encoding="utf-8") as file:
                cars_data = json.load(file)
            
            self.table.refresh(cars_data)

            total_value = sum(car["price"] for car in cars_data)
            self.stats_label.configure(
                text=f"Počet vozidel: {len(cars_data)} | Celková hodnota: {total_value} Kč"
            )

        except FileNotFoundError:
            print("Soubor s daty nebyl nalezen.")
    
    def run(self):
        """ Spuštění hlavní smyčky aplikace """
        self.root.mainloop()