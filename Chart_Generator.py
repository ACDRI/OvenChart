from tkinter import *
from tkinter import filedialog
from over_temps import go_time
from under_temps import go_time2

wo_num = wo_num2 = wo_num3 = wo_num4 = wo_num5 = wo_num6 = wo_num7 = wo_num8 = wo_num9 = wo_num10 = [''] * 10
total_wo = [wo_num, wo_num2, wo_num3, wo_num4, wo_num5, wo_num6, wo_num7, wo_num8, wo_num9, wo_num10]
total_list = []

csv_num = ''
temp_check = ''


def retrieve_entries():
    global total_wo
    global total_list
    global total_entries
    if total_list != []:
        total_list = []
    for x in range(0, 10):
        container = total_entries[x].get()
        if container != '':
            total_list.append(container)
            total_wo_val[x].config(text='\u2713') 

def sel():
    global temp_check
    temp_check = str(selection.get())
    

def exit_now():
    root.destroy()

def submit_now():
    global total_list
    global csv_num
    global temp_check
    check_entries = len(total_list)
    if check_entries > 0 and csv_num != '' and temp_check  == '1':
        go_time(total_list, csv_num)
    elif check_entries > 0 and csv_num != '' and temp_check == '2':
        go_time2(total_list, csv_num)

def browsefunc():
    filename = filedialog.askopenfilename()
    global csv_num
    csv_num = filename.replace('C:/Users/Mike/Python/Personal Projects/Oven Chart Generator/', '')
    print(csv_num)
    pathlabel.config(text=csv_num)


root = Tk()
root.wm_title("Generate Chart")

browsebutton = Button(root, text="Browse for CSV", command=browsefunc)
pathlabel = Label(root)

wo_entry = Button(root, text="Enter WO#'s", command=retrieve_entries)

wo_val = Label(root)
wo_val2 = Label(root)
wo_val3 = Label(root)
wo_val4 = Label(root)
wo_val5 = Label(root)
wo_val6 = Label(root)
wo_val7 = Label(root)
wo_val8 = Label(root)
wo_val9 = Label(root)
wo_val10 = Label(root)

total_wo_val = [wo_val, wo_val2, wo_val3, wo_val4, wo_val5, wo_val6, wo_val7, wo_val8, wo_val9, wo_val10]

work_order = StringVar()
workorder2 = StringVar()
workorder3 = StringVar()
workorder4 = StringVar()
workorder5 = StringVar()
workorder6 = StringVar()
workorder7 = StringVar()
workorder8 = StringVar()
workorder9 = StringVar()
workorder10 = StringVar()
profile = StringVar()
selection = IntVar()

over = Radiobutton(root, text="OVER 500 Degrees", variable=selection, value=1, command=sel)
under = Radiobutton(root, text="LESS THAN 500 Degrees", variable=selection, value=2, command=sel)

ent = Entry(root,textvariable=work_order)
ent2 = Entry(root, textvariable=workorder2)
ent3 = Entry(root, textvariable=workorder3)
ent4 = Entry(root, textvariable=workorder4)
ent5 = Entry(root, textvariable=workorder5)
ent6 = Entry(root, textvariable=workorder6)
ent7 = Entry(root, textvariable=workorder7)
ent8 = Entry(root, textvariable=workorder8)
ent9 = Entry(root, textvariable=workorder9)
ent10 = Entry(root, textvariable=workorder10)

total_entries = [ent, ent2, ent3, ent4, ent5, ent6, ent7, ent8, ent9, ent10]


lab = Label(root, text="WO #1:")
lab_2 = Label(root, text="WO #2:")
lab_3 = Label(root, text="WO #3:")
lab_4 = Label(root, text="WO #4:")
lab_5 = Label(root, text="WO #5:")
lab_6 = Label(root, text="WO #6:")
lab_7 = Label(root, text="WO #7:")
lab_8 = Label(root, text="WO #8:")
lab_9 = Label(root, text="WO #9:")
lab_10 = Label(root, text="WO #10:")


prof = Label(root, text="Profile Type : ")
file_sel = Label(root, text="File Selected : ")

reset = Button(root, text="Exit", command=exit_now)
submit = Button(root, text="Submit", command=submit_now)

lab.grid(row=0,column=0)
lab_2.grid(row=1, column=0)
lab_3.grid(row=2, column=0)
lab_4.grid(row=3, column=0)
lab_5.grid(row=4, column=0)
lab_6.grid(row=5, column=0)
lab_7.grid(row=6, column=0)
lab_8.grid(row=7, column=0)
lab_9.grid(row=8, column=0)
lab_10.grid(row=9, column=0)

ent.grid(row=0,column=1)
ent2.grid(row=1, column=1)
ent3.grid(row=2, column=1)
ent4.grid(row=3, column=1)
ent5.grid(row=4, column=1)
ent6.grid(row=5, column=1)
ent7.grid(row=6, column=1)
ent8.grid(row=7, column=1)
ent9.grid(row=8, column=1)
ent10.grid(row=9, column=1)

wo_val.grid(row=0,column=2)
wo_val2.grid(row=1, column=2)
wo_val3.grid(row=2, column=2)
wo_val4.grid(row=3, column=2)
wo_val5.grid(row=4, column=2)
wo_val6.grid(row=5, column=2)
wo_val7.grid(row=6, column=2)
wo_val8.grid(row=7, column=2)
wo_val9.grid(row=8, column=2)
wo_val10.grid(row=9, column=2)


prof.grid(row=11,column=0)
over.grid(row=11, column=2)
under.grid(row=11, column=1)
browsebutton.grid(row=12,column=0)
file_sel.grid(row=13,column=0)
pathlabel.grid(row=13,column=1)
reset.grid(row=16,column=3)
submit.grid(row=15,column=3)
wo_entry.grid(row=10, column=0)





root.mainloop()


