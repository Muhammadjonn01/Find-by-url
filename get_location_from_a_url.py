import socket
from tkinter import *
import tkinter
from ip2geotools.databases.noncommercial import DbIpCity

def get_ip_details():
    url_value = url.get()
    ip = socket.gethostbyname(url_value)
    response = DbIpCity.get(ip, api_key='free')
    
    ip_label.configure(text="IP: " + ip)
    city_label.configure(text="City: " + response.city)
    region_label.configure(text="Region: " + response.region)
    country_label.configure(text="Country: " + response.country)

root = Tk()
root.geometry('800x500')
root.title('Find by URL')
root.config(background='black')

label = Label(text='Insert a URL:', font='Times 20', fg='white', background='black')
label.place(x=50, y=45)

url = tkinter.Entry(root, font=('arial', 20, 'bold'),
                      bg='white', fg='black', bd=10, width=30)
url.place(x=200, y=40)

ip_label = Label(root, text="IP: ", font='Times 20', fg='white', background='black')
ip_label.place(x=50, y=100)

city_label = Label(root, text="City: ", font='Times 20', fg='white', background='black')
city_label.place(x=50, y=150)

region_label = Label(root, text="Region: ", font='Times 20', fg='white', background='black')
region_label.place(x=50, y=200)

country_label = Label(root, text="Country: ", font='Times 20', fg='white', background='black')
country_label.place(x=50, y=250)

button = tkinter.Button(root, text="Find", font='Times 20', bg='black', fg='white', command=get_ip_details)
button.place(x=400, y=400)

root.mainloop()