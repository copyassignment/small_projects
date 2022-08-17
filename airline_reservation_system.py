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

