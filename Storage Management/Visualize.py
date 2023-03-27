import itertools
from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
import cv2 as cv
from DateBaseProccess import fetchMaterials, postProduct, getProducts, getProductById, getMaterialById, getMaterials
from PIL import ImageTk, Image

window = tk.Tk()
window.title("Storage System")
window.iconbitmap("assets/favicon.ico")
window.geometry("650x350")
window.overrideredirect(True)
#It serves to open the frame in the middle
windowwidth = window.winfo_screenwidth()
windowheight = window.winfo_screenheight()
window.geometry(f"650x350+{(windowwidth // 2) - 350}+{(windowheight // 2) - 230}")

materials = fetchMaterials()
products = getProducts()

def start():
    frame = Frame(window, bg="#1C1C1C", width=650, height=500)
    frame.place(x=0, y=0)

    button = Button(frame, text="Close the System", height=4, width=20, activebackground="grey25", font="Verdana 12 bold", command=window.quit, fg="#1C1C1C", bg="OrangeRed3", relief=FLAT)
    button.place(x=210, y=200)
    button2 = Button(frame, text="Start the System", height=4, width=20, activebackground="grey25", font="Verdana 12 bold", command=firstframe, fg="#1C1C1C", bg="OrangeRed3", relief=FLAT)
    button2.place(x=210, y=80)

