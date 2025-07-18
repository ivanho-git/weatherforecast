form_frame = Frame(root, bg="#2C3333")
form_frame.pack(pady=10)

Label(form_frame, text="🌆 Enter City Name:", **LABEL_STYLE).grid(row=0, column=0, padx=10)

city_var = StringVar()
city_entry = Entry(form_frame, textvariable=city_var, **ENTRY_STYLE, width=25, relief=FLAT)
city_entry.grid(row=0, column=1, padx=10)
