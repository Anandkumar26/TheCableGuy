#!/usr/bin/env python
#==============================================================================
#Title           :cableGuy.py
#Description     :The Cable Guy
#Author          :Tarun Thakur[tarun.thakur@nectechnologies.in]
#                :Manik Sidana[manik.sidana@nectechnologies.in]
#                :Sridhar Rao[sridhar.rao@nectechnologies.in]
#                :Swarvanu Sengupta[swarvanu.sengupta@nectechnologies.in]
#Date            :30 October, 2014
#Version         :1.0
#Usage           :sudo python cableGuy.py <ip-address> <port-number>
#Notes           :Install Python 2.7.3 to run this script.
#Python Version  :2.7.3
#Dependencies    :sudo apt-get install graphviz libgraphviz-dev python-dev
#                :sudo apt-get install python-imaging-tk
#                :sudo apt-get install python-tk
#                :pip install pylint pygraphviz
#==============================================================================

import socket
import json
import os
import errno
import sys
import re
import httplib2
import pygraphviz
import json
import httplib2
import pygraphviz as pgv
import tkMessageBox
#from pygraphviz import *
from Tkinter import *
from tkFileDialog import *
from collections import *
from functools import partial
import Image, ImageTk
import xml.etree.ElementTree as ET

class Welcome():
    def __init__(self,master):
        self.master = master
        self.master.geometry('800x250+100+200')
        self.master.title('THE CABLE GUY')
        self.title = PhotoImage(data="""
                    R0lGODlhDwI/APcAAAAAAAAAMwAAZgAAmQAAzAAA/wArAAArMwArZgArmQArzAAr/wBVAABVMwBV
                    ZgBVmQBVzABV/wCAAACAMwCAZgCAmQCAzACA/wCqAACqMwCqZgCqmQCqzACq/wDVAADVMwDVZgDV
                    mQDVzADV/wD/AAD/MwD/ZgD/mQD/zAD//zMAADMAMzMAZjMAmTMAzDMA/zMrADMrMzMrZjMrmTMr
                    zDMr/zNVADNVMzNVZjNVmTNVzDNV/zOAADOAMzOAZjOAmTOAzDOA/zOqADOqMzOqZjOqmTOqzDOq
                    /zPVADPVMzPVZjPVmTPVzDPV/zP/ADP/MzP/ZjP/mTP/zDP//2YAAGYAM2YAZmYAmWYAzGYA/2Yr
                    AGYrM2YrZmYrmWYrzGYr/2ZVAGZVM2ZVZmZVmWZVzGZV/2aAAGaAM2aAZmaAmWaAzGaA/2aqAGaq
                    M2aqZmaqmWaqzGaq/2bVAGbVM2bVZmbVmWbVzGbV/2b/AGb/M2b/Zmb/mWb/zGb//5kAAJkAM5kA
                    ZpkAmZkAzJkA/5krAJkrM5krZpkrmZkrzJkr/5lVAJlVM5lVZplVmZlVzJlV/5mAAJmAM5mAZpmA
                    mZmAzJmA/5mqAJmqM5mqZpmqmZmqzJmq/5nVAJnVM5nVZpnVmZnVzJnV/5n/AJn/M5n/Zpn/mZn/
                    zJn//8wAAMwAM8wAZswAmcwAzMwA/8wrAMwrM8wrZswrmcwrzMwr/8xVAMxVM8xVZsxVmcxVzMxV
                    /8yAAMyAM8yAZsyAmcyAzMyA/8yqAMyqM8yqZsyqmcyqzMyq/8zVAMzVM8zVZszVmczVzMzV/8z/
                    AMz/M8z/Zsz/mcz/zMz///8AAP8AM/8AZv8Amf8AzP8A//8rAP8rM/8rZv8rmf8rzP8r//9VAP9V
                    M/9VZv9Vmf9VzP9V//+AAP+AM/+AZv+Amf+AzP+A//+qAP+qM/+qZv+qmf+qzP+q///VAP/VM//V
                    Zv/Vmf/VzP/V////AP//M///Zv//mf//zP///wAAAAAAAAAAAAAAACH5BAEAAPwALAAAAAAPAj8A
                    AAj/APcJHEiwoMGDCBMqXMiwocOHECNKVKgsU6ZJk8SgQTMpE7GJIEOKHEmypMmTCJURuzgJjcaO
                    xJShnEmzps2bOHPaJIbmBoCfQIMKvYHmo86jSJMqfZhJTAyhUIOKmSRzqdWJmaJq3cq1a9AYAr2K
                    HQtUDNmzk64KVGb2LNQYVBO6nUu3rtCndrm2zRs1rdpMeO3eiCuXr+HDZIlNQszXQFjGY/dC9rsU
                    DWQAMdDUM3i5c93Aly13zmSV7eXMVQt6Xn3YIuuzKwRKfg20aefUSBezjkF64GzamH9ftn1bOF/c
                    Ok3vNuobOFTjtMHqds7VsWzqAKpCp7s0K/XU209f/1/dO/xc7ZArO0dj0Hz6fe4hg93nHbvW+eNp
                    M4d/OAbynPEh1lt+r+HHX2eUHXgYbgFytcJ/NykD2mtiHNSgXf41R10M0Ag0nX1REVTfbh0ONCKG
                    SREDIgD7nbgaeyZ6hpuLnxVE41w3JHXjiwftKJ+I2FUokI/Y4aeicwZsts+Rh+WoE5HkDcQkcDBO
                    eVlVVvIVm0BZoqjTh84JSVCXqzlJJmtCgrniT9ZBKR80bp7l5E1xdmZUnYh1RFtFnYGFp1hz2iSa
                    fTDGaN8NfyJWYaKebbnihWMlONOZ94lhETHQbJZpRU1NqFVvawLnk2eDTnaTml1l5pEyqanU1Kh6
                    qf8W6prEEHODGLjmquuuum4VA6/A8grjo54NOJMyZPGmpEOZoLHCVkbNWuBqkIol6Ul1irEfQ8pM
                    AqtQhT4mrX0QOrRVuBIR80mt667kKru1ruqRuyvBW29F8b7rqr7zZvKuuvHG1O+/5ZLkaVRiFNyQ
                    MqXWxmW77fpbL8D3DjxxxALnO7G/8trbMb3zYowvvTFlPLLEIQd88r/tQgNyxi9T/DHKtZZI01jo
                    pjubmA97zLLKFqdcscb9vrzyxUAT7THMKIu0Fc9qRQ2gVxmalMm320qt9dY2HSwU1CPZ+lPOXJet
                    0LknOWvACmsbAPZCmMX9lMJZPWW33HjfTfZMUL7/TZJyxkJk1t0GZC3RYncnjlkMiCqckuIGhlR3
                    3pTr/aVXgZ+EkUJqs8223wll0rbngR7kE+SOCwRNDJ6PbkDqDz2d9nMRRaVww5HphDlObGW+cFSl
                    T4S7XrBLGSJJw3sFuknQeFV8Tbgvf5CawRdEZuQIee17SGib9Jv0nEGlMKrK50S+w2YXZNzzCEG6
                    /UHIQlXS+bHiFB77NH0fkYvYG3Rj9QQxDvgg0jytDNAh0aud+DhHl72dpCsO5Fr3QpK8rhSvSyWp
                    IFci+LeuGE4pCYQI9RryraBcy1BvuZlWOCg4qACwMEIZH10OCBIN0vAqGhxJtQDgkPgJZX4ztN8G
                    sbf2mxcihH8O0R78toK/hsjOJCGM3QITosEJ1qQr6TvIs7byvoZU8YkL8WFQMthAnHClf1aJIgJT
                    +DutHISJV1zhSfQHkah80ENB3AlXurg1Im0JJDvkIUMwSBL6gZEm9GtiTej4EDWh8SDXK0gJgcLC
                    idTjkCNRoxOniBDc8aZeHgnlvW4ySaA8smyljCEFXQjKixggKnzchxiBQsa7iPKWo+waJqOmSYa4
                    yIgGSZ6YhP95Eyvq0IUKVGVCRhg1rtyRa7PUCjAVwkiCwHKQxxsJM9XCFUUuEpkiZONDUkkaMlmn
                    JgVE2Oy+lsyg3I52f/FVFtszFm/2ch+eOmFBPpFNkdwTKTuaZlL+uUxxOuSSn9rKsuIYlUo6pJqb
                    FMozHRm18zm0mTgDJDhlJRR9jqmfIaGoWqATy6RA1JcG7aFbSuo0A65TKu0EyjuHEjWvAWCh8xwe
                    YED6kF6iKpbRFGQmN2qVV7rRbATtJFGZQpaLck+O3lsqQ2ynkG1ahSvzLMgWf0gjlqoPnmsxTkMI
                    qU2pJkWeZitiREQqEfec0iQIVScUnwMNVslSGXWtR11lYtf/oM70K3pVRj3wKljCepMh6QRrVmnk
                    l6i8Val3cckNtqrYhAS1loDNK2EHu1ebBPUnN9RJUnuUUojY9CePNYkxRRJIZ1aVOzU5k1OtUkr0
                    QOWZ7asL7MgqEkMelSZn8uhVTroQtkoksXY8CnJhOtfbMHAuNtmRV0sjV1lWt6dlbOMPkQdbmkg3
                    faM1iFXTxcWzQrUkrYVjQaFbkx3hVmrCwU1tI7LD9y6JpxPxLX5L4l6SNIsjG2kJgAcs4JZASK0Q
                    QaI/r5uTuFZ2wc6lYndncj77cjOlXZrtF8u7EH7Kj7vsRaR6RUJZsvguvAXxJEmoat6GztEzE6WL
                    zVCyo09k/3UfqKIKq1i13J/QNy+O421IZdxeDovktEYO4IOLW1qJsFi5u1xlhCHrluhC68Z8me6G
                    0WrZ/UZky9v17pVHguRPHQTFQKLpSJ58lNWGJL1akeFccGq1JJuNUV9poVBWcKs+n7aLQgaJfqFC
                    55KcabrZo4vvENzIJsf0J4eViIPZ2VyYZmofl860pjTF5mAiU6/7ALWoZ4wS2WY1lWd53j1vdMrL
                    gjgoORp1qDsE6pp8FgChPUiZr+lpSmNXzS1VJlLcrFFgm+u2r70LRhkMzcPQkLiyPJhCAp1fR7dZ
                    mgZT9PSsnVtlr5mT12a2lJkrRWGfecnD3so84ezjNfraf/+dJoirh/rupWCVzNqG94cf4qlcFySo
                    hS7meUkCbRi6M9l5VguqI81QwxyQ0W8Et/W8HE5vD3fMIdk1VHzXJRp2dcUS512Ua4hug8v0ubCO
                    GnSEm0bGnHMhBPVrQjwcZginXC3n8zdBNC6U7Q08dHEGubl193PWmvVsyF5vwq9y65dvrcTthjmv
                    F1JwaSeE2ofjdk5uLVSQZGpTstRrPb5rIWkWDBrGSe1UQ25Gl1a6LI/ODspNaRGLdMTudZ8EqR+I
                    ca0xtiGTRq0X31L3vKey1bAsvOIL/1e65/3xdt+7SYzaF8/aeSBc/+TXV4JqACD6IIGXe4uhMltq
                    lhwh8SZXyKCTnr+tOD1q821IfBmSXuFSqivCXb1EbUI/yZPk0BJGjEAjenCk3Frn56732oee4rp8
                    3iGUev6xxJ0S6hMEzFF5/b/t0kXsB0X63Krf9M2cEJ47iHmp/xe4i6NqbOIDJcb5rslpGU7w9Cd6
                    3wlpLW5vz5XcO5+UrjUpl1cQ5pd99DcQ9tdwyjducFdHbDcQ3vd+dHJGWuNY+7N+wUcXLGdddSFc
                    EfgTFjYRlJIk4zd1+ScYAWdJUZGCChgUpXeCC4h0zKd6/6d+bncVP+VkUPFH3TYXJcV/W+EGCLdS
                    OHFaHFJqA2gQEuKDKjSDNhF6oPVSDVhuxUdlbhGCWNEVyNdI//FbEKFTcxcZxUNzc+GBdYGFEsF1
                    mIESt+ZVO0U14Ac3D2gTxFZtAMA2UeiAa3NyoRMDfviHgBiIgRiHDYFkw5eGohE4yPIURrUCL1gP
                    T7FFr7Q8k/8giDFgAIJ4K4gmIZdoiYKIiX/YRYDhiaToh4RIe13xICYBfBBREU5xF4NxgAkBiqBY
                    NVB2gzeWi2FENbI4JN9yiroYjOG2RyVBhj0njOlThw1xKcwISisRSswYjdDojLcUSvgSjc+4eNqI
                    jRbRizSoPL73EMqxe/TBjdSYjdtYd+hIjdCojtJYeK3UjNK4jovXSuioePH4jO4yje+YjvAYjd6I
                    eYCChgbBivrIjfJoj7i0kPx4Ee3oj/94kAc5j+4IflCIa8EWJJ6xgSDReVLRRMRBfuOyGgVIFuwG
                    FRwpPGPBGxPhMiQlLiPpHASJgEXngPZxksdoE1DnK5ZSMCr/gQa7Fi0xeRkeaRcf6BUpORENQhQx
                    YVkXMVm7sw9DSR0ziWkjxyz2wSF4thWHOBFqeEY3wDh+yIT0ASJFsSdA6BZ+QpQ5UZKm5Id7SJZb
                    WReIsiZbqIzLuCFVMZdDwYIl0WMyiUJUMiSssZc/QpiIoXYjUZRRgpjOMR98ORdbeJFb6JivYSP9
                    YXw7SRvGEpliES6eCW6hGTme2ZXHtCKd+ZhpFiZCR3r1Bxz7wW6qiBSMCRmxqZoaMhxKhhi3aRiz
                    eRSheRbGgpNnBB5F0pox+BDEaUEE0hh+iRK6ZxjGuSHNCRnlcSXVmRdKsYTYMSDLiUUKQp0ZCS42
                    9x3fGZAKm1EPtWkXBpAgRykY39lz79lN56kUwekVRjGfdRGfXqF9KoWLOniTxbIUYtMZRRE+U5mY
                    L7KRVnGfkbUfCQqbT4WBE0EsCMJ07OY2dxShCuoZ8ZmUk7KeqWIpqMehrFGVyJii7SUGlGeShKGi
                    MBqjChGSyTIYKCqjOJqjNzZ2GXGJlOWHg+EvOjqkRIppK4ErYQmIuNIR6FmkBBEQADs=
                    """)
        pl0=Label(self.master) # first placeholder
        pl0.grid(row=0)
        self.label = Label(self.master,image=self.title).grid(row=1,column=2,columnspan=2,padx=150)
        pl1=Label(self.master) # first placeholder
        pl1.grid(row=2)
        self.welcome = """Dear Administrator, I'm 'The Cable Guy'. I will help you in checking for any missing cable connections. Please begin by clicking the START button """
        self.label = Label(self.master,text=self.welcome,anchor=W, justify=LEFT,wraplength=550, font=("Times", 12)).grid(row=5,column=2,columnspan=2,padx=150,sticky=E+W)
        pl2=Label(self.master) # first placeholder
        pl2.grid(row=7)
        self.button = Button(self.master, text="START",font=("Times", 16),fg='green',command=self.gototopologyinput).grid(row=8,column=2)
        self.button2 = Button(self.master, text="QUIT",font=("Times", 16),fg='red',command=self.finish).grid(row=8,column=3)

    def gototopologyinput(self):
        root2=Toplevel(self.master)
        adminUI=Admininput(root2)

    def finish(self):
        self.master.destroy()