def firstframe():
    products2 = getProducts()

    window.overrideredirect(False)
    frame1 = Frame(window, bg="#1C1C1C", width=650, height=500)
    frame1.place(x=0, y=0)

    Label1 = Label(frame1, text="Choose Your Product", font="Verdana 12 bold", fg="OrangeRed3", bg="#1C1C1C")
    Label1.place(x=20, y=20)
    Label2 = Label(frame1, text="Name Your Product", font="Verdana 12 bold", fg="OrangeRed3", bg="#1C1C1C")
    Label2.place(x=20, y=50)
    Label3 = Label(frame1, text="Date of Production", font="Verdana 12 bold", fg="OrangeRed3", bg="#1C1C1C")
    Label3.place(x=20, y=80)
    Label4 = Label(frame1, text="Name of Customer", font="Verdana 12 bold", fg="OrangeRed3", bg="#1C1C1C")
    Label4.place(x=20, y=110)
    Label5 = Label(frame1, text="Expiration Date", font="Verdana 12 bold", fg="OrangeRed3", bg="#1C1C1C")
    Label5.place(x=20, y=140)
    Label6 = Label(frame1, text="Storage Code", font="Verdana 12 bold", fg="OrangeRed3", bg="#1C1C1C")
    Label6.place(x=20, y=170)
    Label7 = Label(frame1, text="Used Raw Materials", font="Verdana 12 bold", fg="OrangeRed3", bg="#1C1C1C")
    Label7.place(x=452, y=100)
    Label8 = Label(frame1, text="Description", font="Verdana 12 bold", fg="OrangeRed3", bg="#1C1C1C")
    Label8.place(x=20, y=200)

    def productNames(products3):
        plist = []
        for product in products3:
            name = product[1]
            plist.append(name)
        return plist

    scrollbar = Scrollbar(window)
    scrollbar.place(x=595, y=130, height=118)
    usedMaterials = Listbox(frame1, font="Verdana 12 bold", height=6, width=10, fg="OrangeRed3", bg="#1C1C1C")
    usedMaterials.config(yscrollcommand=scrollbar.set)
    usedMaterials.place(x=480, y=130)

    nameVar = StringVar()
    pName = Label(frame1, width=20, font="Verdana 12 bold", fg="OrangeRed3", bg="grey25", relief=FLAT,textvariable=nameVar)
    pName.place(x=220, y=50)
    dopVar = StringVar()
    pDateOfProduction = Label(frame1, width=20, font="Verdana 12 bold", fg="OrangeRed3", bg="grey25", relief=FLAT,textvariable=dopVar)
    pDateOfProduction.place(x=220, y=80)
    nocVar = StringVar()
    pNameOfCustomer = Label(frame1, width=20, font="Verdana 12 bold", fg="OrangeRed3", bg="grey25", relief=FLAT,textvariable=nocVar)
    pNameOfCustomer.place(x=220, y=110)
    sedVar = StringVar()
    pStorageExpDate = Label(frame1, width=20, font="Verdana 12 bold", fg="OrangeRed3", bg="grey25", relief=FLAT,textvariable=sedVar)
    pStorageExpDate.place(x=220, y=140)
    scVar = StringVar()
    pStorageCode = Label(frame1, width=20, font="Verdana 12 bold", fg="OrangeRed3", bg="grey25", relief=FLAT,textvariable=scVar)
    pStorageCode.place(x=220, y=170)
    dVar = StringVar()
    pDescription = Label(frame1, width=38, height=5, font="Verdana 12 bold", fg="OrangeRed3", bg="grey25", relief=FLAT,textvariable=dVar,wraplength=300, justify="center")
    pDescription.place(x=20, y=230)

    # function that opens camera
    def openCamera():
        cap = cv.VideoCapture(0)
        while cap.isOpened():
            ret, frame = cap.read()
            # if frame is read correctly ret is True
            if not ret:
                print("Can't receive frame. Exiting ...")
                break

            cv.imshow("frame", frame)
            if cv.waitKey(1) == ord("q"):
                break
        cap.release()
        cv.destroyAllWindows()

    # function for opening images
    def openImage():
        name = nameVar.get()
        if name == "":
            return
        novi = Toplevel()
        canvas = Canvas(novi, width=500, height=500)
        canvas.pack(expand=YES, fill=BOTH)
        load = Image.open(f"assets/{name}.png")
        load = load.resize((500, 500), Image.LANCZOS)
        render = ImageTk.PhotoImage(load)
        img = Label(novi, image=render)
        img.image = render
        img.place(x=0, y=0)

    sfbutton = Button(frame1, text="Add New Product", activebackground="grey25", font="Verdana 12", command=secondframe,fg="#1C1C1C", bg="OrangeRed3", relief=FLAT)
    sfbutton.place(x=470, y=20)
    sfbutton2 = Button(frame1, text="Product Image", activebackground="grey25", font="Verdana 12", fg="#1C1C1C",bg="OrangeRed3", relief=FLAT, command=openImage)
    sfbutton2.place(x=480, y=60)
    button2 = Button(frame1, text="Camera", height=3, width=10, activebackground="grey25", font="Verdana 12",fg="#1C1C1C", bg="OrangeRed3", relief=FLAT, command=openCamera)
    button2.place(x=490, y=270)

    def getProductDetail(event):
        if combobox.get() == "":
            return
        productId = 0
        for product in products2:
            if product[1] == combobox.get():
                productId = product[0]
        productDetail = [*getProductById(productId)]
        nameVar.set(productDetail[0][1])
        dopVar.set(productDetail[0][2])
        nocVar.set(productDetail[0][3])
        sedVar.set(productDetail[0][4])
        scVar.set(productDetail[0][5])
        dVar.set(productDetail[0][7])
        x = productDetail[0][6].split(",")
        usedMaterials.delete(0, END)
        for x2 in x:
            usedMaterials.insert(END, x2)
    
    combobox = Combobox(frame1, width=34, height=5,values=(productNames(products2)))
    combobox.bind('<<ComboboxSelected>>', getProductDetail)
    combobox.place(x=220, y=20)


