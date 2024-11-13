import tkinter as tk

# Hàm xử lý các phép toán
def button_click(value):
    current_text = entry_var.get()

    if value == "C":
        entry_var.set("")  # Xóa tất cả
    elif value == "CE":
        entry_var.set(current_text[:-1])  # Xóa ký tự cuối cùng
    elif value == "⌫":
        # Kiểm tra chuỗi có trống hay không trước khi xóa
        if len(current_text) > 0:
            entry_var.set(current_text[:-1])
    elif value == "=":
        try:
            # Kiểm tra và thay thế dấu `%` trong phép toán
            if "%" in current_text:
                current_text = current_text.replace("%", "/100")
            result = eval(current_text)
            entry_var.set(result)
        except:
            entry_var.set("Error")  # Báo lỗi nếu phép toán không hợp lệ
    elif value == "1/x":
        try:
            entry_var.set("1/("+current_text+")")  # Hiển thị như công thức 1/x
        except:
            entry_var.set("Error")
    elif value == "x^2":
        try:
            entry_var.set("("+current_text+")**2")  # Hiển thị như công thức x^2
        except:
            entry_var.set("Error")
    elif value == "√x":
        try:
            entry_var.set("("+current_text+")**0.5")  # Hiển thị như công thức √x
        except:
            entry_var.set("Error")
    elif value == "+/-":
        if current_text.startswith("-"):
            entry_var.set(current_text[1:])
        else:
            entry_var.set("-" + current_text)
    elif value == "%":
        try:
            entry_var.set(float(current_text) / 100)
        except:
            entry_var.set("Error")
    else:
        entry_var.set(current_text + value)

# Thiết lập giao diện chính
root = tk.Tk()
root.title("Calculator")
root.geometry("400x550")
root.config(bg="#e0e0e0")

# Tạo biến lưu trữ văn bản
entry_var = tk.StringVar()

# Thiết kế hộp nhập và hiển thị kết quả
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 24), justify='right', bd=10, insertwidth=2, bg="#333333", fg="white")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

# Định nghĩa các nút và sắp xếp layout
buttons = [
    ("%", 1, 0), ("CE", 1, 1), ("C", 1, 2), ("⌫", 1, 3),
    ("1/x", 2, 0), ("x^2", 2, 1), ("√x", 2, 2), ("/", 2, 3),
    ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("*", 3, 3),
    ("4", 4, 0), ("5", 4, 1), ("6", 4, 2), ("-", 4, 3),
    ("1", 5, 0), ("2", 5, 1), ("3", 5, 2), ("+", 5, 3),
    ("+/-", 6, 0), ("0", 6, 1), (".", 6, 2), ("=", 6, 3)
]

# Thiết kế màu sắc và bố cục nút bấm
button_colors = {
    "num": "#ffffff",
    "op": "#d3d3d3",
    "special": "#ffcc00",
    "equal": "#4CAF50"
}

# Đặt trọng số để các cột và hàng mở rộng khi thay đổi kích thước
for i in range(4):
    root.columnconfigure(i, weight=1)
for i in range(7):
    root.rowconfigure(i, weight=1)

# Tạo các nút bấm và gán sự kiện
for (text, row, col) in buttons:
    color = button_colors["num"] if text.isdigit() or text == '.' else button_colors["op"]
    if text in ["C", "CE", "⌫"]:
        color = button_colors["special"]
    elif text == "=":
        color = button_colors["equal"]
    
    button = tk.Button(root, text=text, font=("Arial", 16), fg="black", bg=color, command=lambda val=text: button_click(val))
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

root.mainloop()







