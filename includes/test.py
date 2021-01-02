from tkinter import * 
import os
from includes.gaugelib import *
from includes.chrono import *
import tkinter.font as font

class Test:
    def __init__(self, master):
        self.master = master

        #Fenêtre qui s'adapte à la taille de l'écran
        width_screen = self.master.winfo_screenwidth()-150
        height_screen = self.master.winfo_screenheight()-150
        space = width_screen/50
        self.master.geometry(f"{width_screen+20}x{height_screen+22}")
        self.master.title("Menu TEST")
        self.master.configure(bg="black", highlightbackground="white", highlightcolor="white", highlightthickness=10, padx=0, pady=0, borderwidth=0, relief="flat")
        # get current working directory
        cwd = os.getcwd()
        # Add full path of the .ico image
        self.master.iconbitmap(cwd + "/images/estaca.ico")

        #Variables du menu
        self.engine_rpm=3547 #RPM
        self.engine_torque=1.98 #Nm
        self.engine_temp=82.6 #°C
        self.p_fuel=3.55 #bars
        self.fuel_cons=2.43 #mL
        self.ice_clutch1=True #True si ICE Clutch ON
        self.motor_rpm=0
        self.motor_torque=0
        self.motor_temp=53.4
        self.distance=8.75 #km
        self.efficiency=712 #km/L
        self.ice_clutch2=False #False si ICE Clutch OFF
        self.fuel_mode=True #True si mode FUEL ON
        self.soc=23 #%
        self.lipo=62 #%
        self.connexion=True #True si état de connexion 3g OK
        self.gps=True #True si connexion GPS OK
        self.speed=26 #km/h
        self.hybride_mode=False #False si mode HY pas activé

        self.master.rowconfigure(0, minsize=height_screen/8)
        self.master.rowconfigure(1, minsize=height_screen/8)
        self.master.rowconfigure(2, minsize=height_screen/8)
        self.master.rowconfigure(3, minsize=height_screen/8)
        self.master.rowconfigure(4, minsize=height_screen/8)
        self.master.rowconfigure(5, minsize=height_screen/8)
        self.master.rowconfigure(6, minsize=2)
        self.master.rowconfigure(7, minsize=height_screen/8)
        self.master.rowconfigure(8, minsize=height_screen/8-2)

        self.master.columnconfigure(0, minsize=width_screen/8)
        self.master.columnconfigure(1, minsize=width_screen/8)
        self.master.columnconfigure(2, minsize=width_screen/8)
        self.master.columnconfigure(3, minsize=width_screen/8)
        self.master.columnconfigure(4, minsize=width_screen/8)
        self.master.columnconfigure(5, minsize=width_screen/8)
        self.master.columnconfigure(6, minsize=width_screen/8)
        self.master.columnconfigure(7, minsize=width_screen/8)

        self.hybride_mode_frame=Frame(self.master, width=width_screen/8, height=height_screen/8-1)
        self.hybride_mode_frame.grid(column=0,row=8)
        self.hybride_mode_frame.pack_propagate(0)
        self.hybride_mode_frame.configure(bg="black")
        
        self.hybride_mode_label= Label(self.hybride_mode_frame, text="HY")
        self.hybride_mode_label.pack(anchor="sw", side=BOTTOM)
        self.hybride_mode_label.configure(bg="white", fg="black", font=("Arial 45 bold"))

        #engine RPM

        self.engine_rpm_frame = Frame(self.master, width=width_screen/8-space, height=height_screen/8-space)
        self.engine_rpm_frame.grid(column=0, row=0)
        self.engine_rpm_frame.configure(bg="black")
        self.engine_rpm_frame.pack_propagate(0)

        self.engine_rpm_label=Label(self.engine_rpm_frame,text="Engine RPM")
        self.engine_rpm_label.pack(side=LEFT)
        self.engine_rpm_label.configure(bg=self.engine_rpm_frame["bg"], fg="white", font=("Arial 15 bold"))

        self.engine_rpm_value_frame=Frame(self.master,width=width_screen/8-space, height=height_screen/8-space)
        self.engine_rpm_value_frame.grid(column=2, row=0)  
        self.engine_rpm_value_frame.configure(bg="black")
        self.engine_rpm_value_frame.pack_propagate(0)

        self.engine_rpm_value_label=Label(self.engine_rpm_value_frame, text=self.engine_rpm)
        self.engine_rpm_value_label.pack()
        self.engine_rpm_value_label.configure(bg=self.engine_rpm_value_frame["bg"], fg="yellow", font=("Arial 30 bold")) 
        self.rpm_frame=Frame(self.master, width=width_screen/8-space, height=height_screen/8-space)
        self.rpm_frame.grid(column=3, row=0)
        self.rpm_frame.configure(bg="black")
        self.rpm_frame.pack_propagate(0)
        self.rpm_label=Label(self.rpm_frame, text="RPM")
        self.rpm_label.pack(anchor="w", side=LEFT)
        self.rpm_label.configure(bg=self.engine_rpm_value_frame["bg"], fg="yellow", font=("Arial 25 bold"))

        #engine Torque
        
        self.engine_torque_frame = Frame(self.master, width=width_screen/8-space, height=height_screen/8-space)
        self.engine_torque_frame.grid(column=0, row=1)
        self.engine_torque_frame.configure(bg="black")
        self.engine_torque_frame.pack_propagate(0)

        self.engine_torque_label=Label(self.engine_torque_frame,text="Engine Torque")
        self.engine_torque_label.pack(side=LEFT)
        self.engine_torque_label.configure(bg=self.engine_torque_frame["bg"], fg="white", font=("Arial 15 bold"))

        self.engine_torque_value_frame=Frame(self.master,width=width_screen/8-space, height=height_screen/8-space)
        self.engine_torque_value_frame.grid(column=2, row=1)  
        self.engine_torque_value_frame.configure(bg="black")
        self.engine_torque_value_frame.pack_propagate(0)

        self.engine_torque_value_label=Label(self.engine_torque_value_frame, text=self.engine_torque)
        self.engine_torque_value_label.pack()
        self.engine_torque_value_label.configure(bg=self.engine_torque_value_frame["bg"], fg="yellow", font=("Arial 30 bold")) 
        self.torque_frame=Frame(self.master, width=width_screen/8-space, height=height_screen/8-space)
        self.torque_frame.grid(column=3, row=1)
        self.torque_frame.configure(bg="black")
        self.torque_frame.pack_propagate(0)
        self.torque_label=Label(self.torque_frame, text="Nm")
        self.torque_label.pack(anchor="w", side=LEFT)
        self.torque_label.configure(bg=self.engine_torque_value_frame["bg"], fg="yellow", font=("Arial 25 bold"))

        #engine Temp
        
        self.engine_temp_frame = Frame(self.master, width=width_screen/8-space, height=height_screen/8-space)
        self.engine_temp_frame.grid(column=0, row=2)
        self.engine_temp_frame.configure(bg="black")
        self.engine_temp_frame.pack_propagate(0)

        self.engine_temp_label=Label(self.engine_temp_frame,text="Engine Temp.")
        self.engine_temp_label.pack(side=LEFT)
        self.engine_temp_label.configure(bg=self.engine_temp_frame["bg"], fg="white", font=("Arial 15 bold"))

        self.engine_temp_value_frame=Frame(self.master,width=width_screen/8-space, height=height_screen/8-space)
        self.engine_temp_value_frame.grid(column=2, row=2)  
        self.engine_temp_value_frame.configure(bg="black")
        self.engine_temp_value_frame.pack_propagate(0)

        self.engine_temp_value_label=Label(self.engine_temp_value_frame, text=self.engine_temp)
        self.engine_temp_value_label.pack()
        self.engine_temp_value_label.configure(bg=self.engine_temp_value_frame["bg"], fg="yellow", font=("Arial 30 bold")) 
        self.temp_frame=Frame(self.master, width=width_screen/8-space, height=height_screen/8-space)
        self.temp_frame.grid(column=3, row=2)
        self.temp_frame.configure(bg="black")
        self.temp_frame.pack_propagate(0)
        self.temp_label=Label(self.temp_frame, text="°C")
        self.temp_label.pack(anchor="w", side=LEFT)
        self.temp_label.configure(bg=self.engine_temp_value_frame["bg"], fg="yellow", font=("Arial 25 bold"))

        #Pression fuel
        
        self.p_fuel_frame = Frame(self.master, width=width_screen/8-space, height=height_screen/8-space)
        self.p_fuel_frame.grid(column=0, row=3)
        self.p_fuel_frame.configure(bg="black")
        self.p_fuel_frame.pack_propagate(0)

        self.p_fuel_label=Label(self.p_fuel_frame,text="P Fuel")
        self.p_fuel_label.pack(side=LEFT)
        self.p_fuel_label.configure(bg=self.p_fuel_frame["bg"], fg="white", font=("Arial 15 bold"))

        self.p_fuel_value_frame=Frame(self.master,width=width_screen/8-space, height=height_screen/8-space)
        self.p_fuel_value_frame.grid(column=2, row=3)  
        self.p_fuel_value_frame.configure(bg="black")
        self.p_fuel_value_frame.pack_propagate(0)

        self.p_fuel_value_label=Label(self.p_fuel_value_frame, text=self.p_fuel)
        self.p_fuel_value_label.pack()
        self.p_fuel_value_label.configure(bg=self.p_fuel_value_frame["bg"], fg="yellow", font=("Arial 30 bold")) 
        self.p_fuel_unit_frame=Frame(self.master, width=width_screen/8-space, height=height_screen/8-space)
        self.p_fuel_unit_frame.grid(column=3, row=3)
        self.p_fuel_unit_frame.configure(bg="black")
        self.p_fuel_unit_frame.pack_propagate(0)
        self.p_fuel_unit_label=Label(self.p_fuel_unit_frame, text="bars")
        self.p_fuel_unit_label.pack(anchor="w", side=LEFT)
        self.p_fuel_unit_label.configure(bg=self.p_fuel_unit_frame["bg"], fg="yellow", font=("Arial 25 bold"))

        #Fuel cons
        
        self.fuel_cons_frame = Frame(self.master, width=width_screen/8-space, height=height_screen/8-space)
        self.fuel_cons_frame.grid(column=0, row=4)
        self.fuel_cons_frame.configure(bg="black")
        self.fuel_cons_frame.pack_propagate(0)

        self.fuel_cons_label=Label(self.fuel_cons_frame,text="Fuel Cons.")
        self.fuel_cons_label.pack(side=LEFT)
        self.fuel_cons_label.configure(bg=self.fuel_cons_frame["bg"], fg="white", font=("Arial 15 bold"))

        self.fuel_cons_value_frame=Frame(self.master,width=width_screen/8-space, height=height_screen/8-space)
        self.fuel_cons_value_frame.grid(column=2, row=4)  
        self.fuel_cons_value_frame.configure(bg="black")
        self.fuel_cons_value_frame.pack_propagate(0)

        self.fuel_cons_value_label=Label(self.fuel_cons_value_frame, text=self.fuel_cons)
        self.fuel_cons_value_label.pack()
        self.fuel_cons_value_label.configure(bg=self.fuel_cons_value_frame["bg"], fg="yellow", font=("Arial 30 bold")) 
        self.fuel_frame=Frame(self.master, width=width_screen/8-space, height=height_screen/8-space)
        self.fuel_frame.grid(column=3, row=4)
        self.fuel_frame.configure(bg="black")
        self.fuel_frame.pack_propagate(0)
        self.fuel_label=Label(self.fuel_frame, text="mL")
        self.fuel_label.pack(anchor="w", side=LEFT)
        self.fuel_label.configure(bg=self.fuel_frame["bg"], fg="yellow", font=("Arial 25 bold"))

        #ICE Clutch n°1
        
        self.ice_clutch1_frame = Frame(self.master, width=width_screen/8-space, height=height_screen/8-space)
        self.ice_clutch1_frame.grid(column=0, row=5)
        self.ice_clutch1_frame.configure(bg="black")
        self.ice_clutch1_frame.pack_propagate(0)

        self.ice_clutch1_label=Label(self.ice_clutch1_frame,text="ICE Clutch")
        self.ice_clutch1_label.pack(side=LEFT)
        self.ice_clutch1_label.configure(bg=self.ice_clutch1_frame["bg"], fg="white", font=("Arial 15 bold"))

        self.ice_clutch1_value_frame=Frame(self.master, width=width_screen/8-2*space, height=height_screen/8-space)
        self.ice_clutch1_value_frame.grid(column=2, row=5)
        self.ice_clutch1_value_frame.configure(bg="red")
        self.ice_clutch1_value_frame.pack_propagate(0)

        self.ice_clutch1_value_label=Label(self.ice_clutch1_value_frame, text="ON")
        self.ice_clutch1_value_label.pack()
        self.ice_clutch1_value_label.configure(bg=self.ice_clutch1_value_frame["bg"], fg="white", font=("Arial 26 bold"))

        #RPM Motor

        self.rpm_motor_frame = Frame(self.master, width=width_screen/8-space, height=height_screen/8-space)
        self.rpm_motor_frame.grid(column=4, row=0)
        self.rpm_motor_frame.configure(bg="black")
        self.rpm_motor_frame.pack_propagate(0)

        self.rpm_motor_label=Label(self.rpm_motor_frame,text="Engine RPM")
        self.rpm_motor_label.pack(side=LEFT)
        self.rpm_motor_label.configure(bg=self.rpm_motor_frame["bg"], fg="white", font=("Arial 15 bold"))

        self.rpm_motor_value_frame=Frame(self.master,width=width_screen/8-space, height=height_screen/8-space)
        self.rpm_motor_value_frame.grid(column=6, row=0)  
        self.rpm_motor_value_frame.configure(bg="black")
        self.rpm_motor_value_frame.pack_propagate(0)

        self.rpm_motor_value_label=Label(self.rpm_motor_value_frame, text=self.motor_rpm)
        self.rpm_motor_value_label.pack()
        self.rpm_motor_value_label.configure(bg=self.rpm_motor_value_frame["bg"], fg="yellow", font=("Arial 30 bold")) 
        self.rpm_frame=Frame(self.master, width=width_screen/8-space, height=height_screen/8-space)
        self.rpm_frame.grid(column=7, row=0)
        self.rpm_frame.configure(bg="black")
        self.rpm_frame.pack_propagate(0)
        self.rpm_label=Label(self.rpm_frame, text="RPM")
        self.rpm_label.pack(anchor="w", side=LEFT)
        self.rpm_label.configure(bg=self.engine_rpm_value_frame["bg"], fg="yellow", font=("Arial 25 bold"))

        
        #Motor Torque
        
        self.torque_motor_frame = Frame(self.master, width=width_screen/8-space, height=height_screen/8-space)
        self.torque_motor_frame.grid(column=4, row=1)
        self.torque_motor_frame.configure(bg="black")
        self.torque_motor_frame.pack_propagate(0)

        self.torque_motor_label=Label(self.torque_motor_frame,text="Motor Torque")
        self.torque_motor_label.pack(side=LEFT)
        self.torque_motor_label.configure(bg=self.torque_motor_frame["bg"], fg="white", font=("Arial 15 bold"))

        self.torque_motor_value_frame=Frame(self.master,width=width_screen/8-space, height=height_screen/8-space)
        self.torque_motor_value_frame.grid(column=6, row=1)  
        self.torque_motor_value_frame.configure(bg="black")
        self.torque_motor_value_frame.pack_propagate(0)

        self.torque_motor_value_label=Label(self.torque_motor_value_frame, text=self.motor_torque)
        self.torque_motor_value_label.pack()
        self.torque_motor_value_label.configure(bg=self.torque_motor_value_frame["bg"], fg="yellow", font=("Arial 30 bold")) 
        self.torque_frame=Frame(self.master, width=width_screen/8-space, height=height_screen/8-space)
        self.torque_frame.grid(column=7, row=1)
        self.torque_frame.configure(bg="black")
        self.torque_frame.pack_propagate(0)
        self.torque_label=Label(self.torque_frame, text="Nm")
        self.torque_label.pack(anchor="w", side=LEFT)
        self.torque_label.configure(bg=self.torque_motor_value_frame["bg"], fg="yellow", font=("Arial 25 bold"))

        #Motor Temp
        
        self.motor_temp_frame = Frame(self.master, width=width_screen/8-space, height=height_screen/8-space)
        self.motor_temp_frame.grid(column=4, row=2)
        self.motor_temp_frame.configure(bg="black")
        self.motor_temp_frame.pack_propagate(0)

        self.motor_temp_label=Label(self.motor_temp_frame,text="Engine Temp.")
        self.motor_temp_label.pack(side=LEFT)
        self.motor_temp_label.configure(bg=self.motor_temp_frame["bg"], fg="white", font=("Arial 15 bold"))

        self.motor_temp_value_frame=Frame(self.master,width=width_screen/8-space, height=height_screen/8-space)
        self.motor_temp_value_frame.grid(column=6, row=2)  
        self.motor_temp_value_frame.configure(bg="black")
        self.motor_temp_value_frame.pack_propagate(0)

        self.motor_temp_value_label=Label(self.motor_temp_value_frame, text=self.motor_temp)
        self.motor_temp_value_label.pack()
        self.motor_temp_value_label.configure(bg=self.motor_temp_value_frame["bg"], fg="yellow", font=("Arial 30 bold")) 
        self.temp_frame=Frame(self.master, width=width_screen/8-space, height=height_screen/8-space)
        self.temp_frame.grid(column=7, row=2)
        self.temp_frame.configure(bg="black")
        self.temp_frame.pack_propagate(0)
        self.temp_label=Label(self.temp_frame, text="°C")
        self.temp_label.pack(anchor="w", side=LEFT)
        self.temp_label.configure(bg=self.motor_temp_value_frame["bg"], fg="yellow", font=("Arial 25 bold"))

        #Distance
        
        self.distance_frame = Frame(self.master, width=width_screen/8-space, height=height_screen/8-space)
        self.distance_frame.grid(column=4, row=3)
        self.distance_frame.configure(bg="black")
        self.distance_frame.pack_propagate(0)

        self.distance_label=Label(self.distance_frame,text="Distance")
        self.distance_label.pack(side=LEFT)
        self.distance_label.configure(bg=self.distance_frame["bg"], fg="white", font=("Arial 15 bold"))

        self.distance_value_frame=Frame(self.master,width=width_screen/8-space, height=height_screen/8-space)
        self.distance_value_frame.grid(column=6, row=3)  
        self.distance_value_frame.configure(bg="black")
        self.distance_value_frame.pack_propagate(0)

        self.distance_value_label=Label(self.distance_value_frame, text=self.distance)
        self.distance_value_label.pack()
        self.distance_value_label.configure(bg=self.distance_value_frame["bg"], fg="yellow", font=("Arial 30 bold")) 
        self.distance_unit_frame=Frame(self.master, width=width_screen/8-space, height=height_screen/8-space)
        self.distance_unit_frame.grid(column=7, row=3)
        self.distance_unit_frame.configure(bg="black")
        self.distance_unit_frame.pack_propagate(0)
        self.distance_unit_label=Label(self.distance_unit_frame, text="km")
        self.distance_unit_label.pack(anchor="w", side=LEFT)
        self.distance_unit_label.configure(bg=self.distance_unit_frame["bg"], fg="yellow", font=("Arial 25 bold"))

        #Efficiency
        
        self.efficiency_frame = Frame(self.master, width=width_screen/8-space, height=height_screen/8-space)
        self.efficiency_frame.grid(column=4, row=4)
        self.efficiency_frame.configure(bg="black")
        self.efficiency_frame.pack_propagate(0)

        self.efficiency_label=Label(self.efficiency_frame,text="Efficiency")
        self.efficiency_label.pack(side=LEFT)
        self.efficiency_label.configure(bg=self.efficiency_frame["bg"], fg="white", font=("Arial 15 bold"))

        self.efficiency_value_frame=Frame(self.master,width=width_screen/8-space, height=height_screen/8-space)
        self.efficiency_value_frame.grid(column=6, row=4)  
        self.efficiency_value_frame.configure(bg="black")
        self.efficiency_value_frame.pack_propagate(0)

        self.efficiency_value_label=Label(self.efficiency_value_frame, text=self.efficiency)
        self.efficiency_value_label.pack()
        self.efficiency_value_label.configure(bg=self.efficiency_value_frame["bg"], fg="yellow", font=("Arial 30 bold")) 
        self.efficiency_unit_frame=Frame(self.master, width=width_screen/8-space, height=height_screen/8-space)
        self.efficiency_unit_frame.grid(column=7, row=4)
        self.efficiency_unit_frame.configure(bg="black")
        self.efficiency_unit_frame.pack_propagate(0)
        self.efficiency_unit_label=Label(self.efficiency_unit_frame, text="km/L")
        self.efficiency_unit_label.pack(anchor="w", side=LEFT)
        self.efficiency_unit_label.configure(bg=self.efficiency_unit_frame["bg"], fg="yellow", font=("Arial 25 bold"))

        #ICE Clutch n°2
        
        self.ice_clutch2_frame = Frame(self.master, width=width_screen/8-space, height=height_screen/8-space)
        self.ice_clutch2_frame.grid(column=4, row=5)
        self.ice_clutch2_frame.configure(bg="black")
        self.ice_clutch2_frame.pack_propagate(0)

        self.ice_clutch2_label=Label(self.ice_clutch2_frame,text="ICE Clutch")
        self.ice_clutch2_label.pack(side=LEFT)
        self.ice_clutch2_label.configure(bg=self.ice_clutch2_frame["bg"], fg="white", font=("Arial 15 bold"))

        self.ice_clutch2_value_frame=Frame(self.master, width=width_screen/8-2*space, height=height_screen/8-space)
        self.ice_clutch2_value_frame.grid(column=6, row=5)
        self.ice_clutch2_value_frame.configure(bg="black",highlightbackground="white", highlightthickness=2)
        self.ice_clutch2_value_frame.pack_propagate(0)

        self.ice_clutch2_value_label=Label(self.ice_clutch2_value_frame, text="OFF")
        self.ice_clutch2_value_label.pack()
        self.ice_clutch2_value_label.configure(bg=self.ice_clutch2_value_frame["bg"], fg="white", font=("Arial 26 bold"))

        #Spacer ligne blanche

        self.spacer_frame = Frame(self.master, width=width_screen, height=5)
        self.spacer_frame.grid(column=0, row=6, columnspan=8)
        self.spacer_frame.configure(bg="white")

        #Fuel mode

        self.fuel_mode_frame = Frame(self.master, width=width_screen/8-space, height=height_screen/5-space)
        self.fuel_mode_frame.grid(column=1, row=7, rowspan=8)
        self.fuel_mode_frame.configure(bg="red")
        self.fuel_mode_frame.pack_propagate(0)

        self.fuel_label=Label(self.fuel_mode_frame, text="FUEL")
        self.fuel_label.pack()
        self.fuel_label.configure(bg=self.fuel_mode_frame["bg"], fg="white", font="Arial 18 bold")

        self.fuel_mode_label=Label(self.fuel_mode_frame, text="ON")
        self.fuel_mode_label.pack(expand=True)
        self.fuel_mode_label.configure(bg=self.fuel_mode_frame["bg"], fg="yellow", font="Arial 40 bold")

        # SOC

        self.soc_frame = Frame(self.master, width=width_screen/8-space, height=height_screen/5-space)
        self.soc_frame.grid(column=2, row=7, rowspan=8)
        self.soc_frame.configure(bg="black", highlightbackground="white", highlightthickness=2)
        self.soc_frame.pack_propagate(0)

        self.soc_label=Label(self.soc_frame, text="SOC")
        self.soc_label.pack()
        self.soc_label.configure(bg=self.soc_frame["bg"],fg="white", font="Arial 18 bold")

        self.soc_value_label=Label(self.soc_frame, text="%s %s" % (self.soc,"%"))
        self.soc_value_label.pack(expand=True)
        self.soc_value_label.configure(bg=self.soc_frame["bg"], fg="yellow", font="Arial 40 bold")

        #LIPO

        self.lipo_frame = Frame(self.master, width=width_screen/8-space, height=height_screen/5-space)
        self.lipo_frame.grid(column=3, row=7, rowspan=8)
        self.lipo_frame.configure(bg="black", highlightbackground="white", highlightthickness=2)
        self.lipo_frame.pack_propagate(0)

        self.lipo_label=Label(self.lipo_frame, text="SOC")
        self.lipo_label.pack()
        self.lipo_label.configure(bg=self.lipo_frame["bg"],fg="white", font="Arial 18 bold")

        self.lipo_value_label=Label(self.lipo_frame, text="%s %s" % (self.lipo,"%"))
        self.lipo_value_label.pack(expand=True)
        self.lipo_value_label.configure(bg=self.lipo_frame["bg"], fg="yellow", font="Arial 40 bold")

        #3G

        self.connexion_frame = Frame(self.master, width=width_screen/8-space, height=height_screen/8-space)
        self.connexion_frame.grid(column=5, row=7)
        self.connexion_frame.configure(bg="green")
        self.connexion_frame.pack_propagate(0)

        self.connexion_label=Label(self.connexion_frame, text="3G")
        self.connexion_label.pack(pady=0.5*space)
        self.connexion_label.configure(bg=self.connexion_frame["bg"],fg="black", font="Arial 20 bold")

        #GPS

        self.gps_frame = Frame(self.master, width=width_screen/8-space, height=height_screen/8-space)
        self.gps_frame.grid(column=5, row=8)
        self.gps_frame.configure(bg="green")
        self.gps_frame.pack_propagate(0)

        self.gps_label=Label(self.gps_frame, text="GPS")
        self.gps_label.pack(pady=0.5*space)
        self.gps_label.configure(bg=self.gps_frame["bg"],fg="black", font="Arial 20 bold")

        #Speed

        self.speed_frame=Frame(self.master, width=width_screen/8-space, height=height_screen/8-space)
        self.speed_frame.grid(column=6, row=7)
        self.speed_frame.configure(bg="black")
        self.speed_frame.pack_propagate(0)

        self.speed_label=Label(self.speed_frame, text="SPEED")
        self.speed_label.pack(anchor=NW, side=LEFT)
        self.speed_label.configure(bg=self.speed_frame["bg"],fg="white",font="Arial 25 bold")

        self.speed_value_frame=Frame(self.master, width=width_screen/8-space, height=height_screen/8-space)
        self.speed_value_frame.grid(column=6, row=8)
        self.speed_value_frame.configure(bg="black")
        self.speed_value_frame.pack_propagate(0)

        self.speed_value_label=Label(self.speed_value_frame, text=self.speed)
        self.speed_value_label.pack(expand=True, anchor=E)
        self.speed_value_label.configure(bg=self.speed_value_frame["bg"],fg="yellow", font="Arial 60 bold")

        self.speed_unit_frame=Frame(self.master, width=width_screen/8-space, height=height_screen/8-space)
        self.speed_unit_frame.grid(column=7, row=8)
        self.speed_unit_frame.configure(bg="black")
        self.speed_unit_frame.pack_propagate(0)

        self.speed_unit_label=Label(self.speed_unit_frame, text="km/h")
        self.speed_unit_label.pack(expand=True, anchor=W)
        self.speed_unit_label.configure(bg=self.speed_unit_frame["bg"],fg="yellow", font="Arial 30 bold")
