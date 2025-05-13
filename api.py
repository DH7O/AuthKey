import tkinter as tk
import random
import string
import requests
import pyperclip  # مكتبة لنسخ النص إلى الحافظة

# دالة لتوليد المفتاح العشوائي
def generate_key():
    length = int(entry_length.get())  # الحصول على طول المفتاح من المدخل النصي
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    label_key.config(text=key)  # عرض المفتاح في الواجهة

# دالة لإرسال المفتاح إلى API والتحقق من صلاحية المفتاح
def verify_key():
    key = label_key.cget("text")  # الحصول على المفتاح المعروض في الواجهة
    if not key:
        result_label.config(text="يرجى توليد مفتاح أولاً.", fg="red")
        return

    url = "https://authkey.onrender.com/verify_key"  # ضع هنا رابط الـ API الفعلي
    payload = {'key': key}

    try:
        response = requests.post(url, data=payload)  # إرسال الطلب إلى API
        if response.status_code == 200:
            result_label.config(text="تم التحقق من المفتاح بنجاح!", fg="green")
        else:
            result_label.config(text="فشل التحقق من المفتاح.", fg="red")
    except Exception as e:
        result_label.config(text=f"حدث خطأ: {e}", fg="red")

# دالة لنسخ المفتاح إلى الحافظة
def copy_key():
    key = label_key.cget("text")  # الحصول على المفتاح المعروض في الواجهة
    if key:
        pyperclip.copy(key)  # نسخ المفتاح إلى الحافظة
        result_label.config(text="تم نسخ المفتاح إلى الحافظة!", fg="green")
    else:
        result_label.config(text="يرجى توليد مفتاح أولاً.", fg="red")

# إنشاء نافذة رئيسية
root = tk.Tk()
root.title("مولد المفاتيح - Flash Key Manager")
root.geometry("500x400")  # تحديد حجم النافذة
root.config(bg="#f5f5f5")

# عنوان البرنامج
title_label = tk.Label(root, text="Flash Key Manager", font=("Arial", 18, "bold"), bg="#4CAF50", fg="white", pady=20)
title_label.pack(fill='x')

# مدخل لطول المفتاح
label_length = tk.Label(root, text="طول المفتاح:", font=("Arial", 12), bg="#f5f5f5")
label_length.pack(pady=5)
entry_length = tk.Entry(root, font=("Arial", 12))
entry_length.pack(pady=5)
entry_length.insert(0, "16")  # قيمة افتراضية للطول

# زر لتوليد المفتاح
generate_button = tk.Button(root, text="توليد المفتاح", font=("Arial", 14), command=generate_key, bg="#4CAF50", fg="white", width=20, height=2, relief="raised", bd=4)
generate_button.pack(pady=20)

# تسمية لعرض المفتاح المولد
label_key = tk.Label(root, text="", font=("Courier", 14), bg="#f5f5f5", fg="black", width=40, height=2, relief="solid", anchor="w", padx=10)
label_key.pack(pady=10)

# زر للتحقق من صلاحية المفتاح
verify_button = tk.Button(root, text="التحقق من صلاحية المفتاح", font=("Arial", 12), command=verify_key, bg="#FF9800", fg="white", width=20, height=2, relief="raised", bd=4)
verify_button.pack(pady=10)

# زر لنسخ المفتاح
copy_button = tk.Button(root, text="نسخ المفتاح", font=("Arial", 12), command=copy_key, bg="#2196F3", fg="white", width=20, height=2, relief="raised", bd=4)
copy_button.pack(pady=10)

# تسمية لعرض النتيجة بعد التحقق أو النسخ
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f5f5f5", fg="black")
result_label.pack(pady=20)

# تشغيل التطبيق
root.mainloop()

