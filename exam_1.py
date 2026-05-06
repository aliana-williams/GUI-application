import tkinter
#creating the main window
main_window = tkinter.Tk()
main_window.title("Aliana's App")
main_window.geometry("450x450")

#instructions
instruction_label = tkinter.Label(main_window, text="Instructions: Use this app to add numbers, calculate BMP, or convert temperature to Celsius")
instruction_label.pack()
#calculator (addition)
def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 + num2
    result_label.config(text="Result: " + str(result))

#BMI
def calculate_bmi():
    weight = float(entry1.get())
    height = float(entry2.get())
    bmi = weight / (height * height) * 703
    result_label.config(text="BMI: " + str(bmi))

#temp
def convert_temp():
    temp = float(entry1.get())
    celsius = (temp - 32) * 5/9
    result_label.config(text="Celsius: " + str(celsius))

#clear
def clear():
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    result_label.config(text="")
#GUI

label1 = tkinter.Label(main_window, text="Enter Weight for BMI or Temperature for conversion:")
label1.pack()
entry1 = tkinter.Entry(main_window)

entry1 = tkinter.Entry(main_window)
entry1.pack()

label2 = tkinter.Label(main_window, text="Enter Height:")
label2.pack()

entry2 = tkinter.Entry(main_window)
entry2.pack()

#buttons
button1 = tkinter.Button(main_window, text="Add", command=calculate)
button1.pack()

button2 = tkinter.Button(main_window, text="Calculate BMI", command=calculate_bmi)
button2.pack()

button3 = tkinter.Button(main_window, text="Convert Temp to Celsius", command=convert_temp)
button3.pack()

button4 = tkinter.Button(main_window, text="Clear", command=clear)
button4.pack()

#output
result_label = tkinter.Label(main_window, text="")
result_label.pack()

#run program
main_window.mainloop()