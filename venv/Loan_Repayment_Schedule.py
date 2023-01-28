# Create graphical user interface
from tkinter import *
from tkinter import ttk
import math


root = Tk()
# Create title and size
root.title('Loan Repayment Schedules')
root.geometry('1000x330')
root.resizable(False, False)
# Create textbox and size
Label(root, text='Loan Amount:').place(x=30, y=30)
Label(root, text='Annual Interest Rate:').place(x=300, y=30)
Label(root, text='Loan Period:').place(x=570, y=30)
e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)

e1.place(x=30, y=70)
e2.place(x=300, y=70)
e3.place(x=570, y=70)

tag = 1
# Create radio button
r = IntVar()
radio1 = Radiobutton(root, text="in years", value=1,
                     variable=r).place(x=700, y=10)
radio2 = Radiobutton(root, text="in months", value=12,
                     variable=r).place(x=700, y=40)
# Create columns of the result table
columns = ("Period", "Payment Amount", "Principal Amount",
           "Interest Amount", "Loan Outstanding Balance")

tree = ttk.Treeview(root, show="headings", column=columns)

for i in range(0, 5):
    tree.column(columns[i], anchor='center')
for i in range(0, 5):
    tree.heading(columns[i], text=columns[i])
tree.pack(side=BOTTOM, fill=X)

# Delete previous contents when starting a new calculation


def delButton(tree):
    x = tree.get_children()
    for item in x:
        tree.delete(item)
# Calculation with famulas


def calc():
    delButton(tree)  # first delete all row in the form
    amount = float(e1.get())  # get loan amount
    interestRate = float(e2.get())  # get annual interest rate
    period = int(e3.get())  # get period
    tag = float(r.get())  # get month or year
    interestRate /= tag
    # Calculate payment monthly
    payment = amount*interestRate * \
        math.pow(1+interestRate, period)/(pow(1+interestRate, period)-1)
    loanBalance = amount
    # Use "for" loop for calculation every time
    for i in range(1, period+1):
        # Calculate principal payment
        PP = payment/math.pow(1+interestRate, 1+period-i)
        INT = payment - PP  # Calculate interest payment
        OB = loanBalance - PP  # Calculate Loan Outstanding Balance
        # Insert the result to the table
        tree.insert('', i, values=(i, '%.2f' % payment, '%.2f' %
                    PP, '%.2f' % INT, '%.2f' % OB))
        loanBalance = OB


Button(root, text='Get Ans', width=10, command=calc).place(x=850, y=50)

# refreshing
mainloop()
