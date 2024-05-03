class Employee:
    """Base class for all employees."""
    def __init__(self, name, employee_id, department, title, base_salary, dob, age):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.title = title
        self.base_salary = base_salary
        self.dob = dob
        self.age = age

    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

    def __str__(self):
        return f"Employee Name: {self.name}, ID: {self.employee_id}, Department: {self.department}"

    def print_relationships(self):
        print(f"Employee {self.name} works in the {self.department} department with employee ID: {self.employee_id}")

    def get_details(self):
        return f"ID: {self.employee_id}, Name: {self.name}, Department: {self.department}"


# Subclasses inheriting from Employee.

class SalesManager(Employee):
    def __init__(self, name, employee_id, department, title, base_salary, dob, age, sales_quota, current_sales, team_size):
        super().__init__(name, employee_id, department, title, base_salary, dob, age)
        self.sales_quota = sales_quota
        self.current_sales = current_sales
        self.team_size = team_size

    def print_relationships(self):
        super().print_relationships()
        print(f"{self.name} is a Sales Manager with a team size of {self.team_size}")


class SalesPerson(Employee):
    def __init__(self, name, emp_id, department, title, base_salary, dob, age, sales_quota=0, current_sales=0):
        super().__init__(name, emp_id, department, title, base_salary, dob, age)
        self.sales_quota = sales_quota
        self.current_sales = current_sales

    def print_relationships(self):
        super().print_relationships()
        print(f"{self.name} is a Sales Person in the {self.department} department.")


class Decorator(Employee):
    def __init__(self, name, emp_id, department, title, base_salary, dob, age):
        super().__init__(name, emp_id, department, title, base_salary, dob, age)

    def print_relationships(self):
        super().print_relationships()
        print(f"{self.name} is a Decorator in the {self.department} department.")


class Marketer(Employee):
    def __init__(self, name, emp_id, department, title, base_salary, dob, age):
        super().__init__(name, emp_id, department, title, base_salary, dob, age)

    def print_relationships(self):
        super().print_relationships()
        print(f"{self.name} is a Marketer in the {self.department} department.")


class Accountant(Employee):
    def __init__(self, name, emp_id, department, title, base_salary, dob, age):
        super().__init__(name, emp_id, department, title, base_salary, dob, age)

    def print_relationships(self):
        super().print_relationships()
        print(f"{self.name} is an Accountant in the {self.department} department.")


class Handyman(Employee):
    def __init__(self, name, emp_id, department, title, base_salary, dob, age):
        super().__init__(name, emp_id, department, title, base_salary, dob, age)

    def print_relationships(self):
        super().print_relationships()
        print(f"{self.name} is a Handyman in the {self.department} department.")


# Example of creating instances of each class
sales_manager = SalesManager("Mariam", "SM456", "Sales", "Regional Manager", 8000, "1979-02-15", "34", 150000, 75000,
                             10)
sales_person = SalesPerson("Alya", "SP789", "Sales", "Sales Rep", 4500, "1988-03-22", "43")
decorator = Decorator("Oshbah", "D123", "Design", "Lead Decorator", 5500, "1990-04-18", "33")
marketer = Marketer("Sausan", "M456", "Marketing", "Marketing Specialist", 6000, "1985-05-25", "49")
accountant = Accountant("Anood", "A789", "Accounting", "Senior Accountant", 7000, "1982-06-30", "43")
handyman = Handyman("Fatima", "H123", "Maintenance", "Head Handyman", 4000, "1976-07-28", "30")

# Printing relationships for all employees
sales_manager.print_relationships()
sales_person.print_relationships()
decorator.print_relationships()
marketer.print_relationships()
accountant.print_relationships()
handyman.print_relationships()


class Supplier:
    # Base class for all types of suppliers
    def __init__(self, supplier_id, name, service_provided, contact_details, agreement_details):
        self.supplier_id = supplier_id
        self.name = name
        self.service_provided = service_provided
        self.contact_details = contact_details
        self.agreement_details = agreement_details

    def get_details(self):
        # Retrieves supplier's details
        return f"Supplier ID: {self.supplier_id}, Name: {self.name}, Service Provided: {self.service_provided}"

    def __str__(self):
        # String representation of a Supplier
        return f"Supplier: {self.get_details()}"