class Admininput():
    def __init__(self,master):
        self.filename = StringVar()
        self.ipvalid = False
        self.ip = StringVar()
        self.netType = IntVar()  # Added new int for holding network type
        self.ctype = StringVar()
        self.cport = StringVar()
        self.master=master
	self.master.grab_set()
        self.master.geometry('800x250+500+200')
        self.master.title('Administrator Inputs')

        self.topofile = Label(self.master, text="Choose Reference-Topology File").grid(row=0,column=1, sticky=W)
        self.filenamebox = Entry(self.master, width=50,textvariable=self.filename).grid(row=0,column=2)
        self.button = Button(self.master, text="Browse", command=self.loadfile, width=10).grid(row=0,column=3)

        self.controlleripname = Label(self.master, text="Enter the IP Address of the Controller").grid(row=1,column=1,sticky=W)
        self.controllerip = Entry(self.master,width=50,textvariable=self.ip).grid(row=1,column=2)

        self.controllerportname = Label(self.master, text="Enter the Port Number of the Controller").grid(row=2,column=1, sticky=W)
        self.controllerport = Entry(self.master,width=50,textvariable=self.cport).grid(row=2,column=2)

        self.networktypename = Label(self.master, text="Please select the Network-Type").grid(row=3,column=1, sticky=W)
  
        networktype1 = Radiobutton(self.master, text="Physical", variable=self.netType, value=1, command=self.PhyControllerOption)
        networktype1.grid(row=3,column=2,sticky=EW)
  
        networktype2 = Radiobutton(self.master, text="Overlay", variable=self.netType, value=2, command=self.VirControllerOption)
        networktype2.grid(row=3,column=3,sticky=W)

        self.controllertypename = Label(self.master, text="Please select the Controller-Type").grid(row=4,column=1, sticky=W)

        self.sanitychecklabel = Label(self.master, text="Sanity Checking").grid(row=5,column=1, sticky=W)
        self.sanitycheckbutton = Button(self.master, text="Check", command=self.sanitycheck)
        self.sanitycheckbutton.grid(row=5,column=2, sticky=EW)

        self.verifybutton = Button(self.master, state=DISABLED, text="Verify Cable Connectivity", command=self.verify)
        self.verifybutton.grid(row=6,column=2, sticky=EW)
        self.backbutton = Button(self.master, text="Back", command=self.finish).grid(row=6,column=3, sticky=EW)


    def loadfile(self):
        self.fname = askopenfilename(parent=self.master,filetypes=(("DOT files", "*.dot"),
                                           ("All files", "*.*")))
        self.filename.set(self.fname)


    def finish(self):
        self.master.destroy()


    def PhyControllerOption(self):
        self.ctype.set("ODL")
        controllertype1 = OptionMenu(self.master,self.ctype, "ODL","PFC","RYU")
        controllertype1.grid(row=4,column=2,sticky=W)
        controllertype1.configure(takefocus=1)


    def VirControllerOption(self):
        self.ctype.set("ODL-YAON")
        controllertype2 = OptionMenu(self.master,self.ctype, "ODL-YAON","ODL-DEFAULT")
        controllertype2.grid(row=4,column=2,sticky=W)
        controllertype2.configure(takefocus=1)


    def sanitycheck(self):
        self.ipvalid = False
        self.portvalid = False
        if self.check_ipv4_address() == 0:
            self.ipvalid = True
	if self.check_port_number() == 0:
            self.portvalid = True

	sane=True

        if self.filename.get() == "":
            #self.sanityval.set("NO FILE NAME ENTERED,")
            tkMessageBox.showerror("The Cable Guy", "Filename is not entered.")
            sane=False
        elif self.ip.get() == "":
            #self.sanityval.set(self.sanityval.get() +" " + "NO IP ADDRESS SET,")
            tkMessageBox.showerror("The Cable Guy", "IP Address is not entered.")
            sane=False
        elif self.ipvalid == False:
            #self.sanityval.set(self.sanityval.get() +" " + "INVALID IP,")
            tkMessageBox.showerror("The Cable Guy", "Invalid IP address.")
            sane=False
        elif self.cport.get() == "":
            #self.sanityval.set(self.sanityval.get() +" " + "PORT NUMBER NOT PROVIDED,")
            tkMessageBox.showerror("The Cable Guy", "Port number is not entered.")
            sane=False
        elif self.portvalid == False:
            #self.sanityval.set(self.sanityval.get() +" " + "INVALID PORT,")
            tkMessageBox.showerror("The Cable Guy", "Invalid Port number.")
            sane=False
        elif self.ctype.get() == "":
            #self.sanityval.set(self.sanityval.get() +" " + "CONTROLLER TYPE NOT CHOSEN,")
            tkMessageBox.showerror("The Cable Guy", "Controller Type is not selected.")
            sane=False
        elif self.ctype.get() != "ODL" and self.ctype.get() != "ODL-YAON":
            tkMessageBox.showerror("The Cable Guy", "Only ODL Controller is supported.")
            sane=False
        	
        if sane == True:
            #self.sanityval.set("All the Values are Fine")
            self.verifybutton.config(state=NORMAL)


    #### Function to validate Port number
    def check_port_number(self):
        try:
            portnum = int(self.cport.get())
            if portnum < 1 or portnum >= 65536:
                return 1
        except Exception:
            return 1
        return 0


    #### Function to validate IP address
    def check_ipv4_address(self):
	addr = self.ip.get()
        try:
            fields = re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", addr)
            if fields is None:
                return 1
            array = []
            for value in fields.groups():
                array.append(int(value))
            for value in array:
                if value > 255 or value < 0:
                    return 1
            return 0
        except Exception as err:
            return 1


    #### Function to print ODL ports summary
    def computeODLSummary(self, ODLDict):
        #### Return without printing anything if ODL dictioanry is blank i.e, no extra ports in ODL
        if not ODLDict:
            return
        OdlSummary = '\n\n'
        OdlSummary = OdlSummary + '-----------------------------------------------------------------------------------------------------'
        OdlSummary = OdlSummary + 'Port connections from ODL [Not present in Admin DOT File]'
        OdlSummary = OdlSummary + '-----------------------------------------------------------------------------------------------------'
        OdlSummary = OdlSummary + "Port".ljust(30)+"Neighbor".ljust(30)
        for ak in sorted(ODLDict):
            av = ODLDict[ak]
            OdlSummary = OdlSummary + ak.ljust(30)+av.ljust(30)
        OdlSummary = OdlSummary + '-----------------------------------------------------------------------------------------------------'
        return OdlSummary


    #### Function to display the result to user
    def computeSummary(self, ResultSet):
        try:
            
            num = len(ResultSet)
            i = 0
            summary = '-----------------------------------------------------------------------------------------------------\n'
            summary = summary + "Port".ljust(30) + "ObservedNbr".ljust(30) + "ExpectedNbr".ljust(26) + "Status".ljust(30)+ '\n'
            summary = summary + '-----------------------------------------------------------------------------------------------------\n'
            while i < num:
                summary = summary + (ResultSet[i].PortName).ljust(30)+(ResultSet[i].ObservedNbr).ljust(30)+(ResultSet[i].ExpectedNbr).ljust(30)+(ResultSet[i].Status).ljust(30)
                i = i + 1
            summary = summary + '\n-----------------------------------------------------------------------------------------------------'
            return summary
        except Exception as err:
            return "Exception: "+str(err)


    #### Function to remove duplicate entries in terms of key-value and value-key pairs in dictionary
    def remove_duplicate(self, Dict):
        #### Eliminate duplicate entires like 1-->2 and 2-->1 for optimization
        #### This would reduce the dictionary size.
        #### List is taken to maintain such key (i.e. edge point)
        #### whose value is also present as key in dictionary
        del_items = []
        for ak in Dict:
            av = Dict[ak]
            if av in Dict and Dict[av] is not None and ak == Dict[av]:
                #### Check if 1-->2 is already inserted. If it is already inserted, we will not append 2-->1.
                if not av in del_items:
                    del_items.append(ak)
    
        item_cnt = len(del_items)
        i = 0
        while i <  item_cnt:
            del Dict[(del_items[i])]
            i += 1
    
        return Dict


    def compare_dict(self, AdminDict, ODLDict):
        #### Tuple to store the result for each port
        TopologyResult = namedtuple("TopologyResult", "PortName ExpectedNbr ObservedNbr Status")
        Summary = []
        fail_edges_dict = {}
    
        #### Calling below function for optimization
        AdminDict = self.remove_duplicate(AdminDict)
        ODLDict = self.remove_duplicate(ODLDict)
    
        #### Loop to compare AdminDict and ODLDict
        for ak in sorted(AdminDict):
            av = AdminDict[ak]
            if ak in ODLDict and ODLDict[ak] is not None and ODLDict[ak] == av:
                observedNbr = av
                expectedNbr = av
                status = "Pass"
                del ODLDict[ak]
                #### To eliminate cases in ODL information is received as
                #### 1-->2
                #### 2-->1
                #### The below check will eliminate the duplicate entires in ODLDict
                #### and gives a clean output for computeODLSummary() function
                if av in ODLDict and ODLDict[av] is not None and ODLDict[av] == ak:
                    del ODLDict[av]
            elif av in ODLDict and ODLDict[av] is not None and ODLDict[av] == ak:
                observedNbr = av
                expectedNbr = av
                status = "Pass"
                del ODLDict[av]
                if ak in ODLDict and ODLDict[ak] is not None and ODLDict[ak] == av:
                    del ODLDict[ak]
            else:
                observedNbr = "None"
                expectedNbr = av
                status = "Fail"
                fail_edges_dict[ak] = av
            Result = TopologyResult(PortName=ak, ExpectedNbr = expectedNbr, ObservedNbr = observedNbr, Status = status)
            Summary.append(Result)
    
        return Summary, fail_edges_dict


    #### This function creates an HTTP Object for ODL userid and password
    def Httpconn(self, uid, password):
        h = httplib2.Http(".cache")
        #### Provide ODL userid and password for authentication
        h.add_credentials(uid, password)
        return h


    #### This function creates a dictionary for ODL topology which contains the mapping of connected edges
    #### recevied from ODL
    def getODLtopoDict(self, h):
        odl_ip = self.ip.get()
        odl_port_num  = self.cport.get()

        #### Create HTTP request string
        request_string = "http://"+odl_ip+":"+odl_port_num+"/controller/nb/v2/topology/default"

        #### Get all the edges from ODL
        resp, content = h.request(request_string, "GET")

        status = resp['status']
        if status != '200':
            err_str =  'Error in HTTP GET ('+str(resp['content-location'])+') error-code:'+str(status)
            tkMessageBox.showerror("The Cable Guy", err_str)
            sys.exit(0)

        edgeProperties = json.loads(content)
        odlEdges = edgeProperties['edgeProperties']

        EdgeObject = namedtuple("EdgeObject", "dpid portnum")
        ODLObjDict = { }

        #### Parse all the edges and create a dictionary
        for edge in odlEdges:
            objkey = EdgeObject(dpid = edge['edge']['headNodeConnector']['node']['id'], portnum = edge['edge']['headNodeConnector']['id'])
            objval = EdgeObject(dpid = edge['edge']['tailNodeConnector']['node']['id'], portnum = edge['edge']['tailNodeConnector']['id'])
            ODLObjDict[objkey] = objval

        return ODLObjDict


    
    def getYAONtopoDict(self, h):
        YAONObjDict = { } 
        odl_ip = self.ip.get()
        odl_port_num  = self.cport.get()
        
        #### Create HTTP request string
        request_string = "http://" + odl_ip + ":" + odl_port_num + "/Yaon/GetInfo/Dummy"
        #request_string = "http://"+odl_ip+":"+odl_port_num+"/Yaon/GetInfo"

        ### Get all the overlay network info from Opendaylight 
        resp, content = h.request(request_string, "GET")

        status = resp['status']
        if status != '200':
            err_str =  'Error in HTTP GET ('+str(resp['content-location'])+') error-code:'+str(status)
            tkMessageBox.showerror("The Cable Guy", err_str)
            sys.exit(0)
 
        ### Get Overlay Network Info Object from xml
        info = ET.fromstring(country_data_as_string)
         
        return YAONObjDict

    #### This function creates a list of switches connected to ODL
    def getODLSwitchList(self, h):
        odl_ip = self.ip.get()
        odl_port_num  = self.cport.get()
        #### Create switch request for switches connected to ODL
        switch_request_string = "http://"+odl_ip+":"+odl_port_num+"/controller/nb/v2/switchmanager/default/nodes"
             
        #### Get all the switches from ODL
        resp, content = h.request(switch_request_string, "GET")
        status = resp['status']
        if status != '200':
            err_str =  'Error in HTTP GET ('+str(resp['content-location'])+') error-code:'+str(status)
            tkMessageBox.showerror("The Cable Guy", err_str)
            sys.exit(0)

        nodeProperties = json.loads(content)
        odlNodes = nodeProperties['nodeProperties']

        switches_list = []
        #### Create a list of switches
        for node in odlNodes:
            switches_list.append(node['node']['id'])

        return switches_list


    #### This function creates a dictionary for the below mapping
    #### DPID:portnumber -> switchname-portname
    #### 00:00:00:00:00:00:00:02:1 --> s2-eth1
    #### This dictionary has been created because ODL topology API doesn't gives
    #### the edges in named format "s2-eth1".
    #### This dictionary would thus help in conversion
    def getODLSwitchDPIDMapping(self, h, switchList, SwitchName_DPID_Mapping):
        odl_ip = self.ip.get()
        odl_port_num  = self.cport.get()
        #### Create Base URL for ports list
        port_request_string = "http://"+odl_ip+":"+odl_port_num+"/controller/nb/v2/switchmanager/default/node/OF/"

        #### Loop for all the switches
        for dpid in switchList:        
             #### Append DPID to port_request_string to get ports for a particular switch
             request_string = port_request_string + dpid
             resp, content = h.request(request_string, "GET")
             status = resp['status']
             if status != '200':
                 err_str =  'Error in HTTP GET ('+str(resp['content-location'])+') error-code:'+str(status)
                 tkMessageBox.showerror("The Cable Guy", err_str)
                 sys.exit(0)
             ConnectorProperties = json.loads(content)
             connectionPorts = ConnectorProperties['nodeConnectorProperties']

             #### Loop for all the ports of a switch
             for port in connectionPorts:
                  dpid = port['nodeconnector']['node']['id']
                  portid =  port['nodeconnector']['id']
                  port_type = port['nodeconnector']['type']
                  port_name = port['properties']['name']['value']
                  #### Insert only ports information. One of the "properties" tag from ODL contains switch information.
                  if port_type != "SW":
                      key = dpid + ':' + portid
                      SwitchName_DPID_Mapping[key] = port_name
 
        return SwitchName_DPID_Mapping


    #### This function translates ODLObjDict from DPID:portnumber -> switchname-portname
    def translateODLDict(self, ODLObjDict, SwitchName_DPID_Mapping):
        ODLObjDictTranslated = { }
        #### Loop through ODLObjDict and perform the translation
        for key in ODLObjDict:
            #### Translated Key
            temp = key.dpid + ':' + key.portnum
            tkey = SwitchName_DPID_Mapping[temp]
            val = ODLObjDict[key].dpid + ':' +  ODLObjDict[key].portnum
            #### Translated Value
            tval = SwitchName_DPID_Mapping[val]
            #### Replace - with : to be in sync with DOT file format
            tkey = tkey.replace("-", ":")
            tval = tval.replace("-", ":")
            #### Insert translated key and value
            ODLObjDictTranslated[tkey] = tval

        return ODLObjDictTranslated


    def getDOTFileDictPhysical(self, G, AdminDict):
        #### Display error message when blank DOT file is specified
        if not G.edges():
            err_str =  'No port information in DOT File'
            tkMessageBox.showerror("The Cable Guy", err_str)

        #### Create admin dictionary
        for edge in G.edges():
            tp = edge.attr.get("tailport", None)
            key = edge[0] + ':' + tp[2:]
            hp = edge.attr.get("headport", None)
            val = edge[1] + ':' + hp[2:]
            #### Checking the key before insertion into Admin Dictionary.
            #### This checking helps in avoiding duplicate entries like
            #### 1-->2, 1-->2 and
            #### 1-->2, 1-->3
            if key in AdminDict:
                err_str =  'Error in DOT File, duplicate entry found for '+objkey.dpid+'-'+objkey.portnum
                tkMessageBox.showerror("The Cable Guy", err_str)
                sys.exit(0)
            else:
                AdminDict[key] = val
        return AdminDict

    def getDOTFileDictVirtual(self, G, AdminDict):
        #### Display error message when blank DOT file is specified
        if not G.edges():
            err_str =  'No port information in DOT File'
            tkMessageBox.showerror("The Cable Guy", err_str)

        #### Create admin dictionary
        for edge in G.edges():
            tp = edge.attr.get("tailport", None)
            key = edge[0] + ':' + tp
            hp = edge.attr.get("headport", None)
            val = edge[1] + ':' + hp
            #### Checking the key before insertion into Admin Dictionary.
            #### This checking helps in avoiding duplicate entries like
            #### 1-->2, 1-->2 and
            #### 1-->2, 1-->3
            if key in AdminDict:
                err_str =  'Error in DOT File, duplicate entry found for '+objkey.dpid+'-'+objkey.portnum
                tkMessageBox.showerror("The Cable Guy", err_str)
                sys.exit(0)
            else:
                AdminDict[key] = val
        return AdminDict



    def verify(self):

        try:
            #### Get Network Type
            networkType = self.netType.get()
            #### Get controller Type
            controllerType = self.ctype.get()

            #### Create dictionary for admin given topology file
            AdminObjDict = {}
            G=pgv.AGraph(self.filename.get())

            # Physical Network Compare
            if networkType == 1:
                #### Read Admin given Physical topology dot file
                AdminObjDict = self.getDOTFileDictPhysical(G, AdminObjDict)

                if controllerType == "ODL":
                    #### Get HTTP Connection object
                    h = self.Httpconn('admin', 'admin')

                    #### Get ODL topology in a dictionary
                    ODLObjDict =self.getODLtopoDict(h)
    
                    # Get all the switches from ODL
                    switches_list = []
                    switches_list = self.getODLSwitchList(h)
    
                    #### Dictionary to contain the below mapping for switches connected to ODL
                    #### DPID:portnumber -> switchname-portname
                    #### 00:00:00:00:00:00:00:02:1 --> s2-eth1
                    #### This dictionary has been created because ODL topology API doesn't gives
                    #### the edges in named format "s2-eth1".
                    #### This dictionary would thus help in conversion
                    SwitchName_DPID_Mapping = { }
                    SwitchName_DPID_Mapping = self.getODLSwitchDPIDMapping(h, switches_list, SwitchName_DPID_Mapping) 

                    ODLObjDictTranslated = { }
                    #### Translate ODLObjDict from DPID:portnumber -> switchname-portname
                    ODLObjDictTranslated = self.translateODLDict(ODLObjDict, SwitchName_DPID_Mapping)
    
                    #### Function to compare two DOT files
                    Summary, fail_edges_dict = self.compare_dict(AdminObjDict, ODLObjDictTranslated)
    
                   # ODLSummary = ''
                   # ODLSummary = self.computeODLSummary(ODLObjDictTranslated)

                    #### Traverse failed edges and make their color attribute to RED
                    for ak in sorted(fail_edges_dict):
                        av = fail_edges_dict[ak]
                        #### Get the switch name from the pattern <switchname>:portname because we need
                        #### to pass only switch name in get_edge() API
                        edge1 = ak.split(':')[0]
                        edge2 = av.split(':')[0]
                        failed_edge = G.get_edge(edge1, edge2)
                        #### Mark the esges as RED whose match is not found from ODL topology
                        failed_edge.attr['color'] = 'red'

                elif controllerType == "PFC":
                    #### TODO
                    a = 1

                elif controllerType == "RYU":
                    #### TODO
                    a = 1
                #### Write the PNG File
                G.layout()
                G.draw('cable_guy_result.png', format='png', prog='dot')


            # Overlay Network Compare
            else:
                print "Checking Overlay Network" 
                #### Read Admin given Virtual topology dot file
                AdminObjDict = self.getDOTFileDictVirtual(G, AdminObjDict) 
                print "Creating new Graph"
                NG = pgv.AGraph(strict=False)

                for key in sorted(AdminObjDict):
                    value = AdminObjDict[key]
                    keySplitParts = key.split(":", 8)
                    valueSplitParts = value.split(":", 8)
                    newKey = keySplitParts[0] + keySplitParts[1] + keySplitParts[2] + keySplitParts[3] + keySplitParts[4] + keySplitParts[5] + keySplitParts[6] + keySplitParts[7] 
                    newValue = valueSplitParts[0] + valueSplitParts[1] + valueSplitParts[2] + valueSplitParts[3] + valueSplitParts[4] + valueSplitParts[5] + valueSplitParts[6] + valueSplitParts[7] 
                    identifier = keySplitParts[8] + valueSplitParts[8]
                    NG.add_edge(newKey, newValue, identifier)             

                if controllerType == "ODL-YAON":
                    print "Comparing with details from YAON"
                    #### Get HTTP Connection object
                    h = self.Httpconn('admin', 'admin')
  
                    #### Get YAON Overlay topology in a dictionary
                    YAONObjDict = self.getYAONtopoDict(h)
                      
                    ODLObjDictTranslated = YAONObjDict 
 
                    #### Function to compare two DOT files
                    Summary, fail_edges_dict = self.compare_dict(AdminObjDict, YAONObjDict)

                    for key in sorted(fail_edges_dict):
                        value = fail_edges_dict[key]
                        keySplitParts = key.split(":",8)
                        valueSplitParts = value.split(":",8)
                        newKey = keySplitParts[0] + keySplitParts[1] + keySplitParts[2] + keySplitParts[3] + keySplitParts[4] + keySplitParts[5] + keySplitParts[6] + keySplitParts[7] 
                        newValue = valueSplitParts[0] + valueSplitParts[1] + valueSplitParts[2] + valueSplitParts[3] + valueSplitParts[4] + valueSplitParts[5] + valueSplitParts[6] + valueSplitParts[7] 
                        identifier = keySplitParts[8] + valueSplitParts[8]
                        failed_edge = NG.get_edge(newKey, newValue, identifier) 
                        failed_edge.attr['color'] = 'red'
 
                elif controllerType == "ODL-DEFAULT":
                    ###TODO
                    a = 1

                #### Write the PNG File
                NG.layout()
                NG.draw('cable_guy_result.png', format='png', prog='dot')


            self.viewimage = Button(self.master, bg="blue",fg="white",text="View Result as Graphs", command=self.imageview).grid(row=6,column=1,sticky=EW) 
            self.viewsummary = Button(self.master, bg="green",fg="white",text="View Summary as text", command=lambda:self.summaryview(Summary, ODLObjDictTranslated)).grid(row=6,column=2,sticky=EW)
    
        #### Handle exceptions
        except socket.error as e:
            if e.errno == errno.ECONNREFUSED:
                print 'Cannot connect to ODL.'
        except Exception as err:
            print 'Error: '+str(err)


    def imageview(self):
        root3a=Toplevel(self.master)
        imageUI=ImageDisplay(root3a)


    def summaryview(self, summary, ODLObjDictTranslated):
        #TODO
        root3b=Toplevel(self.master)
        comparison_summary = ''
        #comparison_summary = self.computeSummary(summary)
        ODLSummary = ''
        #ODLSummary = self.computeODLSummary(ODLObjDictTranslated)
        summary_str = comparison_summary + ODLSummary
        summaryUI=SummaryDisplay(root3b, summary_str)


