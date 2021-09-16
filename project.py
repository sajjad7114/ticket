from tkinter import ttk, messagebox, Tk


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_admin = False

    def become_admin(self):
        self.is_admin = True


class Owner:
    def __init__(self, name, code, account_number):
        self.name = name
        self.code = code
        self.account_number = account_number
        self.earned_money = 0

    def sell(self, ticket_price):
        self.earned_money += ticket_price * 65 / 100


class Customer:
    def __init__(self, name, code, phone_number):
        self.name = name
        self.code = code
        self.phone_number = phone_number


class Ticket:
    def __init__(self, price, employee, launch, time, customer, turn):
        self.price = price
        self.employee = employee
        self.launch = launch
        self.time = time
        self.customer = customer
        self.turn = turn
        turn.sell()
        employee.sell(price)
        launch.owner.sell(price)


class Launch:
    def __init__(self, name, code, capacity, ticket_price, owner):
        self.name = name
        self.code = code
        self.capacity = capacity
        self.ticket_price = ticket_price
        self.owner = owner


class Employee:
    def __init__(self, user, name, code, base_salary, account_number, substation):
        self.user = user
        self.name = name
        self.code = code
        self.base_salary = base_salary
        self.account_number = account_number
        self.substation = substation
        self.earned_money = 0
        self.bought_ticket = 0

    def sell(self, ticket_price):
        self.earned_money += ticket_price * 5 / 100
        self.bought_ticket += 1


class Message:
    def __init__(self, employee, text):
        self.employee = employee
        self.text = text


class Turn:
    def __init__(self, launch, hour):
        self.launch = launch
        self.ticket_number = 0
        self.hour = hour
        self.is_gone = False

    def sell(self):
        self.ticket_number += 1


class Queue:
    def __init__(self):
        self.list = list()

    def enqueue(self, obj):
        self.list.append(obj)

    def dequeue(self):
        obj = self.list[0]
        del self.list[:1]
        return obj

    def is_empty(self):
        if len(self.list) == 0:
            return True
        return False


def generation_error():
    messagebox.showinfo("generation error", "You must fill all the requirements")


def turn_generate(window, name, code, hour):
    name = name.get()
    code = code.get()
    if name == '' or code == '':
        generation_error()
    else:
        check = False
        for launch in launches:
            if launch.name == name and launch.code == code:
                check = True
                break
        if not check:
            messagebox.showinfo("error 404", "Launch didn't found")
        else:
            count = 0
            for turn in turns:
                if turn.launch.name == name and turn.launch.code == code:
                    count += 1
            if count >= 2:
                messagebox.showinfo("count error", "Can't set more than 2 turns to a launch")
            else:
                turn = Turn(launch, hour)
                turns.append(turn)
                window.destroy()


def employee_generate(window, name, code, base_salary, account_number, substation):
    name = name.get()
    code = code.get()
    base_salary = base_salary.get()
    account_number = account_number.get()
    substation = substation.get()
    if name == '' or code == '' or base_salary == '' or account_number == '' or substation == '':
        generation_error()
    else:
        user = User(name, code)
        employee = Employee(user, name, code, int(base_salary), account_number, substation)
        users.append(user)
        employees.append(employee)
        window.destroy()


def launch_generate(window, name, code, capacity, ticket_price, owner_name, owner_code, owner_account_number):
    owner_name = owner_name.get()
    owner_code = owner_code.get()
    owner_account_number = owner_account_number.get()
    name = name.get()
    code = code.get()
    capacity = capacity.get()
    ticket_price = ticket_price.get()
    if owner_name == '' or owner_code == '' or owner_account_number == '' or name == '' or code == '' or capacity == ''\
            or ticket_price == '':
        generation_error()
    else:
        owner = Owner(owner_name, owner_code, owner_account_number)
        launch = Launch(name, code, int(capacity), int(ticket_price), owner)
        owners.append(owner)
        launches.append(launch)
        window.destroy()


def employee_delete(window, employee):
    employee.remove(employee)
    users.remove(employee.user)
    window.destroy()


def launch_delete(window, launch):
    launches.remove(launch)
    owners.remove(launch.owner)
    window.destroy()


