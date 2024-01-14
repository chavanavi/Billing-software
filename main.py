from tkinter import *
import math , random,os
from tkinter import messagebox
class bill_App:
    def __init__(self, root ):
     self.root = root
     self.root.geometry("1350x700+0+0")
     self.root.title("Software billing")
     self.root.title("   Create by.Aviraj Chavan  / 8766546560")
     bg_color="#074463"
     title = Label(self.root, text="Billing Software ",bd=12,relief= GROOVE,bg=bg_color,fg="white", font=("time new roman", 30, "bold"), pady=2).pack(fill=X)


     #=================================varabiles ===============================================
#============================================ costmetics=============================
     self.soap = IntVar()
     self.face_cream = IntVar()
     self.face_wash = IntVar()
     self.spray = IntVar()
     self.gell = IntVar()
     self.loshon = IntVar()
#===================================grocrey=================================
     self.rice = IntVar()
     self.food_oil = IntVar()
     self.daal = IntVar()
     self.wheat = IntVar()
     self.sugar = IntVar()
     self.tea = IntVar()
#============================================cold drinks==========================
     self.maza = IntVar()
     self.cock = IntVar()
     self.frooti = IntVar()
     self.thumbsup = IntVar()
     self.limca= IntVar()
     self.sprite = IntVar()
#=======================Total Product price &Tax varabile==============================
     self.cosmetic_price = StringVar()
     self.grocery_price = StringVar()
     self.cold_drink_price = StringVar()
     self.cosmetic_tax = StringVar()
     self.grocery_tax = StringVar()
     self.cold_drink_tax = StringVar()

#=============================customer========================================
     self.c_name = StringVar()
     self.c_phone = StringVar()
     self.c_bill_no = StringVar()
     x = random.randint(1000, 9999)
     self.c_bill_no.set(str(x))
     self.search_bill = StringVar()
