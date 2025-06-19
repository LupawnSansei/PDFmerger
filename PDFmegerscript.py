from pypdf import PdfWriter
import datetime
import tkinter as tk
from tkinter.filedialog import askopenfilename

def gather_pdfs():
    gaining_pdfs = True
    while gaining_pdfs:
        pdf = input("Enter q to quit.")

        if pdf == 'q':
            gaining_pdfs = False
        else:
            gather_file()


def gather_file():
    tk.Tk().withdraw()  # part of the import if you are not using other tkinter functions

    fn = askopenfilename()
    print("user chose", fn)
    pdf_list.append(fn)


merger = PdfWriter()

pdf_list = []

gather_pdfs()





go_or_stop = True
while go_or_stop:
    print("This will be the order in which the files will be merged in:")
    for pdf in pdf_list:
        print(pdf)
    choice = input("Is this the correct order? (Y/n) ")

    if choice.lower()== 'y':
        for pdf in pdf_list:
            merger.append(pdf)

        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
        merger.write("merged_" + formatted_datetime)
        go_or_stop = False
        merger.close()
    elif choice.lower() == 'n':
        pdf_list.clear()
        gather_pdfs()
