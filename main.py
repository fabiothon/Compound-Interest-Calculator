
# =============================================================================
# Compound Interest Calculator
# =============================================================================

# Libraries
import math 
import customtkinter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#Variables
period = float(0)

# APPLICATION: Definition of initial application layout
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("800x600")
root.title("Compound Interest Calculator")

label = customtkinter.CTkLabel(master=root, text="This is a testapplication for ZHAW-INE to show the possibility for an interactive math-based simulation.", 
                               font = ("Arial", 11))
label.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER, y = -80)

label_pa = customtkinter.CTkLabel(master=root, text="Principle amount [$]", font = ("Arial", 10))
label_pa.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER, x = -260, y = 300)

label_ir = customtkinter.CTkLabel(master=root, text="Interest rate [%]", font = ("Arial", 10))
label_ir.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER, x = -270, y = 340)

label_t = customtkinter.CTkLabel(master=root, text="Time [Years]", font = ("Arial", 10))
label_t.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER, x = -275, y = 380)


# APPLICATION: Slider definition
slider_principle_amount = customtkinter.CTkSlider(master=root, width=400, height=16, from_= 0, to = 1500, border_width=5.5)
slider_principle_amount.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER, y = 120)

slider_interest_rate = customtkinter.CTkSlider(master=root, width=400, height=16, from_= 0, to = 30, border_width=5.5)
slider_interest_rate.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER, y = 160)

slider_time = customtkinter.CTkSlider(master=root, width=400, height=16, from_= 0, to = 40, border_width=5.5)
slider_time.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER, y = 200)

# Matplot Setup for plotting
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER, y = -140)

# Calculator
def compound_interest(period,principle_amount,interest_rate,time):   
    amounts = []
    cis = []
    for period in range(time):
        amt = principle_amount * (math.pow((1 + (interest_rate/100)),period+1))
        amounts.append(amt)
        ci = amt - principle_amount
        cis.append(ci)
        
    return amounts, cis

def update_and_calculate():
    principle_amount = slider_principle_amount.get()
    interest_rate = slider_interest_rate.get()
    time = int(slider_time.get())

    amounts, cis = compound_interest(period, principle_amount, interest_rate, time)

    ax.clear()
    ax.bar(range(1, time + 1), amounts, color='navy')
    ax.bar(range(1, time + 1), cis, bottom=amounts, color='coral')
    ax.set_xlabel('Time Period [Years]')
    ax.set_ylabel('Compound Amount [$]')
    ax.set_title('Compound Interest Over Time')
    canvas.draw()

# APPLICATION: Calculation
button_calculate = customtkinter.CTkButton(master=root, text="Calculate", command=update_and_calculate)
button_calculate.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER, y = 200)

root.mainloop()