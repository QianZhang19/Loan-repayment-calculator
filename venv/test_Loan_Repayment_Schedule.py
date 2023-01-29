from Loan_Repayment_Schedule import delButton
from Loan_Repayment_Schedule import calc
from tkinter import *
from tkinter import ttk

root = Tk()
tree = ttk.Treeview(root, show="headings")
root = None


def test_delButton():
    output = delButton(tree)
    assert output == root
