import tkinter as tk
import random

def generate_winner():
    winner_number = random.randint(1, 100)
    label_text.set("Переможець:")
    winner_label.config(text=str(winner_number))

# Створюємо головне вікно
root = tk.Tk()
root.title("Визначник переможця")
root.geometry("400x200")

# Створюємо напис
label_text = tk.StringVar()
label_text.set("Натисни, щоб дізнатися переможця")
label = tk.Label(root, textvariable=label_text, font=("Helvetica", 16))
label.pack(pady=20)

# Створюємо місце для номера переможця
winner_label = tk.Label(root, text="?", font=("Helvetica", 24))
winner_label.pack(pady=10)

# Створюємо кнопку для генерації переможця
generate_button = tk.Button(root, text="Згенерувати", command=generate_winner, font=("Helvetica", 14))
generate_button.pack(pady=20)

# Запускаємо головний цикл програми
root.mainloop()
