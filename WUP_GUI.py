from tkinter import *
import pyhid_usb_relay
from time import sleep
import serial
import emoji
from tkinter import ttk
from serial.tools import list_ports
import threading
from tkinter import messagebox
import webbrowser


top = Tk()
top.geometry("800x470")


def xmd1041_current():
    J0.configure(state=NORMAL)
    usb1 = K.get()
    J0.delete("1.0", "end")
    serial_port = usb1.split(' -')[0]
    #serial_port = "COM34"
    ser = serial.Serial(serial_port, 115200, timeout=1)
    while True:
        J0.configure(state=NORMAL)
        ser.write(b'MEAS:SHOW?\n')
        myResponse1 = str(ser.readline())
        spl = myResponse1.split("'")[1].split('A')[0]
        #print("spl: " + spl)
        myResponse = str(float(spl))
        #print(myResponse)
        J0.insert(END, myResponse + "A")
        J0.update_idletasks()
        sleep(1)
        J0.delete("1.0", "end")
        J0.configure(state=DISABLED)


def stop_button():
    J0.delete("1.0", "end")
    J0.configure(state=DISABLED)


def current_measure():
    thread = threading.Thread(target=xmd1041_current)
    thread.start()


def rack_restart():
    on = {'cl30': "HFBS0",
          'cl30f': "HFBSf",
          'cl30b': "HFBSb",
          'mute': "HFBSM",
          'obd': "HFBSO"}

    off = {'cl30': "HFBC0",
           'cl30f': "HFBCf",
           'cl30b': "HFBCb",
           'mute': "HFBCM",
           'obd': "HFBCO"}

    #serial_port = "COM22"
    usb1 = H.get()
    serial_port = usb1.split(' -')[0]
    ser = serial.Serial(port=serial_port, baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=1)
    sleep(0.1)
    cmd_off = off.get('cl30', -1)
    ser.write(cmd_off.encode() + b'\n')
    sleep(0.5)
    cmd_off = off.get('cl30f', -1)
    ser.write(cmd_off.encode() + b'\n')
    sleep(0.5)
    cmd_off = off.get('cl30b', -1)
    ser.write(cmd_off.encode() + b'\n')
    sleep(0.5)
    cmd_on = on.get('cl30', -1)
    ser.write(cmd_on.encode() + b'\n')
    sleep(0.5)
    cmd_on = on.get('cl30f', -1)
    ser.write(cmd_on.encode() + b'\n')
    sleep(0.5)
    cmd_on = on.get('cl30b', -1)
    ser.write(cmd_on.encode() + b'\n')
    I.configure(state=NORMAL)
    I.insert(END, "Rack restarted!\n")
    I.configure(state=DISABLED)


def KL30():
    I.configure(state='normal')
    response = var1.get()
    print(response)
    on = {'cl30': "HFBS0",
          'cl30f': "HFBSf",
          'cl30b': "HFBSb",
          'mute' : "HFBSM",
          'obd'  : "HFBSO" }

    off = {'cl30': "HFBC0",
           'cl30f': "HFBCf",
           'cl30b': "HFBCb",
           'mute' : "HFBCM",
           'obd'  : "HFBCO" }

    #serial_port = "COM22"
    usb1 = H.get()
    serial_port = usb1.split(' -')[0]
    ser = serial.Serial(port=serial_port, baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=1)
    sleep(0.1)
    if response == 0:
        cmd_off = off.get('cl30', -1)
        ser.write(cmd_off.encode() + b'\n')
        I.configure(state=NORMAL)
        I.insert(END, "Cl30 is OFF!\n")
        I.configure(state=DISABLED)

    else:
        cmd_on = on.get('cl30', -1)
        ser.write(cmd_on.encode() + b'\n')
        I.configure(state=NORMAL)
        I.insert(END, "Cl30 is ON!\n")
        I.configure(state=DISABLED)


def KL30F():
    response = var2.get()
    on = {'cl30': "HFBS0",
          'cl30f': "HFBSf",
          'cl30b': "HFBSb",
          'mute': "HFBSM",
          'obd': "HFBSO"}

    off = {'cl30': "HFBC0",
           'cl30f': "HFBCf",
           'cl30b': "HFBCb",
           'mute': "HFBCM",
           'obd': "HFBCO"}

    #serial_port = "COM22"
    usb1 = H.get()
    serial_port = usb1.split(' -')[0]
    ser = serial.Serial(port=serial_port, baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=1)
    sleep(0.1)
    if response == 0:
        cmd_off = off.get('cl30f', -1)
        ser.write(cmd_off.encode() + b'\n')
        I.configure(state=NORMAL)
        I.insert(END, "Cl30F is OFF!\n")
        I.configure(state=DISABLED)
    else:
        cmd_on = on.get('cl30f', -1)
        ser.write(cmd_on.encode() + b'\n')
        I.configure(state=NORMAL)
        I.insert(END, "Cl30F is ON!\n")
        I.configure(state=DISABLED)