class ImageDisplay:
    def __init__(self,master):
        self.master=master
        self.scroll=Scrollbar(self.master)
        #### self.image = Image.open("file.png")
        #self.photo = ImageTk.PhotoImage(file='fileAdmin.png')
        self.photo = ImageTk.PhotoImage(file='cable_guy_result.png')
        w = 2*self.photo.width()
        h = 2*self.photo.height()
        self.master.geometry("%dx%d+%d+%d" % (w, h, 0, 0))
        self.master.title('Topology View')
        self.image1=Label(self.master, image=self.photo).grid(row=1,column=1)
        self.button=Button(self.master, text="OK", command = self.close).grid(row=2,column=1)

    def close(self):
        self.master.destroy()

class ScrollImageDisplay:
    def __init__(self,master):
        self.master=master
        frame=Frame(self.master,width=300,height=300)
        frame.grid(row=0,column=0)
        canvas=Canvas(frame,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,500,500))
        hbar=Scrollbar(frame,orient=HORIZONTAL)
        hbar.pack(side=BOTTOM,fill=X)
        hbar.config(command=canvas.xview)
        vbar=Scrollbar(frame,orient=VERTICAL)
        vbar.pack(side=RIGHT,fill=Y)
        vbar.config(command=canvas.yview)
        canvas.config(width=300,height=300)
        canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        canvas.pack(side=LEFT,expand=True,fill=BOTH)
        self.photo=PhotoImage(file='fileAdmin.png')
        canvas.create_image(0,0,image=self.photo)

class SummaryDisplay:
    def __init__(self,master,summary):
        self.master=master
        self.summary=summary
        self.master.geometry('300x500+100+100')
        self.master.title('Summary Of Results')
        text1=Text(self.master)
        text1.grid(row=1,column=1)
        text1.insert(INSERT,summary)
        text1.insert(END,"")
        #text1.pack()

        okbut=Button(self.master, text="OK", justify=LEFT, anchor=W, command = self.close).grid(row=2,column=1, sticky=EW)

    def close(self):
        self.master.destroy()
        
def main():
    root = Tk()
    cableguy = Welcome(root)
    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()

if __name__ == "__main__":
    main()