# Subclasses for specific types of suppliers, each adding its own attributes:
class Caterer(Supplier):
    # Inherits from Supplier and adds a menu_options attribute.
    def __init__(self, supplier_id, name, contact_details, agreement_details, menu_options):
        super().__init__(supplier_id, name, "Catering", contact_details, agreement_details)
        self.menu_options = menu_options


class Cleaner(Supplier):
    # Inherits from Supplier and adds a cleaning_services_offered attribute.
    def __init__(self, supplier_id, name, contact_details, agreement_details, cleaning_services_offered):
        super().__init__(supplier_id, name, "Cleaning", contact_details, agreement_details)
        self.cleaning_services_offered = cleaning_services_offered


class Decorator(Supplier):
    # Inherits from Supplier and adds a decoration_styles attribute.
    def __init__(self, supplier_id, name, contact_details, agreement_details, decoration_styles):
        super().__init__(supplier_id, name, "Decorating", contact_details, agreement_details)
        self.decoration_styles = decoration_styles


class Entertainer(Supplier):
    # Inherits from Supplier and adds an entertainment_services attribute.
    def __init__(self, supplier_id, name, contact_details, agreement_details, entertainment_services):
        super().__init__(supplier_id, name, "Entertainment", contact_details, agreement_details)
        self.entertainment_services = entertainment_services


class FurnitureSupplier(Supplier):
    # Inherits from Supplier and adds a furniture_items attribute.
    def __init__(self, supplier_id, name, contact_details, agreement_details, furniture_items):
        super().__init__(supplier_id, name, "Furniture Supply", contact_details, agreement_details)
        self.furniture_items = furniture_items


# Creating instances to demonstrate:
caterer = Caterer("C123", "Delicious Catering", "contact@delicious.com", "Contract #1",
                  ["Italian", "Chinese", "Mexican"])
cleaner = Cleaner("CL456", "Sparkle Clean", "clean@sparkle.com", "Contract #2", ["Office Cleaning", "Event Cleanup"])
decorator = Decorator("D789", "Elegant Designs", "designs@elegant.com", "Contract #3", ["Modern", "Classic", "Vintage"])
entertainer = Entertainer("E101", "Party Entertainers", "fun@partyentertainers.com", "Contract #4",
                          ["Live Music", "Magicians", "Comedians"])
furniture_supplier = FurnitureSupplier("F212", "Comfort Furniture", "furnish@comfort.com", "Contract #5",
                                       ["Chairs", "Tables", "Decorative"])


class Client:
    # Represents a client who can host events.
    def __init__(self, name):
        self.name = name
        self.events = []

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    # Receiving the Event object in a function creates the association
    def hosts_event(self, event):
        self.events.append(event)

    def __str__(self):
        return f"Client name is: {self.get_name()}"


class Guest:
    # Represents a guest who can attend events.
    def __init__(self, name):
        self.name = name
        self.events = []

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    # Receiving the Event object in a function creates the association
    def attends_event(self, event):
        self.events.append(event)

    def __str__(self):
        return f"Guest name is: {self.get_name()}"


class Client:
    def __init__(self, name):
        self.name = name
        self.hosted_events = []

    def get_name(self):
        return self.name

    def hosts_event(self, event):
        self.hosted_events.append(event)

class Guest:
    def __init__(self, name):
        self.name = name
        self.attending_events = []

    def get_name(self):
        return self.name

    def attends_event(self, event):
        self.attending_events.append(event)


class Client:
    def __init__(self, name):
        self.name = name
        self.hosted_events = []

    def get_name(self):
        return self.name

    def hosts_event(self, event):
        self.hosted_events.append(event)


