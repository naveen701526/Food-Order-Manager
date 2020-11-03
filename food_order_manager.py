from tkinter import *
from tkinter import messagebox
from db import Database

# create window object
app = Tk()
app.title('Food Manager')
app.geometry('800x400')

db = Database('store.db')


def populate_list():
    food_list.delete(0, END)
    for row in db.fetch():
        food_list.insert(END, row)


def add_item():
    if food_text.get() == '' or customer_text.get() == '' or quantity_text.get() == '' or bill_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(food_text.get(), customer_text.get(),
              quantity_text.get(), bill_text.get())
    food_list.delete(0, END)
    food_list.insert(END, (food_text.get(), customer_text.get(),
                            quantity_text.get(), bill_text.get()))
    clear_text()
    populate_list()


def select_item(event):
    try:
        global selected_item
        index = food_list.curselection()[0]
        selected_item = food_list.get(index)

        food_entry.delete(0, END)
        food_entry.insert(END, selected_item[1])
        customer_entry.delete(0, END)
        customer_entry.insert(END, selected_item[2])
        quantity_entry.delete(0, END)
        quantity_entry.insert(END, selected_item[3])
        bill_entry.delete(0, END)
        bill_entry.insert(END, selected_item[4])
    except IndexError:
        pass


def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()


def update_item():
    db.update(selected_item[0], food_text.get(), customer_text.get(),
              quantity_text.get(), bill_text.get())
    populate_list()


def clear_text():
    food_entry.delete(0, END)
    customer_entry.delete(0, END)
    quantity_entry.delete(0, END)
    bill_entry.delete(0, END)




# food
food_text = StringVar()
food_label = Label(app, text="Food Order Name", font=('bold', 14), pady=20)
food_label.grid(row=0, column=0, sticky=W)
food_entry = Entry(app, textvariable=food_text)
food_entry.grid(row=0, column=1)

# customer number
customer_text = StringVar()
customer_label = Label(app, text="Customer Number", font=('bold', 14))
customer_label.grid(row=0, column=2, sticky=W)
customer_entry = Entry(app, textvariable=customer_text)
customer_entry.grid(row=0, column=3)

#Quantity of food or total number of food items
quantity_text = StringVar()
quantity_label = Label(app, text="Number of Items", font=('bold', 14))
quantity_label.grid(row=1, column=0, sticky=W)
quantity_entry = Entry(app, textvariable=quantity_text)
quantity_entry.grid(row=1, column=1)

# Price paid by the customer for the items 
bill_text = StringVar()
bill_label = Label(app, text='Bill', font=('bold', 14))
bill_label.grid(row=1, column=2, sticky=W)
bill_entry = Entry(app, textvariable=bill_text)
bill_entry.grid(row=1, column=3)

# Food Items List (Listbox)
food_list = Listbox(app, height=8, width=50, border=0)
food_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

# Create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)
# Set scroll to listbox
food_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=food_list.yview)

# Bind select
food_list.bind('<<ListboxSelect>>', select_item)


# Buttons
add_btn = Button(app, text='Add Part', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text='Remove Part', width=12, command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text='Update Part', width=12, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text='Clear Input', width=12, command=clear_text)
clear_btn.grid(row=2, column=3)

# Populate data
populate_list()


# start program
app.mainloop()