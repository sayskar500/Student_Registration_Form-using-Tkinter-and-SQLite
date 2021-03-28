from tkinter import *
import sqlite3
root = Tk()

root.geometry('710x500')
root.title("Registration Information")

label_1 = Label(root, text="REGISTRATION FORMAT",bg="#D3D3D3",fg="black", width=60,relief= "solid" ,borderwidth=2, font=("bold", 14)).place(x=20, y=20)

label_2 = Label(root,height=2, width=60,relief= "solid" ,borderwidth=2, font=("bold", 14)).place(x=20, y=42)

label_3 = Label(root,height=5, width=60,relief= "solid" ,borderwidth=2, font=("bold", 14)).place(x=20, y=84)

label_4 = Label(root, text="OWNER INFORMATION",bg="#D3D3D3",fg="black", width=60,relief= "solid" ,borderwidth=2, font=("bold", 14)).place(x=20, y=210)

label_5 = Label(root,height=2, width=60,relief= "solid" ,borderwidth=2, font=("bold", 14)).place(x=20, y=232)

label_6 = Label(root,height=2, width=60,relief= "solid" ,borderwidth=2, font=("bold", 14)).place(x=20, y=272)

label_7 = Label(root,height=2, width=60,relief= "solid" ,borderwidth=2, font=("bold", 14)).place(x=20, y=316)

label_8 = Label(root,height=2, width=60,relief= "solid" ,borderwidth=2, font=("bold", 14)).place(x=20, y=358)

label_9 = Label(root,height=2, width=60,relief= "solid" ,borderwidth=2, font=("bold", 14)).place(x=20, y=400)

label_0 = Label(root,height=2, width=60,relief= "solid" ,borderwidth=2, font=("bold", 14)).place(x=20, y=449)

label_10 = Label(root, text="ADDITIONAL INFORMATION",bg="#D3D3D3",fg="black", width=60,relief= "solid" ,borderwidth=2, font=("bold", 14)).place(x=20, y=516)

label_11 = Label(root,height=2, width=60,relief= "solid" ,borderwidth=2, font=("bold", 14)).place(x=20, y=538)

label_12 = Label(root,height=2, width=60,relief= "solid" ,borderwidth=2, font=("bold", 14)).place(x=20, y=580)

label_13 = Label(root,height=2, width=15,relief= "solid" ,borderwidth=2, font=("bold", 12)).place(x=397, y=232)

label_14 = Label(root,height=2, width=15,relief= "solid" ,borderwidth=2, font=("bold", 13)).place(x=397, y=273)

label_14 = Label(root,height=2, width=16,relief= "solid" ,borderwidth=2, font=("bold", 13)).place(x=536, y=315)

label_15 = Label(root,height=2, width=10,relief= "solid" ,borderwidth=2, font=("bold", 12)).place(x=356, y=358)

label_16 = Label(root,height=2, width=12,relief= "solid" ,borderwidth=2, font=("bold", 12)).place(x=572, y=358)

label_17 = Label(root,height=2, width=8,relief= "solid" ,borderwidth=2, font=("bold", 14)).place(x=356, y=400)

label_18 = Label(root,height=2, width=10,relief= "solid" ,borderwidth=2, font=("bold", 14)).place(x=571, y=400)

label_19 = Label(root,height=2, width=23,relief= "solid" ,borderwidth=2, font=("bold", 14)).place(x=428, y=449)

label_20 = Label(root,height=2, width=10,relief= "solid" ,borderwidth=2, font=("bold", 14)).place(x=571, y=400)

tab11 = Label(root, text="Registration Period:", width=16, font='Helvetica 8 bold').place(x=24, y=44)

tab12 =Label(root, text="(check one)", width=10, font=("bold", 8)).place(x=28, y=62)

C11 = Checkbutton(root, text = "One Year", width = 10).place(x=136, y=44) 

C12 = Checkbutton(root, text = "Two Years ($2 discount applies)", width = 25).place(x= 240, y=44) 

C13 = Checkbutton(root, text = "Three Years ($3 discount applies)", width = 25).place(x=460, y=44) 

tab13 =Label(root, text="(not available for vehicle subject to emission testing)", width=37, font=("bold", 7)).place(x=447, y=63)

tab21 = Label(root, text="Registration Type:", width=16, font='Helvetica 8 bold').place(x=24, y=86)

tab22 =Label(root, text="(check one)", width=16, font=("bold", 8)).place(x=24, y=102)

C21 = Checkbutton(root, text = "Original", width = 10).place(x=130, y=86) 

C22 = Checkbutton(root, text = "Renewal", width = 10).place(x=230, y=86) 

C23 = Checkbutton(root, text = "Private", width = 10).place(x=340, y=86) 

C24 = Checkbutton(root, text = "Reissue (Plates and Decals)", width = 20).place(x=440, y=86) 

tab23 =Label(root, text="see reissue Plates below under plate information", width=34, font=("bold", 7)).place(x=470, y=104)

C25 = Checkbutton(root, text = "Reissue (Decals Only)", width = 20).place(x=130, y=116) 

C26 = Checkbutton(root, text = "Rental Vehicle", width = 10).place(x=290, y=116) 

C27 = Checkbutton(root, text = "Transfer Lisence Plate Number", width = 22).place(x=400, y=116) 

entry_1 = Entry(root,text="Enter Plate Num",width = 15).place(x=582, y=120)

C29 = Checkbutton(root, text = "For Hire (complete 'For hire information' sector)", font=("bold",7) ,width = 35).place(x=24, y=140) 

C210 = Checkbutton(root, text = "Rideshareing (varpool)(cannot exceed 15 including driver)",font=("bold",8) , width =45).place(x=290, y=140) 

entry_2 = Entry(root,width = 5).place(x=590, y=144)

