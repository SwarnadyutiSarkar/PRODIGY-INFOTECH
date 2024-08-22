import tkinter as tk
from tkinter import ttk

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature(value, unit):
    if unit.lower() == 'celsius':
        fahrenheit = celsius_to_fahrenheit(value)
        kelvin = celsius_to_kelvin(value)
        return f"{value} Celsius = {fahrenheit:.2f} Fahrenheit\n{value} Celsius = {kelvin:.2f} Kelvin"
    elif unit.lower() == 'fahrenheit':
        celsius = fahrenheit_to_celsius(value)
        kelvin = fahrenheit_to_kelvin(value)
        return f"{value} Fahrenheit = {celsius:.2f} Celsius\n{value} Fahrenheit = {kelvin:.2f} Kelvin"
    elif unit.lower() == 'kelvin':
        celsius = kelvin_to_celsius(value)
        fahrenheit = kelvin_to_fahrenheit(value)
        return f"{value} Kelvin = {celsius:.2f} Celsius\n{value} Kelvin = {fahrenheit:.2f} Fahrenheit"
    else:
        return "Invalid unit of measurement. Please use 'Celsius', 'Fahrenheit', or 'Kelvin'."

def on_convert():
    try:
        temperature = float(entry_temp.get())
        unit = combo_unit.get()
        result = convert_temperature(temperature, unit)
        result_text.set(result)
    except ValueError:
        result_text.set("Invalid input. Please enter a numeric value for the temperature.")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Create and place the widgets
tk.Label(root, text="Temperature:").grid(row=0, column=0, padx=10, pady=10)
entry_temp = tk.Entry(root)
entry_temp.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Unit:").grid(row=1, column=0, padx=10, pady=10)
combo_unit = ttk.Combobox(root, values=['Celsius', 'Fahrenheit', 'Kelvin'])
combo_unit.grid(row=1, column=1, padx=10, pady=10)
combo_unit.set('Celsius')

tk.Button(root, text="Convert", command=on_convert).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify='left')
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
