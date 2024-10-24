import tkinter as tk
from tkinter import messagebox

def calculate_change(payment, cost):
    change = payment - cost
    if change < 0:
        return "Amount due is insufficient."
    
    coins = [500, 100, 50, 10]
    result = {coin: 0 for coin in coins}

    for coin in coins:
        count = change // coin
        change -= count * coin
        result[coin] = count 
    if change > 0:
        return "1 and 5 yen are missing."
    
    return result

def calculate():
    payment = int(payment_entry.get())
    cost = int(cost_entry.get())
    change_result = calculate_change(payment, cost)

    if isinstance(change_result, str):
        messagebox.showinfo("Result", change_result)
    else:
        result_message = "\n".join([f"{coin}円: {count}枚" for coin, count in change_result.items() if count > 0])
        messagebox.showinfo("Change Breakdown", result_message if result_message else "No change")

# main window
root = tk.Tk()
root.title("Change counting system")
root.geometry("500x400")

tk.Label(root, text=u"Amount Paid（円）:", font=("Times",14)).pack(pady=5)
payment_entry = tk.Entry(root)
payment_entry.pack(pady=5)

tk.Label(root, text="Amount of goods（円）:",font=("Times",14)).pack(pady=5)
cost_entry = tk.Entry(root)
cost_entry.pack(pady=5)

tk.Button(root, text="Accountant", command=calculate,font=("Times",14)).pack(pady=20)

root.mainloop()