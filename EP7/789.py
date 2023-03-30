import tkinter as tk
from tkinter import messagebox
from EP7 import Customer_List
import ttkbootstrap as ttk
from Nutrition_List import NutritionData, get_customer_data

# create an instance of NutritionData
nutrition_data = NutritionData('nutrition_list.db')

# get customer data from customer_list.db
customer_data = get_customer_data('customer_list.db')

# add data to nutrition_list.db for each customer
for customer in customer_data:
    nutrition_data.add_data(customer[0], None, None)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer List")
        self.root.geometry("900x550")
        self.db = Customer_List.Database()
        self.style = ttk.Style()
        self.style.theme_use('litera')
        self.name_var = None
        self.email_var = None
        self.age_var = None
        self.address_var = None
        self.tree = None
        self.dark_mode = None
        self.create_widgets_tab1()
        self.view_records()

    def create_widgets_tab1(self):
        # Create a notebook
        notebook = ttk.Notebook(root)
        notebook.pack(fill="both", expand=True)

        # Create tabs
        tab1 = ttk.Frame(notebook)
        tab2 = ttk.Frame(notebook)

        notebook.add(tab1, text="Customer Management")
        notebook.add(tab2, text="Nutrition Adjustment")

        # Create customer form
        title1_frame = tk.Frame(tab1, padx=10, pady=5)
        title1_frame.pack()
        tk.Label(title1_frame, text="Customer Management", font=('Arial', 35, 'bold')).grid(row=0, column=0)

        # Create customer form
        title2_frame = tk.Frame(tab2, padx=10, pady=5)
        title2_frame.pack()
        tk.Label(title2_frame, text="Nutrition Adjustment", font=('Arial', 35, 'bold')).grid(row=0, column=0)

        self.name_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.address_var = tk.StringVar()
        form_frame = tk.Frame(tab1, padx=10, pady=5)
        form_frame.pack()
        tk.Label(form_frame, text="Name: ").grid(row=0, column=0, sticky="w")
        tk.Entry(form_frame, textvariable=self.name_var).grid(row=0, column=1, pady=5)
        tk.Label(form_frame, text="Email: ").grid(row=1, column=0, sticky="w")
        tk.Entry(form_frame, textvariable=self.email_var).grid(row=1, column=1, pady=5)
        tk.Label(form_frame, text="Age: ").grid(row=2, column=0, sticky="w")
        tk.Entry(form_frame, textvariable=self.age_var).grid(row=2, column=1, pady=5)
        tk.Label(form_frame, text="Address: ").grid(row=3, column=0, sticky="w")
        tk.Entry(form_frame, textvariable=self.address_var).grid(row=3, column=1, pady=5)
        tk.Button(form_frame, text="Add Record", command=self.add_record, width=15).grid(row=4, column=1, pady=10)

        # Create treeview to display customers
        tree_frame = tk.Frame(tab1, padx=10, pady=5)
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


        # Add buttons to modify selected record

        btn_frame = tk.Frame(tab1, padx=10, pady=5)
        btn_frame.pack()
        tk.Button(btn_frame, text="Edit", command=self.edit_record, width=10).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Delete", command=self.delete_record, width=10).grid(row=0, column=1, padx=10)

        # Add dark mode toggle button
        dark_frame = tk.Frame(tab1, pady=10)
        dark_frame.pack()
        self.dark_mode = tk.BooleanVar(value=False)
        ttk.Checkbutton(dark_frame, text="Dark Mode", variable=self.dark_mode, bootstyle="light-round-toggle",
                        command=self.change_theme).grid(row=0, column=0)


    def change_theme(self):
        style = ttk.Style()
        if self.dark_mode.get():
            style.theme_use('darkly')
        else:
            style.theme_use('litera')

    def add_record(self):
        name = self.name_var.get()
        email = self.email_var.get()
        age = self.age_var.get()
        address = self.address_var.get()

        # Clear input fields
        self.name_var.set("")
        self.email_var.set("")
        self.age_var.set("")
        self.address_var.set("")

        # Move focus away from input fields
        self.root.focus()

        # Insert new record into database and update view
        self.db.insert(name, email, age, address)
        self.view_records()

    def view_records(self):
        # Clear previous data
        self.tree.delete(*self.tree.get_children())

        # Fetch new data from database
        rows = self.db.fetch()

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
            edit_window = tk.Toplevel(self.root)
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
                                    command=lambda: self.save_record(edit_window, id_entry.get(), name_entry.get(),
                                                                     email_entry.get(), age_entry.get(),
                                                                     address_entry.get()))
            save_button.grid(row=5, column=1, pady=10)

        else:
            messagebox.showerror("Error", "Please select a record to edit.")

    def save_record(self, edit_window, selected_id, name, email, age, address):
        self.db.update(selected_id, name, email, age, address)
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
                self.db.remove(id)
                self.view_records()



if __name__ == "__main__":
    root = ttk.Window(themename='litera')
    app = App(root)
    root.mainloop()