class Guest:
    def __init__(self, name):
        self.name = name
        self.attending_events = []

    def get_name(self):
        return self.name

    def attends_event(self, event):
        self.attending_events.append(event)


class Event:
    def __init__(self, name=None, host=None, attendees=None, event_schedule=None):
        self.name = name
        self.host = host
        self.attendees = attendees if attendees else []
        self.event_schedule = event_schedule if event_schedule else EventSchedule()

    def set_host(self, client):
        self.host = client
        client.hosts_event(self)

    def add_attendee(self, guest):
        self.attendees.append(guest)
        guest.attends_event(self)

    def add_schedule_detail(self, detail_type, detail):
        self.event_schedule.add_schedule_detail(detail_type, detail)

    def __str__(self):
        return f"Event Name: {self.name}, Host: {self.host.get_name() if self.host else 'None'}, Attendees: {', '.join([attendee.get_name() for attendee in self.attendees])}, Schedule: {self.event_schedule}"


class EventSchedule:
    def __init__(self):
        self.details = {}

    def add_schedule_detail(self, detail_type, detail):
        self.details[detail_type] = detail

    def __str__(self):
        return ', '.join(f"{detail_type}: {detail}" for detail_type, detail in self.details.items())

# Main program
client1 = Client("Shatha")
guest1 = Guest("Furooz")
guest2 = Guest("Alanood")
event1 = Event()  # Creating an instance of Event

event1.name = "Special Event"  # Setting attributes of the event
event1.set_host(client1)
event1.add_attendee(guest1)
event1.add_attendee(guest2)
event1.add_schedule_detail("Date", "2022-08-20")
event1.add_schedule_detail("Start Time", "11:00 AM")
event1.add_schedule_detail("End Time", "3:00 PM")

print(event1)
class Supplier:
    # Represents a general supplier providing services for events.
    def __init__(self, name, service):
        self.name = name
        self.service = service
        self.status = "Available"

    def provide_service(self):
        self.status = "Hired"

    def __str__(self):
        return f"Supplier name is: {self.name}, Service: {self.service}, Status: {self.status}"

class FurnitureSupplier(Supplier):
    def __init__(self, name):
        super().__init__(name, "Furniture")

class EntertainerSupplier(Supplier):
    def __init__(self, name):
        super().__init__(name, "Entertainment")

class DecoratorSupplier(Supplier):
    def __init__(self, name):
        super().__init__(name, "Decoration")

class CleanerSupplier(Supplier):
    def __init__(self, name):
        super().__init__(name, "Cleaning")
# Creating simple association relationships
class Guest:
    def __init__(self, name):
        self.name = name

class Client:
    def __init__(self, name):
        self.name = name

class Venue:
    def __init__(self, name):
        self.name = name
class CateringSupplier(Supplier):
    def __init__(self, name):
        super().__init__(name, "Catering")

# Implementing composition relationship for Event and EventSchedule
class EventSchedule:
    def __init__(self):
        self.details = {}

    def add_schedule_detail(self, detail_type, detail):
        self.details[detail_type] = detail

    def __str__(self):
        return ', '.join(f"{type}: {info}" for type, info in self.details.items())

class Event:
    def __init__(self, name):
        self.name = name
        self.schedule = {}  # Using a dictionary to hold schedule details

    def add_schedule_detail(self, detail_type, detail):
        self.schedule[detail_type] = detail

    def __str__(self):
        schedule_details = ', '.join(f"{key}: {value}" for key, value in self.schedule.items())
        return f"Event {self.name} with details: {schedule_details}"



# Main program to demonstrate relationships and dependencies
event = Event("Annual Conference")
event.add_schedule_detail("Date", "2024-12-05")
event.add_schedule_detail("Start Time", "10:00 AM")
event.add_schedule_detail("End Time", "6:00 PM")

guest1 = Guest("Tom")
client1 = Client("Company X")
venue1 = Venue("Grand Hall")
supplier1 = CateringSupplier("Epic Catering")


print(event)
import tkinter as tk
from tkinter import messagebox
import pickle
import os

