from tkinter import * 
from tkinter import ttk
import tkinter as tk 
import tkinter.messagebox

class POS : 
    def __init__(self,root):
        self.root = root 
        self.root.title("Warm Coffee")
        self.root.geometry("1370x750+0+0")
        self.root.configure(background = "cadetblue")

        Change_input = StringVar()
        Cash_input = StringVar()
        Tax_input = StringVar()
        SubTotal_input = StringVar()
        Total_input = StringVar()
        Item = StringVar()
        Qty = StringVar()
        Amount = StringVar()
        choice = StringVar()

        MainFrame = Frame(self.root , bg = 'cadetblue')
        MainFrame.grid(padx=8 , pady=5)

        ButtonFrame = Frame(MainFrame , bg = 'cadetblue' , bd=5 , width=1348 , height=160 , padx=4 , pady=4 , relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame , bg='cadetblue' , bd=5 , width=800 , height=300 , padx=4 , pady=4 , relief=RIDGE)
        DataFrame.pack(side=LEFT)

        DataFrameLEFTCOVER = LabelFrame(DataFrame , bg='cadetblue' , bd=5 , width=800 , height=300 , padx=4 , pady=4 ,
                                        font=('arial' , 12 , 'bold') , text="List of Sale" , relief=RIDGE )
        DataFrameLEFTCOVER.pack(side=LEFT)

        ChangeButtonFrame = Frame(DataFrameLEFTCOVER , bd=5 , width=300 , height=460 , pady=4 , relief=RIDGE)
        ChangeButtonFrame.pack(side=RIGHT , padx=4)

        ReceiptFrame = Frame(DataFrameLEFTCOVER , bd=5 , width=200 , height=400 , pady = 5 , padx=1 , relief=RIDGE)
        ReceiptFrame.pack(side=RIGHT , padx=4) 

        FoodItemFrame = LabelFrame(DataFrame , bd=5 , width= 450 , height= 300 , padx=5 , pady=2 , relief=RIDGE , bg = 'cadetblue' , font=('arial',12 , 'bold') , text="Items")
        FoodItemFrame.pack(side=RIGHT)

        CalFrame = Frame(ButtonFrame , bd=5 , width=432 , height=140 , relief=RIDGE)
        CalFrame.grid(row = 0 , column= 0 , padx= 5)

        ChangeFrame = Frame(ButtonFrame , bd=5 , width=500 , height=140 , pady=2 , relief=RIDGE)
        ChangeFrame.grid(row=0 , column= 1 , padx = 5)

        RemoveFrame = Frame(ButtonFrame , bd=5 , width=400 , height=140 , pady=4 , relief=RIDGE)
        RemoveFrame.grid(row = 0 , column= 2 , padx=5)

        # ===================================== Entry & Label widget =====================================
        self.lblSubTotal = Label(CalFrame , font=('arial' , 14 , 'bold') , text="Sub Total" , bd=5)
        self.lblSubTotal.grid(row=0 , column=0 , sticky=W , padx=5)
        self.txtSubTotal = Entry(CalFrame , font=('arial' , 14 , 'bold') , textvariable=SubTotal_input , bd=2 , width=24 )
        self.txtSubTotal.grid(row = 0 , column = 1 , padx =5)

        self.lblTax = Label(CalFrame , font=('arial' , 14 , 'bold') , text="Tax" , bd=5)
        self.lblTax.grid(row=1 , column=0 , sticky=W , padx=5)
        self.txtSubTotal = Entry(CalFrame , font=('arial' , 14 , 'bold') , textvariable=Tax_input , bd=2 , width=24 )
        self.txtSubTotal.grid(row = 1 , column = 1 , padx =5)

        self.lblTax = Label(CalFrame , font=('arial' , 14 , 'bold') , text="Total" , bd=5)
        self.lblTax.grid(row=2 , column=0 , sticky=W , padx=5)
        self.txtSubTotal = Entry(CalFrame , font=('arial' , 14 , 'bold') , textvariable=Total_input , bd=2 , width=24 )
        self.txtSubTotal.grid(row = 2 , column = 1 , padx =5)

        # ===================================== Entry & Label widget =====================================
        self.lblMoP = Label(ChangeFrame , font=('arial' , 14 , 'bold') , text="Method of Payment" , bd=5)
        self.lblMoP.grid(row=0 , column=0 , sticky=W , padx=5)
        self.cboMoP = ttk.Combobox(ChangeFrame , font=('arial' , 14 , 'bold')  , width=36 , state='readonly' , textvariable=choice , justify=RIGHT )

        self.cboMoP['values'] = ('' , 'Cash' , 'Ture Money' , 'Poung tung')
        self.cboMoP.current(0)
        self.cboMoP.grid(row = 0 , column = 1 )

        self.lblCost = Label(ChangeFrame , font=('arial' , 14 , 'bold') , text="Cash" , bd=5)
        self.lblCost.grid(row=1 , column=0 , sticky=W , padx=5)
        self.txtCost = Entry(ChangeFrame , font=('arial' , 14 , 'bold') , textvariable=Tax_input , bd=2 , width=38 )
        self.txtCost.grid(row = 1 , column = 1 , padx =5)

        self.lblChange = Label(ChangeFrame , font=('arial' , 14 , 'bold') , text="Change" , bd=5)
        self.lblChange.grid(row=2 , column=0 , sticky=W , padx=5)
        self.txtChange = Entry(ChangeFrame , font=('arial' , 14 , 'bold') , textvariable=Total_input , bd=2 , width=38 )
        self.txtChange.grid(row = 2 , column = 1 , padx =5)

        # ===================================== Entry & Label widget =====================================
        self.btnPay = Button(RemoveFrame , padx=2 , font=('arial' , 15 , 'bold') , text='Pay' , width=10 , height=1 , bd=2)
        self.btnPay.grid(row = 0 , column=0 , pady=2 , padx=4)




if __name__ == '__main__':
    root = Tk()
    application = POS(root)
    root.mainloop()