def secondframe():
    window.overrideredirect(False)
    for i in window.winfo_children():
        i.destroy()

    frame2 = Frame(window, bg="#1C1C1C", width=650, height=500)
    frame2.place(x=0, y=0)

    pNameLabel = Label(frame2, text="Name Your Product", font="Verdana 12 bold", fg="OrangeRed3", bg="#1C1C1C")
    pNameLabel.place(x=20, y=20)
    pDateOfProductionLabel = Label(frame2, text="Date of Production", font="Verdana 12 bold", fg="OrangeRed3", bg="#1C1C1C")
    pDateOfProductionLabel.place(x=20, y=50)
    pNameOfCustomerLabel = Label(frame2, text="Name of Customer", font="Verdana 12 bold", fg="OrangeRed3", bg="#1C1C1C")
    pNameOfCustomerLabel.place(x=20, y=80)
    pStorageExpDateLabel = Label(frame2, text="Expiration Date", font="Verdana 12 bold", fg="OrangeRed3", bg="#1C1C1C")
    pStorageExpDateLabel.place(x=20, y=110)
    pStorageCodeLabel = Label(frame2, text="Storage Code", font="Verdana 12 bold", fg="OrangeRed3", bg="#1C1C1C")
    pStorageCodeLabel.place(x=20, y=140)
    pDescriptionLabel = Label(frame2, text="Description", font="Verdana 12 bold", fg="OrangeRed3", bg="#1C1C1C")
    pDescriptionLabel.place(x=20, y=170)
    pListOfMatCodesLabel = Label(frame2, text="Raw Materials", font="Verdana 12 bold", fg="OrangeRed3", bg="#1C1C1C")
    pListOfMatCodesLabel.place(x=485, y=20)

    pName = Entry(frame2, width=20, font="Verdana 12 bold", fg="OrangeRed3", bg="grey25", relief=FLAT)
    pName.place(x=220, y=20)
    pDateOfProduction = Entry(frame2, width=20, font="Verdana 12 bold", fg="OrangeRed3", bg="grey25", relief=FLAT)
    pDateOfProduction.place(x=220, y=50)
    pNameOfCustomer = Entry(frame2, width=20, font="Verdana 12 bold", fg="OrangeRed3", bg="grey25", relief=FLAT)
    pNameOfCustomer.place(x=220, y=80)
    pStorageExpDate = Entry(frame2, width=20, font="Verdana 12 bold", fg="OrangeRed3", bg="grey25", relief=FLAT)
    pStorageExpDate.place(x=220, y=110)
    pStorageCode = Entry(frame2, width=20, font="Verdana 12 bold", fg="OrangeRed3", bg="grey25", relief=FLAT)
    pStorageCode.place(x=220, y=140)
    pDescription = Entry(frame2, width=38, font="Verdana 12 bold", fg="OrangeRed3", bg="grey25", relief=FLAT, justify="center")
    pDescription.place(x=20, y=200)

    #Add new product function
    def fillList():
        class Checkbar(Frame):
            def __init__(self, parent=None, picks=None, side=TOP, anchor=W):
                Frame.__init__(self, parent)
                if picks is None:
                    picks = []
                self.vars = []
                for pick in picks:
                    var = IntVar()
                    chk = Checkbutton(self, text=pick, variable=var, font="Verdana 12 bold", fg="OrangeRed3")
                    chk.pack(side=side, anchor=anchor, expand=YES)
                    self.vars.append(var)
            def state(self):
                return map((lambda var: var.get()), self.vars)

        if __name__ == '__main__':
            matnames = []
            for mat in [*materials]:
                matnames.append(mat[1])
            lng = Checkbar(frame2, matnames)
            lng.config(relief=GROOVE, bd=2)
            lng.place(x=497, y=50)

            def addProduct():
                checkedMaterials = []
                for idx, rw in enumerate(list(lng.state())):
                    if rw == 1:
                        checkedMaterials.append((materials[idx][1]))
                output_string = ""
                for datum in checkedMaterials:
                    output_string += datum + ","
                product = [pName.get(), pDateOfProduction.get(), pNameOfCustomer.get(), pStorageExpDate.get(), pStorageCode.get(), output_string, pDescription.get()]
                temp = [*product]
                postProduct(temp)

            sfbutton1 = Button(frame2, text="Back", activebackground="grey25", font="Verdana 12", command=firstframe, fg="#1C1C1C", bg="OrangeRed3", relief=FLAT)
            sfbutton1.place(x=20, y=300)
            sfbutton2 = Button(frame2, text="Add Product", activebackground="grey25", font="Verdana 12", command=addProduct, fg="#1C1C1C", bg="OrangeRed3", relief=FLAT)
            sfbutton2.place(x=220, y=300)
            sfbutton3 = Button(frame2, text="Material Details", activebackground="grey25", font="Verdana 12",command=thirdframe,fg="#1C1C1C", bg="OrangeRed3", relief=FLAT)
            sfbutton3.place(x=450, y=300)
    fillList()