def employee_create(window):
    window.destroy()
    employee_create_root = Tk()
    employee_create_root.title("Employee edit")
    label_name = ttk.Label(employee_create_root, text="Name")
    label_name.grid(row=0, column=0)
    name = ttk.Entry(employee_create_root)
    name.grid(row=0, column=1)
    label_code = ttk.Label(employee_create_root, text="Code")
    label_code.grid(row=1, column=0)
    code = ttk.Entry(employee_create_root)
    code.grid(row=1, column=1)
    label_base_salary = ttk.Label(employee_create_root, text="Base salary")
    label_base_salary.grid(row=2, column=0)
    base_salary = ttk.Entry(employee_create_root)
    base_salary.grid(row=2, column=1)
    label_account_number = ttk.Label(employee_create_root, text="Account Number")
    label_account_number.grid(row=3, column=0)
    account_number = ttk.Entry(employee_create_root)
    account_number.grid(row=3, column=1)
    label_substation = ttk.Label(employee_create_root, text="Substation")
    label_substation.grid(row=4, column=0)
    substation = ttk.Entry(employee_create_root)
    substation.grid(row=4, column=1)
    employee_editing_button = ttk.Button(employee_create_root, text="Create")
    employee_editing_button.grid(row=5, column=1)
    employee_editing_button.config(command=lambda: employee_generate(employee_create_root, name, code, base_salary,
                                                                     account_number, substation))
    employee_create_root.mainloop()


def launch_create(window):
    window.destroy()
    launch_create_root = Tk()
    launch_create_root.title("Launch edit")
    label_name = ttk.Label(launch_create_root, text="Name")
    label_name.grid(row=0, column=0)
    name = ttk.Entry(launch_create_root)
    name.grid(row=0, column=1)
    label_code = ttk.Label(launch_create_root, text="Code")
    label_code.grid(row=1, column=0)
    code = ttk.Entry(launch_create_root)
    code.grid(row=1, column=1)
    label_capacity = ttk.Label(launch_create_root, text="Capacity")
    label_capacity.grid(row=2, column=0)
    capacity = ttk.Entry(launch_create_root)
    capacity.grid(row=2, column=1)
    label_ticket_price = ttk.Label(launch_create_root, text="Ticket price")
    label_ticket_price.grid(row=3, column=0)
    ticket_price = ttk.Entry(launch_create_root)
    ticket_price.grid(row=3, column=1)
    label_owner_name = ttk.Label(launch_create_root, text="Owner name")
    label_owner_name.grid(row=4, column=0)
    owner_name = ttk.Entry(launch_create_root)
    owner_name.grid(row=4, column=1)
    label_owner_code = ttk.Label(launch_create_root, text="Owner code")
    label_owner_code.grid(row=5, column=0)
    owner_code = ttk.Entry(launch_create_root)
    owner_code.grid(row=5, column=1)
    label_owner_account_number = ttk.Label(launch_create_root, text="Owner account number")
    label_owner_account_number.grid(row=6, column=0)
    owner_account_number = ttk.Entry(launch_create_root)
    owner_account_number.grid(row=6, column=1)
    launch_editing_button = ttk.Button(launch_create_root, text="Create")
    launch_editing_button.grid(row=7, column=1)
    launch_editing_button.config(command=lambda: launch_generate(launch_create_root, name, code, capacity, ticket_price,
                                                                 owner_name, owner_code, owner_account_number))
    launch_create_root.mainloop()


def send_message(window, text, employee):
    text = text.get()
    message = Message(employee, text)
    messages.enqueue(message)
    window.destroy()


def information_edition(window, employee):
    window.destroy()
    information_edit_root = Tk()
    information_edit_root.title("ask for edit")
    text = ttk.Entry(information_edit_root, width=100)
    text.grid(row=0, column=0)
    text.insert(0, "I am " + employee.name + " my Code is:" + employee.code + " Please Edit my account")
    information_edit_button = ttk.Button(information_edit_root, text="Send")
    information_edit_button.grid(row=1, column=0)
    information_edit_button.config(command=lambda: send_message(information_edit_root, text, employee))
    information_edit_root.mainloop()


