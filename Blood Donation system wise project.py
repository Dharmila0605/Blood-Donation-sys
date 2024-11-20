import sqlite3
from tkinter import *
from tkinter import messagebox, ttk
import tkinter as tk
from PIL import Image, ImageTk


class Home:
    def __init__(self, root):
        self.root = root
        self.root.title("DONATE BLOOD SAVE LIFE")

        self.conn = sqlite3.connect('blooddonate.db')
        self.cursor = self.conn.cursor()

        # Create tables if they don't exist
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS donors (
                                id INTEGER PRIMARY KEY,
                                name TEXT not null,
                                age INTEGER not null,
                                blood_group TEXT not null,
                                gender TEXT not null,
                                phone_number TEXT unique,
                                address TEXT not null,
                                diabetic TEXT not null,
                                alcoholic TEXT not null,
                                time_availability TEXT not null
                            )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS receivers (
                                id INTEGER PRIMARY KEY,
                                name TEXT not null,
                                age INTEGER,
                                blood_group TEXT not null,
                                address TEXT not null,
                                phone_number TEXT unique,
                                emergency TEXT
                            )''')

        self.conn.commit()
        self.bg_img = Image.open('c:\\Users\\thiru\\OneDrive\\Pictures\\BDbg.png.jpg')

        self.bg_img = self.bg_img.resize((700,700))
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.bg_lbl = Label(root, image=self.bg_img)
        self.bg_lbl.place(x=0, y=0)

        self.home_title = Label(root, text="WELCOME TO BLOOD DONATION SYSTEM", font=('Times New Roman', 25, 'bold'))
        self.home_title.pack(fill='x')

        self.donor_btn = Button(root, text='donate', font=('Courier New', 15, 'bold'), command=self.donor_page)
        self.donor_btn.place(x=50, y=230)

        self.recieve_btn = Button(root, text='receive', font=('Courier New', 15, 'bold'), command=self.recieve_page)
        self.recieve_btn.place(x=550, y=230)

    def donor_page(self):
        self.home_title.destroy()
        self.donor_btn.destroy()
        self.recieve_btn.destroy()

        root = self.root
        self.donor_page_title = Label(root, text='DONOR DETAILS', font=('Arial Narrow', 25, 'bold'))
        self.donor_page_title.pack(fill='x')

        self.donor_name = Label(root, text="ENTER YOUR NAME: ", font=('Courier New', 15, 'bold'))
        self.donor_name.place(x=50, y=150)
        self.name_entry = Entry(root, font=('Courier New', 15, 'bold'))
        self.name_entry.place(x=250, y=150)

        self.donor_age = Label(root, text="ENTER YOUR AGE: ", font=('Courier New', 15, 'bold'))
        self.donor_age.place(x=50, y=180)
        self.age_entry = Entry(root, font=('Courier New', 15, 'bold'))
        self.age_entry.place(x=250, y=180)

        self.donor_bgroup = Label(root, text="BLOODGROUP: ", font=('Courier New', 15, 'bold'))
        self.donor_bgroup.place(x=50, y=210)
        self.bgroup_entry = Entry(root, font=('Courier New', 15, 'bold'))
        self.bgroup_entry.place(x=250, y=210)

        self.donor_gender = Label(root, text="GENDER: ", font=('Courier New', 15, 'bold'))
        self.donor_gender.place(x=50, y=240)
        self.gender_entry = Entry(root, font=('Courier New', 15, 'bold'))
        self.gender_entry.place(x=250, y=240)

        self.donor_phonenum = Label(root, text="PHONE NUMBER: ", font=('Courier New', 15, 'bold'))
        self.donor_phonenum.place(x=50, y=270)
        self.phonenum_entry = Entry(root, font=('Courier New', 15, 'bold'))
        self.phonenum_entry.place(x=250, y=270)

        self.donor_address = Label(root, text="ADDRESS: ", font=('Courier New', 15, 'bold'))
        self.donor_address.place(x=50, y=300)
        self.address_entry = Entry(root, font=('Courier New', 15, 'bold'))
        self.address_entry.place(x=250, y=300)

        self.donor_diabetic = Label(root, text="DIABETIC(YES/NO):", font=('Courier New', 15, 'bold'))
        self.donor_diabetic.place(x=50, y=330)
        self.diabetic_entry = Entry(root, font=('Courier New', 15, 'bold'))
        self.diabetic_entry.place(x=260, y=330)

        self.donor_alcoholic = Label(root, text="ALCOHOLIC(YES/NO):", font=('Courier New', 15, 'bold'))
        self.donor_alcoholic.place(x=50, y=360)
        self.alcoholic_entry = Entry(root, font=('Courier New', 15, 'bold'))
        self.alcoholic_entry.place(x=260, y=360)

        self.donor_avail = Label(root, text="TIME AVAILABILITY:", font=('Courier New', 15, 'bold'))
        self.donor_avail.place(x=50, y=390)
        self.avail_entry = Entry(root, font=('Courier New', 15, 'bold'), width='18')
        self.avail_entry.place(x=260, y=390)

        self.submit_btn = Button(root, text='SUBMIT', font=('Courier New', 15, 'bold'), bd=4, command=self.login_donor)
        self.submit_btn.place(x=350, y=420)

        self.bck_btn = Button(root, text='BACK', font=('Courier New', 15, 'bold'), bd=4, width=6,
                              command=self.back_to_home_donor)
        self.bck_btn.place(x=40, y=420)

    def recieve_page(self):
        self.home_title.destroy()
        self.donor_btn.destroy()
        self.recieve_btn.destroy()

        root = self.root
        self.recieve_page_title = Label(root, text='RECEIVER DETAILS', font=('Arial Narrow', 25, 'bold'))
        self.recieve_page_title.pack(fill='x')

        self.recieve_name = Label(root, text="ENTER YOUR NAME: ", font=('Courier New', 15, 'bold'))
        self.recieve_name.place(x=50, y=150)
        self.name_entry = Entry(root, font=('Courier New', 15, 'bold'))
        self.name_entry.place(x=250, y=150)

        self.recieve_age = Label(root, text="ENTER YOUR AGE: ", font=('Courier New', 15, 'bold'))
        self.recieve_age.place(x=50, y=180)
        self.age_entry = Entry(root, font=('Courier New', 15, 'bold'))
        self.age_entry.place(x=250, y=180)

        self.recieve_bgroup = Label(root, text="BLOODGROUP: ", font=('Courier New', 15, 'bold'))
        self.recieve_bgroup.place(x=50, y=210)
        self.bgroup_entry = Entry(root, font=('Courier New', 15, 'bold'))
        self.bgroup_entry.place(x=250, y=210)

        self.recieve_address = Label(root, text="ADDRESS: ", font=('Courier New', 15, 'bold'))
        self.recieve_address.place(x=50, y=240)
        self.address_entry = Entry(root, font=('Courier New', 15, 'bold'))
        self.address_entry.place(x=250, y=240)

        self.recieve_num = Label(root, text="PHONE NUMBER:", font=('Courier New', 15, 'bold'))
        self.recieve_num.place(x=50, y=270)
        self.num_entry = Entry(root, font=('Courier New', 15, 'bold'))
        self.num_entry.place(x=250, y=270)

        self.recieve_emer = Label(root, text="EMERGENCY(Yes/No):", font=('Courier New', 15, 'bold'))
        self.recieve_emer.place(x=50, y=300)
        self.emer_entry = Entry(root, font=('Courier New', 15, 'bold'))
        self.emer_entry.place(x=255, y=300)

        self.submit_btn = Button(root, text='SUBMIT', font=('Courier New', 15, 'bold'), bd=4,
                                 command=self.login_reciever)
        self.submit_btn.place(x=350, y=330)

        self.bck_btn = Button(root, text='BACK', font=('Courier New', 15, 'bold'), bd=4, width=6,
                              command=self.back_to_home_recieve)
        self.bck_btn.place(x=40, y=330)

    def login_donor(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        blood_group = self.bgroup_entry.get()
        gender = self.gender_entry.get()
        phone_number = self.phonenum_entry.get()
        address = self.address_entry.get()
        diabetic = self.diabetic_entry.get()
        alcoholic = self.alcoholic_entry.get()
        time_availability = self.avail_entry.get()

        if not name.isalpha():
            messagebox.showerror("Error", "Enter correct name")
        elif not age.isdigit() or not (18 <= int(age) <= 65):
            messagebox.showerror("Error", "Age should be between 18 and 65")
        elif not phone_number.isdigit() or len(phone_number) != 10:
            messagebox.showerror("Error", "Phone number should be 10 digits")
        else:
            self.cursor.execute('''INSERT INTO donors 
                                (name, age, blood_group, gender, phone_number, address, diabetic, alcoholic, time_availability) 
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                                (name, age, blood_group, gender, phone_number, address, diabetic, alcoholic,
                                 time_availability))

            self.conn.commit()

            messagebox.showinfo('Success', 'Donor details submitted successfully!')

            print("DONOR DETAILS STORED IN DATABASE")
            for row in self.cursor.execute("SELECT * FROM donors"):
                print(row)

    def login_reciever(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        blood_group = self.bgroup_entry.get()
        address = self.address_entry.get()
        phone_number = self.num_entry.get()
        emergency = self.emer_entry.get()

        if not name.isalpha():
            messagebox.showerror("Error", "Enter correct name")
        elif not age.isdigit() or not (18 <= int(age) <= 65):
            messagebox.showerror("Error", "Age should be between 18 and 65 to donate blood")
        elif not phone_number.isdigit() or len(phone_number) != 10:
            messagebox.showerror("Error", "Phone number must be 10 digits")
        else:
            messagebox.showinfo('Success', 'Submitted details')

            matched_donors = self.cursor.execute("SELECT * FROM donors WHERE blood_group=?", (blood_group,)).fetchall()
            if matched_donors:
                self.display_matched_donors(matched_donors)
            else:
                messagebox.showinfo("No Match", "No matching donors found.")

            self.cursor.execute('''INSERT INTO receivers 
                                (name, age, blood_group, address, phone_number, emergency) 
                                VALUES (?, ?, ?, ?, ?, ?)''',
                                (name, age, blood_group, address, phone_number, emergency))

            self.conn.commit()

            print('RECEIVER DETAILS STORED IN DATABASE')
            for row in self.cursor.execute("SELECT * FROM receivers"):
                print(row)

    def display_matched_donors(self, matched_donors):
        top = Toplevel()
        top.title("Matched Donors")

        tree = ttk.Treeview(top, columns=("Name", "Age", "Blood Group", "Gender", "Phone Number", "Address", "Diabetic", "Alcoholic", "Time Availability"))
        tree.heading("#0", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Age", text="Age")
        tree.heading("Blood Group", text="Blood Group")
        tree.heading("Gender", text="Gender")
        tree.heading("Phone Number", text="Phone Number")
        tree.heading("Address", text="Address")
        tree.heading("Diabetic", text="Diabetic")
        tree.heading("Alcoholic", text="Alcoholic")
        tree.heading("Time Availability", text="Time Availability")

        for donor in matched_donors:
            tree.insert("", "end", text=donor[0], values=(donor[1], donor[2], donor[3], donor[4], donor[5], donor[6], donor[7], donor[8], donor[9]))

        tree.pack()

    def back_to_home_donor(self):
        self.donor_page_title.destroy()
        self.donor_name.destroy()
        self.name_entry.destroy()
        self.donor_age.destroy()
        self.age_entry.destroy()
        self.donor_gender.destroy()
        self.gender_entry.destroy()
        self.donor_bgroup.destroy()
        self.bgroup_entry.destroy()
        self.donor_phonenum.destroy()
        self.phonenum_entry.destroy()
        self.donor_address.destroy()
        self.address_entry.destroy()
        self.donor_diabetic.destroy()
        self.diabetic_entry.destroy()
        self.donor_alcoholic.destroy()
        self.alcoholic_entry.destroy()
        self.submit_btn.destroy()
        self.bck_btn.destroy()
        home = Home(root)

    def back_to_home_recieve(self):
        self.recieve_page_title.destroy()
        self.recieve_name.destroy()
        self.name_entry.destroy()
        self.recieve_age.destroy()
        self.age_entry.destroy()
        self.recieve_bgroup.destroy()
        self.bgroup_entry.destroy()
        self.recieve_num.destroy()
        self.num_entry.destroy()
        self.recieve_emer.destroy()
        self.emer_entry.destroy()
        self.submit_btn.destroy()
        self.bck_btn.destroy()
        home = Home(root)


root = Tk()
home = Home(root)
root.geometry('700x500+550+150')
root.mainloop()