C211 = Checkbutton(root, text = "Amateur Radio Operator Call Letters - specify letters", font=("bold",8) ,width = 42).place(x=24, y=164) 

entry_3 = Entry(root,width = 10).place(x=300, y=166)

C212 = Checkbutton(root, text = "Others: specify", width = 10).place(x=380, y=164) 

entry_4 = Entry(root,width = 20).place(x=484, y=168)

label_221 = Label(root, text="Owners full name or Business name", width=30, font=("bold", 8)).place(x=24, y=234)

entry_221 = Entry(root,width=60).place(x=24, y=250)

label_222 = Label(root, text="Telephone number", width=14, font=("bold", 8)).place(x=402, y=234)

entry_222 = Entry(root).place(x=402, y=250)

label_223 = Label(root, text="DMV customer number", width=18, font=("bold", 8)).place(x=542, y=234)

entry_223 = Entry(root).place(x=542, y=250)

label_224 = Label(root, text="Co-Owners full name or Business name", width=31, font=("bold", 8)).place(x=24, y=274)

entry_224 = Entry(root,width=60).place(x=24, y=293)

label_225 = Label(root, text="Telephone number", width=14, font=("bold", 8)).place(x=402, y=275)

entry_225 = Entry(root).place(x=402, y=293)

label_226 = Label(root, text="DMV customer number", width=18, font=("bold", 8)).place(x=542, y=275)

entry_226 = Entry(root).place(x=542, y=293)

label_227 = Label(root, text="NOTE: Owners must provide their residence business address where requested ", width=65, font=("bold", 8)).place(x=24, y=318)

label_228 = Label(root, text="this address can not be a P.O box", width=27, font=("bold", 8)).place(x=24, y=338)

label_229 = Label(root, text="DMV customer number", width=18, font=("bold", 8)).place(x=542, y=318)

entry_229 = Entry(root).place(x=542, y=334)

label_2210 = Label(root, text="Owners RESIDENCE/HOME/BUSINESS Address", width=37, font=("bold", 8)).place(x=24, y=360)

entry_2210 = Entry(root,width=50).place(x=24, y=376)

label_2211 = Label(root, text=" CITY", width=8, font=("bold", 8)).place(x=372, y=360)

entry_2211 = Entry(root,width=12).place(x=362, y=376)

label_2212 = Label(root, text="STATE", width=10, font=("bold", 8)).place(x=476, y=360)

entry_2212 = Entry(root,width=17).place(x=459, y=376)

label_2213 = Label(root, text="ZIP CODE", width=10, font=("bold", 8)).place(x=596, y=360)

entry_2213 = Entry(root,width= 17).place(x=576, y=376)

label_2214 = Label(root, text="Co-owners RESIDENCE/HOME/BUSINESS Address", width=37, font=("bold", 8)).place(x=24, y=402)

entry_2214 = Entry(root,width=50).place(x=24, y=420)

label_2215 = Label(root, text=" CITY", width=8, font=("bold", 8)).place(x=372, y=402)

entry_2215 = Entry(root,width=12).place(x=362, y=420)

label_2216 = Label(root, text="STATE", width=10, font=("bold", 8)).place(x=476, y=402)

entry_2216 = Entry(root,width=17).place(x=459, y=420)

label_2217 = Label(root, text="ZIP CODE", width=10, font=("bold", 8)).place(x=596, y=402)

entry_2217 = Entry(root,width= 17).place(x=576, y=420)

label_2218 = Label(root, text="Owner Email Address", width=20, font=("bold", 8)).place(x=24, y=455)

entry_2218 = Entry(root,width=30).place(x=24, y=475)

label_2219 = Label(root, text="Owner Email Address", width=19, font=("bold", 8)).place(x=430, y=455)

entry_2219 = Entry(root,width=30).place(x=439, y=475)

label_31 = Label(root, text="Location where vehicle is principally garaged", width=36, font=("bold", 7)).place(x=24, y=542)

entry_32 = Entry(root,width=10 ).place(x=180, y=559)

label_33 = Label(root, text="If new location enter date changed", width=30, font=("bold", 7)).place(x=250, y=542)

entry_34 = Entry(root, ).place(x=274, y=559)

label_35 = Label(root, text="Are any of the owners on active military ", width=35, font=("bold", 7)).place(x=450, y=542)

label_351 = Label(root, text=" duty or service?", width=23, font=("bold", 7)).place(x=450, y=559)

C31 = Checkbutton(root, text = "CITY",font = ("bold",6), width = 5).place(x=22, y=555) 

C32 = Checkbutton(root, text = "COUNTRY",font = ("bold",6), width =8).place(x=65, y=555) 

C33 = Checkbutton(root, text = "TOWN",font = ("bold",6), width = 5).place(x=130, y=555) 

C34 = Checkbutton(root, text = "YES", font = ("bold",7), width = 5).place(x=559, y=555) 

C35 = Checkbutton(root, text = "NO", font = ("bold",7),width = 5).place(x=610, y=555) 

label_2214 = Label(root, text="Registration mailing address", width=22, font=("bold", 8)).place(x=24, y=582)

entry_2214 = Entry(root,width=25).place(x=24, y=600)

label_2215 = Label(root, text=" CITY", width=8, font=("bold", 8)).place(x=372, y=582)

entry_2215 = Entry(root,width=12).place(x=362, y=600)

label_2216 = Label(root, text="STATE", width=10, font=("bold", 8)).place(x=476, y=582)

entry_2216 = Entry(root,width=17).place(x=459, y=600)

label_2217 = Label(root, text="ZIP CODE", width=10, font=("bold", 8)).place(x=596, y=582)

entry_2217 = Entry(root,width= 17).place(x=576, y=600)

root.mainloop()