def employee_edition(window, employee, account_number, substation):
    account_number = account_number.get()
    substation = substation.get()
    if account_number == '' or substation == '':
        generation_error()
    else:
        employee.account_number = account_number
        employee.substation = substation
        window.destroy()


def employee_edit(window, employee):
    employee_edit_root = Tk()
    employee_edit_root.title("Employee edit")
    label_name = ttk.Label(employee_edit_root, text="Name")
    label_name.grid(row=0, column=0)
    name = ttk.Label(employee_edit_root, text=employee.name)
    name.grid(row=0, column=1)
    label_code = ttk.Label(employee_edit_root, text="Code")
    label_code.grid(row=1, column=0)
    code = ttk.Label(employee_edit_root, text=employee.code)
    code.grid(row=1, column=1)
    label_base_salary = ttk.Label(employee_edit_root, text="Base salary")
    label_base_salary.grid(row=2, column=0)
    base_salary = ttk.Label(employee_edit_root, text=str(employee.base_salary))
    base_salary.grid(row=2, column=1)
    label_account_number = ttk.Label(employee_edit_root, text="Account number")
    label_account_number.grid(row=3, column=0)
    account_number = ttk.Entry(employee_edit_root)
    account_number.insert(0, str(employee.account_number))
    account_number.grid(row=3, column=1)
    label_substation = ttk.Label(employee_edit_root, text="Substation")
    label_substation.grid(row=4, column=0)
    substation = ttk.Entry(employee_edit_root)
    substation.insert(0, employee.substation)
    substation.grid(row=4, column=1)
    window.destroy()
    employee_editing_button = ttk.Button(employee_edit_root, text="Edit")
    employee_editing_button.grid(row=5, column=1)
    employee_editing_button.config(command=lambda: employee_edition(employee_edit_root, employee, account_number,
                                                                    substation))
    employee_edit_root.mainloop()


def launch_edit(window, launch):
    launch_edit_root = Tk()
    launch_edit_root.title("Launch edit")
    label_name = ttk.Label(launch_edit_root, text="Name")
    label_name.grid(row=0, column=0)
    name = ttk.Entry(launch_edit_root)
    name.insert(0, launch.name)
    name.grid(row=0, column=1)
    label_code = ttk.Label(launch_edit_root, text="Code")
    label_code.grid(row=1, column=0)
    code = ttk.Entry(launch_edit_root)
    code.insert(0, launch.code)
    code.grid(row=1, column=1)
    label_capacity = ttk.Label(launch_edit_root, text="Capacity")
    label_capacity.grid(row=2, column=0)
    capacity = ttk.Entry(launch_edit_root)
    capacity.insert(0, str(launch.capacity))
    capacity.grid(row=2, column=1)
    label_ticket_price = ttk.Label(launch_edit_root, text="Ticket price")
    label_ticket_price.grid(row=3, column=0)
    ticket_price = ttk.Entry(launch_edit_root)
    ticket_price.insert(0, str(launch.ticket_price))
    ticket_price.grid(row=3, column=1)
    label_owner_name = ttk.Label(launch_edit_root, text="Owner name")
    label_owner_name.grid(row=4, column=0)
    owner_name = ttk.Entry(launch_edit_root)
    owner_name.insert(0, launch.owner.name)
    owner_name.grid(row=4, column=1)
    label_owner_code = ttk.Label(launch_edit_root, text="Owner code")
    label_owner_code.grid(row=5, column=0)
    owner_code = ttk.Entry(launch_edit_root)
    owner_code.insert(0, launch.owner.code)
    owner_code.grid(row=5, column=1)
    label_owner_account_number = ttk.Label(launch_edit_root, text="Owner account number")
    label_owner_account_number.grid(row=6, column=0)
    owner_account_number = ttk.Entry(launch_edit_root)
    owner_account_number.insert(0, launch.owner.account_number)
    owner_account_number.grid(row=6, column=1)
    launches.remove(launch)
    owners.remove(launch.owner)
    window.destroy()
    launch_editing_button = ttk.Button(launch_edit_root, text="Edit")
    launch_editing_button.grid(row=7, column=1)
    launch_editing_button.config(command=lambda: launch_generate(launch_edit_root, name, code, capacity,ticket_price,
                                                                 owner_name, owner_code, owner_account_number))
    launch_edit_root.mainloop()