def thirdframe():
    material2 = getMaterials()

    window.overrideredirect(False)
    frame3 = Frame(window, bg="#1C1C1C", width=650, height=500)
    frame3.place(x=0, y=0)

    Label1 = Label(frame3, text="Choose Your Material", font="Verdana 12 bold", fg="OrangeRed3", bg="#1C1C1C")
    Label1.place(x=20, y=20)
    Label2 = Label(frame3, text="Name Your Material", font="Verdana 12 bold", fg="OrangeRed3", bg="#1C1C1C")
    Label2.place(x=20, y=50)
    Label3 = Label(frame3, text="Date of Purchase", font="Verdana 12 bold", fg="OrangeRed3", bg="#1C1C1C")
    Label3.place(x=20, y=80)
    Label4 = Label(frame3, text="Name of Supplier", font="Verdana 12 bold", fg="OrangeRed3", bg="#1C1C1C")
    Label4.place(x=20, y=110)
    Label5 = Label(frame3, text="Expiration Date", font="Verdana 12 bold", fg="OrangeRed3", bg="#1C1C1C")
    Label5.place(x=20, y=140)
    Label6 = Label(frame3, text="Storage Code", font="Verdana 12 bold", fg="OrangeRed3", bg="#1C1C1C")
    Label6.place(x=20, y=170)
    Label8 = Label(frame3, text="Description", font="Verdana 12 bold", fg="OrangeRed3", bg="#1C1C1C")
    Label8.place(x=20, y=200)

    def materialNames(material3):
        mlist = []
        for material in material3:
            name = material[1]
            mlist.append(name)
        return mlist

    nameVar = StringVar()
    pName = Label(frame3, width=20, font="Verdana 12 bold", fg="OrangeRed3", bg="grey25", relief=FLAT, textvariable=nameVar)
    pName.place(x=220, y=50)
    dopVar = StringVar()
    pDateOfProduction = Label(frame3, width=20, font="Verdana 12 bold", fg="OrangeRed3", bg="grey25", relief=FLAT, textvariable=dopVar)
    pDateOfProduction.place(x=220, y=80)
    nocVar = StringVar()
    pNameOfCustomer = Label(frame3, width=20, font="Verdana 12 bold", fg="OrangeRed3", bg="grey25", relief=FLAT, textvariable=nocVar)
    pNameOfCustomer.place(x=220, y=110)
    sedVar = StringVar()
    pStorageExpDate = Label(frame3, width=20, font="Verdana 12 bold", fg="OrangeRed3", bg="grey25", relief=FLAT, textvariable=sedVar)
    pStorageExpDate.place(x=220, y=140)
    scVar = StringVar()
    pStorageCode = Label(frame3, width=20, font="Verdana 12 bold", fg="OrangeRed3", bg="grey25", relief=FLAT, textvariable=scVar)
    pStorageCode.place(x=220, y=170)
    dVar = StringVar()
    pDescription = Label(frame3, width=38, height=5, font="Verdana 12 bold", fg="OrangeRed3", bg="grey25", relief=FLAT,textvariable=dVar,
    wraplength=300, justify="center")
    pDescription.place(x=20, y=230)

    sfbutton1 = Button(frame3, text="Back", activebackground="grey25", font="Verdana 12", command=secondframe, fg="#1C1C1C", bg="OrangeRed3", relief=FLAT)
    sfbutton1.place(x=520, y=300)

    def getMaterialDetail(event):
        if combobox.get() == "":
            return
        productId = 0
        for material in material2:
            if material[1] == combobox.get():
                materialId = material[0]
        materialDetail = [*getMaterialById(materialId)]
        nameVar.set(materialDetail[0][1])
        dopVar.set(materialDetail[0][2])
        nocVar.set(materialDetail[0][3])
        sedVar.set(materialDetail[0][4])
        scVar.set(materialDetail[0][5])
        dVar.set(materialDetail[0][6])

    combobox = Combobox(frame3, width=34, height=5, values=(materialNames(material2)))
    combobox.bind('<<ComboboxSelected>>', getMaterialDetail)
    combobox.place(x=220, y=20)

start()
window.mainloop()
