from tkinter import *
import sqlite3

root = Tk()
root.title('Address Book')
root.geometry('295x500')
root.iconbitmap('images/icons/groot.ico')
# Databases

# Create or connect to a database
conn = sqlite3.connect('address_book.db')

# Create a cursor
c = conn.cursor()

# Create a table
'''
c.execute("""CREATE TABLE addresses(
   first_name text,
   last_name text,
   address text,
   city text, 
   state text,
   zipcode integer )""")
'''

def save():
    # Create or connect to a database
    conn = sqlite3.connect('address_book.db')
    # Create a cursor
    c = conn.cursor()

    record_id = edit_box.get()
    c.execute("""UPDATE addresses SET
              first_name = :first,
              last_name = :last,
              address = :address,
              city = :city,
              state = :state,
              zipcode = :zipcode
              
              WHERE oid = :oid""",
              {
                  'first': f_name_editor.get(),
                  'last': l_name_editor.get(),
                  'address': address_editor.get(),
                  'city': city_editor.get(),
                  'state': state_editor.get(),
                  'zipcode': zipcode_editor.get(),

                  'oid': record_id
              })

    # Commit to changes in database
    conn.commit()
    # Close connection
    conn.close()

    editor.destroy()
# Create edit function
def edit():
    global editor
    editor = Tk()
    editor.title('Update A Record')
    editor.geometry('295x210')
    editor.iconbitmap('images/icons/groot.ico')

    # Create or connect to a database
    conn = sqlite3.connect('address_book.db')
    # Create a cursor
    c = conn.cursor()

    record_id = edit_box.get()
    c.execute("SELECT * FROM addresses WHERE oid =" + record_id)
    records = c.fetchall()
    # The for loop from here is below all these boxes and labels
    # Create global boxes to be used in other functions
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor
    # Create Text Boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)
    # Create Labels
    f_name_label = Label(editor, text='First Name')
    f_name_label.grid(row=0, column=0, pady=(10, 0))
    l_name_label = Label(editor, text='Last Name')
    l_name_label.grid(row=1, column=0)
    address_label = Label(editor, text='Address')
    address_label.grid(row=2, column=0)
    city_label = Label(editor, text='City')
    city_label.grid(row=3, column=0)
    state_label = Label(editor, text='State')
    state_label.grid(row=4, column=0)
    zipcode_label = Label(editor, text='Zipcode')
    zipcode_label.grid(row=5, column=0)

    # Loop through records to fill resp boxes
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    # Create save button to save record
    save_btn = Button(editor, text='Save Record', command=save)
    save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=87)
    # To clear edit box
    edit_box.delete(0, END)
# To delete a record
def delete():
    # Create or connect to a database
    conn = sqlite3.connect('address_book.db')
    # Create a cursor
    c = conn.cursor()

    # Delete record
    c.execute("DELETE from addresses WHERE oid = " + edit_box.get())

    # Commit to changes in database
    conn.commit()
    # Close connection
    conn.close()

    edit_box.delete(0, END)

# Create Submit Function
def submit():
    # Create or connect to a database
    conn = sqlite3.connect('address_book.db')
    # Create a cursor
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              })

    # Commit to changes in database
    conn.commit()
    # Close connection
    conn.close()

    # Clear text in the boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

def query():
    # Create or connect to a database
    conn = sqlite3.connect('address_book.db')
    # Create a cursor
    c = conn.cursor()
    # oid is a unique number for each record
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    #print(records)
    index_label = Label(root,font=('arial', 10, 'bold'), text='  Name             ID')
    index_label.grid(row=12, column=0, columnspan=2)
    # Loop through records
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=13, column=0, columnspan=2)

    # Commit to changes in database
    conn.commit()
    # Close connection
    conn.close()

# Create Text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10,0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)
edit_box = Entry(root, width=30)
edit_box.grid(row=9, column=1, pady=5)

# Create Labels
f_name_label = Label(root, text='First Name')
f_name_label.grid(row=0, column=0, pady=(10,0))
l_name_label = Label(root, text='Last Name')
l_name_label.grid(row=1, column=0)
address_label = Label(root, text='Address')
address_label.grid(row=2, column=0)
city_label = Label(root, text='City')
city_label.grid(row=3, column=0)
state_label = Label(root, text='State')
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text='Zipcode')
zipcode_label.grid(row=5, column=0)
delete_box_label = Label(root, text='Select ID')
delete_box_label.grid(row=9, column=0, pady=5)

# Create Submit Button
submit_btn = Button(root, text='Submit', command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=101)
# Create Query Button
query_btn = Button(root, text='Show Records', command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=83)
# Create Delete Button
delete_btn = Button(root, text='Delete Records', command=delete)
delete_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=80)
# Create Edit Button
edit_btn = Button(root, text='Edit Records', command=edit)
edit_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=86)
# Commit to changes in database
conn.commit()

# Close connection
conn.close()

root.mainloop()