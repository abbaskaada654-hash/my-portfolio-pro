import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class DentalClinicPro:
    def __init__(self, root):
        self.root = root
        self.root.title("نظام إدارة العيادة - المهندس عباس كعدة")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f2f5") # لون خلفية عصري

        # إنشاء قاعدة البيانات
        self.init_db()

        # العنوان الرئيسي
        header = tk.Label(root, text="إدارة بيانات المرضى", font=("Arial", 22, "bold"), bg="#f0f2f5", fg="#1a73e8")
        header.pack(pady=30)

        # حاوية المدخلات (Frame)
        frame = tk.Frame(root, bg="white", padx=20, pady=20, highlightbackground="#dcdcdc", highlightthickness=1)
        frame.pack(pady=10, padx=20, fill="x")

        tk.Label(frame, text="اسم المريض:", bg="white", font=("Arial", 12)).grid(row=0, column=0, sticky="w", pady=5)
        self.name_entry = tk.Entry(frame, font=("Arial", 12), width=30)
        self.name_entry.grid(row=0, column=1, pady=5, padx=10)

        tk.Label(frame, text="رقم الهاتف:", bg="white", font=("Arial", 12)).grid(row=1, column=0, sticky="w", pady=5)
        self.phone_entry = tk.Entry(frame, font=("Arial", 12), width=30)
        self.phone_entry.grid(row=1, column=1, pady=5, padx=10)

        # زر الحفظ بتنسيق أنيق
        save_btn = tk.Button(root, text="حفظ في النظام", command=self.save_patient, 
                             bg="#1a73e8", fg="white", font=("Arial", 12, "bold"), 
                             padx=20, pady=10, cursor="hand2", border=0)
        save_btn.pack(pady=30)

    def init_db(self):
        conn = sqlite3.connect('clinic.db')
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS patients (name TEXT, phone TEXT)")
        conn.commit()
        conn.close()

    def save_patient(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name and phone:
            conn = sqlite3.connect('clinic.db')
            c = conn.cursor()
            c.execute("INSERT INTO patients VALUES (?, ?)", (name, phone))
            conn.commit()
            conn.close()
            messagebox.showinfo("نجاح", f"تم تسجيل المريض {name} بنجاح!")
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("تنبيه", "يرجى إكمال البيانات")

if __name__ == "__main__":
    root = tk.Tk()
    app = DentalClinicPro(root)
    root.mainloop()