
import tkinter as tk
from functools import partial

# функции калькулятора
def press(key):
    entry.insert(tk.END, key)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
        history.append(str(result))
        if history_visible:
            update_history()
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# управление историей
def toggle_history():
    global history_visible
    history_visible = not history_visible
    if history_visible:
        history_list.grid(row=1, column=4, rowspan=5, padx=(5,10), pady=10, sticky='ns')
        update_history()
    else:
        history_list.grid_forget()

def update_history():
    history_list.delete(0, tk.END)
    for item in history:
        history_list.insert(tk.END, item)

# окно
root = tk.Tk()
root.title("Калькулятор")
root.resizable(False, False)
root.configure(bg="#2b2b2b")

history_visible = False
history = []

# поле ввода
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='ridge', bg="#1e1e1e", fg="white", justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

# кнопка история
history_btn = tk.Button(root, text="История", font=('Arial', 12), bg="#007aff", fg="white", command=toggle_history)
history_btn.grid(row=6, column=0, columnspan=4, pady=(0,10), sticky='we')

# Listbox для истории (по умолчанию не отображается)
history_list = tk.Listbox(root, height=6, width=20, bg="#1e1e1e", fg="white", font=('Arial', 12))

# кнопки калькулятора
buttons = [
    ('7', "#3c3c3c"), ('8', "#3c3c3c"), ('9', "#3c3c3c"), ('/', "#ff9500"),
    ('4', "#3c3c3c"), ('5', "#3c3c3c"), ('6', "#3c3c3c"), ('*', "#ff9500"),
    ('1', "#3c3c3c"), ('2', "#3c3c3c"), ('3', "#3c3c3c"), ('-', "#ff9500"),
    ('C', "#ff3b30"), ('0', "#3c3c3c"), ('=', "#34c759"), ('+', "#ff9500")
]

row_val = 1
col_val = 0

for (text, color) in buttons:
    if text == '=':
        action = calculate
    elif text == 'C':
        action = clear
    else:
        action = partial(press, text)
    
    tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), bg=color, fg="white",
              activebackground="#5e5e5e", activeforeground="white", relief='ridge',
              command=action).grid(row=row_val, column=col_val, padx=5, pady=5)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
