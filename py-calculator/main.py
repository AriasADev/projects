import sys
import os
from tkinter import *
from decimal import Decimal, InvalidOperation

def enforce_aspect(event):
    if event.widget == root:
        w, h = root.winfo_width(), root.winfo_height()
        if w / h != aspect_ratio:
            root.geometry(f"{int(h * aspect_ratio)}x{h}" if w > h * aspect_ratio else f"{w}x{int(w / aspect_ratio)}")

def calculator():
    global root, aspect_ratio
    root = Tk()
    aspect_ratio = 3 / 4
    root.title("Calculator")
    root.geometry("375x500")  # Start 25% bigger
    root.minsize(375, 500)

    # Handle icon for bundled executable
    if getattr(sys, 'frozen', False):  # If running as a bundled executable
        icon_path = os.path.join(sys._MEIPASS, 'icon.ico')
    else:  # If running as a script
        icon_path = 'icon.ico'

    try:
        root.iconbitmap(default=icon_path)
    except Exception as e:
        print(f"Error loading icon: {e}")

    root.bind("<Configure>", enforce_aspect)

    create_ui_elements(root)
    root.mainloop()

def create_ui_elements(container):
    """
    A dedicated function to add UI elements to a container (e.g., the root window).
    """
    # Create a display (Entry widget) at the top of the calculator
    global display
    display = Entry(container, font=("Arial", 20), justify="right", bd=10)
    display.pack(fill="x", padx=10, pady=10)

    # Create a frame to hold the buttons
    button_frame = Frame(container)
    button_frame.pack(padx=10, pady=10, expand=True)

    # Define the button layout (rows of buttons)
    button_texts = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["C", "0", ".", "DEL"],
        ["+", "="],
    ]

    # Create buttons and add them to the frame
    for row in button_texts:
        row_frame = Frame(button_frame)
        row_frame.pack(fill="x", expand=True)
        for text in row:
            button = Button(
                row_frame,
                text=text,
                font=("Arial", 14),
                width=6,  # Adjusted width for better fit
                height=2,
                command=lambda t=text: handle_button_click(t)  # Attach command
            )
            button.pack(side="left", padx=5, pady=5, expand=True, fill="both")

# Function to handle button clicks
def handle_button_click(value):
    """
    Handle button clicks. Add the button value to the display or perform actions.
    """
    current = display.get()  # Get the current value from the display
    if value == "C":  # Clear the display
        display.delete(0, END)
    elif value == "DEL":  # Delete the last character or clear if "Error" is displayed
        if current == "Error":
            display.delete(0, END)  # Clear the display if it's showing "Error"
        else:
            display.delete(len(current) - 1, END)  # Delete the last character
    elif value == "=":  # Evaluate the expression
        try:
            # Use Decimal for precise arithmetic
            result = eval_decimal_expression(current)
            display.delete(0, END)
            display.insert(END, str(result))
        except (InvalidOperation, Exception):
            display.delete(0, END)
            display.insert(END, "Error")
    else:  # Add the button's value to the display
        if value == "." and "." in current.split()[-1]:  # Avoid multiple dots in a number
            return
        display.insert(END, value)



def eval_decimal_expression(expression):
    """
    Evaluate a mathematical expression using Decimal for precision.
    """
    # Replace operators to work with Decimal
    expression = expression.replace("/", "//")  # Force integer division to act like Decimal division
    return Decimal(eval(expression, {"__builtins__": {}}, {"Decimal": Decimal}))

calculator()