def KL30B():
    response = var3.get()
    on = {'cl30': "HFBS0",
          'cl30f': "HFBSf",
          'cl30b': "HFBSb",
          'mute': "HFBSM",
          'obd': "HFBSO"}

    off = {'cl30': "HFBC0",
           'cl30f': "HFBCf",
           'cl30b': "HFBCb",
           'mute': "HFBCM",
           'obd': "HFBCO"}

    #serial_port = "COM22"
    usb1 = H.get()
    serial_port = usb1.split(' -')[0]
    ser = serial.Serial(port=serial_port, baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=1)
    sleep(0.1)
    if response == 0:
        cmd_off = off.get('cl30b', -1)
        ser.write(cmd_off.encode() + b'\n')
        I.configure(state=NORMAL)
        I.insert(END, "Cl30B is OFF!\n")
        I.configure(state=DISABLED)
    else:
        cmd_on = on.get('cl30b', -1)
        ser.write(cmd_on.encode() + b'\n')
        I.configure(state=NORMAL)
        I.insert(END, "Cl30B is ON!\n")
        I.configure(state=DISABLED)


def OBD():
    response = var4.get()
    on = {'cl30': "HFBS0",
          'cl30f': "HFBSf",
          'cl30b': "HFBSb",
          'mute': "HFBSM",
          'obd': "HFBSO"}

    off = {'cl30': "HFBC0",
           'cl30f': "HFBCf",
           'cl30b': "HFBCb",
           'mute': "HFBCM",
           'obd': "HFBCO"}

    #serial_port = "COM22"
    usb1 = H.get()
    serial_port = usb1.split(' -')[0]
    ser = serial.Serial(port=serial_port, baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=1)
    sleep(0.1)
    if response == 0:
        cmd_off = off.get('obd', -1)
        ser.write(cmd_off.encode() + b'\n')
        I.configure(state=NORMAL)
        I.insert(END, "OBD is OFF!\n")
        I.configure(state=DISABLED)
    else:
        cmd_on = on.get('obd', -1)
        ser.write(cmd_on.encode() + b'\n')
        I.configure(state=NORMAL)
        I.insert(END, "OBD is ON!\n")
        I.configure(state=DISABLED)


def Standard_Pulse():
    delay = 0.5
    relay = pyhid_usb_relay.find()
    relay.toggle_state(2)
    sleep(delay)
    relay.toggle_state(2)
    I.configure(state=NORMAL)
    I.insert(END, "500ms Pulse Triggered\n")
    I.configure(state=DISABLED)
    #print("Triggered Pulse: " + "500ms")


def Trigger():
    length = B.get()
    delay = int(length)/1000
    relay = pyhid_usb_relay.find()
    relay.toggle_state(1)
    sleep(delay)
    relay.toggle_state(1)
    I.configure(state=NORMAL)
    I.insert(END, length + "ms Pulse Triggered\n")
    I.configure(state=DISABLED)
    #print("Triggered Pulse: " + length + "ms")


Frame1 = Frame(top, highlightbackground="black", highlightthickness=1, width=375, height=120, bd=0)
Frame1.pack()
Frame1.place(x=20, y=140)
Frame2 = Frame(top, highlightbackground="black", highlightthickness=1, width=375, height=150, bd=0)
Frame2.pack()
Frame2.place(x=20, y=270)
Frame3 = Frame(top, highlightbackground="black", highlightthickness=1, width=375, height=130)
Frame3.pack()
Frame3.place(x=20, y=0)


##########################-------------WUP_Buttons---------------####################
A0 = Label(top, text="[ What's the worst that can happen? ]", width=40, background="light blue", bd=3, borderwidth=2)
A0.place(x=60, y=145)

A = Button(top, text="500ms_Pulse", command=Standard_Pulse, width=28, fg='black')
A.place(x=100, y=220)

B = Spinbox(top, from_=0, to=1000, width=10)
B.place(x=100, y=182)

