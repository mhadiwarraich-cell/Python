import tkinter as tk
from tkinter import ttk, messagebox

class RestaurantOrderMangement:
    
    
    def __init__(self, root):
        self.root = root
        self.root.title("Restruant Mangement App")
        
        self.menu_items = {
            "FRIES MEAL":2,
            "LUNCH MEAL":2,
            "BURGER MEAL":3,
            "PIZZA  MEAL":4,
            "CHESSE BURGER":2.5,
            "DRINKS":1,
        }
        
        
        self.exange_rate = 82
        self.setup_background(root)
        
        
        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        
        ttk.Label(
            frame,
            text="Resturant Order Management",
            font=("Arial", 20, "bold")
        ).grid(row=0, columnspan=3, padx=10, pady=10)
        
        self.menu_labels = {} 
        self.menu_quantities = {}
        
        
        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            label = ttk.Label(
                frame,
                text=f"{item} (£{price}):",
                font=("Arival", 12)
            )
            
            
            label.grid(row=i, column=0, padx=10, pady=5)
            self.menu_labels[item] = label
            
            
            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quanitites[item] = quantity_entry
            
            self.currency_var = tk.Stringvar()
            ttk.Label(
                frame,
                text="Currency:",
                font=("Arial, 12")
            ).grid(
                row=len(self.menu_items) + 1,
                column=0,
                padx=10,
                pady=5
            )
                
            currency_dropdown = ttk.Combobox(
                frame,
                textvevariable=self.currency_var,
                state="redonly",
                width=18,
                values=("GBD", "PKR")
            )
            currency_dropdown.grid(
                row=len()
            )
            