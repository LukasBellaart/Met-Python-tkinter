import tkinter as tk
window = tk.Tk()

color = False
def switchColor():
    global color
    color = not color
    if color:
        print('light turning on')
        button.configure(text="turn light off")
        window.configure(bg="yellow")
    elif not color:
        print('light turning off')
        button.configure(text="turn light on")
        window.configure(bg="black")

button = tk.Button(text='...', bg="white", fg="black", command = switchColor)
button.pack(pady = 20, padx = 20)

# schijf hier tussen je code



# schijf hier tussen je code

window.mainloop()