C = Button(top, text="Trigger(in ms)", width=14, fg='black', command=Trigger)
C.place(x=200, y=178)


##########################-------- Rack_control----------------------------###################
D0 = Label(top, text="[ Tak! Tak! Tak! ]", width=40, background="light blue", bd=3)
D0.place(x=60, y=280)

D = Button(top, text="Rack_Restart", command=rack_restart, width=28, fg='black')
D.place(x=100, y=350)

var1 = IntVar(value=1)
E = Checkbutton(top, text="K30", command=KL30, variable=var1)
E.place(x=150, y=380)

var2 = IntVar(value=1)
E = Checkbutton(top, text="K30F", command=KL30F, variable=var2)
E.place(x=200, y=380)

var3 = IntVar(value=1)
E = Checkbutton(top, text="K30B", command=KL30B, variable=var3)
E.place(x=250, y=380)

var4 = IntVar(value=1)
F = Checkbutton(top, text="OBD", command=OBD, variable=var4)
F.place(x=100, y=380)

G = Label(top, text='I-BOX COM:')
G.place(x=60, y=320)

Ibox_com = StringVar(value='Set I-Box COM Port')
com_port = list_ports.comports()
H = ttk.Combobox(top, width=30, textvariable=Ibox_com, values=com_port)
H.place(x=135, y=320)


####################--------------text Box-----------------###################################
I0 = Label(top, text="Console:", width=10, background="light blue")
I0.place(x=420, y=0)
I = Text(top, height=25, width=45, state=DISABLED)
I.place(x=420, y=20)


#######################----------------Multimeter-------------############################
K0 = Label(top, text="Multimeter COM: ", width=13, background="light blue")
K0.place(x=25, y=20)
multimeter_com = StringVar(value="Select Multimeter COM port")
K = ttk.Combobox(top, width=25, textvariable=multimeter_com, values=com_port)
K.place(x=130, y=20)
J = Label(top, text="Current :", width=7, background="light blue")
J.place(x=25, y=80)
J0 = Text(top, height=1.5, width=10, state=DISABLED, foreground="green", font=('courier', 15, 'bold'))
J0.place(x=90, y=67)

multimeter_start = Button(top, text="Start",width=20, command=current_measure)
multimeter_start.place(x=225, y=75)
# multimeter_stop = Button(top, text="Stop", width=10, command=stop_button)
# multimeter_stop.place(x=200, y=95)


############################--------------Info----------------#############################
def message_box():
    # messagebox.showinfo("Information",
    #                     "Version:\n0.1\n\nMore info:\n<Link>\n\nContact: Anuj Sharma, Anuj.sharma@partner.bmw.de\n\n")
    message_window = Toplevel()
    message_window.geometry("380x210")
    message_window.title("Information")
    label1 = Label(message_window, text="Version:", background="light blue", font=('courier', 8, 'bold'))
    label1.pack()
    label1.place(x=20, y=15)
    label10 = Label(message_window, text="v0.1", font=('courier', 8))
    label10.pack()
    label10.place(x=90, y=15)
    label2 = Label(message_window, text="More info:", background="light blue", font=('courier', 8, 'bold'))
    label2.pack()
    label2.place(x=20, y=65)
    label20 = Button(message_window, text="Repository Link", command=link, font=('Helvetica', 8))
    label20.pack()
    label20.place(x=110, y=60)
    label3 = Label(message_window, text="Contact:", background="light blue", font=('courier', 8, 'bold'))
    label3.place(x=20, y=115)
    label30 = Label(message_window, text="Anuj Sharma (Anuj.sharma@partner.bmw.de)", font=('Helvetica', 8, 'underline'))
    label30.place(x=90, y=115)
    ok_button = Button(message_window, text="OK", command= message_window.destroy, width=10)
    ok_button.pack()
    ok_button.place(x=140, y=175)


def link():
    webbrowser.open_new(r"https://cc-github.bmwgroup.net/anujsharmapartner/What_are_those")


info_box = Button(top, text="INFO", width=10, command=message_box)
info_box.place(x=350, y=430)


title = emoji.emojize(':high_voltage:') + emoji.emojize(':high_voltage:') + " Somewhere between 0-13V, We Exist! " + emoji.emojize(':high_voltage:') + emoji.emojize(':high_voltage:')
top.title(title)
top.iconbitmap(r"C:\00_Tools\00_ICON\business_construction_avatar_engineer_man_employee_person_worker_icon_262353.ico")
top.mainloop()