def set_turn(window, hour):
    set_turn_root = Tk()
    set_turn_root.title("Set Turn")
    initial_name = ''
    initial_code = ''
    for turn in turns:
        if turn.hour == hour:
            initial_name = turn.launch.name
            initial_code = turn.launch.code
            turns.remove(turn)
            break
    label_name = ttk.Label(set_turn_root, text="Launch name")
    label_name.grid(row=0, column=0)
    name = ttk.Entry(set_turn_root)
    name.insert(0, initial_name)
    name.grid(row=0, column=1)
    label_code = ttk.Label(set_turn_root, text="Launch code")
    label_code.grid(row=1, column=0)
    code = ttk.Entry(set_turn_root)
    code.insert(0, initial_code)
    code.grid(row=1, column=1)
    window.destroy()
    set_turn_button = ttk.Button(set_turn_root, text="Edit")
    set_turn_button.grid(row=2, column=1)
    set_turn_button.config(command=lambda: turn_generate(set_turn_root, name, code, hour))
    set_turn_root.mainloop()


def turn_panel():
    turn_root = Tk()
    turn_root.title("Turns")
    for hour in range(9, 19, 1):
        check = False
        for turn in turns:
            if turn.hour == hour:
                check = True
                break
        turn_time_label = ttk.Label(turn_root, text=str(hour)+":00")
        turn_time_label.grid(row=hour - 9, column=0)
        string = "Not assigned"
        if check:
            string = turn.launch.name
        turn_launch_label = ttk.Label(turn_root, text=string)
        turn_launch_label.grid(row=hour - 9, column=1)
        string = ''
        bought = False
        if check:
            string = 'bought tickets: ' + str(turn.ticket_number)
            if turn.ticket_number > 0:
                bought = True
        turn_tickect_label = ttk.Label(turn_root, text=string)
        turn_tickect_label.grid(row=hour - 9, column=2)
        turn_button = ttk.Button(turn_root, text="Edit")
        turn_button.grid(row=hour - 9, column=3)
        if bought:
            turn_button.state(['disabled'])
        turn_button.config(command=lambda hour=hour: set_turn(turn_root, hour))

    turn_root.mainloop()


def financial_panel():
    financial_root = Tk()
    financial_root.title("Financial")
    total_money = 0
    for ticket in tickets:
        total_money += ticket.price
    string = "total money:" + str(total_money)
    total_label = ttk.Label(financial_root, text=string)
    total_label.grid(row=0, column=0)
    total_to_launches = 0
    count = 0
    for owner in owners:
        string = owner.name + ":" + str(owner.earned_money)
        owner_money_label = ttk.Label(financial_root, text=string)
        owner_money_label.grid(row=count, column=1)
        count += 1
        total_to_launches += owner.earned_money
    string = "total money for launches:" + str(total_to_launches)
    total_owner_money_label = ttk.Label(financial_root, text=string)
    total_owner_money_label.grid(row=count, column=1)
    total_to_employees = 0
    count = 0
    for employee in employees:
        string = employee.name + ":" + str(employee.earned_money + employee.base_salary)
        employee_money_label = ttk.Label(financial_root, text=string)
        employee_money_label.grid(row=count, column=2)
        count += 1
        total_to_employees += employee.earned_money + employee.base_salary
    string = "total money to employees:" + str(total_to_employees)
    total_employee_money_label = ttk.Label(financial_root, text=string)
    total_employee_money_label.grid(row=count, column=2)
    financial_root.mainloop()


