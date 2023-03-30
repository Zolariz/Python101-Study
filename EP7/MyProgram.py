import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from EP7 import Customer_List


# สร้างคลาสหลักโดยใช้ tk.Tk และสร้าง ttk.Notebook

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My Application")
        self.geometry("900x600")

        self.style = ttk.Style()
        self.style.theme_use('litera')

        # create a notebook
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True)

        # add tabs to notebook
        self.tab1 = Tab1(self.notebook)
        self.notebook.add(self.tab1, text="Customer Management")

        self.tab2 = Tab2(self.notebook)
        self.notebook.add(self.tab2, text="Nutrition Adjustment")


class Tab1(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.title1_frame = tk.Frame(self, padx=10, pady=15)
        self.title1_frame.pack()
        tk.Label(self.title1_frame, text="Customer Management", font=('Arial', 35, 'bold')).grid(row=0, column=0)
        self.db1 = Customer_List.Database()

        # create a label and entry widget to search for a customer
        self.search_frame = tk.Frame(self, padx=10, pady=5)
        self.search_frame.pack()
        tk.Label(self.search_frame, text="Search Customer: ").grid(row=0, column=0)
        self.search_entry = tk.Entry(self.search_frame, width=30)
        self.search_entry.grid(row=0, column=1, padx=10, pady=15, ipady=5)
        self.search_button = ttk.Button(self.search_frame, text="Search", command=self.search, width=15)
        self.search_button.grid(row=0, column=2, padx=10, pady=15)
        self.clear_button = ttk.Button(self.search_frame, text="Clear", command=self.clear_search, width=15)
        self.clear_button.grid(row=0, column=3, padx=10, pady=15)

        # Create treeview to display customers
        tree_frame = tk.Frame(self, padx=10, pady=5)
        tree_frame.pack()
        self.tree = ttk.Treeview(tree_frame, columns=("id", "name", "email", "age", "address"), show="headings")
        self.tree.heading("id", text="ID", anchor="center")
        self.tree.heading("name", text="Name")
        self.tree.heading("email", text="Email")
        self.tree.heading("age", text="Age", anchor="center")
        self.tree.heading("address", text="Address")
        self.tree.column("id", width=50, anchor="center")
        self.tree.column("name", width=200)
        self.tree.column("email", width=200)
        self.tree.column("age", width=50, anchor="center")
        self.tree.column("address", width=300)
        self.tree.pack()
        self.view_records()

        # Add buttons to modify selected record
        btn_frame = tk.Frame(self, padx=10, pady=5)
        btn_frame.pack()
        tk.Button(btn_frame, text="Add", command=self.add_record, width=15).grid(row=0, column=0, padx=10, ipady=10)
        tk.Button(btn_frame, text="Edit", command=self.edit_record, width=15).grid(row=0, column=1, padx=10, ipady=10)
        tk.Button(btn_frame, text="Delete", command=self.delete_record, width=15).grid(row=0, column=2, padx=10,
                                                                                       ipady=10)

    def search(self):
        keyword = self.search_entry.get()
        rows = self.db1.search(keyword)
        self.display_records(rows)

    def clear_search(self):
        self.search_entry.delete(0, 'end')
        self.view_records()

    def display_records(self, rows):
        # Clear existing records from the treeview
        for record in self.tree.get_children():
            self.tree.delete(record)

        # Insert new records into the treeview
        for row in rows:
            self.tree.insert("", "end", values=row)

    def add_record(self):
        add_window = tk.Toplevel(self)
        add_window.title("Add Record")
        add_window.geometry("400x250")
        add_window.resizable(False, False)

        self.name_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.address_var = tk.StringVar()

        # Clear input fields
        self.name_var.set("")
        self.email_var.set("")
        self.age_var.set("")
        self.address_var.set("")

        name = self.name_var.get()
        email = self.email_var.get()
        age = self.age_var.get()
        address = self.address_var.get()

        # Create a form for adding a new record
        form_frame1 = tk.Frame(add_window, padx=10, pady=10)
        form_frame1.pack(fill="both", expand=True)

        # Add form fields for each attribute of the record
        id_label = tk.Label(form_frame1, text="ID:")
        id_label.grid(row=0, column=0, sticky="w")
        id_entry = tk.Entry(form_frame1, width=30)
        id_entry.grid(row=0, column=1)

        name_label = tk.Label(form_frame1, text="Name:")
        name_label.grid(row=1, column=0, sticky="w")
        name_entry = tk.Entry(form_frame1, width=30, textvariable=self.name_var)
        name_entry.grid(row=1, column=1)

        email_label = tk.Label(form_frame1, text="Email:")
        email_label.grid(row=2, column=0, sticky="w")
        email_entry = tk.Entry(form_frame1, width=30, textvariable=self.email_var)
        email_entry.grid(row=2, column=1)

        age_label = tk.Label(form_frame1, text="Age:")
        age_label.grid(row=3, column=0, sticky="w")
        age_entry = tk.Entry(form_frame1, width=30, textvariable=self.age_var)
        age_entry.grid(row=3, column=1)

        address_label = tk.Label(form_frame1, text="Address:")
        address_label.grid(row=4, column=0, sticky="w")
        address_entry = tk.Entry(form_frame1, width=30, textvariable=self.address_var)
        address_entry.grid(row=4, column=1)

        # Add a button to save the new record
        save_button = tk.Button(form_frame1, text="Save",
                                command=lambda: self.save_record1(add_window, id_entry.get(), name_entry.get(),
                                                                  email_entry.get(), age_entry.get(),
                                                                  address_entry.get()))
        save_button.grid(row=5, column=1, pady=10)

        # Insert new record into database and update view
        self.db1.insert(name, email, age, address)
        self.view_records()

    def save_record1(self, add_window, record_id, name, email, age, address):
        self.db1.update(record_id, name, email, age, address)
        add_window.destroy()
        self.view_records()

    def view_records(self):
        # Clear previous data
        self.tree.delete(*self.tree.get_children())

        # Fetch new data from database
        rows = self.db1.fetch()

        # Insert fetched data to treeview
        for row in rows:
            self.tree.insert("", "end", values=row)

    def edit_record(self):
        # Get selected record
        selected = self.tree.focus()
        if selected:
            values = self.tree.item(selected, "values")
            id, name, email, age, address = values

            # Create a new window for editing the record
            edit_window = tk.Toplevel(self)
            edit_window.title("Edit Record")
            edit_window.geometry("400x250")
            edit_window.resizable(False, False)

            # Create a form for editing the record
            form_frame = tk.Frame(edit_window, padx=10, pady=10)
            form_frame.pack(fill="both", expand=True)

            # Add form fields for each attribute of the record
            id_label = tk.Label(form_frame, text="ID:")
            id_label.grid(row=0, column=0, sticky="w")
            id_entry = tk.Entry(form_frame, width=30)
            id_entry.insert(0, id)
            id_entry.grid(row=0, column=1)

            name_label = tk.Label(form_frame, text="Name:")
            name_label.grid(row=1, column=0, sticky="w")
            name_entry = tk.Entry(form_frame, width=30)
            name_entry.insert(0, name)
            name_entry.grid(row=1, column=1)

            email_label = tk.Label(form_frame, text="Email:")
            email_label.grid(row=2, column=0, sticky="w")
            email_entry = tk.Entry(form_frame, width=30)
            email_entry.insert(0, email)
            email_entry.grid(row=2, column=1)

            age_label = tk.Label(form_frame, text="Age:")
            age_label.grid(row=3, column=0, sticky="w")
            age_entry = tk.Entry(form_frame, width=30)
            age_entry.insert(0, age)
            age_entry.grid(row=3, column=1)

            address_label = tk.Label(form_frame, text="Address:")
            address_label.grid(row=4, column=0, sticky="w")
            address_entry = tk.Entry(form_frame, width=30)
            address_entry.insert(0, address)
            address_entry.grid(row=4, column=1)

            # Add a button to save the edited record
            save_button = tk.Button(form_frame, text="Save",
                                    command=lambda: self.save_record2(edit_window, id_entry.get(), name_entry.get(),
                                                                      email_entry.get(), age_entry.get(),
                                                                      address_entry.get()))
            save_button.grid(row=5, column=1, pady=10)

        else:
            messagebox.showerror("Error", "Please select a record to edit.")

    def save_record2(self, edit_window, selected_id, name, email, age, address):
        self.db1.update(selected_id, name, email, age, address)
        edit_window.destroy()
        self.view_records()

    def delete_record(self):
        # Get selected record
        selected = self.tree.focus()
        if selected:
            values = self.tree.item(selected, "values")
            id = values[0]

            # Confirm deletion
            confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this record?")
            if confirm:
                self.db1.remove(id)
                self.view_records()


class Tab2(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.bmr_entry = None
        title_frame = tk.Frame(self, padx=10, pady=5)
        title_frame.pack()
        tk.Label(title_frame, text="Nutrition Adjustment", font=('Arial', 35, 'bold')).grid(row=0, column=0)

        input_frame = tk.Frame(self, padx=10, pady=5)
        input_frame.pack()
        weight_label = ttk.Label(input_frame, text="Weight (kg): ")
        weight_label.grid(row=0, column=0)

        self.weight_entry = ttk.Entry(input_frame)
        self.weight_entry.grid(row=0, column=1)

        fat_label = ttk.Label(input_frame, text="% Body Fat: ")
        fat_label.grid(row=1, column=0)

        self.fat_entry1 = ttk.Entry(input_frame)
        self.fat_entry1.grid(row=1, column=1)

        # create Menubutton with options for activity level
        activity_frame = tk.Frame(self, padx=10, pady=5)
        activity_frame.pack()
        activity_label = ttk.Label(activity_frame, text="Activity Level:")
        activity_label.grid(row=0, column=0)

        self.activity_level = tk.StringVar()  # variable to store selected option
        activity_options = ['sedentary', 'lightly active', 'moderately active', 'very active', 'extra active']
        self.activity_level.set(activity_options[0])  # set default value

        activity_menu = tk.OptionMenu(activity_frame, self.activity_level, *activity_options)
        activity_menu.config(width=20)
        activity_menu.grid(row=0, column=1)

        # call display_bmr() when submit button is pressed
        cal_frame = tk.Frame(self, padx=10, pady=5)
        cal_frame.pack()
        submit_button = ttk.Button(cal_frame, text="Submit", command=self.calculate_and_display_macros, width=20)
        submit_button.grid(row=0, column=0)

        result_frame1 = tk.Frame(self, padx=10, pady=10)
        result_frame1.pack()
        self.result_label1 = ttk.Label(result_frame1, text="Your BMR is")
        self.result_label1.grid(row=3, column=0)

        self.result_label2 = ttk.Label(result_frame1, text="", width=10, anchor='center')
        self.result_label2.grid(row=3, column=1)

        self.result_label3 = ttk.Label(result_frame1, text="calories/day.")
        self.result_label3.grid(row=3, column=2)

        self.result_label4 = ttk.Label(result_frame1, text="Your TDEE is")
        self.result_label4.grid(row=4, column=0)

        self.result_label5 = ttk.Label(result_frame1, text="", width=10, anchor='center')
        self.result_label5.grid(row=4, column=1)

        self.result_label6 = ttk.Label(result_frame1, text="calories/day.")
        self.result_label6.grid(row=4, column=2)

        # create labels and entries for inputs
        macro_frame = tk.Frame(self, padx=10, pady=10)
        macro_frame.pack()
        self.protein_label = tk.Label(macro_frame, text="% Protein:")
        self.protein_label.grid(row=0, column=0)
        self.protein_entry = tk.Entry(macro_frame)
        self.protein_entry.grid(row=1, column=0)

        self.carbs_label = tk.Label(macro_frame, text="% Carbs:")
        self.carbs_label.grid(row=2, column=0)
        self.carbs_entry = tk.Entry(macro_frame)
        self.carbs_entry.grid(row=3, column=0)

        self.fat_label2 = tk.Label(macro_frame, text="% Fat:")
        self.fat_label2.grid(row=4, column=0)
        self.fat_entry2 = tk.Entry(macro_frame)
        self.fat_entry2.grid(row=5, column=0)

        # create label for displaying result
        result_frame2 = tk.Frame(self, padx=10, pady=10)
        result_frame2.pack()
        self.result_label7 = tk.Label(result_frame2, text="Protein: ")
        self.result_label7.grid(row=0, column=0)

        self.result_label8 = tk.Label(result_frame2, text="", width=5, anchor='center')
        self.result_label8.grid(row=0, column=1)

        self.result_label9 = tk.Label(result_frame2, text="g = Meat: ")
        self.result_label9.grid(row=0, column=2)

        self.result_label10 = tk.Label(result_frame2, text="", width=5, anchor='center')
        self.result_label10.grid(row=0, column=3)

        self.result_label11 = tk.Label(result_frame2, text="g", anchor='e')
        self.result_label11.grid(row=0, column=4)

        self.result_label12 = tk.Label(result_frame2, text="Carbs: ")
        self.result_label12.grid(row=1, column=0)

        self.result_label13 = tk.Label(result_frame2, text="", width=5, anchor='center')
        self.result_label13.grid(row=1, column=1)

        self.result_label14 = tk.Label(result_frame2, text="g = Rice: ")
        self.result_label14.grid(row=1, column=2)

        self.result_label15 = tk.Label(result_frame2, text="", width=5, anchor='center')
        self.result_label15.grid(row=1, column=3)

        self.result_label16 = tk.Label(result_frame2, text="g")
        self.result_label16.grid(row=1, column=4)

        self.result_label17 = tk.Label(result_frame2, text="Fat: ")
        self.result_label17.grid(row=2, column=0)

        self.result_label18 = tk.Label(result_frame2, text="", width=5, anchor='center')
        self.result_label18.grid(row=2, column=1)

        self.result_label19 = tk.Label(result_frame2, text="g = Oil: ")
        self.result_label19.grid(row=2, column=2)

        self.result_label20 = tk.Label(result_frame2, text="", width=5, anchor='center')
        self.result_label20.grid(row=2, column=3)

        self.result_label21 = tk.Label(result_frame2, text="tbsp")
        self.result_label21.grid(row=2, column=4)

    def calculate_bmr(self):
        weight = float(self.weight_entry.get())
        fat_percent = float(self.fat_entry1.get())
        lbm = weight * (1 - (fat_percent / 100))
        bmr = 370 + (21.6 * lbm)
        return bmr

    def calculate_and_display_macros(self):
        # calculate BMR
        bmr = self.calculate_bmr()

        # calculate TDEE
        activity_level = self.activity_level.get()
        tdee = calculate_total_daily_energy_expenditure(bmr, activity_level)

        # get macro percentages from entries
        protein_percent = float(self.protein_entry.get())
        carbs_percent = float(self.carbs_entry.get())
        fat_percent2 = float(self.fat_entry2.get())

        # calculate macros
        protein, carbs, fat = calculate_macros_with_percentage(tdee, protein_percent, carbs_percent, fat_percent2)

        # calculate food quantities
        meat = protein * 4.55
        rice = carbs * 3.4
        fats = fat / 13

        # update result label with macros and food quantities
        result_text1 = f'{bmr:.2f}'
        self.result_label2.config(text=result_text1)

        result_text2 = f'{tdee:.2f}'
        self.result_label5.config(text=result_text2)

        result_text3 = f'{protein:.2f}'
        self.result_label8.config(text=result_text3)

        result_text4 = f'{meat: .2f}'
        self.result_label10.config(text=result_text4)

        result_text5 = f'{carbs: .2f}'
        self.result_label13.config(text=result_text5)

        result_text6 = f'{rice: .2f}'
        self.result_label15.config(text=result_text6)

        result_text7 = f'{fat: .2f}'
        self.result_label18.config(text=result_text7)

        result_text8 = f'{fats: .2f}'
        self.result_label20.config(text=result_text8)


def calculate_total_daily_energy_expenditure(bmr, activity_level):
    if activity_level == 'sedentary':
        activity_multiplier = 1.2
    elif activity_level == 'lightly active':
        activity_multiplier = 1.375
    elif activity_level == 'moderately active':
        activity_multiplier = 1.55
    elif activity_level == 'very active':
        activity_multiplier = 1.725
    elif activity_level == 'extra active':
        activity_multiplier = 1.9
    else:
        activity_multiplier = 0
    tdee = bmr * activity_multiplier
    return tdee


def calculate_macros_with_percentage(tdee, protein_percent, carbs_percent, fat_percent):
    protein_calories = tdee * protein_percent / 100
    carbs_calories = tdee * carbs_percent / 100
    fat_calories = tdee * fat_percent / 100

    protein = protein_calories / 4
    carbs = carbs_calories / 4
    fat = fat_calories / 9

    return protein, carbs, fat


if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
