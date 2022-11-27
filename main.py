import tkinter

# Window with title and size specs
window = tkinter.Tk()
window.title("Unit Converter")
window.minsize(width=300, height=200)

# miles label
miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=1, column=3)

# miles entry
miles_entry = tkinter.Entry(width=10)
miles_entry.grid(row=1, column=2)

# isequal label
is_equal_label = tkinter.Label(text="is equal to")
is_equal_label.grid(row=2, column=1)


# function to calculate miles to kms
def calculate_kms():
    entry = miles_entry.get()
    output_label["text"] = float(entry) * 1.60934


# Calculate button
calculate_button = tkinter.Button(text="Calculate", command=calculate_kms)
calculate_button.grid(row=3, column=2)

# Output label
output_label = tkinter.Label()
output_label.grid(row=2, column=2)

# Main loop to keep the screen running
window.mainloop()