def employee_panel():
    while not messages.is_empty():
        message = messages.dequeue()
        messagebox.showinfo(message.employee.name, message.text)
    count = 0
    employee_root = Tk()
    employee_root.title("Launch")
    for employee in employees:
        string = "name:" + employee.name + " code:" + employee.code + " base_salary:" + str(employee.base_salary)
        string = string + " account_number:" + employee.account_number + " substation:" + employee.substation
        employee_label = ttk.Label(employee_root, text=string)
        employee_label.grid(row=count, column=0)
        employee_edit_button = ttk.Button(employee_root, text="Edit")
        employee_edit_button.grid(row=count, column=1)
        employee_edit_button.config(command=lambda employee=employee: employee_edit(employee_root, employee))
        employee_delete_button = ttk.Button(employee_root, text="Delete")
        employee_delete_button.grid(row=count, column=2)
        employee_delete_button.config(command=lambda employee=employee: employee_delete(employee_root, employee))
        count = count + 1
    employee_create_button = ttk.Button(employee_root, text="New")
    employee_create_button.grid(row=count, column=0)
    employee_create_button.config(command=lambda: employee_create(employee_root))
    employee_root.mainloop()


def see_launch(launch_code):
    see_launch_root = Tk()
    code = launch_code.get()
    if code == '':
        generation_error()
    else:
        for turn in turns:
            count = 0
            if turn.launch.code == code:
                label1 = ttk.Label(see_launch_root, text="hour")
                label1.grid(row=count, column=0)
                label2 = ttk.Label(see_launch_root, text=turn.hour)
                label2.grid(row=count, column=1)
                count += 1
                label3 = ttk.Label(see_launch_root, text="bought tickets")
                label3.grid(row=count, column=0)
                label4 = ttk.Label(see_launch_root, text=turn.ticket_number)
                label4.grid(row=count, column=1)
                count += 1
    see_launch_root.mainloop()


def launch_panel():
    count = 0
    launch_root = Tk()
    launch_root.title("Launch")
    for launch in launches:
        string = "name:" + launch.name + " code:" + launch.code + " capacity:" + str(launch.capacity) + " ticket_price:"
        string = string + str(launch.ticket_price) + " owner_name:" + launch.owner.name + " owner_code:" + launch.owner.code
        string = string + " owner_account_number:" + launch.owner.account_number
        launch_label = ttk.Label(launch_root, text=string)
        launch_label.grid(row=count, column=0)
        launch_edit_button = ttk.Button(launch_root, text="Edit")
        launch_edit_button.grid(row=count, column=1)
        launch_edit_button.config(command=lambda launch=launch: launch_edit(launch_root, launch))
        launch_delete_button = ttk.Button(launch_root, text="Delete")
        launch_delete_button.grid(row=count, column=2)
        launch_delete_button.config(command=lambda launch=launch: launch_delete(launch_root, launch))
        count = count + 1
    launch_create_button = ttk.Button(launch_root, text="New")
    launch_create_button.grid(row=count, column=0)
    launch_create_button.config(command=lambda: launch_create(launch_root))
    launch_code = ttk.Entry(launch_root)
    launch_code.grid(row=count + 1, column=0)
    launch_button = ttk.Button(launch_root, text="See")
    launch_button.grid(row=count + 1, column=1)
    launch_button.config(command=lambda: see_launch(launch_code))
    launch_root.mainloop()


def admin_panel():
    admin_root = Tk()
    admin_root.title("admin")
    launch_button = ttk.Button(admin_root, text='launches')
    launch_button.grid(row=0, column=0)
    launch_button.config(command=launch_panel)
    employee_button = ttk.Button(admin_root, text='employees')
    employee_button.grid(row=0, column=1)
    employee_button.config(command=employee_panel)
    financial_button = ttk.Button(admin_root, text='financial')
    financial_button.grid(row=1, column=0)
    financial_button.config(command=financial_panel)
    turn_button = ttk.Button(admin_root, text='turns')
    turn_button.grid(row=1, column=1)
    turn_button.config(command=turn_panel)
    admin_root.mainloop()


