import tkinter as tk

root = tk.Tk()
root.title("PDF-Excel Arama Aracı")

pdf_label = tk.Label(root, text="PDF dosyası:")
pdf_label.grid(row=0, column=0, padx=10, pady=10)
pdf_entry = tk.Entry(root, width=50)
pdf_entry.grid(row=0, column=1, padx=10, pady=10)
pdf_button = tk.Button(root, text="Gözat")
pdf_button.grid(row=0, column=2, padx=10, pady=10)

excel_label = tk.Label(root, text="Excel dosyası:")
excel_label.grid(row=1, column=0, padx=10, pady=10)
excel_entry = tk.Entry(root, width=50)
excel_entry.grid(row=1, column=1, padx=10, pady=10)
excel_button = tk.Button(root, text="Gözat")
excel_button.grid(row=1, column=2, padx=10, pady=10)

column_label = tk.Label(root, text="Sütun:")
column_label.grid(row=2, column=0, padx=10, pady=10)
column_entry = tk.Entry(root, width=50)
column_entry.grid(row=2, column=1, padx=10, pady=10)

term_label = tk.Label(root, text="Aranan kelime:")
term_label.grid(row=3, column=0, padx=10, pady=10)
term_entry = tk.Entry(root, width=50)
term_entry.grid(row=3, column=1, padx=10, pady=10)

arananYer_label = tk.Label(root, text="diger aramalar (örn: n):")
arananYer_label.grid(row=4, column=0, padx=10, pady=10)
arananYer_entry = tk.Entry(root, width=50)
arananYer_entry.grid(row=4, column=1, padx=10, pady=10)

result_label = tk.Label(root, text="Sonuçlar:")
result_label.grid(row=5, column=0, padx=10, pady=10)
result_text = tk.StringVar()
result_output = tk.Label(root, textvariable=result_text, width=60, height=10, anchor="nw", justify="left")
result_output.grid(row=5, column=1, padx=10, pady=10)

search_button = tk.Button(root, text="Ara")
search_button.grid(row=6, column=1, padx=10, pady=10)

root.mainloop()