data_path = "data"
os.makedirs(data_path, exist_ok=True)


class Entity:
    def __init__(self, entity_type, id_number, name, location, email):
        self.entity_type = entity_type
        self.id_number = id_number
        self.name = name
        self.location = location
        self.email = email

    def to_dict(self):
        return {
            "ID": self.id_number,
            "Name": self.name,
            "Location": self.location,
            "Email": self.email
        }


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Management System")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Select Entity to Manage:").pack(pady=5)

        entities = ["Employee", "Event", "Client", "Supplier", "Guest", "Venue"]
        self.entity_var = tk.StringVar(self)
        self.entity_var.set(entities[0])

        entity_option_menu = tk.OptionMenu(self, self.entity_var, *entities)
        entity_option_menu.pack()

        tk.Label(self, text="Enter ID Number").pack(pady=5)
        self.id_entry = tk.Entry(self)
        self.id_entry.pack()

        tk.Label(self, text="Enter Name").pack(pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        tk.Label(self, text="Enter Position/Location").pack(pady=5)
        self.position_entry = tk.Entry(self)
        self.position_entry.pack()

        tk.Label(self, text="Enter Email").pack(pady=5)
        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        add_button = tk.Button(self, text="Add", command=self.add_entity)
        add_button.pack(pady=10)

        delete_button = tk.Button(self, text="Delete", command=self.delete_entity)
        delete_button.pack(pady=5)

        update_button = tk.Button(self, text="Update", command=self.update_entity)
        update_button.pack(pady=5)

        display_button = tk.Button(self, text="Display Details", command=self.display_details)
        display_button.pack(pady=5)

        next_page_button = tk.Button(self, text="Next Page", command=self.open_next_page)
        next_page_button.pack(pady=5)

    def add_entity(self):
        entity_type = self.entity_var.get()
        entity = Entity(entity_type, self.id_entry.get(), self.name_entry.get(), self.position_entry.get(),
                        self.email_entry.get())

        filename = os.path.join(data_path, f"{entity_type}_data.pkl")
        try:
            with open(filename, 'wb') as file:
                pickle.dump(entity.to_dict(), file)
            messagebox.showinfo("Success", f"{entity_type} added successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add {entity_type}: {str(e)}")

    def delete_entity(self):
        entity_type = self.entity_var.get()
        filename = os.path.join(data_path, f"{entity_type}_data.pkl")
        try:
            os.remove(filename)
            messagebox.showinfo("Success", f"{entity_type} data deleted successfully.")
        except FileNotFoundError:
            messagebox.showerror("Error", f"No {entity_type} data found.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete {entity_type}: {str(e)}")

    def update_entity(self):
        entity_type = self.entity_var.get()
        entity = Entity(entity_type, self.id_entry.get(), self.name_entry.get(), self.position_entry.get(),
                        self.email_entry.get())

        filename = os.path.join(data_path, f"{entity_type}_data.pkl")
        try:
            with open(filename, 'wb') as file:
                pickle.dump(entity.to_dict(), file)
            messagebox.showinfo("Success", f"{entity_type} data updated successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update {entity_type}: {str(e)}")

    def display_details(self):
        entity_type = self.entity_var.get()
        filename = os.path.join(data_path, f"{entity_type}_data.pkl")
        try:
            with open(filename, 'rb') as file:
                data = pickle.load(file)
                messagebox.showinfo(f"{entity_type} Details", f"{entity_type} Data:\n{data}")
        except FileNotFoundError:
            messagebox.showerror("Error", f"No {entity_type} data found.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to display {entity_type} details: {str(e)}")

    def open_next_page(self):
        next_page = NextPage(self)
        self.withdraw()
        next_page.mainloop()
        self.deiconify()
    def open_next_page(self):
        new_window = tk.Toplevel(self)
        NextPage(new_window)

class NextPage:
    def __init__(self, master):
        self.master = master
        self.master.title("NextPage")

        # Event ID input and button setup
        tk.Label(self.master, text="Enter Event ID:").pack(pady=10)
        self.event_id_entry = tk.Entry(self.master)
        self.event_id_entry.pack()
        event_details_button = tk.Button(self.master, text="Get Event Details", command=self.get_event_details)
        event_details_button.pack(pady=10)

        # Client ID input and button setup
        tk.Label(self.master, text="Enter Client ID:").pack(pady=10)
        self.client_id_entry = tk.Entry(self.master)
        self.client_id_entry.pack()
        client_details_button = tk.Button(self.master, text="Get Client Details", command=self.get_client_details)
        client_details_button.pack(pady=10)

        # Supplier ID input and button setup
        tk.Label(self.master, text="Enter Supplier ID:").pack(pady=10)
        self.supplier_id_entry = tk.Entry(self.master)
        self.supplier_id_entry.pack()
        supplier_details_button = tk.Button(self.master, text="Get Supplier Details", command=self.display_supplier_details)
        supplier_details_button.pack(pady=10)


        # Guest ID input and button setup
        tk.Label(self.master, text="Enter Guest ID:").pack(pady=10)
        self.guest_id_entry = tk.Entry(self.master)
        self.guest_id_entry.pack()
        guest_details_button = tk.Button(self.master, text="Get Guest Details", command=self.display_guest_details)
        guest_details_button.pack(pady=10)

        # Venue ID input and button setup
        tk.Label(self.master, text="Enter Venue ID:").pack(pady=10)
        self.venue_id_entry = tk.Entry(self.master)
        self.venue_id_entry.pack()
        venue_details_button = tk.Button(self.master, text="Get Venue Details", command=self.display_venue_details)
        venue_details_button.pack(pady=10)

    def get_event_details(self):
        event_id = self.event_id_entry.get().strip()
        if event_id == "SM456":
            # Simulating fetching event details with more realistic data
            event = Event("SM456", "Annual Tech Conference", "Convention Center, Silicon Valley", "2023-08-15")
            details = f"Event ID: {event.event_id}\nName: {event.name}\nLocation: {event.location}\nDate: {event.date}"
            messagebox.showinfo("Event Details", details)
        else:
            messagebox.showerror("Error", "Event details not found for ID: " + event_id)

    def get_client_details(self):
        client_id = self.client_id_entry.get().strip()
        if client_id == "SM456":
            # Simulating fetching client details with more realistic data
            client = Client("SM456", "Nova Industries", "contact@novaindustries.com")
            details = f"Client ID: {client.id_number}\nName: {client.name}\nEmail: {client.email}"
            messagebox.showinfo("Client Details", details)
        else:
            messagebox.showerror("Error", "Client details not found for ID: " + client_id)

    def display_guest_details(self):
        guest_id = self.guest_id_entry.get().strip()
        if guest_id == "SM456":
            # Simulating fetching guest details with more realistic data
            messagebox.showinfo("Guest Details", "Guest ID: SM456\nName: John Doe\nAffiliation: Tech Blogger\nSpecial Requirements: Vegan meal")
        else:
            messagebox.showerror("Error", "Guest details not found for ID: " + guest_id)

    def display_venue_details(self):
        venue_id = self.venue_id_entry.get().strip()
        if venue_id == "SM456":
            # Simulating fetching venue details with more realistic data
            messagebox.showinfo("Venue Details", "Venue ID: SM456\nName: Grand Expo Center\nLocation: Downtown Metropolis\nCapacity: 5000 attendees")
        else:
            messagebox.showerror("Error", "Venue details not found for ID: " + venue_id)

    def display_supplier_details(self):
        supplier_id = self.supplier_id_entry.get().strip()
        if supplier_id == "SM456":
            # Simulating fetching supplier details with more realistic data
            messagebox.showinfo("Supplier Details", "Supplier ID: SM456\nCompany: Global Event Suppliers Inc.\nProducts: Audio systems, Lighting, Catering")
        else:
            messagebox.showerror("Error", "Supplier details not found for ID: ")



if __name__ == "__main__":
    app = Application()
    app.mainloop()