def information_panel(user):
    information_root = Tk()
    information_root.title(user.username)
    for employee in employees:
        if employee.user.username == user.username:
            label_name = ttk.Label(information_root, text="Name")
            label_name.grid(row=0, column=0)
            name = ttk.Label(information_root, text=employee.name)
            name.grid(row=0, column=1)
            label_code = ttk.Label(information_root, text="Code")
            label_code.grid(row=1, column=0)
            code = ttk.Label(information_root, text=employee.code)
            code.grid(row=1, column=1)
            label_base_salary = ttk.Label(information_root, text="Base salary")
            label_base_salary.grid(row=2, column=0)
            base_salary = ttk.Label(information_root, text=str(employee.base_salary))
            base_salary.grid(row=2, column=1)
            label_account_number = ttk.Label(information_root, text="Account number")
            label_account_number.grid(row=3, column=0)
            account_number = ttk.Label(information_root, text=employee.account_number)
            account_number.grid(row=3, column=1)
            label_substation = ttk.Label(information_root, text="Substation")
            label_substation.grid(row=4, column=0)
            substation = ttk.Label(information_root, text=employee.substation)
            substation.grid(row=4, column=1)
            information_editing_button = ttk.Button(information_root, text="Edit")
            information_editing_button.grid(row=5, column=1)
            information_editing_button.config(command=lambda: information_edition(information_root, employee))
    information_root.mainloop()


def financial_information_panel(user):
    financial_information_root = Tk()
    financial_information_root.title(user.username)
    for employee in employees:
        if employee.user.username == user.username:
            label_count = ttk.Label(financial_information_root, text="Ticket count")
            label_count.grid(row=0, column=0)
            count = ttk.Label(financial_information_root, text=employee.bought_ticket)
            count.grid(row=0, column=1)
            label_salary = ttk.Label(financial_information_root, text="Salary")
            label_salary.grid(row=1, column=0)
            code = ttk.Label(financial_information_root, text=str(employee.earned_money + employee.base_salary))
            code.grid(row=1, column=1)
    financial_information_root.mainloop()


def sell(employee, turn, customer):
    if turn.ticket_number >= turn.launch.capacity:
        messagebox.showerror("full capacity", "maximum capacity reached!")
    else:
        ticket = Ticket(turn.launch.ticket_price, employee, turn.launch, turn.hour, customer, turn)
        tickets.append(ticket)
        messagebox.showinfo("OK", "Thank you!")


def generate_customer(window, employee, turn, name, code, phone):
    name = name.get()
    phone = phone.get()
    if name == '' and phone == '':
        generation_error()
    else:
        customer = Customer(name, code, phone)
        customers.append(customer)
        window.destroy()
        sell(employee, turn, customer)


def editing_customer(window, employee, turn, customer, phone):
    phone = phone.get()
    if phone == '':
        generation_error()
    else:
        window.destroy()
        customer.phone_number = phone
        sell(employee, turn, customer)


def edit_customer(employee, turn, customer):
    edit_customer_root = Tk()
    edit_customer_root.title("set customer")
    label_name = ttk.Label(edit_customer_root, text="Name")
    label_name.grid(row=0, column=0)
    name = ttk.Label(edit_customer_root, text=customer.name)
    name.grid(row=0, column=1)
    label_phone = ttk.Label(edit_customer_root, text="Phone number")
    label_phone.grid(row=1, column=0)
    phone = ttk.Entry(edit_customer_root)
    phone.grid(row=1, column=1)
    phone.insert(0, customer.phone_number)
    code_button = ttk.Button(edit_customer_root, text="OK")
    code_button.grid(row=2, column=1)
    code_button.config(command=lambda: editing_customer(edit_customer_root, employee, turn, customer, phone))
    edit_customer_root.mainloop()


def set_customer(employee, turn, code):
    set_customer_root = Tk()
    set_customer_root.title("set customer")
    label_name = ttk.Label(set_customer_root, text="Name")
    label_name.grid(row=0, column=0)
    name = ttk.Entry(set_customer_root)
    name.grid(row=0, column=1)
    label_phone = ttk.Label(set_customer_root, text="Phone number")
    label_phone.grid(row=1, column=0)
    phone = ttk.Entry(set_customer_root)
    phone.grid(row=1, column=1)
    customer_set_button = ttk.Button(set_customer_root, text="OK")
    customer_set_button.grid(row=2, column=1)
    customer_set_button.config(command=lambda: generate_customer(set_customer_root, employee, turn, name, code, phone))
    set_customer_root.mainloop()


