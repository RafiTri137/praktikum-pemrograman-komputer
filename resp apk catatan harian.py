import tkinter as tk
from tkinter import messagebox, scrolledtext
import datetime

# -------------------------
# Fungsi untuk menyimpan catatan
# -------------------------
def simpan_catatan():
    isi = entry_catatan.get("1.0", tk.END).strip()
    
    if isi == "":
        messagebox.showwarning("Peringatan", "Catatan tidak boleh kosong!")
        return
    
    tanggal = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    with open("diary.txt", "a", encoding="utf-8") as file:
        file.write(f"[{tanggal}] {isi}\n")
    
    entry_catatan.delete("1.0", tk.END)
    messagebox.showinfo("Sukses", "Catatan berhasil disimpan!")

# -------------------------
# Fungsi untuk melihat catatan
# -------------------------
def lihat_catatan():
    try:
        with open("diary.txt", "r", encoding="utf-8") as file:
            isi = file.read()
    except FileNotFoundError:
        isi = "Belum ada catatan tersimpan."

    # Jendela baru untuk menampilkan catatan
    window_catatan = tk.Toplevel(root)
    window_catatan.title("Semua Catatan")
    window_catatan.geometry("450x400")

    txt = scrolledtext.ScrolledText(window_catatan, width=50, height=20, wrap=tk.WORD)
    txt.pack(padx=10, pady=10)
    txt.insert(tk.END, isi)
    txt.configure(state="disabled")

# -------------------------
# GUI Utama
# -------------------------
root = tk.Tk()
root.title("Aplikasi Catatan Harian")
root.geometry("400x300")

label = tk.Label(root, text="Tulis Catatan Anda:", font=("Arial", 12))
label.pack(pady=5)

entry_catatan = scrolledtext.ScrolledText(root, width=40, height=8, wrap=tk.WORD)
entry_catatan.pack(pady=5)

btn_simpan = tk.Button(root, text="Simpan Catatan", font=("Arial", 10), width=20, command=simpan_catatan)
btn_simpan.pack(pady=5)

btn_lihat = tk.Button(root, text="Lihat Semua Catatan", font=("Arial", 10), width=20, command=lihat_catatan)
btn_lihat.pack(pady=5)

root.mainloop()
