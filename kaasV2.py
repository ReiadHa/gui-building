import tkinter as tk
import tkinter as ttk
from tkinter import *

def clear_frame():
   for widgets in frame.winfo_children():
      widgets.destroy()
def hoi():
    for i in VraagSet1: 
     print(i.get())





window = tk.Tk()
window.geometry('600x300')


vragenLijst = ['hoe ziet het kaas er uit?','wat voor kleur is de verpaking?','wat voor taal wordt gebruikt op de verpaking?']
list1 = ['heeft gaten' , 'geel Kaas' , 'bruin Kaas', 'iets groen op de kaas' ]
list2 = ['goren' , 'geel' , 'blauw' ]
list3 = ['engels' , 'Franse' , 'Nederlands' ]
list4 = [list1,list2,list3]

extra = 1
relX = 0.1
relY = 0.1  
LX = 0.05
LY = 0.03
index = 0
VraagSet1= []
for x in list4:
    vraag1 = tk.StringVar()
    label1 = tk.Label(text = f'{vragenLijst[index]}', bg='black',fg='white')
    label1.place(relx=LX, rely=LY, anchor='nw')
    index += 1
    LY += 0.2
    for i in x:
        radio1 = ttk.Radiobutton(window, text=i, value=i, variable=vraag1)
        radio1.place(relx=relX,rely=relY,anchor='nw')
        relX += 0.22
    VraagSet1.append(vraag1)

    extra = 0
    relX = 0.1
    relY += 0.2
    
checkBut = tk.Button(window, text='check', command=hoi)
checkBut.pack(side=BOTTOM)










frame = Frame(window)
# frame.pack(side="top", expand=True, fill="both")
window.mainloop()

# kaas = input('is de kaas geel? ')
# if kaas =='ja':
#     vraag1 = input('zit er gaten in? ')
#     if vraag1 =='ja':
#         vraag2 = input('is de kaas bruin? ')
#         if vraag2 =='ja': 
#             print('dan is het een alberthein kaas. ')
#     else: 
#         vraag3 = input('zit er groene plekken op de kaas? ')
    
#     if vraag3 == 'ja': print('dan is het een franse kaas ')

# else: 
#     vraag4= input('is de kaas wit? ') 
#     if vraag4 == 'ja':      
#         print('dan is het een lidl kaas ')
#     else : 
#         vraag5 = input('heeft de kaas een blaauwe verpaking? ')
#     if vraag5 == 'ja':
#         print('dan is het een jumbo kaas. ')