#=================== customer details freame ========================
     F1=LabelFrame(self.root , bd=10 , relief=GROOVE , text="customer details" , font=("time new roman" , 15 , "bold"),fg="gold",bg=bg_color)
     F1.place(x=0,y=80,relwidth=1)

     cname_1Lab=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("time new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
     cname_text= Entry(F1,width=15, textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

     cphn_1Lab = Label(F1, text="Phone No.", bg=bg_color, fg="white", font=("time new roman", 18, "bold")).grid( row=0, column=2, padx=20, pady=5)
     cphn_text = Entry(F1, width=15,textvariable=self.c_phone, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

     c_bill_1Lab = Label(F1, text="Bill Number", bg=bg_color, fg="white", font=("time new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
     c_bill_text = Entry(F1, width=15,textvariable=self.search_bill, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

     bill_btn=Button(F1,text="search",command=self.find_bill,width=10,bd=7,font="arial 12 bold ").grid(row=0,column=6,pady=10,padx=10)

#===================================================cost metics freem ========================================
     F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="costmetics ",font=("time new roman",15,"bold"),fg="gold",bg=bg_color)
     F2.place(x=5,y=180,width=325,height=380)

     bath_lbl=Label(F2, text="Bath Soap", font=("times new roman ", 16, "bold "), bg=bg_color, fg="lightgreen").grid(row=0,column=0,padx=10,pady=10, sticky="w")
     bath_txt=Entry(F2, width=10,textvariable=self.soap,font=("times new roman ", 16, "bold "),bd=5, relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

     Face_cream_lbl = Label(F2, text="Face cream", font=("times new roman ", 16, "bold "), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
     Face_cream_txt = Entry(F2, width=10,textvariable=self.face_cream, font=("times new roman ", 16, "bold "), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

     Face_w_lbl = Label(F2, text="Face wash", font=("times new roman ", 16, "bold "), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
     Face_w_txt = Entry(F2, width=10,textvariable=self.face_wash, font=("times new roman ", 16, "bold "), bd=5, relief=SUNKEN).grid(row=2, column=1,padx=10, pady=10)

     Hair_s_lbl = Label(F2, text="Hair spray", font=("times new roman ", 16, "bold "), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
     Hair_s_txt = Entry(F2, width=10, textvariable=self.spray,font=("times new roman ", 16, "bold "), bd=5, relief=SUNKEN).grid(row=3, column=1,padx=10, pady=10)

     Hair_g_lbl = Label(F2, text="Hair Gall ", font=("times new roman ", 16, "bold "), bg=bg_color,fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
     Hair_g_txt = Entry(F2, width=10,textvariable=self.gell, font=("times new roman ", 16, "bold "), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10,pady=10)

     Body_lbl = Label(F2, text="Body Loshan", font=("times new roman ", 16, "bold "), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
     Body_txt = Entry(F2, width=10,textvariable=self.loshon, font=("times new roman ", 16, "bold "), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10,pady=10)



#===================================================Gorocry  freem ========================================
     F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery  ",font=("time new roman",15,"bold"),fg="gold",bg=bg_color)
     F3.place(x=340,y=180,width=325,height=380)

     g1_lbl = Label(F3, text="Rice", font=("times new roman ", 16, "bold "), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
     g1_txt = Entry(F3, width=10,textvariable=self.rice ,font=("times new roman ", 16, "bold "), bd=5, relief=SUNKEN).grid(row=0, column=1,padx=10, pady=10)

     g2_lbl = Label(F3, text="Food oil", font=("times new roman ", 16, "bold "), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
     g2_txt = Entry(F3, width=10, textvariable=self.food_oil,font=("times new roman ", 16, "bold "), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

     g3_lbl = Label(F3, text="Daal", font=("times new roman ", 16, "bold "), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
     g3_txt = Entry(F3, width=10,textvariable=self.daal ,font=("times new roman ", 16, "bold "), bd=5, relief=SUNKEN).grid(row=2, column=1,padx=10, pady=10)

     g4_lbl = Label(F3, text="Wheat ", font=("times new roman ", 16, "bold "), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
     g4_txt = Entry(F3, width=10,textvariable=self.wheat ,font=("times new roman ", 16, "bold "), bd=5, relief=SUNKEN).grid(row=3, column=1,padx=10, pady=10)

     g5_lbl = Label(F3, text="Sugar", font=("times new roman ", 16, "bold "), bg=bg_color,fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
     g5_txt = Entry(F3, width=10,textvariable=self.sugar, font=("times new roman ", 16, "bold "), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10,pady=10)

     g6_lbl = Label(F3, text="Tea", font=("times new roman ", 16, "bold "), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
     g6_txt = Entry(F3, width=10, textvariable=self.tea,font=("times new roman ", 16, "bold "), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10,pady=10)

#===================================================COld drink freem ========================================
     F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold drink ",font=("time new roman",15,"bold"),fg="gold",bg=bg_color)
     F4.place(x=670,y=180,width=325,height=380)

     c1_lbl = Label(F4, text="Maza", font=("times new roman ", 16, "bold "), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
     c1_txt = Entry(F4, width=10, textvariable=self.maza,font=("times new roman ", 16, "bold "), bd=5, relief=SUNKEN).grid(row=0, column=1,padx=10, pady=10)

     c2_lbl = Label(F4, text="Cock", font=("times new roman ", 16, "bold "), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
     c2_txt = Entry(F4, width=10,textvariable=self.cock, font=("times new roman ", 16, "bold "), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

     c3_lbl = Label(F4, text="Frooti", font=("times new roman ", 16, "bold "), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
     c3_txt = Entry(F4, width=10,textvariable=self.frooti, font=("times new roman ", 16, "bold "), bd=5, relief=SUNKEN).grid(row=2, column=1,padx=10, pady=10)

     c4_lbl = Label(F4, text="Thumbs Up", font=("times new roman ", 16, "bold "), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
     c4_txt = Entry(F4, width=10,textvariable=self.thumbsup, font=("times new roman ", 16, "bold "), bd=5, relief=SUNKEN).grid(row=3, column=1,padx=10, pady=10)

     c5_lbl = Label(F4, text="Limca ", font=("times new roman ", 16, "bold "), bg=bg_color,fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
     c5_txt = Entry(F4, width=10,textvariable=self.limca, font=("times new roman ", 16, "bold "), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10,pady=10)

     c6_lbl = Label(F4, text="Sprite", font=("times new roman ", 16, "bold "), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
     c6_txt = Entry(F4, width=10, textvariable=self.sprite,font=("times new roman ", 16, "bold "), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10,pady=10)
#============================================ bill area ========================================
     F5=Frame(self.root,bd=10,relief=GROOVE)
     F5.place(x=1010,y=180,width=340,height=380)
     bill_tital=Label(F5,text="Bill Area",font="arial 15 bold ",bd=7,relief=GROOVE).pack(fill=X)
     scrol_y=Scrollbar(F5,orient=VERTICAL)
     self.textarea=Text(F5,yscrollcommand=scrol_y.set)
     scrol_y.pack(side=RIGHT,fill=Y)
     scrol_y.config(command= self.textarea.yview)
     self.textarea.pack(fill=BOTH,expand=1)


#========================================================button freem ===================
     F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Mane", font=("time new roman", 15, "bold"), fg="gold", bg=bg_color)
     F6.place(x=0, y=560, relwidth=1, height=140)

     m1=Label(F6,text="Total cosmetic price ", bg=bg_color,fg="white",font=("time  new roman ",14,"bold")).grid(row=0,column=0,pady=1,padx=20,sticky="w")
     m1_txt=Entry(F6,width=18,font="arial 10 bold",textvariable=self.cosmetic_price,bd=7,relief=SUNKEN).grid(row=0,column=1,pady=1,padx=10)

     m2= Label(F6, text="Total Grocery price ", bg=bg_color, fg="white", font=("time  new roman ", 14, "bold")).grid(row=1, column=0, pady=1, padx=20, sticky="w")
     m2_txt = Entry(F6, width=18,font="arial 10 bold",textvariable=self.grocery_price , bd=7, relief=SUNKEN).grid(row=1, column=1, pady=1, padx=10)

     m3= Label(F6, text="Total cold drinks price ", bg=bg_color, fg="white", font=("time  new roman ", 14, "bold")).grid(row=2, column=0, pady=1, padx=20, sticky="w")
     m3_txt = Entry(F6, width=18, font="arial 10 bold", textvariable=self.cold_drink_price,bd=7, relief=SUNKEN).grid(row=2, column=1, pady=1, padx=10)

     c1 = Label(F6, text=" cosmetic Tax ", bg=bg_color, fg="white", font=("time  new roman ", 14, "bold")).grid(row=0, column=2, pady=1, padx=20, sticky="w")
     c1_txt = Entry(F6, width=18, font="arial 10 bold", textvariable=self.cosmetic_tax,bd=7, relief=SUNKEN).grid(row=0, column=3, pady=1, padx=10)

     c2 = Label(F6, text=" Grocery Tax ", bg=bg_color, fg="white", font=("time  new roman ", 14, "bold")).grid(row=1, column=2, pady=1, padx=20, sticky="w")
     c2_txt = Entry(F6, width=18, font="arial 10 bold", textvariable=self.grocery_tax,bd=7, relief=SUNKEN).grid(row=1, column=3, pady=1, padx=10)

     c3 = Label(F6, text=" cold drinks Tax ", bg=bg_color, fg="white", font=("time  new roman ", 14, "bold")).grid(row=2, column=2, pady=1, padx=20, sticky="w")
     c3_txt = Entry(F6, width=18, font="arial 10 bold",textvariable=self.cold_drink_tax, bd=7, relief=SUNKEN).grid(row=2, column=3, pady=1, padx=10)

     btn_F=Frame(F6,bd=7,relief=GROOVE)
     btn_F.place(x=750,width=580,height=105)
     total_btu =Button(btn_F,command=self.total, text="Total", bg="blue", fg="white",bd=2, pady=15, width=10, font="arial 12 bold").grid(row=0,column=0,padx=5,pady=5)
     GBill_btu = Button(btn_F, text="Genrate Bill",command=self.bill_area, bg="blue", fg="white", bd=2, pady=15, width=10, font="arial 12 bold").grid(row=0, column=1, padx=5, pady=5)
     Clear_btu = Button(btn_F, text="Clear",command=self.clear_data, bg="blue", fg="white", bd=2, pady=15, width=10, font="arial 12 bold").grid(row=0, column=2, padx=5, pady=5)
     Exit_btu = Button(btn_F, text="Exit",command=self.Exit_app, bg="blue", fg="white", bd=2, pady=15, width=10, font="arial 12 bold").grid(row=0, column=3, padx=5, pady=5)
     self.welcome_bill()
    def total(self):
     self.c_s_p=self.soap.get()*40
     self.c_fc_p=self.face_cream.get() * 120
     self.c_fw_p=self.face_wash.get() * 60
     self.c_sh_p=self.spray.get() * 180
     self.c_hg_p=self.gell.get() * 140
     self.c_bl_p=self.loshon.get() * 180
     self.total_cosmetic_price=float(
                                 self.c_s_p+
                                 self.c_fc_p+
                                 self.c_fw_p+
                                 self.c_sh_p+
                                 self.c_hg_p+
                                 self.c_bl_p
                                )
     self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
     self.c_tax=round((self.total_cosmetic_price*0.05),2)
     self.cosmetic_tax.set("Rs. "+str(self.c_tax))

     self.g_r_p=self.rice.get()*40
     self.g_f_p=self.food_oil.get() * 180
     self.g_d_p=self.daal.get() * 60
     self.g_w_p=self.wheat.get() * 240
     self.g_s_p=self.sugar.get() * 45
     self.g_t_p = self.tea.get() * 150

     self.total_grocery_price=float(
                                      self.g_r_p+
                                      self.g_f_p +
                                      self.g_d_p +
                                      self.g_w_p +
                                      self.g_s_p+
                                      self.g_t_p

                                     )
     self.grocery_price.set("Rs. "+str(self.total_grocery_price))
     self.g_tax=round((self.total_grocery_price*0.1),2)
     self.grocery_tax.set("Rs. "+str(self.g_tax))

     self.d_m_p=self.maza.get() * 60
     self.d_c_p=self.cock.get() * 60
     self.d_f_p=self.frooti.get() * 50
     self.d_t_p =self.thumbsup.get() * 45
     self.d_l_p =self.limca.get() * 40
     self.d_s_p =self.sprite.get() * 60
     self.total_cold_drinks_price=float(
                                      self.d_m_p +
                                      self.d_c_p+
                                      self.d_f_p +
                                      self.d_t_p +
                                      self.d_l_p +
                                      self.d_s_p
                                    )
     self.cold_drink_price.set("Rs. "+str(self.total_cold_drinks_price))
     self.d_tax=round((self.total_cold_drinks_price*0.05),2)
     self.cold_drink_tax.set("Rs. "+str(self.d_tax))

     self.Total_bill=float(self.total_cosmetic_price+
                           self.total_grocery_price+
                           self.total_cold_drinks_price+
                           self.c_tax+
                           self.g_tax+
                           self.d_tax
                           )


    def welcome_bill(self):
        self.textarea.delete("1.0",END)
        self.textarea.insert(END,"\tWelCome WebCode Reatil \n")
        self.textarea.insert(END, f"\n Bill Number : {self.c_bill_no.get()}")
        self.textarea.insert(END, f"\n Customer Name :{self.c_name.get()}")
        self.textarea.insert(END, f"\n Phone Number : {self.c_phone.get()}")
        self.textarea.insert(END, f"\n=====================================")
        self.textarea.insert(END, f"\n Products\t\tQTY\t\tPrice")
        self.textarea.insert(END, f"\n=====================================")
    def bill_area(self):
     if self.c_name.get() == "" or self.c_phone.get() == "":
      messagebox.showerror("Error","Customer  details are must ")
     elif self.cosmetic_price.get()=="Rs.0.0" and self.grocery_price.get()=="Rs.0.0" and self.cold_drink_price.get()=="Rs.0.0" :
      messagebox.showerror("Error", "No product selected ")


     else:
      self.welcome_bill()
     #========Cosmetics==========
     if self.soap.get()!=0:
      self.textarea.insert(END,F"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
     if self.face_cream.get()!=0:
      self.textarea.insert(END,F"\n face cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
     if self.face_wash.get()!=0:
      self.textarea.insert(END,F"\n face wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
     if self.spray.get()!=0:
      self.textarea.insert(END,F"\n spray\t\t{self.spray.get()}\t\t{self.c_sh_p}")
     if self.gell.get() != 0:
       self.textarea.insert(END, F"\n gell\t\t{self.gell.get()}\t\t{self.c_hg_p}")
     if self.loshon.get() != 0:
       self.textarea.insert(END, F"\n loshan\t\t{self.loshon.get()}\t\t{self.c_bl_p}")
     #====================grocery===============================================

     if self.rice.get()!=0:
      self.textarea.insert(END,F"\n rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
     if self.food_oil.get()!=0:
      self.textarea.insert(END,F"\n food_oil\t\t{self.food_oil.get()}\t\t{self.g_f_p}")
     if self.daal.get()!=0:
      self.textarea.insert(END,F"\n dall\t\t{self.daal.get()}\t\t{self.g_d_p}")
     if self.wheat.get()!=0:
      self.textarea.insert(END,F"\n wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
     if self.sugar.get() != 0:
       self.textarea.insert(END, F"\n sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")
     if self.tea.get() != 0:
        self.textarea.insert(END, F"\n tea\t\t{self.tea.get()}\t\t{self.g_t_p}")

     #============================ cold drink=============================

     if self.maza.get()!=0:
      self.textarea.insert(END,F"\n maza\t\t{self.maza.get()}\t\t{self.d_m_p}")
     if self.cock.get()!=0:
      self.textarea.insert(END,F"\n cock\t\t{self.cock.get()}\t\t{self.d_c_p}")
     if self.frooti.get()!=0:
      self.textarea.insert(END,F"\n frooti\t\t{self.frooti.get()}\t\t{self.d_f_p}")
     if self.thumbsup.get()!=0:
      self.textarea.insert(END,F"\n thumbsu\t\t{self.thumbsup.get()}\t\t{self.d_t_p}")
     if self.limca.get() != 0:
       self.textarea.insert(END, F"\n limca\t\t{self.limca.get()}\t\t{self.d_l_p}")
     if self.sprite.get() != 0:
       self.textarea.insert(END, F"\n sprite\t\t{self.sprite.get()}\t\t{self.d_s_p}")

     self.textarea.insert(END, f"\n-------------------------------------")
     if self.cosmetic_tax.get()!="RS. 0.0":
      self.textarea.insert(END, f"\n Cosmetic Tax \t\t\t{self.cosmetic_tax.get()}")
     if self.grocery_tax.get()!="RS. 0.0":
      self.textarea.insert(END, f"\n grocery Tax \t\t\t{self.grocery_tax.get()}")
     if self.cold_drink_tax.get()!="RS. 0.0":
      self.textarea.insert(END, f"\n cold drink Tax \t\t\t{self.cold_drink_tax.get()}")

     self.textarea.insert(END, f"\n Total Bill:  \t\t\tRS. {str(self.Total_bill)}")
     self.textarea.insert(END, f"\n-------------------------------------")
     self.save_bill()

    def save_bill(self):
     op = messagebox.askyesno("Save the Bill", "Do you Want to Save the Bill ?")
     if op > 0:
      self.bill_data = self.textarea.get("1.0", END)
      f1 = open("bills" + str(self.c_bill_no.get()) + ".txt", "w")
      f1.write(self.bill_data)
      f1.close()
      messagebox.showinfo("save", f"Bill no.{self.c_bill_no.get} saved successfully")
     else:
      return

    def find_bill(self):
     present = "no"
     for i in os.listdir("bills/"):
      if i.split('.')[0] == self.search_bill.get():
       f1 = open(f"bills{i}", "r")
       self.textarea.delete("1.0", END)
       for d in f1:
        self.textarea.insert(END, d)
       f1.close()
       present = "yes"
     if present == "no":
      messagebox.showerror("Error", "Invalid Bill No .")

    def clear_data(self):
     op = messagebox.askyesno("clear ", "Do you really want to  Clear data  ?")
     if op > 0:
      # ============================================ costmetics=============================
      self.soap.set(0)
      self.face_cream.set(0)
      self.face_wash.set(0)
      self.spray.set(0)
      self.gell.set(0)
      self.loshon.set(0)
      # ===================================grocrey=================================
      self.rice.set(0)
      self.food_oil.set(0)
      self.daal.set(0)
      self.wheat.set(0)
      self.sugar.set(0)
      self.tea.set(0)
      # ============================================cold drinks==========================
      self.maza.set(0)
      self.cock.set(0)
      self.frooti.set(0)
      self.thumbsup.set(0)
      self.limca.set(0)
      self.sprite.set(0)
      # =======================Total Product price &Tax varabile==============================
      self.cosmetic_price.set("")
      self.grocery_price.set("")
      self.cold_drink_price.set("")
      self.cosmetic_tax.set("")
      self.grocery_tax.set("")
      self.cold_drink_tax.set("")

      # =============================customer========================================
      self.c_name.set("")
      self.c_phone.set("")
      self.c_bill_no.set("")
      x = random.randint(1000, 9999)
      self.c_bill_no.set(str(x))
      self.search_bill.set("")
      self.welcome_bill()


    def Exit_app(self):
     op = messagebox.askyesno("Exit ", "Do you really want to exit  ?")
     if op > 0:
      self.root.destroy()









root =Tk()
obj = bill_App(root)
root.mainloop()

