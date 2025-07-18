output_frame = Frame(root, bg="#222831", bd=2, relief=GROOVE)
output_frame.pack(pady=20, ipadx=10, ipady=10)

icon_label = Label(output_frame, bg="#222831")
icon_label.grid(row=0, column=0, columnspan=2, pady=10)

weather_main = StringVar()
description = StringVar()
temperature = StringVar()
pressure = StringVar()

info = [
    ("🌦️ Weather", weather_main),
    ("📝 Description", description),
    ("🌡️ Temperature", temperature),
    ("🎯 Pressure", pressure),
]

for i, (label, var) in enumerate(info, start=1):
    Label(output_frame, text=label + ":", **LABEL_STYLE).grid(row=i, column=0, sticky=W, padx=10, pady=5)
    Label(output_frame, textvariable=var, **LABEL_STYLE).grid(row=i, column=1, sticky=W, padx=10)
