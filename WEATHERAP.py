from tkinter import *
from tkinter import ttk
import  requests


def getdata():
    city=cityname.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=9a4a25a970140e7ade2156bf516a135f").json()
    desclabel0.config(text=data["weather"][0]["description"])
    temperaturelabel0.config(text=str(data["main"]["temp"]-273.15))
    pressurelabel0.config(text=data["main"]["pressure"])
    wlabel0.config(text=data["weather"][0]["main"])
    
    


root=Tk()
root.title("WEATHER APP")
root.config(bg="red")
root.geometry("700x700")



name=Label(root,text="WEATHER APP PROJECT",)
name.place(x=25,y=50,height=50,width=450)

cityname=StringVar()
listname=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com=ttk.Combobox(root,text="weather cube app",values=listname,textvariable=cityname)


com.place(x=25,y=120,height=50,width=450)



#category creation


wlabel=Label(root,text="weather climate")
wlabel.place(x=25,y=260,height=50,width=210)

desclabel=Label(root,text="Description")
desclabel.place(x=25,y=330,height=50,width=210)

pressurelabel=Label(root,text="Pressure")
pressurelabel.place(x=25,y=400,height=50,width=210)

temperaturelabel=Label(root,text="temperature")
temperaturelabel.place(x=25,y=470,height=50,width=210)

#creating the data input fields

wlabel0=Label(root,text="")
wlabel0.place(x=250,y=260,height=50,width=210)

desclabel0=Label(root,text="")
desclabel0.place(x=250,y=330,height=50,width=210)

temperaturelabel0=Label(root,text="")
temperaturelabel0.place(x=250,y=470,height=50,width=210)


pressurelabel0=Label(root,text="")
pressurelabel0.place(x=250,y=400,height=50,width=210)


done=Button(root,text="ENTER",command=getdata)
done.place(y=190,height=50,width=100,x=200)
root.mainloop()
