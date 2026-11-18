
import tkinter as tk
from tkinter import ttk, messagebox
import html


APP_NAME = "HTML Entity Decoder"


def decode_html():
    text = input_text.get("1.0", "end-1c")

    if not text:
        messagebox.showwarning("แจ้งเตือน", "กรุณาป้อนข้อความ")
        return

    try:
        # ถอดรหัส HTML Entity ซ้อนกันสูงสุด 10 ชั้น
        result = text

        for _ in range(10):
            decoded = html.unescape(result)

            if decoded == result:
                break

            result = decoded

        output_text.delete("1.0", "end")
        output_text.insert("1.0", result)

    except Exception as e:
        messagebox.showerror("Error", str(e))


def copy_result():
    result = output_text.get("1.0", "end-1c")

    if not result:
        return

    root.clipboard_clear()
    root.clipboard_append(result)
    root.update()

    messagebox.showinfo("สำเร็จ", "คัดลอกข้อความแล้ว")


def clear_all():
    input_text.delete("1.0", "end")
    output_text.delete("1.0", "end")


def paste_text():
    try:
        text = root.clipboard_get()
        input_text.insert("insert", text)
    except tk.TclError:
        pass


# Main Window
root = tk.Tk()
root.title(APP_NAME)
root.geometry("750x600")
root.minsize(600, 450)

# Style
style = ttk.Style()
style.theme_use("clam")

main = ttk.Frame(root, padding=15)
main.pack(fill="both", expand=True)

# Header
ttk.Label(
    main,
    text="HTML Entity Decoder",
    font=("Tahoma", 18, "bold")
).pack(anchor="w", pady=(0, 10))

ttk.Label(
    main,
    text="ป้อนข้อความ HTML Entity ที่ต้องการถอดรหัส"
).pack(anchor="w")

# Input
ttk.Label(main, text="ข้อความต้นฉบับ").pack(anchor="w", pady=(10, 5))

input_frame = ttk.Frame(main)
input_frame.pack(fill="both", expand=True)

input_text = tk.Text(
    input_frame,
    height=8,
    font=("Consolas", 11),
    wrap="word"
)
input_text.pack(side="left", fill="both", expand=True)

input_scroll = ttk.Scrollbar(
    input_frame,
    orient="vertical",
    command=input_text.yview
)
input_scroll.pack(side="right", fill="y")
input_text.configure(yscrollcommand=input_scroll.set)

# Buttons
button_frame = ttk.Frame(main)
button_frame.pack(fill="x", pady=12)

ttk.Button(
    button_frame,
    text="ถอดรหัส",
    command=decode_html
).pack(side="left", padx=(0, 5))

ttk.Button(
    button_frame,
    text="วางข้อความ",
    command=paste_text
).pack(side="left", padx=5)

ttk.Button(
    button_frame,
    text="คัดลอกผลลัพธ์",
    command=copy_result
).pack(side="left", padx=5)

ttk.Button(
    button_frame,
    text="ล้างทั้งหมด",
    command=clear_all
).pack(side="right")

# Output
ttk.Label(main, text="ผลลัพธ์หลังถอดรหัส").pack(anchor="w", pady=(5, 5))

output_frame = ttk.Frame(main)
output_frame.pack(fill="both", expand=True)

output_text = tk.Text(
    output_frame,
    height=8,
    font=("Consolas", 11),
    wrap="word",
    background="#f0f0f0"
)
output_text.pack(side="left", fill="both", expand=True)

output_scroll = ttk.Scrollbar(
    output_frame,
    orient="vertical",
    command=output_text.yview
)
output_scroll.pack(side="right", fill="y")
output_text.configure(yscrollcommand=output_scroll.set)

# Footer
ttk.Label(
    main,
    text="รองรับ HTML Entity, Numeric Entity และการถอดรหัสซ้อน",
    foreground="gray"
).pack(anchor="w", pady=(10, 0))

root.mainloop()
