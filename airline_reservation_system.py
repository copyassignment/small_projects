import tkinter as tk
import datetime

admin = {'admin': 'admin'}
manager = {'manager': 'manager'}
standard = {'standard': 'standard'}
scheduled = {'AGENTX44': ["10:10", 'Manila', "Delayed"], 'ADO2354': ['5:30', 'Cebu City', 'Delayed'],
             'ASIA1231': ['1:49', 'Boracay', 'Scheduled'], 'AGENT221': ['7:40', 'Cagayan De Oro', 'Scheduled'],
             'ASIAPACIFIC': ['2:50', 'Albay', 'Delayed'], 'AB3452': ['9:320', 'Laguna', 'Scheduled'],
             'LA3452': ['8:40', 'Dumaguete City', 'Scheduled']}
cancelled = {'ASIA3456': ["3:00", "Marawi City", "Cancelled"]}

def delete_users_account():  # This function is responsible for deleting users
    def delete_users_back():
        user = username.get()
        if not (user in admin or user in manager or user in cancelled):
            root = tk.Tk()
            root.title("Username Not Found!")
            tk.Label(master=root, text="Username not found! Please try again!").grid(row=1, column=1)

        else:
            if username.get() == 'admin':
                a = tk.Tk()
                a.title("Can't Delete user!")
                tk.Label(master=a, text="Cannot Delete user!").grid(row=1, column=1)
                a.mainloop()
            elif user in admin:
                if user != 'admin':
                    del admin[user]
                    ad = tk.Tk()
                    ad.title("Success!")
                    tk.Label(master=ad, text="Admin User Successfully Deleted!").grid(row=1, column=1)

            elif user in manager:
                del manager[user]
                ad = tk.Tk()
                ad.title("Success!")
                tk.Label(master=ad, text=" Manager Successfully Deleted!").grid(row=1, column=1)
            if user in standard:
                del standard[user]
                ad = tk.Tk()
                ad.title("Success!")
                tk.Label(master=ad, text="Standard User Successfully Deleted!").grid(row=1, column=1)

    users_delete_acc = tk.Tk()
    users_delete_acc.title("Delete A User")
    tk.Label(master=users_delete_acc, text="Enter the Username").grid(row=1, column=0)
    username = tk.Entry(master=users_delete_acc)
    username.grid(row=1, column=1)
    admin2 = tk.Button(master=users_delete_acc, text="Confirm Deletion", width=25, command=delete_users_back).grid(
        row=1, column=2)