def check_customer(window, employee, turn, code):
    code = code.get()
    if code == '':
        generation_error()
    else:
        window.destroy()
        check = False
        for customer in customers:
            if customer.code == code:
                check = True
                break
        if check:
            edit_customer(employee, turn, customer)
        else:
            set_customer(employee, turn, code)


def get_customer(window, employee, turn):
    window.destroy()
    customer_root = Tk()
    customer_root.title("customer")
    label_code = ttk.Label(customer_root, text="Code")
    label_code.grid(row=0, column=0)
    code = ttk.Entry(customer_root)
    code.grid(row=0, column=1)
    code_button = ttk.Button(customer_root, text="OK")
    code_button.grid(row=1, column=1)
    code_button.config(command=lambda: check_customer(customer_root, employee, turn, code))
    customer_root.mainloop()


def sell_panel(user):
    sell_root = Tk()
    sell_root.title("Sell ticket")
    for employee in employees:
        if employee.user.username == user.username:
            for hour in range(9, 19, 1):
                check = False
                for turn in turns:
                    if turn.hour == hour:
                        check = True
                        break
                sell_time_label = ttk.Label(sell_root, text=str(hour) + ":00")
                sell_time_label.grid(row=hour - 9, column=0)
                string = "Not assigned"
                if check:
                    string = turn.launch.name
                sell_launch_label = ttk.Label(sell_root, text=string)
                sell_launch_label.grid(row=hour - 9, column=1)
                string = ''
                if check:
                    string = 'bought tickets: ' + str(turn.ticket_number)
                sell_tickect_label = ttk.Label(sell_root, text=string)
                sell_tickect_label.grid(row=hour - 9, column=2)
                string = ''
                if check:
                    string = 'launch capacity: ' + str(turn.launch.capacity)
                sell_capacity_label = ttk.Label(sell_root, text=string)
                sell_capacity_label.grid(row=hour - 9, column=3)
                sell_button = ttk.Button(sell_root, text="Sell")
                sell_button.grid(row=hour - 9, column=4)
                if not check:
                    sell_button.state(['disabled'])
                sell_button.config(command=lambda hour=hour: get_customer(sell_root, employee, turn))
    sell_root.mainloop()


def user_panel(user):
    user_root = Tk()
    user_root.title("admin")
    information_button = ttk.Button(user_root, text='private information')
    information_button.grid(row=0, column=0)
    information_button.config(command=lambda: information_panel(user))
    financial_information_button = ttk.Button(user_root, text='financial information')
    financial_information_button.grid(row=0, column=1)
    financial_information_button.config(command=lambda: financial_information_panel(user))
    sell_button = ttk.Button(user_root, text='sell ticket')
    sell_button.grid(row=0, column=2)
    sell_button.config(command=lambda: sell_panel(user))
    user_root.mainloop()


def login_fail():
    messagebox.showinfo("can't login", "Username or password is incorrect")


def login(window, password, username):
    u = username.get()
    p = password.get()
    window.destroy()
    check = False
    for user in users:
        if user.username == u:
            check = True
            if user.password == p:
                if user.is_admin:
                    admin_panel()
                else:
                    user_panel(user)
                break
            else:
                login_fail()
    if not check:
        login_fail()


def to_login():
    pass_root = Tk()
    label1 = ttk.Label(pass_root, text='username: ')
    label1.grid(row=0, column=0)
    username = ttk.Entry(pass_root)
    username.grid(row=0, column=1)
    label2 = ttk.Label(pass_root, text='password: ')
    label2.grid(row=1, column=0)
    password = ttk.Entry(pass_root)
    password.grid(row=1, column=1)
    enter_button = ttk.Button(pass_root, text='Enter')
    enter_button.grid(row=2, column=0)
    enter_button.config(command=lambda window=pass_root: login(window, password, username))
    pass_root.mainloop()


admin = User("Mahsa", "71147114")
admin.become_admin()
users = list()
users.append(admin)
launches = list()
owners = list()
employees = list()
messages = Queue()
tickets = list()
turns = list()
customers = list()
root = Tk()
root.title("first")
button = ttk.Button(root, text='login')
button.place(x=0, y=0)
button.config(command=to_login)
root.mainloop()
