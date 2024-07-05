import customtkinter as ctk
import tkinter as tk

# Dictionary to track open quantity windows
open_windows = []

# def add_product_frame(parent, product_id):
#     product_frame = ctk.CTkFrame(parent, width=760, height=150)
#     product_frame.pack(padx=10, pady=10)

#     # Example content in product frame
#     name_label = ctk.CTkLabel(product_frame, text=f"Product {product_id}")
#     name_label.pack(pady=10)

#     add_to_cart_button = ctk.CTkButton(product_frame, text="Add to Cart", command=lambda: open_quantity_window(product_id))
#     add_to_cart_button.pack(pady=10)
        
def open_quantity_window(product_id):
    global open_windows

    # Check if the window is already open
    if product_id in open_windows:
        open_windows[product_id].focus()
        return
    
    # Create a new window
    quantity_window = ctk.CTkToplevel()
    quantity_window.title(f"Quantity for Product {product_id}")
    quantity_window.geometry("300x200")

    def on_closing():
        del open_windows[product_id]
        quantity_window.destroy()

    quantity_window.protocol("WM_DELETE_WINDOW", on_closing)
    open_windows[product_id] = quantity_window

    # Add quantity selection elements
    quantity_label = ctk.CTkLabel(quantity_window, text="Enter quantity:")
    quantity_label.pack(pady=10)

    quantity_entry = ctk.CTkEntry(quantity_window)
    quantity_entry.pack(pady=10)

    add_button = ctk.CTkButton(quantity_window, text="Add", command=lambda: add_to_cart(product_id, quantity_entry.get()))
    add_button.pack(pady=10)
        
def add_to_cart(product_id, quantity):
    global open_windows

    # Handle adding to cart logic here
    print(f"Product {product_id} added to cart with quantity {quantity}")
    open_windows[product_id].destroy()
    del open_windows[product_id]

def main():
    root = ctk.CTk()
    root.title("Store Menu")
    root.geometry("800x600")
    
    scrollable_frame = ctk.CTkScrollableFrame(root, width=780, height=580)
    scrollable_frame.pack(padx=10, pady=10)
    
    # Example of adding product frames
    for i in range(5):  # Suppose there are 5 products
        add_product_frame(scrollable_frame, i)

    root.mainloop()

if __name__ == "__main__":
    main()