def user_management():  # this function is responsible for adding users
    def adding_user():
        def adding_admin():
            def admin_username():
                def admin_username_back():
                    password = passwrd.get()
                    admin[user] = password
                    root = tk.Tk()
                    root.title("Success")
                    tk.Label(master=root, text="Admin Successfully Added!").grid(row=1, column=1)

                user = username.get()
                if user in admin or user in manager or user in standard:
                    root = tk.Tk()
                    root.title("Username Already Exists!")
                    tk.Label(master=root, text="Username Already Exists! Please Try Again").grid(row=1, column=1)
                    manage_user_scheduled.destroy()
                    system.destroy()
                else:
                    tk.Label(master=system, text="Enter the Password").grid(row=2, column=0)
                    passwrd = tk.Entry(master=system, show='*')
                    passwrd.grid(row=2, column=1)
                    tk.Button(master=system, text="Confirm Password", command=admin_username_back, width=25).grid(row=2,
                                                                                                                  column=3)

            system = tk.Tk()
            system.title("Add An Admin")
            tk.Label(master=system, text="Enter the Username").grid(row=1, column=0)
            username = tk.Entry(master=system)
            username.grid(row=1, column=1)
            admin3 = tk.Button(master=system, text="Confirm Username", width=25, command=admin_username).grid(row=1,
                                                                                                              column=3)

        def add_manager():
            def manager_username():
                def manager_users_back():
                    password = passwrd.get()
                    manager[user] = password
                    root = tk.Tk()
                    root.title("Success")
                    tk.Label(master=root, text="Manager Successfully Added!").grid(row=1, column=1)

                user = username.get()
                if user in admin3 or user in manager or user in standard:
                    root = tk.Tk()
                    root.title("Username Already Exists!")
                    tk.Label(master=root, text="Username Already Exists! Please Try Again").grid(row=1, column=1)
                    manage_user_scheduled.destroy()
                    system.destroy()
                else:
                    tk.Label(master=system, text="Enter the Password").grid(row=2, column=0)
                    passwrd = tk.Entry(master=system, show='*')
                    passwrd.grid(row=2, column=1)
                    tk.Button(master=system, text="Confirm Password", command=manager_users_back, width=25).grid(row=2,
                                                                                                                 column=3)

            system = tk.Tk()
            system.title("Add A Manager")
            tk.Label(master=system, text="Enter the Username").grid(row=1, column=0)
            username = tk.Entry(master=system)
            username.grid(row=1, column=1)
            admin3 = tk.Button(master=system, text="Confirm Username", width=25, command=manager_username).grid(row=1,
                                                                                                                column=3)

        def adding_standard():
            def standard_username():
                def standard_back_users():
                    password = passwrd.get()
                    standard[user] = password
                    root = tk.Tk()
                    root.title("Success")
                    tk.Label(master=root, text="Standard User Successfully Added!").grid(row=1, column=1)

                user = username.get()
                if user in admin or user in manager or user in standard:
                    root = tk.Tk()
                    root.title("Username Already Exists!")
                    tk.Label(master=root, text="Username Already Exists! Please Try Again").grid(row=1, column=1)

                    system.destroy()
                else:
                    tk.Label(master=system, text="Enter the Password").grid(row=2, column=0)
                    passwrd = tk.Entry(master=system, show='*')
                    passwrd.grid(row=2, column=1)
                    tk.Button(master=system, text="Confirm Password", command=standard_back_users, width=25).grid(row=2,
                                                                                                                  column=3)

            system = tk.Tk()
            system.title("Add A Standard User")
            tk.Label(master=system, text="Enter the Username").grid(row=1, column=0)
            username = tk.Entry(master=system)
            username.grid(row=1, column=1)
            admin3 = tk.Button(master=system, text="Confirm Username", width=25, command=standard_username).grid(row=1,
                                                                                                                 column=3)

        adding_users_scheduled = tk.Tk()
        adding_users_scheduled.title("Add A User")
        tk.Button(master=adding_users_scheduled, width=25, text="Add An Admin", command=adding_admin).grid(row=1,
                                                                                                           column=1)
        tk.Button(master=adding_users_scheduled, width=25, text="Add A Supervisor", command=add_manager).grid(row=2,
                                                                                                              column=1)
        tk.Button(master=adding_users_scheduled, width=25, text="Add A Standard User", command=adding_standard).grid(
            row=3, column=1)

    def display_users():
        display_scheduled = tk.Tk()
        display_scheduled.title("View Users")
        tk.Label(master=display_scheduled, text="Admin Are:").grid(row=0, column=0)
        e = 0
        for a in admin:
            e += 1
            tk.Label(master=display_scheduled, text=("------", a)).grid(row=e, column=0)
        e += 1
        tk.Label(master=display_scheduled, text="Manager Are:").grid(row=e, column=0)
        for a in manager:
            e += 1
            tk.Label(master=display_scheduled, text=("-----", a)).grid(row=e, column=0)
        e += 1
        tk.Label(master=display_scheduled, text="Standard Users Are:").grid(row=e, column=0)
        for a in standard:
            e += 1
            tk.Label(master=display_scheduled, text=("-----", a)).grid(row=e, column=0)

    def deleting_users():
        def deleting_back_user():
            user = username.get()
            if not (user in admin or user in manager or user in standard):
                root = tk.Tk()
                root.title("Username Not Found!")
                tk.Label(master=root, text="Username not found! Please try again!").grid(row=1, column=1)
            else:
                if user in admin:
                    del admin[user]
                    admin1 = tk.Tk()
                    admin1.title("Success!")
                    tk.Label(master=admin1, text="Admin User Successfully Deleted!").grid(row=1, column=1)
                    delete_users_scheduled.destroy()
                elif user in manager:
                    del manager[user]
                    admin1 = tk.Tk()
                    admin1.title("Success!")
                    tk.Label(master=admin1, text=" Manager Successfully Deleted!").grid(row=1, column=1)
                    delete_users_scheduled.destroy()
                if user in standard:
                    del standard[user]
                    admin1 = tk.Tk()
                    admin1.title("Success!")
                    tk.Label(master=admin1, text="Standard User Successfully Deleted!").grid(row=1, column=1)
                    delete_users_scheduled.destroy()

        delete_users_scheduled = tk.Tk()
        delete_users_scheduled.title("Delete A User")
        tk.Label(master=delete_users_scheduled, text="Enter the Username").grid(row=1, column=0)
        username = tk.Entry(master=delete_users_scheduled)
        username.grid(row=1, column=1)
        admin2 = tk.Button(master=delete_users_scheduled, text="Confirm Deletion", width=25,
                           command=deleting_back_user).grid(row=1, column=2)

    manage_user_scheduled = tk.Tk()
    manage_user_scheduled.title("Manage Users")
    tk.Button(master=manage_user_scheduled, text="Add Users", width=25, command=adding_user).grid(row=1, column=0)
    tk.Button(master=manage_user_scheduled, text="Delete A User", width=25, command=deleting_users).grid(row=2,
                                                                                                         column=0)
    tk.Button(master=manage_user_scheduled, text="View Current Users", width=25, command=display_users).grid(row=3,
                                                                                                             column=0)




def update():
    scheduled_update = tk.Tk()
    scheduled_update.title("Update/Add A Flight")
    tk.Label(master=scheduled_update, text="Enter The Flight Number").grid(row=1, column=0)
    number_of_flight = tk.Entry(master=scheduled_update)
    number_of_flight.grid(row=1, column=1)

    def update_btn1():
        if number_of_flight.get() not in scheduled:
            scheduled[number_of_flight.get()] = ["", "", ""]
        tk.Label(master=scheduled_update, text="Enter Departure Time").grid(row=3, column=0)
        departure_time = tk.Entry(master=scheduled_update)
        departure_time.grid(row=3, column=1)
        tk.Label(master=scheduled_update, text="Enter Status").grid(row=4, column=0)
        stat = tk.Entry(master=scheduled_update)
        stat.grid(row=4, column=1)
        tk.Label(master=scheduled_update, text="Enter Destination").grid(row=5, column=0)
        destination_place = tk.Entry(master=scheduled_update)
        destination_place.grid(row=5, column=1)

        def update_btn2():
            if departure_time.get() != "":
                scheduled[number_of_flight.get()][0] = departure_time.get()
            if stat.get() != "":
                scheduled[number_of_flight.get()][2] = stat.get()
            if destination_place.get() != "":
                scheduled[number_of_flight.get()][1] = destination_place.get()
            update_root = tk.Tk()
            update_root.title("Successfully Updated!")
            tk.Label(master=update_root, text="Successfully Updated!!").grid(row=0, column=0)
            scheduled_update.destroy()

        tk.Button(master=scheduled_update, text="Confirm", command=update_btn2).grid(row=6, column=1)

    tk.Button(master=scheduled_update, text="Confirm", command=update_btn1).grid(row=2, column=1)
    scheduled_update.mainloop()

