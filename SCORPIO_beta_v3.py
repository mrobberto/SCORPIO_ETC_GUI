#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 08:56:51 2021

@author: robberto
"""

# Import the library tkinter
from tkinter import *
from tkinter import messagebox  # needed for python3.x
from tkinter import filedialog as fd
from tkinter import ttk

import os
import numpy as np
import pandas as pd
import operator
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from astropy.table import Table
from scipy import interpolate
import math as math


class MainWindow:
    
        
        
    def __init__(self, win):

        # Constructing the left/right frames
        # , width=400, height=800)
        self.frame0_top = Frame(root, background="bisque")
        self.frame0_top.place(x=0, y=0, anchor="nw", width=1920, height=160)

        # Displaying the frame1 in row 0 and column 0
        # frame0_top.geometry("400x800")
        # frame0_top.grid(row=0, column=0)

        # Constructing the first frame, frame1
        # , width=400, height=800)
        self.frame0_bottom = Frame(root, background="gray")
        # Displaying the frame1 in row 0 and column 0
        self.frame0_bottom.place(x=0, y=161, anchor="nw", width=1920, height=800)

        ######################################################################
        # Constructing the first frame, frame1
        self.frame1 = Frame(self.frame0_top, bg="light gray",
                            relief=RIDGE)  # , padx=15, pady=15)
        # Displaying the frame1 in row 0 and column 0
        self.frame1.place(x=2, y=2, width=446, height=160)

        self.w = Canvas(self.frame1, width=446, height=160)
#        self.w.create_rectangle(8, 8, 488, 35, outline='blue')
        self.w.pack()

#this is a dumb comment"
# =============================================================================
#         self.label_Atmosferic_Window = Label(
#             self.frame1, text="Grating")
#         self.label_Atmosferic_Window.place(x=10, y=10)
#         #####
# 
#         # Constructing the button b1 in frame1
#         # Dropdown menu options
#         options = [
#             "Low Red",
#             "Low Blue",
#             "High Red",
#             "High Blue"
#         ]        # datatype of menu text
#         self.bandpass = StringVar()
#         # initial menu text
#         self.bandpass.set(options[2])
#         # Create Dropdown menu
#         self.drop = OptionMenu(self.frame1, self.bandpass, *options)
#         self.drop.place(x=73, y=10)
# 
# =============================================================================

        #####
        self.w.create_rectangle(8, 8, 438, 78, outline='blue')

        ### SLIT WIDTH ###
        ##################
        self.label_SlitWidth = Label(self.frame1, text="Slit Width")
        self.label_SlitWidth.place(x=10, y=20)
#        # Dropdown menu options
        slit_options = [
             '0.36',
             '0.54',
             '0.72',
             '1.08',
             '1.44',
             '1.16',
             '4.32'
        ]
#        # datatype of menu text
        self.slit_selected = StringVar()
#
#        # initial menu text
        self.slit_selected.set(slit_options[2])
#
#        # Create Dropdown menu
#        self.slit_drop = OptionMenu(self.frame1 , self.slit_selected , slit_options[2], *slit_options)
        self.slit_drop = OptionMenu(self.frame1 , self.slit_selected ,  *slit_options)
        self.slit_drop.place(x=110, y=17)
        self.label_arcsec1 = Label(self.frame1, text="arcsec")
        self.label_arcsec1.place(x=180, y=20)


# =============================================================================
#         init_SlitWidth = StringVar()
#         init_SlitWidth.set("0.7")
#         self.Entry_SlitWidth = Entry(
#             self.frame1, width=4, textvariable=init_SlitWidth)
#         self.Entry_SlitWidth.place(x=110, y=37)
#         self.label_arcsec1 = Label(self.frame1, text="arcsec")
#         self.label_arcsec1.place(x=180, y=40)
# 
# =============================================================================
        ### NR. OF EXPOSURES ###
        ########################
        self.label_Entry_NrOfDitheredPairs = Label(self.frame1, text="Nr. of dithered pairs")
        self.label_Entry_NrOfDitheredPairs.place(x=240, y=20)
        self.init_Entry_NrOfDitheredPairs = IntVar()
#        self.init_Entry_NrOfDitheredPairs.set(2)
        self.Entry_NrOfDitheredPairs = Entry(self.frame1, width=4, textvariable=self.init_Entry_NrOfDitheredPairs)
        self.Entry_NrOfDitheredPairs.place(x=375, y=17)

        ### ANGULAR EXTENT ###
        ######################
        self.label_AngularExtent = Label(self.frame1, text="Seeing FWHM")
        self.label_AngularExtent.place(x=10, y=50)
        init_AngExt = StringVar()
        init_AngExt.set("0.4")
        self.Entry_AngularExtent = Entry(
            self.frame1, width=4, textvariable=init_AngExt)
        self.Entry_AngularExtent.place(x=110, y=47)
        self.label_arcsec1 = Label(self.frame1, text="arcsec")
        self.label_arcsec1.place(x=155, y=50)
        
#        self.label_ADC = Label(self.frame1, text="ADC Deployed")
#        self.label_ADC.place(x=275, y=50)
        self.ADCon = IntVar()
        self.Check_ADC = Checkbutton(self.frame1, text='ADC on', variable=self.ADCon)
        self.Check_ADC.place(x=225, y=50)

        self.button_Accept = Button(self.frame1, text="IR Config", command=self.DisplayframeIR)
        self.button_Accept.place(x=325, y=50)
# #######################################################################################################################
#         ### USE AOS ###
# #######################################################################################################################
#         self.label_GLAO = Label(self.frame1, text="GLAO?")
#         self.label_GLAO.place(x=255, y=70)
#         self.selected_GLAO = StringVar(value='SAM')
#         modes = ['SAM', 'Natural Seeing']
#         counter = 0
#         for mode in modes:
#             self.r_GLAO = Radiobutton(
#                 self.frame1,
#                 text=mode,
#                 value=mode,
#                 variable=self.selected_GLAO
#             )
#             self.r_GLAO.place(x=300+counter*60, y=69)
#             counter += 1

# =============================================================================
#         ### FOWLER PAIRS ###
#         ####################
#         self.label_FowlerSampling = Label(self.frame1, text="Fowler Pairs")
#         self.label_FowlerSampling.place(x=320, y=70)
#         init_Fowler = StringVar()
#         init_Fowler.set("16")
#         self.Entry_NrFowlerPairs = Entry(
#             self.frame1, width=4, textvariable=init_Fowler)
#         self.Entry_NrFowlerPairs.place(x=400, y=67)
# 
# =============================================================================
        #####
        self.w.create_rectangle(8, 88, 438, 150, outline='blue')

# =============================================================================
#         self.selected_MagnitudeSystem = StringVar(value='Vega')
#         modes = ['AB', 'Vega']
#         counter = 0
#         for mode in modes:
#             self.r_ABORVEGA = Radiobutton(
#                 self.frame2b,
#                 text=mode,
#                 value=mode,
#                 variable=self.selected_MagnitudeSystem
#             )
#             self.r_ABORVEGA.place(x=120+counter*40, y=18)
#             counter += 1
# 
# =============================================================================
#######################################################################################################################
        ### USE FLUX OR MAGNITUDES ###
#######################################################################################################################
        self.label_FluxORmag = Label(self.frame1, text="Use Line Flux or magnitude?")
        self.label_FluxORmag.place(x=20, y=95)
        self.selected_FluxORmag = StringVar(value='Use magnitude')
        modes = ['Use Line Flux', 'Use magnitude']
        counter = 0
        for mode in modes:
            self.r_FluxORmag = Radiobutton(
                self.frame1,
                text=mode,
                value=mode,
                variable=self.selected_FluxORmag,
                command=self.hide_FluxORmag
            )
            self.r_FluxORmag.place(x=20+counter*120, y=120)
            counter += 1


#######################################################################################################################
#######################################################################################################################

        # Constructing the CONFIGURATION FRAME
        # , padx=15, pady=15)
        self.frameIR = Frame(root,  background="light gray",relief=RIDGE)
        # Displaying the frame2
        self.frameIR.place(x=2000, y=100, width=560, height=270)
        
        self.w1 = Canvas(self.frameIR, width=560, height=270)
#        self.w.create_rectangle(8, 8, 488, 35, outline='blue')
        self.w1.pack()

        self.w1.create_rectangle(8, 8, 552, 262, outline='blue')


        self.label_frameIR_Header = Label(self.frameIR, text='Sampling Parameters')
        self.label_frameIR_Header.config(font =("Courier", 20))
        self.label_frameIR_Header.place(x=150, y=20)
#        self.frameIRHeader.pack() 
        
        self.label_frameIR_ColHead = Label(self.frameIR, text='NExp/pointing')#      Nframes  Nsamples Nskip')
        self.label_frameIR_ColHead.config(font =("Arial", 12))
        self.label_frameIR_ColHead.place(x=100, y=55)
        self.label_frameIR_ColHeadTime = Label(self.frameIR, text='Time/pointing (s)')#      Nframes  Nsamples Nskip')
        self.label_frameIR_ColHeadTime.config(font =("Arial", 12))
        self.label_frameIR_ColHeadTime.place(x=395, y=55)

        self.label_frameIR_ColHead = Label(self.frameIR, text='Nframes  Nsamples  Nskip     Ramp Time (s)')
        self.label_frameIR_ColHead.config(font =("Arial", 12))
        self.label_frameIR_ColHead.place(x=163, y=90)
        self.label_frameIR_ColHead = Label(self.frameIR, text='(per ramp)       (per group)')
        self.label_frameIR_ColHead.config(font =("Arial", 12))
        self.label_frameIR_ColHead.place(x=160, y=107)
        self.label_frameIR_ColHead = Label(self.frameIR, text='Efficiency')
        self.label_frameIR_ColHead.config(font =("Arial", 12))
        self.label_frameIR_ColHead.place(x=487, y=90)


        self.label_Header_gr = Label(self.frameIR, text='g, r channels')
        self.label_Header_gr.place(x=15, y=75)
        self.label_Header_iz = Label(self.frameIR, text='i, z channels')
        self.label_Header_iz.place(x=15, y=100)
        self.label_Header_Y = Label(self.frameIR, text='Y channel')
        self.label_Header_Y.place(x=15, y=125)
        self.label_Header_J = Label(self.frameIR, text='J channels')
        self.label_Header_J.place(x=15, y=150)
        self.label_Header_H = Label(self.frameIR, text='H channels')
        self.label_Header_H.place(x=15, y=175)
        self.label_Header_K = Label(self.frameIR, text='K channels')
        self.label_Header_K.place(x=15, y=200)

        self.init_NExp_gr = IntVar()
        self.init_NExp_gr.set("1")
        self.frameIR_NExp_gr = Entry(self.frameIR, width=4, textvariable = self.init_NExp_gr)
        self.frameIR_NExp_gr.place(x=115, y=75)
   
        self.init_NExp_iz = IntVar()
        self.init_NExp_iz.set("2")
        self.frameIR_NExp_iz = Entry(self.frameIR, width=4, textvariable = self.init_NExp_iz)
        self.frameIR_NExp_iz.place(x=115, y=100)

        self.init_NExp_Y = IntVar()
        self.init_NExp_Y.set("3")
        self.frameIR_NExp_Y = Entry(self.frameIR, width=4, textvariable = self.init_NExp_Y)
        self.frameIR_NExp_Y.place(x=115, y=125)

        self.init_NExp_J = IntVar()
        self.init_NExp_J.set("3")
        self.frameIR_NExp_J = Entry(self.frameIR, width=4, textvariable = self.init_NExp_J)
        self.frameIR_NExp_J.place(x=115, y=150)

        self.init_NExp_H = IntVar()
        self.init_NExp_H.set("3")
        self.frameIR_NExp_H = Entry(self.frameIR, width=4, textvariable = self.init_NExp_H)
        self.frameIR_NExp_H.place(x=115, y=175)

        self.init_NExp_K = IntVar()
        self.init_NExp_K.set("3")
        self.frameIR_NExp_K = Entry(self.frameIR, width=4, textvariable = self.init_NExp_K)
        self.frameIR_NExp_K.place(x=115, y=200)

###########################

        self.init_Nframes_Y = IntVar()
        self.init_Nframes_Y.set("16")
        self.frameIR_Nframes_Y = Entry(self.frameIR, width=4, textvariable = self.init_Nframes_Y)
        self.frameIR_Nframes_Y.place(x=165, y=125)

        self.init_Nframes_J = IntVar()
        self.init_Nframes_J.set("16")
        self.frameIR_Nframes_J = Entry(self.frameIR, width=4, textvariable = self.init_Nframes_J)
        self.frameIR_Nframes_J.place(x=165, y=150)

        self.init_Nframes_H = IntVar()
        self.init_Nframes_H.set("16")
        self.frameIR_Nframes_H = Entry(self.frameIR, width=4, textvariable = self.init_Nframes_H)
        self.frameIR_Nframes_H.place(x=165, y=175)

        self.init_Nframes_K = IntVar()
        self.init_Nframes_K.set("16")
        self.frameIR_Nframes_K = Entry(self.frameIR, width=4, textvariable = self.init_Nframes_K)
        self.frameIR_Nframes_K.place(x=165, y=200)

###########################

        self.init_Nsamples_Y = IntVar()
        self.init_Nsamples_Y.set("4")
        self.frameIR_Nsamples_Y = Entry(self.frameIR, width=4, textvariable = self.init_Nsamples_Y)
        self.frameIR_Nsamples_Y.place(x=215, y=125)

        self.init_Nsamples_J = IntVar()
        self.init_Nsamples_J.set("4")
        self.frameIR_Nsamples_J = Entry(self.frameIR, width=4, textvariable = self.init_Nsamples_J)
        self.frameIR_Nsamples_J.place(x=215, y=150)

        self.init_Nsamples_H = IntVar()
        self.init_Nsamples_H.set("4")
        self.frameIR_Nsamples_H = Entry(self.frameIR, width=4, textvariable = self.init_Nsamples_H)
        self.frameIR_Nsamples_H.place(x=215, y=175)

        self.init_Nsamples_K = IntVar()
        self.init_Nsamples_K.set("4")
        self.frameIR_Nsamples_K = Entry(self.frameIR, width=4, textvariable = self.init_Nsamples_K)
        self.frameIR_Nsamples_K.place(x=215, y=200)

###########################

        self.init_Nskip_Y = IntVar()
        self.init_Nskip_Y.set("16")
        self.frameIR_Nskip_Y = Entry(self.frameIR, width=4, textvariable = self.init_Nskip_Y)
        self.frameIR_Nskip_Y.place(x=265, y=125)

        self.init_Nskip_J = IntVar()
        self.init_Nskip_J.set("16")
        self.frameIR_Nskip_J = Entry(self.frameIR, width=4, textvariable = self.init_Nskip_J)
        self.frameIR_Nskip_J.place(x=265, y=150)

        self.init_Nskip_H = IntVar()
        self.init_Nskip_H.set("16")
        self.frameIR_Nskip_H = Entry(self.frameIR, width=4, textvariable = self.init_Nskip_H)
        self.frameIR_Nskip_H.place(x=265, y=175)

        self.init_Nskip_K = IntVar()
        self.init_Nskip_K.set("16")
        self.frameIR_Nskip_K = Entry(self.frameIR, width=4, textvariable = self.init_Nskip_K)
        self.frameIR_Nskip_K.place(x=265, y=200)

###########################
        self.init_RampTime_Y = IntVar()
        self.init_RampTime_Y.set("16")
        self.frameIR_RampTime_Y = Entry(self.frameIR, width=7, textvariable = self.init_RampTime_Y)
        self.frameIR_RampTime_Y.place(x=315, y=125)

        self.init_RampTime_J = IntVar()
        self.init_RampTime_J.set("16")
        self.frameIR_RampTime_J = Entry(self.frameIR, width=7, textvariable = self.init_RampTime_J)
        self.frameIR_RampTime_J.place(x=315, y=150)

        self.init_RampTime_H = IntVar()
        self.init_RampTime_H.set("16")
        self.frameIR_RampTime_H = Entry(self.frameIR, width=7, textvariable = self.init_RampTime_H)
        self.frameIR_RampTime_H.place(x=315, y=175)

        self.init_RampTime_K = IntVar()
        self.init_RampTime_K.set("16")
        self.frameIR_RampTime_K = Entry(self.frameIR, width=7, textvariable = self.init_RampTime_K)
        self.frameIR_RampTime_K.place(x=315, y=200)
###########################

        self.init_ExpTime_gr = IntVar()
        self.init_ExpTime_gr.set("16")
        self.frameIR_ExpTime_gr = Label(self.frameIR, width=7, textvariable = self.init_ExpTime_gr, bg = 'White')
        self.frameIR_ExpTime_gr.place(x=405, y=78)

        self.init_ExpTime_iz = IntVar()
        self.init_ExpTime_iz.set("16")
        self.frameIR_ExpTime_iz = Label(self.frameIR, width=7, textvariable = self.init_ExpTime_iz, bg = 'White')
        self.frameIR_ExpTime_iz.place(x=405, y=103)

        self.init_ExpTime_Y = IntVar()
        self.init_ExpTime_Y.set("16")
        self.frameIR_ExpTime_Y = Label(self.frameIR, width=7, textvariable = self.init_ExpTime_Y, bg = 'White')
        self.frameIR_ExpTime_Y.place(x=405, y=128)

        self.init_ExpTime_J = IntVar()
        self.init_ExpTime_J.set("16")
        self.frameIR_ExpTime_J = Label(self.frameIR, width=7, textvariable = self.init_ExpTime_J, bg = 'White')
        self.frameIR_ExpTime_J.place(x=405, y=153)

        self.init_ExpTime_H = IntVar()
        self.init_ExpTime_H.set("16")
        self.frameIR_ExpTime_H = Label(self.frameIR, width=7, textvariable = self.init_ExpTime_H, bg = 'White')
        self.frameIR_ExpTime_H.place(x=405, y=178)

        self.init_ExpTime_K = IntVar()
        self.init_ExpTime_K.set("16")
        self.frameIR_ExpTime_K = Label(self.frameIR, width=7, textvariable = self.init_ExpTime_K, bg = 'White')
        self.frameIR_ExpTime_K.place(x=405, y=203)
        
###########################
        self.init_Efficiency_Y = IntVar()
        self.init_Efficiency_Y.set("16")
        self.frameIR_Efficiency_Y = Label(self.frameIR, width=5, textvariable = self.init_Efficiency_Y, bg = 'White')
        self.frameIR_Efficiency_Y.place(x=490, y=128)

        self.init_Efficiency_J = IntVar()
        self.init_Efficiency_J.set("16")
        self.frameIR_Efficiency_J = Label(self.frameIR, width=5, textvariable = self.init_Efficiency_J, bg = 'White')
        self.frameIR_Efficiency_J.place(x=490, y=153)

        self.init_Efficiency_H = IntVar()
        self.init_Efficiency_H.set("16")
        self.frameIR_Efficiency_H = Label(self.frameIR, width=5, textvariable = self.init_Efficiency_H, bg = 'White')
        self.frameIR_Efficiency_H.place(x=490, y=178)

        self.init_Efficiency_K = IntVar()
        self.init_Efficiency_K.set("16")
        self.frameIR_Efficiency_K = Label(self.frameIR, width=5, textvariable = self.init_Efficiency_K, bg = 'White')
        self.frameIR_Efficiency_K.place(x=490, y=203)

# =============================================================================
#        self.button_Default = Button(self.frameIR, text="Default",  highlightbackground='#3E4149', command=self.DefaultIRTime)
        self.button_Default = Button(self.frameIR, text="Default", command=self.DefaultIRTime)
        self.button_Default.place(x=50, y=230)

        self.button_Calculate = Button(self.frameIR, text="Calculate",  command=self.CalculateIRTime)
        self.button_Calculate.place(x=240, y=230)

        self.button_Accept = Button(self.frameIR, text="Accept", command=self.hideframeIR)
        self.button_Accept.place(x=420, y=230)
# =============================================================================


           
#        self.w = Canvas(self.frame2, width=496       
#        self. w.create_rectangle(8, 8, 488, 150, outline='blue')
#        self.w.pack()


#######################################################################################################################
#######################################################################################################################

        # Constructing the second frame, frame2
        # , padx=15, pady=15)
        self.frame2 = Frame(self.frame0_top, bg="light gray")
        # Displaying the frame2
        self.frame2.place(x=447, y=2, width=496, height=160)

        self.w = Canvas(self.frame2, width=496, height=160)
        self. w.create_rectangle(8, 8, 488, 150, outline='blue')
        self.w.pack()

        ### LINE FLUX ###
        #################
        self.label_LineFlux = Label(self.frame2, text="Line Flux")
        self.label_LineFlux.place(x=15, y=20)
        init_LineFlux = StringVar()
        init_LineFlux.set("9.0")
        self.Entry_LineFlux = Entry(self.frame2, width=4, textvariable=init_LineFlux)
        self.Entry_LineFlux.place(x=77, y=17)
        self.label_LineFluxUnits = Label(
            self.frame2, text="x 1E-17 erg/s/cm\u00b2")
        self.label_LineFluxUnits.place(x=127, y=20)

        ### CENTRAL WAVELENGTH ###
        ##########################
        self.label_CentralWl = Label(self.frame2, text="Central Wavelength")
        self.label_CentralWl.place(x=15, y=53)
        init_CentralWl = StringVar()
        init_CentralWl.set("6563")
        self.Entry_CentralWl = Entry(
            self.frame2, width=4, textvariable=init_CentralWl)
        self.Entry_CentralWl.place(x=147, y=50)
        self.selected_LineWlUnits = StringVar(value='Angstrom')
        modes = ['Angstrom', 'micron']
        counter = 0
        for mode in modes:
            self.r_LineWlUnits = Radiobutton(
                self.frame2,
                text=mode,
                value=mode,
                variable=self.selected_LineWlUnits
            )
            self.r_LineWlUnits.place(x=230+counter*100, y=53)
            counter += 1  

        ### REDSHIFT ###
        ################
        self.label_LineRedshift = Label(self.frame2, text="Redshift")
        self.label_LineRedshift.place(x=15, y=85)
        init_LineRedshift = StringVar()
        init_LineRedshift.set("0.0")
        self.Entry_LineRedshift = Entry(
            self.frame2, width=5, textvariable=init_LineRedshift)
        self.Entry_LineRedshift.place(x=77, y=82)
        
        
       # self.Button_checkRedshiftedWl = Button(self.frame2,text="check", 
       #                                       relief=RAISED, command=self.check_RedshiftedWavelength)
       # self.Button_checkRedshiftedWl.place(x=210,y=67)

# =============================================================================
#         ### REDSHIFTED WAVELENGTH ###
#         ################
#         self.label_RedshiftAdopted = Label(self.frame2, text="Redshit adopted")
#         self.label_RedshiftAdopted.place(x=280, y=85)
#         init_RedshiftAdopted = StringVar()
#         RWL = float(init_LineRedshift.get() ) # 6563*(1+float(init_LineRedshift.get()))
#         RWL_string = str(RWL)
#         init_RedshiftAdopted.set(RWL)# "{:7.2f}".format=(RWL))
#         self.Entry_RedshiftAdopted = Entry(
#             self.frame2, width=5, textvariable=init_RedshiftAdopted)
#         self.Entry_RedshiftAdopted.place(x=422, y=82)
# 
# =============================================================================
        ### SOURCE WFHM ###
        ###################
        self.label_FWHM = Label(self.frame2, text="Source FWHM")
        self.label_FWHM.place(x=15, y=120)
        init_FWHM = StringVar()
        init_FWHM.set("30")
        self.Entry_FWHM = Entry(self.frame2, width=4, textvariable=init_FWHM)
        self.Entry_FWHM.place(x=110, y=117)
        self.label_FWHM = Label(self.frame2, text="km/s")
        self.label_FWHM.place(x=155, y=120)


##############################################################################################################
##############################################################################################################

        # Constructing the third frame, frame2b
        # , padx=15, pady=15)
        self.frame2b = Frame(self.frame0_top, bg="light gray")
        # Displaying the frame3
        self.frame2b.place(x=447, y=2, width=496, height=160)

        self.w = Canvas(self.frame2b, width=496, height=160)
        self.w.create_rectangle(8, 8, 488, 150, outline='blue')
        self.w.pack()


#        self.w.create_rectangle(8, 8, 488, 90, outline = 'blue')
      #####
       # self.w.create_rectangle(8, 128, 488, 260, outline = 'blue')

        ### MAGNITUDE ###
        ######################
        self.label_Magnitude = Label(self.frame2b, text="Magnitude")
        self.label_Magnitude.place(x=10, y=18)
        init_SourceMagnitude = StringVar()
        init_SourceMagnitude.set("18.6")
        self.Entry_Magnitude = Entry(self.frame2b, width=5, textvariable=init_SourceMagnitude)
        self.Entry_Magnitude.place(x=78, y=15)
        self.selected_MagnitudeSystem = StringVar(value='Vega')
        modes = ['AB', 'Vega']
        counter = 0
        for mode in modes:
            self.r_ABORVEGA = Radiobutton(
                self.frame2b,
                text=mode,
                value=mode,
                variable=self.selected_MagnitudeSystem,
#                command = self.hide_Vegamag
                command = self.shift_ABorVegamag
            )
            self.r_ABORVEGA.place(x=120+counter*40, y=18)
            counter += 1

      
        # Dropdown menu options
        VegaMag_options = [
            "U",
            "B",
            "V",
            "R",
            "I",
            "Y",
            "J",
            "H",
            "Ks",
            "K"
        ]
        # datatype of menu text
        self.Vega_band = StringVar()
        # initial menu text
        self.Vega_band.set(VegaMag_options[2])        
        # Create Dropdown menu
        self.menu_Vega_band = OptionMenu(self.frame2b, self.Vega_band, *VegaMag_options)
        self.menu_Vega_band.place(x=220, y=18)
       
        # Dropdown menu options
        ABMag_options = [
            "u_SDSS",
            "g_SDSS",
            "r_SDSS",
            "i_SDSS",
            "z_SDSS",
            "Y_VISTA",
            "J_VISTA",
            "H_VISTA",
            "K_VISTA"
        ]
        # datatype of menu text
        self.AB_band = StringVar()
        # initial menu text
        self.AB_band.set(ABMag_options[2])        
        # Create Dropdown menu
        self.menu_AB_band = OptionMenu(self.frame2b, self.AB_band, *ABMag_options)
        self.menu_AB_band.place(x=2200, y=18)



        ### Type of spectrum  ###
        #########################
        self.label_TypeOfSpectrum = Label(self.frame2b, text="Spectrum")
        self.label_TypeOfSpectrum.place(x=290, y=18)
        # Dropdown menu
        options = [
            "Flat F_nu",
            "My own spectrum",
        ]
        self.TypeOfSpectrum = StringVar()
        self.TypeOfSpectrum.set(options[0])
        # Create Dropdown menu
        self.drop_TypeOfSpectrum = OptionMenu(
            self.frame2b, self.TypeOfSpectrum, *options, command=self.select_SourceSpectrum)
        self.drop_TypeOfSpectrum.place(x=347, y=18)
        self.drop_TypeOfSpectrum.config(width=10)

        ### SOURCE FILENAME ###
        ###########WEEEEEE#####
        self.label_Filename = Label(self.frame2b, text="Filename")
        self.label_Filename.place(x=10, y=53)
        self.Entry_Filename = Entry(self.frame2b, width=30)
        self.Entry_Filename.place(x=70, y=50)
 
        ### WAVELENGTH UNIT ###
        ################
        self.label_SpectrumWlUnits = Label(self.frame2b, text="Wavelength Unit")
        self.label_SpectrumWlUnits.place(x=10, y=83)
        self.selected_SpectrumWlUnits = StringVar(value='Angstrom')
        modes = ['Angstrom', 'Micron']
        counter = 0
        for mode in modes:
            self.r_SpectrumWlUnits = Radiobutton(
                self.frame2b,
                text=mode,
                value=mode,
                variable=self.selected_SpectrumWlUnits
            )
            self.r_SpectrumWlUnits.place(x=120+counter*90, y=83)
            counter += 1
            
        # F_lam or F_nu buttons
        #######################
        self.label_SpectrumWlUnits = Label(self.frame2b, text="Spectral Unit")
        self.label_SpectrumWlUnits.place(x=10, y=113)
        self.buttons_FlamORFnu_index = {}
        self.selected_FlamORFnu = StringVar(value='F_lam')
        modes = ['F_lam', 'F_nu']
        counter = 0
        for mode in modes:
            self.r_FlamORFnu = Radiobutton(
                self.frame2b,
                text=mode,
                value=mode,
                variable=self.selected_FlamORFnu,
            )
            self.r_FlamORFnu.place(x=120+counter*90, y=113)
            counter += 1
            self.buttons_FlamORFnu_index[mode]=self.selected_FlamORFnu

        ### MAGNITUDE REDSHIFT ###
        ################
        self.label_MagnitudeRedshift = Label(self.frame2b, text="Redshift")
        self.label_MagnitudeRedshift.place(x=350, y=85)
        init_MagnitudeRedshift = StringVar()
        init_MagnitudeRedshift.set("0.0")
        self.Entry_MagnitudeRedshift = Entry(
            self.frame2b, width=4, textvariable=init_MagnitudeRedshift)
        self.Entry_MagnitudeRedshift.place(x=412, y=82)
            


########################################################################################################
########################################################################################################

        # Constructing frame Exp Time vs SNR
        # , padx=15, pady=15)
        self.frame4 = Frame(self.frame0_top, bg="light gray")
        # Displaying the frame2
        self.frame4.place(x=940, y=2, width=346, height=160)

        self.w = Canvas(self.frame4, width=346, height=160)
        self.w.create_rectangle(8, 8, 338, 150, outline='blue')
        self.w.pack()



#        self.w.create_rectangle(8, 8, 488, 64, outline='blue')
        ### ExpTimeORSNR ###
        ####################
        self.label_ExpTimeORSNR = Label(
            self.frame4, text="Input an exposure time or a desired SNR")
        self.label_ExpTimeORSNR.place(x=20, y=17)
        self.selected_ExpTimeORSNR = StringVar()
        modes = ['Determine Exposure Time', 'Determine Signal to Noise']
        counter = 0
        for mode in modes:
            self.r_ExpTimeORSNR = Radiobutton(
                self.frame4,
                text=mode,
                value=mode,
                variable=self.selected_ExpTimeORSNR,
                command=self.hide_ExpTimeORSNR
            )
            self.r_ExpTimeORSNR.place(x=10, y=45+counter*50)
            counter += 1
        #self.selected_ExpTimeORSNR.set('Determine Exposure Time')

 #       self.w.create_rectangle(8, 64, 238, 102, outline='blue')
        
        ### DESIRED SNR ###
        ###########################
        self.label_DesiredSNR = Label(self.frame4, text="needed to reach SNR")
        self.label_DesiredSNR.place(x=50, y=68)
        init_SNR = StringVar()
        init_SNR.set("10")
        self.Entry_DesiredSNR = Entry(self.frame4, width=7, textvariable=init_SNR)
        self.Entry_DesiredSNR.place(x=190, y=65)

        ### TOTAL EXPOSURE TIME ###
        ###########################
        self.label_TotalExpTime = Label(self.frame4, text="achieved with Total Exp. Time")
        self.label_TotalExpTime.place(x=50, y=116)
        self.init_TotalExpTime = StringVar()
#        self.init_TotalExpTime.set("1200")
        self.Entry_TotalExpTime = Entry(self.frame4, width=6, textvariable=self.init_TotalExpTime)
        self.Entry_TotalExpTime.place(x=240, y=113)
        self.label_s = Label(self.frame4, text="s")
        self.label_s.place(x=305, y=117)



##############################################################################################################
##############################################################################################################

        # Constructing the fifth frame, frame5

        # , padx=15, pady=15)
        self.frame5 = Frame(self.frame0_top, bg="light gray")
        self.frame5.place(x=1280, y=2, width=396, height=65)

        self.w5 = Canvas(self.frame5, width=396, height=65)
        self.w5.create_rectangle(8, 8, 388, 59, outline='blue')
        self.w5.pack()

  #      self.w.create_rectangle(8, 8, 488, 62, outline = 'blue')

        ### OPTIONAL INPUT ###
        ######################
        self.label_AirmassANDWaterVapor = Label(
            self.frame5, text="Optional Input: Airmass and Water Vapour")
        self.label_AirmassANDWaterVapor.place(x=10, y=12)
        self.selected_AirmassORWaterVapor = StringVar()
        selfmodes_AirmassORWaterVapor = [
            'Use Default', 'Airmass and Water Vapor Column']
        counter = 0
        for mode in selfmodes_AirmassORWaterVapor:
            self.radio_AirmassORWaterVapor = Radiobutton(
                self.frame5,
                text=mode,
                value=mode,
                variable=self.selected_AirmassORWaterVapor,
                command=self.hide_AirmassORWaterVapor
            )
            self.radio_AirmassORWaterVapor.place(x=10+counter*115, y=35)
            counter += 1
        self.selected_AirmassORWaterVapor.set('Use Default')

# =============================================================================
# =============================================================================
# # ###
# =============================================================================
# 
# =============================================================================
        # , padx=15, pady=15)
        self.frame5b = Frame(self.frame0_top, bg="light gray")
        self.frame5b.place(x=1280, y=64, width=396, height=98)
   #     self.w.create_rectangle(8, 62, 228, 112, outline = 'blue')

        self.w5b = Canvas(self.frame5b, width=396, height=98)
        self.w5b.create_rectangle(8, 3, 388, 88, outline='blue')
        self.w5b.pack()

        ### AIRMASS ###
        ###############
        self.label_Airmass = Label(self.frame5b, text="Airmass")
        self.label_Airmass.place(x=10, y=15)
        self.selected_Airmass = StringVar()
        self.modes_Airmass = ['1.0', '1.5', '2.0']
        counter = 0
        for mode in self.modes_Airmass:
            self.radio_Airmass = Radiobutton(
                self.frame5b,
                text=mode,
                value=mode,
                variable=self.selected_Airmass,
#                command = self.hide
            )
            self.radio_Airmass.place(x=70+counter*50, y=15)
            counter += 1
        self.selected_Airmass.set('1.0')

#        self.w5b.create_rectangle(8, 3, 244, 52, outline='blue')

        ### Water Vapor ###
        ###################
        self.label_WaterVapor = Label(self.frame5b, text="H2O (mm)")
        self.label_WaterVapor.place(x=10, y=45)
        self.selected_WaterVapor = StringVar()
        self.modes_WaterVapor = ['2.3', '4.3', '7.6', '10.0']
        counter = 0
        for mode in self.modes_WaterVapor:
            self.radio_WaterVapor = Radiobutton(
                self.frame5b,
                text=mode,
                value=mode,
                variable=self.selected_WaterVapor
                # command = self.hide_AirmassORWaterVapor
            )
#       radio_WaterVapor_1p0 =  Radiobutton(self.frame5, text=modes[0], value=modes[0], variable=self.selected_WaterVapor,
#           state = 'disabled',
#           #command = self.hide_AirmassORWaterVapor
#       )
            self.radio_WaterVapor.place(x=100+counter*50, y=45)
            counter += 1
        self.selected_WaterVapor.set('4.3')

######################################################################

# =============================================================================
# # =============================================================================
# #         # Constructing the last frame
# #         # , padx=15, pady=15)
# # =============================================================================
        self.frame6 = Frame(self.frame0_top, bg="light gray")
        # Dislaying the self.frame2
        self.frame6.place(x=1670, y=1, width=120, height=160)

        self.w = Canvas(self.frame6, width=120, height=160)
        self.w.create_rectangle(8, 8, 112, 152, outline='blue')
        self.w.pack()

        ### CALCULATE OR EXIT ###
        #########################
        self.button_Calculate = Button(self.frame6, text="Calculate", command=self.XTcalc, 
                                       #background='#232323',#'000000',
                                       #fg='#b7f731',
                                       relief='flat')
        self.button_Calculate.place(x=15, y=20, height = 80)
        # , command=root_exit)
        self.button_Exit = Button(self.frame6, text="Exit", command=self.root_exit)
        self.button_Exit.place(x=30, y=120)


# =============================================================================
#         #########################
#         ### OUTPUT FRAME ###
#         #########################
# 
# =============================================================================
        self.frame_out = Frame(self.frame0_bottom, bg="light gray")
        self.frame_out.place(x=2, y=2, width=1920, height=720)

        self.w = Canvas(self.frame_out, width=1920, height=714)
        self.w.create_rectangle(8, 8, 1780, 46, outline='blue')
        self.w.pack()

        self.text_SCORPIO_Header = Text(self.frame_out, width=251, height=2, background='light gray')
        #self.text_SCORPIO_Header.insert(INSERT, text)
        self.text_SCORPIO_Header.place(x=12, y=10)
        

        self.set = ttk.Treeview(self.frame_out)
        self.set.place(x=2, y=50, width=1775, height=280)
# =========================================]====================================
#         self.set['columns']= ('Parameter', 'Value','Units')
#         self.set.column("#0", width=0,  stretch=NO)
#         self.set.column("Parameter",anchor=CENTER, width=150)
#         self.set.column("Value",anchor=CENTER, width=100)
#         self.set.column("Units",anchor=CENTER, width=235)
# # 
#         self.set.heading("#0",text="",anchor=CENTER)
#         self.set.heading("Parameter",text="Parameter",anchor=CENTER)
#         self.set.heading("Value",text="Value",anchor=CENTER)
#         self.set.heading("Units",text="Units",anchor=CENTER)
# # 
        self.set['columns']= ('Parameter', 'Value1','Value2','Value3','Value4','Value5','Value6','Value7','Value8','Units')
        self.set.column("#0", width=0,  stretch=NO)
        self.set.column("Parameter",anchor=CENTER, width=120)
        self.set.column("Value1",anchor=CENTER, width=70)
        self.set.column("Value2",anchor=CENTER, width=120)
        self.set.column("Value3",anchor=CENTER, width=110)
        self.set.column("Value4",anchor=CENTER, width=105)
        self.set.column("Value5",anchor=CENTER, width=125)
        self.set.column("Value6",anchor=CENTER, width=240)
        self.set.column("Value7",anchor=CENTER, width=310)
        self.set.column("Value8",anchor="e", width=300)
        self.set.column("Units",anchor=CENTER, width=235)
# 
        self.set.heading("#0",text="",anchor=CENTER)
        self.set.heading("Parameter",text="Parameter",anchor=CENTER)
        self.set.heading("Value1",text="g band",anchor=CENTER)
        self.set.heading("Value2",text="r band",anchor=CENTER)
        self.set.heading("Value3",text="i band",anchor=CENTER)
        self.set.heading("Value4",text="z band",anchor=CENTER)
        self.set.heading("Value5",text="Y band",anchor=CENTER)
        self.set.heading("Value6",text="J band",anchor=CENTER)
        self.set.heading("Value7",text="H band",anchor=CENTER)
        self.set.heading("Value8",text="Ks band",anchor="e")
        self.set.heading("Units",text="Units",anchor=CENTER)



# =============================================================================
#        self.set.insert(parent='',index='end',iid=0,text='',values=('101','john','Gold'))
#        self.set.insert(parent='',index='end',iid=1,text='',values=('102','jack',"Silver"))
#        self.set.insert(parent='',index='end',iid=2,text='',values=('103','joy','Bronze'))
# 
# =============================================================================

# =============================================================================
#         ##################################
#         ###  PLOT OBSERVATIONS OR SNR? ###
#         ##################################
# 
# =============================================================================
        self.w.create_rectangle(8, 336, 422, 367, outline='blue')
 
        self.selected_PlotObsORSNR = StringVar(value='Plot Observations')
        modes = ['Plot Observations', 'Plot Signal to Noise']
        commands=[self.plot_obs,self.plot_snr]
        counter = 0
        for mode in modes:
            self.r_PlotObsORSNR = Radiobutton(
                self.frame_out,
                text=mode,
                value=mode,
                variable=self.selected_PlotObsORSNR,
                command=commands[counter]
            )
            self.r_PlotObsORSNR.place(x=12+counter*200, y=340)
            counter += 1


# =============================================================================
#         ##################################
#         ###  PLOT DEFAULT WL OR USER SPECIFIED?  ###
#         ##################################
# 
# =============================================================================
        self.w.create_rectangle(430, 336, 972, 367, outline='blue')
 
        self.label_PlotWavelengthRange  = Label(self.frame_out, text="Wl range:")
        self.label_PlotWavelengthRange.place(x=450, y=340)
        self.selected_PlotWavelengthRange = StringVar(value='Default')
        modes = ['Default', 'User set']
        counter = 0
        for mode in modes:
            self.r_PlotWavelengthRange = Radiobutton(
                self.frame_out,
                text=mode,
                value=mode,
                variable=self.selected_PlotWavelengthRange,
                command = self.hide_PlotWithUserSpecifiedWavelengths
            )
            self.r_PlotWavelengthRange.place(x=515+counter*75, y=340)
            counter += 1

# =============================================================================
#         wl_0 = StringVar()
#         wl_1 = StringVar()
#         wl_range=self.bandpass.get()
#         wl_0.set(wl_range[0])
#         wl_1.set(wl_range[-1])
# 
# =============================================================================
        self.Entry_lambdamin= Entry(self.frame_out, width=6)
        self.Entry_lambdamin.place(x=695, y=338)
        self.Entry_lambdamin.configure(state='disabled')

        self.label_2dash = Label(self.frame_out, text="--")
        self.label_2dash.place(x=750, y=340)
        self.label_2dash.configure(state='disabled')

        self.Entry_lambdamax= Entry(self.frame_out, width=6)
        self.Entry_lambdamax.place(x=765, y=338)
        self.Entry_lambdamax.configure(state='disabled')

        self.label_lambdamicron = Label(self.frame_out, text="micron")
        self.label_lambdamicron.place(x=830, y=340)
        self.label_lambdamicron.configure(state='disabled')
        
        self.Button_RefreshPlot = Button(self.frame_out,text="Refresh", command=self.RefreshPlot)
        self.Button_RefreshPlot.place(x=880,y=337)                                 


# =============================================================================
# # =============================================================================
# # Last set of buttons for the printout  
# # 

        self.w.create_rectangle(8, 655, 492, 710, outline='blue')

        self.button_PrintToFile = Button(self.frame_out, text="Print to file", command=self.PrintToFile, relief=RAISED) 
        self.button_PrintToFile.place(x=10, y=670)        

        self.buttons = {}
        text_buttons=["Throughput", "Transmission", "Background", "Signal", "Noise", "S/N"] 
        offset = [0,1,2,0,1,2]
        counter = 0
        for name in text_buttons:
            self.button_var = IntVar()
            self.button_var.set(0)
            self.cb = Checkbutton(self.frame_out, text=name, variable=self.button_var)
            self.cb.place(x=130+120*offset[counter], y= 663+20*int(counter/3))
            self.buttons[name]=self.button_var
            counter = counter+1





        self.initial_setup()


# =============================================================================
#         for name in os.listdir(filedir):
#             if name.endswith('.py') or name.endswith('.pyc'):
#                 if name not in ("____.py", "_____.pyc"):
#                     var = tk.IntVar() 
#                     var.set(0)
#                     cb.pack()
#                     buttons.append((var,name))
# 
# =============================================================================


# =============================================================================
#     def ReadThroughputFiles(self):
#         self.SCORPIO_throughput_ADC = np.loadtxt(os.path.join(homedir,"SCORPIO/SpecEff","octocam_ADC.txt"),skiprows=1) #lambda[micron], transmission
#         self.SCORPIO_throughput_ADC[:,0] = SCORPIO_throughput_ADC[:,0] * 1E-3
# #
#         self.SCORPIO_throughput_g = np.loadtxt(os.path.join(homedir,"SCORPIO/SpecEff","octocam_SDSS_g.txt"),skiprows=1) #lambda[micron], transmission
#         self.SCORPIO_throughput_r = np.loadtxt(os.path.join(homedir,"SCORPIO/SpecEff","octocam_SDSS_r.txt"),skiprows=1) #lambda[micron], transmission
#         self.SCORPIO_throughput_i = np.loadtxt(os.path.join(homedir,"SCORPIO/SpecEff","octocam_SDSS_i.txt"),skiprows=1) #lambda[micron], transmission
#         self.SCORPIO_throughput_z = np.loadtxt(os.path.join(homedir,"SCORPIO/SpecEff","octocam_SDSS_z.txt"),skiprows=1) #lambda[micron], transmission
#         self.SCORPIO_throughput_Y = np.loadtxt(os.path.join(homedir,"SCORPIO/SpecEff","octocam_Y.txt"),skiprows=1) #lambda[micron], transmission
#         self.SCORPIO_throughput_J = np.loadtxt(os.path.join(homedir,"SCORPIO/SpecEff","octocam_J.txt"),skiprows=1) #lambda[micron], transmission
#         self.SCORPIO_throughput_H = np.loadtxt(os.path.join(homedir,"SCORPIO/SpecEff","octocam_H.txt"),skiprows=1) #lambda[micron], transmission
#         self.SCORPIO_throughput_K = np.loadtxt(os.path.join(homedir,"SCORPIO/SpecEff","octocam_K.txt"),skiprows=1) #lambda[micron], transmission
# 
#         self.SCORPIO_bandpass_g = np.loadtxt(os.path.join(homedir,"SCORPIO/bandpass","octocam_SDSS_g.txt")) #lambda[micron], transmission
#         self.SCORPIO_bandpass_r = np.loadtxt(os.path.join(homedir,"SCORPIO/bandpass","octocam_SDSS_r.txt")) #lambda[micron], transmission
#         self.SCORPIO_bandpass_i = np.loadtxt(os.path.join(homedir,"SCORPIO/bandpass","octocam_SDSS_i.txt")) #lambda[micron], transmission
#         self.SCORPIO_bandpass_z = np.loadtxt(os.path.join(homedir,"SCORPIO/bandpass","octocam_SDSS_z.txt")) #lambda[micron], transmission
#         self.SCORPIO_bandpass_Y = np.loadtxt(os.path.join(homedir,"SCORPIO/bandpass","octocam_Y.txt")) #lambda[micron], transmission
#         self.SCORPIO_bandpass_J = np.loadtxt(os.path.join(homedir,"SCORPIO/bandpass","octocam_J.txt")) #lambda[micron], transmission
#         self.SCORPIO_bandpass_H = np.loadtxt(os.path.join(homedir,"SCORPIO/bandpass","octocam_H.txt")) #lambda[micron], transmission
#         self.SCORPIO_bandpass_K = np.loadtxt(os.path.join(homedir,"SCORPIO/bandpass","octocam_K.txt")) #lambda[micron], transmission
# =============================================================================

    def read_throughput_files(self):
        homedir = os.getcwd() 
        self.SCORPIO_throughput_ADC = np.loadtxt(os.path.join(homedir,"SpecEff","octocam_ADC.txt"),skiprows=1) #lambda[micron], transmission
        self.SCORPIO_throughput_ADC[:,0] = self.SCORPIO_throughput_ADC[:,0] * 1E-3
#
        self.SCORPIO_throughput_g = np.loadtxt(os.path.join(homedir,"SpecEff","octocam_SDSS_g.txt"),skiprows=1) #lambda[micron], transmission
        self.SCORPIO_throughput_r = np.loadtxt(os.path.join(homedir,"SpecEff","octocam_SDSS_r.txt"),skiprows=1) #lambda[micron], transmission
        self.SCORPIO_throughput_i = np.loadtxt(os.path.join(homedir,"SpecEff","octocam_SDSS_i.txt"),skiprows=1) #lambda[micron], transmission
        self.SCORPIO_throughput_z = np.loadtxt(os.path.join(homedir,"SpecEff","octocam_SDSS_z.txt"),skiprows=1) #lambda[micron], transmission
        self.SCORPIO_throughput_Y = np.loadtxt(os.path.join(homedir,"SpecEff","octocam_Y.txt"),skiprows=1) #lambda[micron], transmission
        self.SCORPIO_throughput_J = np.loadtxt(os.path.join(homedir,"SpecEff","octocam_J.txt"),skiprows=1) #lambda[micron], transmission
        self.SCORPIO_throughput_H = np.loadtxt(os.path.join(homedir,"SpecEff","octocam_H.txt"),skiprows=1) #lambda[micron], transmission
        self.SCORPIO_throughput_K = np.loadtxt(os.path.join(homedir,"SpecEff","octocam_K.txt"),skiprows=1) #lambda[micron], transmission
        
        
# =============================================================================
#         self.SCORPIO_bandpass_g = np.loadtxt(os.path.join(homedir,"SCORPIO/bandpass","octocam_SDSS_g.txt")) #lambda[micron], transmission
#         self.SCORPIO_bandpass_r = np.loadtxt(os.path.join(homedir,"SCORPIO/bandpass","octocam_SDSS_r.txt")) #lambda[micron], transmission
#         self.SCORPIO_bandpass_i = np.loadtxt(os.path.join(homedir,"SCORPIO/bandpass","octocam_SDSS_i.txt")) #lambda[micron], transmission
#         self.SCORPIO_bandpass_z = np.loadtxt(os.path.join(homedir,"SCORPIO/bandpass","octocam_SDSS_z.txt")) #lambda[micron], transmission
#         self.SCORPIO_bandpass_Y = np.loadtxt(os.path.join(homedir,"SCORPIO/bandpass","octocam_Y.txt")) #lambda[micron], transmission
#         self.SCORPIO_bandpass_J = np.loadtxt(os.path.join(homedir,"SCORPIO/bandpass","octocam_J.txt")) #lambda[micron], transmission
#         self.SCORPIO_bandpass_H = np.loadtxt(os.path.join(homedir,"SCORPIO/bandpass","octocam_H.txt")) #lambda[micron], transmission
#         self.SCORPIO_bandpass_K = np.loadtxt(os.path.join(homedir,"SCORPIO/bandpass","octocam_K.txt")) #lambda[micron], transmission
# 
# =============================================================================
        self.GeminiTel_wl_g  = [385,	400,	469,	510,	552]
        self.GeminiTel_wl_r  = [552,	580,	622,	650,	691]
        self.GeminiTel_wl_i  = [691,	720,	755,	780,	818]
        self.GeminiTel_wl_z  = [818,	850,	889,	922,	960]
        self.GeminiTel_wl_Y  = [960,	1000,	1040,	1090,	1120]
        self.GeminiTel_wl_J  = [1150,	1200,	1250,	1300,	1350]
        self.GeminiTel_wl_H  = [1500,	1550,	1630,	1700,	1760]
        self.GeminiTel_wl_K  = [2000,	2100,	2175,	2280,	2350]
        self.GeminiTel_th_g  = [0.481,	0.554,	0.705,	0.773,	0.809]
        self.GeminiTel_th_r  = [0.809,	0.829,	0.851,	0.862,	0.878]
        self.GeminiTel_th_i  = [0.878,	0.889,	0.896,	0.903,	0.912]
        self.GeminiTel_th_z  = [0.914,	0.916,	0.922,	0.926,	0.930]
        self.GeminiTel_th_Y  = [0.930,	0.934,	0.936,	0.940,	0.941]
        self.GeminiTel_th_J  = [0.942,	0.943,	0.946,	0.948,	0.946]
        self.GeminiTel_th_H  = [0.954,	0.955,	0.957,	0.957,	0.957]
        self.GeminiTel_th_K  = [0.957,	0.958,	0.958,	0.957,	0.927]


    def RefreshPlot(self):
        if self.selected_PlotObsORSNR.get() == "Plot Observations":
            self.plot_obs()
        else:
            self.plot_snr()
          
            
        ######################################################################

    def initial_setup(self):
        self.selected_FluxORmag.set('Use magnitude')
        self.hide_FluxORmag()
        self.selected_AirmassORWaterVapor.set('Use Default')
        self.hide_AirmassORWaterVapor()
        self.hide_ExpTimeORSNR()
        self.selected_ExpTimeORSNR.set('Determine Signal to Noise')
        self.read_throughput_files()
        self.det_RN_SingleFrame = 14   #electrons readout noise (single sample, kTC excluded)
        self.init_TotalExpTime.set("1200")
        self.init_Entry_NrOfDitheredPairs.set(1)
        self.DefaultIRTime()
         

#        self.selected_PlotObsORSNR.set('Plot Observations') 
# =============================================================================
#         wl_range=spec_struct["wave"] 
#         #for the output window, set the lambdamin/max of the bandpass
#         wl_0 = wl_range[0]
#         wl_1 = wl_range[-1]
#         self.Entry_lambdamin.set(str(wl_0))
#         self.Entry_lambdamax.set(str(wl_1))
#         
# =============================================================================

    # collect all parameters and put it in a dictionary

    def collect_all_parameters(self):
        all_parameters = {
#            "bandpass": self.bandpass.get(),
#            "slit": self.Entry_SlitWidth.get(),
            "slit": self.slit_selected.get(),
            "NofDithers": self.Entry_NrOfDitheredPairs.get()*2, #1 pair is 2 dithers
            "AngularExt": self.Entry_AngularExtent.get(),
#            "NrFowlerPairs": self.Entry_NrFowlerPairs.get(),
            "FluxORMag": self.selected_FluxORmag.get(), #['Line Flux', 'magnitude']
            "LineFlux": self.Entry_LineFlux.get(),  # 1E-17 units
            "CentralWl": self.Entry_CentralWl.get(),
            "LineWlUnits": self.selected_LineWlUnits.get(),
            "LineRedshift": self.Entry_LineRedshift.get(),
            "FWHM": self.Entry_FWHM.get(),
            "SourceMagnitude": self.Entry_Magnitude.get(),
            "Magnitude System": self.selected_MagnitudeSystem.get(), #['AB', 'Vega']
            "Vega_band": self.Vega_band.get(),
            "AB_band": self.AB_band.get(),
            "TypeOfSpectrum": self.TypeOfSpectrum.get(),
            "Filename": self.Entry_Filename.get(),
            "FluxUnits": self.selected_FlamORFnu.get(),
            "MagnitudeRedshift": self.Entry_MagnitudeRedshift.get(),
            "SpectrumWlUnits": self.selected_SpectrumWlUnits.get(),
            "ExpTimeORSNR": self.selected_ExpTimeORSNR.get(),
            "TotalExpTime": self.Entry_TotalExpTime.get(),
            "DesiredSNR": self.Entry_DesiredSNR.get(),
            "AirmassORWaterVapor": self.selected_AirmassORWaterVapor.get(),
            "Airmass": self.selected_Airmass.get(),
            "WaterVapor": self.selected_WaterVapor.get()
        }
        return(all_parameters)


        
    def hide_FluxORmag(self):
        if self.selected_FluxORmag.get() == 'Use magnitude':
             self.frame2.place(x=2447, y=2, width=496, height=160)   # move  out frame 2
             self.frame2b.place(x=447, y=2, width=496, height=160)
        else:
             self.frame2.place(x=447, y=2, width=496, height=160)  # move  out frame 2b
             self.frame2b.place(x=2447, y=2, width=496, height=160) 

            
    def hide_Vegamag(self):
        if self.selected_MagnitudeSystem.get() == 'AB':
            self.menu_Vega_band.configure(state='disabled')               
        else:
            self.menu_Vega_band.configure(state='normal')               


    def shift_ABorVegamag(self):
        if self.selected_MagnitudeSystem.get() == 'AB':
            self.menu_Vega_band.place(x=2200, y=18)
            self.menu_AB_band.place(x=220, y=18)
        else:
            self.menu_Vega_band.place(x=220, y=18)
            self.menu_AB_band.place(x=2200, y=18)

    
    def read_ABfilters(self):
        homedir = os.getcwd() 
        filter_path = homedir + '/Filters/'
        AB_filter = self.AB_band.get()
        if AB_filter  == 'u_SDSS':
            df = pd.read_csv(filter_path+'u_SDSS.res.txt', delimiter='\s+', header=None)
        if AB_filter  == 'g_SDSS':
            df = pd.read_csv(filter_path+'g_SDSS.res.txt', delimiter='\s+', header=None)
        if AB_filter  == 'r_SDSS':
            df = pd.read_csv(filter_path+'r_SDSS.res.txt', delimiter='\s+', header=None)
        if AB_filter  == 'i_SDSS':
            df = pd.read_csv(filter_path+'i_SDSS.res.txt', delimiter='\s+', header=None)
        if AB_filter  == 'z_SDSS':
            df = pd.read_csv(filter_path+'z_SDSS.res.txt', delimiter='\s+', header=None)
        if AB_filter  == 'Y_VISTA':
            df = pd.read_csv(filter_path+'Y_uv.res.txt', delimiter='\s+', comment='#', header=None)
        if AB_filter  == 'J_VISTA':
            df = pd.read_csv(filter_path+'J_uv.res.txt', delimiter='\s+', comment='#', header=None)
        if AB_filter  == 'H_VISTA':
            df = pd.read_csv(filter_path+'H_uv.res.txt', delimiter='\s+', comment='#', header=None)
        if AB_filter  == 'K_VISTA':
            df = pd.read_csv(filter_path+'K_uv.res.txt', delimiter='\s+', comment='#', header=None)
#        wl_A = df[0]
#        tp   = df[1]
        return df.to_numpy() 

    def DisplayframeIR(self):
        self.frameIR.place(x=100, y=100, width=560, height=270)

    def hideframeIR(self):
        self.frameIR.place(x=2000, y=100, width=560, height=270)

    def hide_AirmassORWaterVapor(self):
        if self.selected_AirmassORWaterVapor.get() == 'Use Default':
              for child in self.frame5b.winfo_children():
                  try:
                      if child.widgetName != 'frame':  # frame has no state, so skip
                          child.configure(state='disabled')
                  except Exception as e:
                      print(e)
        else:
              for child in self.frame5b.winfo_children():
                  try:
                      if child.widgetName != 'frame':  # frame has no state, so skip
                          child.configure(state='normal')
                  except Exception as e:
                      print(e)

    def hide_ExpTimeORSNR(self):
        if self.selected_ExpTimeORSNR.get() == 'Determine Exposure Time':
            self.label_TotalExpTime.configure(state='disabled')
            self.Entry_TotalExpTime.configure(state='disabled')
            self.label_s.configure(state='disabled')
            ### HIDE SNR ###
            ###########################
            self.label_DesiredSNR.configure(state='normal')
            self.Entry_DesiredSNR.configure(state='normal')
        else:
            self.label_TotalExpTime.configure(state='normal')
            self.Entry_TotalExpTime.configure(state='normal')
            self.label_s.configure(state='normal')
            ### HIDE SNR ###
            ###########################
            self.label_DesiredSNR.configure(state='disabled')
            self.Entry_DesiredSNR.configure(state='disabled')

    def hide_PlotWithUserSpecifiedWavelengths(self):
        if self.selected_PlotWavelengthRange.get() == 'Default':
            self.Entry_lambdamin.configure(state='disabled')
            self.label_2dash.configure(state='disabled')
            self.Entry_lambdamax.configure(state='disabled')
            self.label_lambdamicron.configure(state='disabled')
        else:
            self.Entry_lambdamin.configure(state='normal')
            self.label_2dash.configure(state='normal')
            self.Entry_lambdamax.configure(state='normal')
            self.label_lambdamicron.configure(state='normal')


    def validate(self, all_parameters):
        #validate nr of exposures
        if all_parameters["NofDithers"].isdigit() == False:
           messagebox.showerror(title=None,message="Nr. of Exp must be an integer > 0")
        elif int(all_parameters["NofDithers"]) < 1:   
           messagebox.showerror(title=None,message="Nr. of Exp must be an integer > 0")
        # validate line flux
        if all_parameters["FluxORMag"] == 'Use Line Flux':
           if float(all_parameters["LineFlux"]) <= 0:
             messagebox.showerror(title=None, message="Line Flux must be  > 0")
           if float(all_parameters["CentralWl"]) <= 0:
             messagebox.showerror(
                 title=None, message="Central Wavelength must be  > 0")

#    def check_RedshiftedWavelength(self): 
#        print('pippo')
#        CentralWl = float(self.Entry_CentralWl.get())
#        Redshift =  float(self.Entry_Redshift.get())
#        RedshiftedWavelength = CentralWl * (1+Redshift)
#        RedshiftedWavelength_string = "{:.2f}".format(RedshiftedWavelength)
#        print(CentralWl, Redshift, RedshiftedWavelength, RedshiftedWavelength_string)
#        self.Entry_RedshiftAdopted.insert(END,RedshiftedWavelength_string)

 #       # validate redshift
 #       if float(all_parameters["Redshift"]) < 0:
 #          messagebox.showerror(title=None, message="Redshift must be  >= 0")
         
# =============================================================================
# =============================================================================
#          ;make the structure into something useful
# =============================================================================
    def DefaultIRTime(self):
        
        self.init_NExp_gr.set = (1)
        self.init_NExp_iz.set = (2)
        self.init_NExp_Y.set = (3)
        self.init_NExp_J.set = (3)
        self.init_NExp_H.set = (3)
        self.init_NExp_K.set = (3)
        
        self.init_Nframes_Y.set(16)
        self.init_Nframes_J.set(16)
        self.init_Nframes_H.set(16)
        self.init_Nframes_K.set(16)

        self.init_Nsamples_Y.set(4)
        self.init_Nsamples_J.set(4)
        self.init_Nsamples_H.set(4) 
        self.init_Nsamples_K.set(4)

        self.init_Nskip_Y.set(16) 
        self.init_Nskip_J.set(16) 
        self.init_Nskip_H.set(16) 
        self.init_Nskip_K.set(16) 
 
        self.init_RampTime_Y.set("196.61")
        self.init_RampTime_J.set("196.61")
        self.init_RampTime_H.set("196.61")
        self.init_RampTime_K.set("196.61")

        self.init_ExpTime_gr.set("1200")
        self.init_ExpTime_iz.set("600")
        self.init_ExpTime_Y.set("589.82")
        self.init_ExpTime_J.set("589.82")
        self.init_ExpTime_H.set("589.82")
        self.init_ExpTime_K.set("589.82")

        self.init_Efficiency_Y.set("0.89%")
        self.init_Efficiency_J.set("0.89%")
        self.init_Efficiency_H.set("0.89%")
        self.init_Efficiency_K.set("0.89%")
        

    def CalculateIRTime(self):
        
        K1, K2, K3, time_IR = self.CalculateSamplingParameters()
        self.init_RampTime_Y.set("{:.2f}".format(float(time_IR[0])))
        self.init_RampTime_J.set("{:.2f}".format(float(time_IR[1])))
        self.init_RampTime_H.set("{:.2f}".format(float(time_IR[2])))
        self.init_RampTime_K.set("{:.2f}".format(float(time_IR[3])))
        n0 = [self.frameIR_NExp_Y.get(), self.frameIR_NExp_J.get(), self.frameIR_NExp_H.get(), self.frameIR_NExp_K.get()]
        n1 = map(int,n0)
        n2 = list(n1)
        n = np.asarray(n2)*time_IR
        self.init_ExpTime_Y.set("{:.2f}".format(float(n[0])))
        self.init_ExpTime_J.set("{:.2f}".format(float(n[1])))
        self.init_ExpTime_H.set("{:.2f}".format(float(n[2])))
        self.init_ExpTime_K.set("{:.2f}".format(float(n[3])))
        TotalExpTime = float(self.init_TotalExpTime.get())
        NrOfDithers=  self.init_Entry_NrOfDithers.get() * 2 #1 pair is 2 dithers
        OptimalRampTime = TotalExpTime / NrOfDithers
        print(OptimalRampTime)
#        self.efficiency_Y.set("{:.2f}".format(float(n[0]))/OptimalRampTime)
        print("{:.2f}".format(float(n[0]/OptimalRampTime)))
        self.init_Efficiency_Y.set("{:.2f}%".format(float(n[0]/OptimalRampTime)))
        self.init_Efficiency_J.set("{:.2f}%".format(float(n[1]/OptimalRampTime)))
        self.init_Efficiency_H.set("{:.2f}%".format(float(n[2]/OptimalRampTime)))
        self.init_Efficiency_K.set("{:.2f}%".format(float(n[3]/OptimalRampTime)))
        
    def  CalculateSamplingParameters(self):
        #
        tf = 0.65536 # = 2048.*2048./32/2E5  # time needed to read the full array (2048x2048 over 32 output lines at 200KHz)
        m0 = [self.frameIR_Nsamples_Y.get(), self.frameIR_Nsamples_J.get(), self.frameIR_Nsamples_H.get(), self.frameIR_Nsamples_K.get()] #read and average 16 frames ()
        s0= [self.frameIR_Nskip_Y.get(), self.frameIR_Nskip_J.get(), self.frameIR_Nskip_H.get(), self.frameIR_Nskip_K.get()]  #read and average 16 frames ()
        m1 = map(int,m0)
        s1 = map(int,s0)
        m2 = list(m1)
        s2 = list(s1)
        m = np.asarray(m2)
        s = np.asarray(s2)
    #       s = 0   #skip 0 frames
        tg = (m+s)*tf #exposure frame per group
#        n0 = [self.frameIR_NExp_Y.get(), self.frameIR_NExp_J.get(), self.frameIR_NExp_H.get(), self.frameIR_NExp_K.get()]
        n0 = [self.frameIR_Nframes_Y.get(), self.frameIR_Nframes_J.get(), self.frameIR_Nframes_H.get(), self.frameIR_Nframes_K.get()]
        n1 = map(int,n0)
        n2 = list(n1)
        n = np.asarray(n2)
        print(n)

              # max(np.round(Exptime/tg)[0],2)   #number of groups, at least 2 to get a "ramp"
        time_IR = (n-1)*tg
        K1 =  12  * (n-1)/(n*(n+1))*self.det_RN_SingleFrame**2/m
        K2 =  6/5. * (n**2+1)*(n-1)/(n*(n+1)) * tg
        K3 = -2 * (m**2-1)/(m*(n**2+n)) * tf
        print(K1, K2, K3, time_IR)
        return K1, K2, K3, time_IR

# =============================================================================
# #      MULTIACCUM SAMPLING IN THE IR CHANNELS
#             if i >= 3:
#                 K1,K2,K3,time_IR= CalculateSamplingParameters(self, f)
#                 Noise_Sig_tg = K2[i-3] * sig_rateSpecObs*time_IR 
#                 Noise_Sig_tf = K3[i-3] * sig_rateSpecObs*time_IR 
#                 Noise_Sig = K1[i-3] + Noise_Sig_tg + Noise_Sig_tf
#                 Noise_Bg_tg = K2[i-3] * bkSpecObs*time_IR
#                 Noise_Bg_tf = K3[i-3] * bkSpecObs*time_IR
#                 Noise_Bg = K1[i-3] + Noise_Bg_tg + Noise_Bg_tf
#                 time = time_IR * dither
#                 NoiseVar = Noise_Sig*nPixSpatial + Noise_Bg*nPixSpatial + +stat["dark"]*nPixSpatial*time_IR
#                 noiseSpecObs = np.sqrt(NoiseVar * dither)
#                 signalSpecObs =  sig_rateSpecObs * time
# 
# =============================================================================

    def select_SourceSpectrum(self,arg1):
        if arg1 == 'My own spectrum':
# =============================================================================
#             self.label_Filename.configure(state='normal')
#             self.Entry_Filename.configure(state='normal')
#             self.r_FlamORFnu.configure(state='normal',value='F_lam')
#             self.r_FlamORFnu.configure(state='normal',value='F_nu')
#             self.label_SpectrumWlUnits.configure(state='normal')
#             self.r_SpectrumWlUnits.configure(state='normal')
#             self.label_MagnitudeRedshift.configure(state='normal')
#             self.Entry_MagnitudeRedshift.configure(state='normal')
# 
# =============================================================================
            self.Entry_Filename.delete(0,END) 
            self.source_filename = StringVar()
            filetypes = (
                ('text files', '*.txt'),
                ('text files', '*.dat'),
                ('text files', '*.fits'),
                ('All files', '*.*')
                )
            self.source_fullpathfilename = fd.askopenfilename(
                title='Open a file',
                initialdir = os.getcwd()+'/templates/',
                filetypes=filetypes)            
            full_path = os.path.dirname(self.source_fullpathfilename)
            self.selected_directory = full_path.replace(os.getcwd()+'/templates/','')   #e.g.'Pickles_1998
            self.selected_file = self.source_fullpathfilename.replace(os.getcwd()+'/templates/','') #e.g. '
            self.Entry_Filename.insert(END,self.selected_file)
            
# =============================================================================
#  =============================================================================
# # =============================================================================
# #
# =============================================================================
    def read_SourceSpectrum(self):
        logc=np.log10(29979245800.)  
        if self.selected_directory == 'Pickles_1998':
            df = pd.read_csv(self.source_fullpathfilename, delimiter='\s+', header=None)
            df = df.to_numpy()
            wl_A = df[:,0] # Restframe Wavelength (Angstrom)
            userspec_wl_um =  (df[:,0]).flatten() / 10000.0   # we work with wl in micron
            userspec_Flam =  (df[:,1]).flatten() # Flux per unit wavelength (ergs/s/cm^2/Angstrom)
            userspec_Flam *= 1E8                 # Flux per unit wavelength (ergs/s/cm^2/cm)
            userspec_Fnu = userspec_Flam *10**logc / (userspec_wl_um*1E-4)**2
#            print('stop here')
#            if all_parameters["TypeOfSpectrum"] ==  "My own spectrum":
    ##          print(self.source_filename)

        if self.selected_directory == 'galaxies':
            df = pd.read_csv(self.source_fullpathfilename, delimiter='\s+', header=None)
            df = df.to_numpy()
            wl_A = df[:,0]
            userspec_wl_um =  (df[:,0]).flatten() / 10000.0   # we work with wl in micron
            userspec_Flam =  (df[:,1]).flatten()
            userspec_Fnu = userspec_Flam *10**logc / (userspec_wl_um*1E-4)**2
#            print('stop here')
#            if all_parameters["TypeOfSpectrum"] ==  "My own spectrum":
    ##          print(self.source_filename)

# =============================================================================
#       #B) Stellar Models: Allard Spectra
        if self.selected_directory == 'BT-Settl-CIFSST2011bc/SPECTRA':
              t_lwr = Table.read(self.source_fullpathfilename,format='fits')#,names=['WAVE','FLUX','dFLUX'])
#             #
              wl = t_lwr['wl_A'] # angstrom
              wl_range = (wl >= 3E2) & (wl <= 3E6) 
              wl = wl[wl_range]
#             
              Flam = 10**(t_lwr['Flam']-8)   #Flam = erg/cm2/s/A , from README.rtf file of Allard.
              Flam = Flam[wl_range]
#             
              userspec_wl_um = wl / 10000.0  
              userspec_Fnu = Flam * 10**logc / (wl*1E-4)**2
# =============================================================================
# =============================================================================
        if self.selected_directory == 'others':
# #             #
              df = pd.read_csv(self.source_fullpathfilename, delimiter='\s+', header=None)
              df = df.to_numpy()
              wl = df[2:,0]
              Fl = df[2:,1]
              if self.selected_LineWlUnits.get() == 'Angstrom':
                   wl_A = wl  #
                   userspec_wl_um = wl_A /10000.0
              else:
                   usersepc_wl_um = wl                  
              if self.selected_FlamORFnu.get() == 'F_lam':
                   Flam =Fl
                   userspec_Fnu = Fl * 10**logc / (userspec_wl_um*1E-4)**2
              else:    
                   userspec_Fnu = Fl
# # =============================================================================
# =============================================================================
        self.user_Wave = userspec_wl_um#A
        self.user_Flux = userspec_Fnu#lam
        return 
# ====== =======================================================================
#         else:
#          ### FILENAME ###
#          ################
#             print('disable all')
#             self.label_Filename.configure(state='disabled')
#             self.Entry_Filename.configure(state='disabled')
#             self.r_FlamORFnu.configure(state='disabled',value='F_lam')
#             self.r_FlamORFnu.configure(state='disabled',value='F_nu')
#             self.label_SpectrumWlUnits.configure(state='disabled')
#             self.r_SpectrumWlUnits.configure(state='disabled')
#             self.label_MagnitudeRedshift.configure(state='disabled')
#             self.Entry_MagnitudeRedshift.configure(state='disabled')
# 
# =============================================================================
#purpose is to mimic what output would look like based on the inherent flaws of optics of telescope
#basic process: convert everything to velocity, make a gaussian kernal and convolve it with the rest of the function, 
#               then convert back to wavelength

 

    def Moffat4(self,FWHM,beta):# ;eta is the Moffat parameter, FWHM in arcsec
# =============================================================================
#     ;examples:
#     ;a) to display the PSF, FWHM=0.8"
#     ;IDL> show3,moffat(0.5)/max(moffat(0.5))  
#     ;b) to find the encircled energy over a long slit of 0.8", FWHM=0.45"
#     ;slit=0.8 & print,total((moffat(0.45))[320-(slit/2.*100):320+(slit/2.*100-1),*])
#     
#     ;==========================================================================
#     dist_circle, circle, 2048 ;ancillary for Moffat below - will result in a 2048x2048 image with source centered at (1024-1)/2 = (511.5,511.5), i.e. peaks at the pixel center  
# =============================================================================
        xc=512
        yc=512
        rows, cols = (xc, yc)
        dist_circle=np.zeros((xc,yc))
        for i in range(rows):
            for j in range(cols):
                dist_circle[i,j] = np.sqrt( (i-xc/2)**2 + (j-yc/2)**2 )
    #    ;beta = 2.    ;appropriate from SAM, e-mail from Tokovinin; set =3 for VLT/FORS1 and =100 for a Gaussian profile
        FWHM_75=FWHM*75.   #;use 0.0033*4 =0.0122" pixels
        alpha = FWHM_75 / (2.*np.sqrt(2.**(1./beta)-1.))  # ; well known relation, e.g. from http://pixinsight.com/doc/tools/DynamicPSF/DynamicPSF.html
                                                           # ; or Patat 2011 http://www.aanda.org/articles/aa/full_html/2011/03/aa15537-10/aa15537-10.html    
    #    ;got this analytic form Patat et al. or http://en.wikipedia.org/wiki/Moffat_distribution
        PSF_Moffat4 = (beta-1)/(np.pi*alpha**2)/(1.+dist_circle**2/alpha**2)**beta     
        return PSF_Moffat4
# =============================================================================
# =============================================================================


    def DMDslit4(self,Nslit_X,Nslit_Y):
# =============================================================================
#         ;1DMD side is typically 10micron size = 166.6mas.
#         ;the gap is 0.6micron wide, i.e. 10mas (exactly!).
#         ;we sample the gap with 3 pixels: 1 pixel=0.2micron=3.33mas. The grid is therefore made of 
#         ; 3pixel wide gap
#         ; 50pixel wide mirror sides
#         ; 1" is therefore 300pixels. 
#         ;if we work with images of 2048x2048 pixels, we have 6.82" fields; enough for a decent long slit.
#         ;therefore
# =============================================================================
#        slit=fltarr(2048,2048)+1
        rows, cols = (512, 512)
        slit4=[]#np.zeros(shape=(rows,cols))
        for i in range(rows):
            col = []
            for j in range(cols):
                col.append(1)
            slit4.append(col)
        slit4=np.array(slit4)
        
 #       edges = np.arange(1,50*51,52)
        Xparity = np.fmod(Nslit_X/2,1)
# =============================================================================
# =============================================================================
        if Xparity != 0:
              slit4[0:256-int(Nslit_X*8), :] = 0 
              slit4[256+int(Nslit_X*8):,:] = 0
        else:          
              slit4[0:256-int(Nslit_X/2*13), :] = 0 
              slit4[256+int(Nslit_X/2*13):,:] = 0
#
        Yparity = np.fmod(Nslit_Y/2,1)
        if Yparity != 0:
              slit4[:,0:256-int(Nslit_Y*8)] = 0 
              slit4[:,256+int(Nslit_Y*8):] = 0
        else: 
              slit4[:,0:256-int(Nslit_Y/2*7)] = 0 
              slit4[:,256+int(Nslit_Y/2*7):] = 0
# 
# =============================================================================
        return slit4


# =============================================================================
# # =============================================================================
# # =============================================================================
# 
# =============================================================================
    def slit_loss(self,FWHM,beta,Nslit_X,Nslit_Y):
       PSF_in = self.Moffat4(FWHM,beta)
       slit = self.DMDslit4(Nslit_X,Nslit_Y)
       PSF_out = np.multiply(PSF_in,slit)
       slit_loss=np.sum(PSF_out)   #sum(PSF_in-PSF_out)/sum(PSF_in)
       return slit_loss

# =============================================================================




    def degrade_resolution(self, wavelengths, flux, center_wave, spec_res, disp, px_tot):    
    #0.40471199999999996 1.34252 4096
# =============================================================================
#       Number of pixels to be output -
        Npix_spec = px_tot * 3./2.  # if px_tot=4096, this is 6144 pixels
#     
# =============================================================================
#       the log of speed of light in cm/s
        logc=np.log10(29979245800.)  
#     
# =============================================================================
#       make "velocity" grid centered at the central wavelength of the band
#       sampled at 1 km/s, from -300,000 to 300,000 Km/s
        vel=(np.arange(600001)-300000) # big array of integers....   [km/s]
#     
# =============================================================================
#       the array of wavelengths coming in input is converted to velocity difference vs. central wavelength, in km/s
        in_vel=(wavelengths/center_wave-1)*10.**(1*logc-5) 
#     
# =============================================================================
#       if the array of wavelengths too wide
#       we can get non-physical velocities: kill them and their relative input flux array
#       create vectors in velocity space, picking realistic values (keeping good indices)
        in_vel_short = in_vel[ np.where( (in_vel > vel[0]) & (in_vel < vel[600000]) )[0] ]
        in_flux_short = flux[ np.where( (in_vel > vel[0]) & (in_vel < vel[600000]) )[0] ] 
#     
# =============================================================================
#       these new arrays of rel. velocities from the center_wave, and relative fluxes, are n
#       calculated starting from the wavelengths and therefore are not uniformly sampled...
#       interpolate to equally spaced km/s, up to 600000 points

#        interp_flux = np.interp(vel, in_vel_short, in_flux_short, fill_value = "extrapolate")   
        f = interpolate.interp1d(in_vel_short, in_flux_short, fill_value = "extrapolate")   
        interp_flux = f(vel)
        
#     
# =============================================================================
#       now we need to blur this highly dispersed spectrum with the response of the slit, in km/s.
#       sigma  = the resolution of the spectrograph in km/s, expressed as sigma of the Gaussian response.
#       it is Delta_lam/lam = Delta_v/c = FWHM/c = 2SQRT(2log2)/c, since
#       FWHM = 2*SQRT(2*log2) x sigma = 2.35 x sigma.
#       Therefore, since FWHM/c = Dlambda/lambda = 1/R, we have sigma*2.35 = c/R, i.e. 
        sigma = (10.**(logc-5)/spec_res)/(2*np.sqrt(2*np.log(2))) 
#     
# =============================================================================
#       Now make a smaller velocity array with the same velocity "resolution" as the steps in vel, above
        n = np.round(8.*sigma) # e.g. 1018km/s  if sigma=127.31km/s 
        # make sure that n is odd so there is a well defined central velocity...
        if (n % 2 == 0): 
            n = n + 1   #i.e. n=1019
#       create an array of n values in the range [-4*sigma,+4*sigma] in km/s, e.g. from -509km/s to +509km/s in this case   
        vel_kernel = np.arange(n) - np.floor(n/2.0) 
#     
# =============================================================================
#       create a normalized gaussian (unit area) with width=sigma
        gauss_kernel = (1/(np.sqrt(2*np.pi)*sigma)) * np.exp(-0.5*vel_kernel**2.0/sigma**2.0)
#     
# =============================================================================
#       convolve flux with gaussian kernel
        convol_flux = np.convolve(interp_flux, gauss_kernel , mode="same") 
        convol_wave = center_wave * (vel*10.**(-1*logc+5.0) + 1.0 ) # [micron] weirdly spaced, as derived from km/s
#     
# =============================================================================
#       and the real pixel scale 
        real_wave = np.arange(Npix_spec) * disp * 10.**(-4.)     #6000pix * 10A/pix * 1E-4mic/A  => [micron]
        real_wave = real_wave - real_wave[int(np.round(Npix_spec/2.))]   
        real_wave = real_wave + center_wave # [pixel]    print(real_wave)
#     
# =============================================================================
#       interpolate onto the pixel scale of the detector
        out_wave = real_wave
        out_flux = np.interp(real_wave , convol_wave, convol_flux)
        
        out = {"lam": out_wave, #[micron]
              "flux": out_flux} #same unit in input e.g. erg/cm2/s/micron
        
        return(out)
    
# =============================================================================
# =============================================================================
    
                            
         

# =============================================================================
# =============================================================================

    def plot_obs(self) :
        
        struct=self.spec_struct
        
# =============================================================================
# =============================================================================
#          ;make the structure into something useful
# =============================================================================
        DICT_wave_grid  = struct['wave']
        DICT_sn_index   = struct['sn_index']
        DICT_filt_index = struct['filt_index']
        DICT_tpSpecObs  = struct['tp']
        DICT_fltSpecObs = struct['filt']
        DICT_tranSpecObs= struct['tran']
        DICT_bkSpecObs  = struct['bk']
        DICT_signalSpecObs = struct['signal']
        DICT_noiseSpecObs=struct['noise']
        DICT_snSpecObs  = struct['sn']
        center     = struct['center']
        time       = struct['time']
        lineF      = struct['LineFlux']
        line_width = struct["line_width"]
        
# =============================================================================
#         for i in range(8):
#             wave_grid = DICT_wave_grid[i] 
#             sn_index  = DICT_sn_index[i]  
#             filt_index = DICT_filt_index[i]
#             tpSpecObs = DICT_tpSpecObs[i]  
#          fltSpecObs = DICT_fltSpecObs[i]
#             tranSpecObs = DICT_tranSpecObs[i] 
#             bkSpecObs = DICT_bkSpecObs[i] 
#             signalSpecObs = DICT_signalSpecObs[i] 
#             noiseSpecObs = DICT_noiseSpecObs[i]
#             snSpecObs = DICT_snSpecObs[i] 
#                 
#             #recover background * time
#             bkSpecObs = np.array(bkSpecObs[i]) * time         
# =============================================================================
     
        if ( (self.selected_PlotWavelengthRange.get() == 'Default') & (self.selected_FluxORmag.get() == 'Use magnitude') ):
#              xrange = np.array([ float(self.wl_0), float(self.wl_1) ]) 
            fltSpecObs = DICT_fltSpecObs[0]
            index=np.where(fltSpecObs[0] > 0)
            xrange=[0.38,2.4]
            fig = Figure(figsize=(16,6))
            a = fig.add_subplot(111)
            fig.subplots_adjust(top=0.98, bottom=0.18, left=0.04, right=0.96) 
            a.axis(xmin=0.380,xmax=2.4)
            a.set_xlabel("Wavelength (micron)", fontsize=12)
            a.set_ylabel("Transmission", fontsize=12)
              
            x = DICT_wave_grid[0]
            y = np.array(DICT_fltSpecObs[0]) * time/max( np.array(DICT_fltSpecObs[0])*time)     
            a.plot(x[index], y[index],color='white')

        if ( (self.selected_PlotWavelengthRange.get() == 'Default') & (self.selected_FluxORmag.get() == 'Use Line Flux') ):
            for i in range(8):
                m=np.max(DICT_signalSpecObs[i])
                if m != 0:
                    wave_grid = DICT_wave_grid[i]
                    signalSpecObs = DICT_signalSpecObs[i]
                    max_signal = m
            index=np.where(abs(wave_grid-center) < .01)
            xrange=[np.floor(min(wave_grid[index]*100))/100.,np.ceil(max(wave_grid[index]*100))/100. ]
       
            x = wave_grid[index]
            y = signalSpecObs[index]/max_signal    
            fig = Figure(figsize=(16,6))
            a = fig.add_subplot()#111)
            fig.subplots_adjust(top=0.98, bottom=0.18, left=0.04, right=0.96) 
              
            a.plot(x, y,color='white') #no lines shown              
              #a.axis(xmin=xrange[0],xmax=xrange[1])
            a.axis(xmin=0.38,xmax=2.4)
            a.set_xlabel("Wavelength (micron)", fontsize=12)
            a.set_ylabel("Transmission", fontsize=12)

        if ( (self.selected_PlotWavelengthRange.get() == 'User set') & (self.selected_FluxORmag.get() == 'Use magnitude') ):
            wave_grid = [] 
            fltSpecObs = []
            for i in range(8):
                 wave_grid = np.append(wave_grid, DICT_wave_grid[i])
                 fltSpecObs =  np.append(fltSpecObs, DICT_fltSpecObs[i])
            xrange = np.array([ float(self.Entry_lambdamin.get()), float(self.Entry_lambdamax.get())]) 
            index = np.where( (wave_grid > xrange[0]) & (wave_grid < xrange[1]) )
        
            x = wave_grid
            y = fltSpecObs * time/max(fltSpecObs*time)     
            fig = Figure(figsize=(16,6))
            a = fig.add_subplot(111)
            fig.subplots_adjust(top=0.98, bottom=0.18, left=0.04, right=0.96) 

            a.plot(x[index], y[index],color='white')
            a.axis(xmin=xrange[0],xmax=xrange[1])
            a.set_xlabel("Wavelength (micron)", fontsize=12)
            a.set_ylabel("Transmission", fontsize=12)

        if ( (self.selected_PlotWavelengthRange.get() == 'User set') & (self.selected_FluxORmag.get() == 'Use Line Flux') ):
            wave_grid = [] 
            signalSpecObs = []
            for i in range(8):
                 wave_grid = np.append(wave_grid, DICT_wave_grid[i])
                 signalSpecObs =  np.append(signalSpecObs, DICT_signalSpecObs[i])
            xrange = np.array([ float(self.Entry_lambdamin.get()), float(self.Entry_lambdamax.get())]) 
            index = np.where( (wave_grid > xrange[0]) & (wave_grid < xrange[1]) )
              
#              if ((len(xrange) == 1) and (xrange[0].item == 0)):
#            xrange = np.array([ float(self.Entry_lambdamin.get()), float(self.Entry_lambdamax.get())]) 
#              index = np.where( (wave_grid > xrange[0]) & (wave_grid < xrange[1]) )
       
            x = wave_grid
            y = signalSpecObs/max(signalSpecObs)     
            fig = Figure(figsize=(16,6))
            a = fig.add_subplot()#111)
            fig.subplots_adjust(top=0.98, bottom=0.18, left=0.04, right=0.96) 
              
            a.plot(x[index], y[index],color='white') #no lines shown              
              #a.axis(xmin=xrange[0],xmax=xrange[1])
            a.axis(xmin=min(x[index]), xmax=max(x[index]))
            a.set_xlabel("Wavelength (micron)", fontsize=12)
            a.set_ylabel("Transmission", fontsize=12)
              
        full_sig = []
        for i in range(8):
            signalSpecObs = DICT_signalSpecObs[i] 
            full_sig  = np.append(full_sig,signalSpecObs)
        max_signal=np.max(full_sig)  #calculated again just for safety...

        for i in range(8):
            wave_grid = DICT_wave_grid[i] 
            sn_index  = DICT_sn_index[i]  
            filt_index = DICT_filt_index[i]
            tpSpecObs = DICT_tpSpecObs[i]  
            fltSpecObs = DICT_fltSpecObs[i]
            tranSpecObs = DICT_tranSpecObs[i] 
            bkSpecObs = DICT_bkSpecObs[i] 
            signalSpecObs = DICT_signalSpecObs[i] 
            noiseSpecObs = DICT_noiseSpecObs[i]
            snSpecObs = DICT_snSpecObs[i]                   
            #recover background * time
            bkSpecObs = np.array(DICT_bkSpecObs[i]) * time
  
            index=np.where(fltSpecObs > 0)
            if np.max(signalSpecObs) == 0:
                signalSpecObs = wave_grid * 0.0
# =============================================================================
#   ;*************************************
#   ;*************************************
#   ; plot the atmosphere and the throughput
#   ;*************************************
#   ;*************************************
#   
# =============================================================================
# =============================================================================
#   ;atmospheric trasparency
# =============================================================================
#               oplot, wave_grid, tranSpecObs, color=purple, thick=2
            if i == 0:
                line_tran, = a.plot(wave_grid, tranSpecObs,'m-',label='tran')
                line_tp, = a.plot(wave_grid, tpSpecObs,'g-',label="tp")
                a.plot(wave_grid, np.sqrt(bkSpecObs)/(2*max_signal), 'r-', label='sky res')
                a.plot(wave_grid, signalSpecObs/(2*max_signal),'b-',label='science')
            else: 
               line_tran, = a.plot(wave_grid, tranSpecObs,'m-')
               line_tp, = a.plot(wave_grid, tpSpecObs,'g-')
               a.plot(wave_grid, np.sqrt(bkSpecObs)/(2*max_signal), 'r-')
               a.plot(wave_grid, signalSpecObs/(2*max_signal),'b-')
#
# =============================================================================
            a.legend(bbox_to_anchor=(0.9, 0.97),
                        loc='upper left', borderaxespad=0.02)
        #a.legend(loc='best')
            self.printed_atmtrans = tranSpecObs
            self.printed_background = bkSpecObs     
            self.printed_throughput = tpSpecObs
            self.printed_signal = signalSpecObs
            self.printed_wavegrid = wave_grid
            self.printed_noise = noiseSpecObs
            self.printed_snr = snSpecObs

# =============================================================================
# =============================================================================
#     
            a2 = a.twinx()
            #ax2.plot(t, s2, 'r.')
            a2.set_ylabel('photons/pixel')
#            a2.axis(ymin=0, ymax=2*max(signalSpecObs))
            a2.axis(ymin=0, ymax=2*max_signal)
# =============================================================================

        canvas = FigureCanvasTkAgg(fig, master=self.frame_out)
        canvas.get_tk_widget().place(x=2, y=410, width=1780, height=245)#pack()
        canvas.draw()
        self.button_Calculate.configure(text="Calculate", bg = "green")
 
# =============================================================================
# # =============================================================================
# # # =============================================================================
# # # 
         
    def plot_snr(self):

        struct=self.spec_struct
        
        struct=self.spec_struct
        
# =============================================================================
# =============================================================================
#          ;make the structure into something useful
# =============================================================================
        DICT_wave_grid  = struct['wave']
        DICT_sn_index   = struct['sn_index']
        DICT_filt_index = struct['filt_index']
        DICT_tpSpecObs  = struct['tp']
        DICT_fltSpecObs = struct['filt']
        DICT_tranSpecObs= struct['tran']
        DICT_bkSpecObs  = struct['bk']
        DICT_signalSpecObs = struct['signal']
        DICT_noiseSpecObs=struct['noise']
        DICT_snSpecObs  = struct['sn']
        center     = struct['center']
        time       = struct['time']
        lineF      = struct['LineFlux']
        line_width = struct["line_width"]
       
# =============================================================================
# =============================================================================
#          ;make the structure into something useful
# =============================================================================
# =============================================================================
#         wave_grid  = struct['wave']
#         sn_index   = struct['sn_index']
#         noiseSpecObs=struct['noise']
#         snSpecObs  = struct['sn']
#         tpSpecObs  = struct['tp']
#         filt_index = struct['filt_index']
#         signalSpecObs = struct['signal']
#         bkSpecObs  = struct['bk']
#         tranSpecObs= struct['tran']
#         center     = struct['center']
#         time       = struct['time']
#         fltSpecObs = struct['filt']
#         lineF      = struct['LineFlux']
#         line_width = struct["line_width"]
# 
# =============================================================================
        for i in range(8):
            wave_grid = np.squeeze(DICT_wave_grid[i])
            sn_index  = np.squeeze(DICT_sn_index[i]) 
            filt_index = np.squeeze(DICT_filt_index[i])
            tpSpecObs = np.squeeze(DICT_tpSpecObs[i])  
            fltSpecObs = np.squeeze(DICT_fltSpecObs[i])
            tranSpecObs = np.squeeze(DICT_tranSpecObs[i]) 
            bkSpecObs = np.squeeze(DICT_bkSpecObs[i]) 
            signalSpecObs = np.squeeze(DICT_signalSpecObs[i]) 
            noiseSpecObs = np.squeeze(DICT_noiseSpecObs[i])
            snSpecObs = np.squeeze(DICT_snSpecObs[i])           

            #recover background * time
            bkSpecObs = np.array(DICT_bkSpecObs[i]) * time

            wave_grid = []
            fltSpecObs = []
            tranSpecObs = []
            bkSpecObs = []
            tpSpecObs = []
            signalSpecObs = []
            noiseSpecObs = []
            snSpecObs     = []
            for i in range(8):
                wave_grid     = np.append(wave_grid, DICT_wave_grid[i]) 
                fltSpecObs    = np.append(fltSpecObs, DICT_fltSpecObs[i])
                tranSpecObs   = np.append(tranSpecObs, DICT_tranSpecObs[i])
                bkSpecObs     = np.append(bkSpecObs, DICT_bkSpecObs[i])
                tpSpecObs     = np.append(tpSpecObs, DICT_tpSpecObs[i])
                signalSpecObs = np.append(signalSpecObs, DICT_signalSpecObs[i])
                noiseSpecObs  = np.append(noiseSpecObs, DICT_noiseSpecObs[i])
                snSpecObs     = np.append(snSpecObs, DICT_snSpecObs[i])

        

        if ( (self.selected_PlotWavelengthRange.get() == 'Default') & (self.selected_FluxORmag.get() == 'Use magnitude') ):
#              xrange = np.array([ float(self.wl_0), float(self.wl_1) ]) 
# =============================================================================
#               index=np.where(fltSpecObs > 0.05)
#               xrange=[np.floor(min(wave_grid[index]*100))/100.,np.ceil(max(wave_grid[index]*100))/100. ]
#               
#               x = wave_grid
#               y = fltSpecObs * time/max(fltSpecObs*time)     
#               fig = Figure(figsize=(16,6))
#               a = fig.add_subplot(111)
#               fig.subplots_adjust(top=0.98, bottom=0.18, left=0.12, right=0.86) 
# 
#               a.plot(x[index], y[index],color='white')
#               a.axis(xmin=xrange[0],xmax=xrange[1])
#               a.set_xlabel("Wavelength (micron)", fontsize=12)
#               a.set_ylabel("Transmission", fontsize=12)
# 
# =============================================================================
#            fltSpecObs = DICT_fltSpecObs[0]
#            index=np.where(fltSpecObs[0] > 0)
            xrange=[0.38,2.4]
            fig = Figure(figsize=(16,6))
            a = fig.add_subplot(111)
            fig.subplots_adjust(top=0.98, bottom=0.18, left=0.04, right=0.96) 
            a.axis(xmin=0.380,xmax=2.4)
            a.set_xlabel("Wavelength (micron)", fontsize=12)
            a.set_ylabel("Transmission", fontsize=12)
              
            x = wave_grid
            y = np.array(fltSpecObs * time/max( np.array(fltSpecObs*time)) )
            a.plot(x, y,color='white')
            
            index = np.where( (wave_grid >= 0.385) & (wave_grid <= 2.35) )

        if ( (self.selected_PlotWavelengthRange.get() == 'Default') & (self.selected_FluxORmag.get() == 'Use Line Flux') ):
#              if ((len(xrange) == 1) and (xrange[0].item == 0)):
#              index=np.where(abs(wave_grid-center) < .01)
 #             xrange=[np.floor(min(wave_grid[index]*100))/100.,np.ceil(max(wave_grid[index]*100))/100. ]
#              else:
                   # index=np.where((wave_grid < max(xrange)) & (wave_grid > min(xrange)))
            xrange=[0.38,2.4]
            fig = Figure(figsize=(16,6))
            a = fig.add_subplot()#111)
            fig.subplots_adjust(top=0.98, bottom=0.18, left=0.04, right=0.96) 
            a.axis(xmin=0.380,xmax=2.4)
            a.set_xlabel("Wavelength (micron)", fontsize=12)
            a.set_ylabel("Transmission", fontsize=12)
                      
            x = wave_grid
            y = signalSpecObs/max(signalSpecObs)     
            a.plot(x, y,color='white') #no lines shown              

            index = np.where( (wave_grid >= 0.385) & (wave_grid <= 2.35) )
            
        if ( (self.selected_PlotWavelengthRange.get() == 'User set') & (self.selected_FluxORmag.get() == 'Use magnitude') ): 
              xrange = np.array([ float(self.Entry_lambdamin.get()), float(self.Entry_lambdamax.get())]) 
              index = np.where( (wave_grid > xrange[0]) & (wave_grid < xrange[1]) )
        
              x = wave_grid
              y = fltSpecObs * time/max(fltSpecObs*time)     
              fig = Figure(figsize=(16,6))
              a = fig.add_subplot(111)
              fig.subplots_adjust(top=0.98, bottom=0.18, left=0.04, right=0.96) 

              a.plot(x[index], y[index],color='white')
              a.axis(xmin=xrange[0],xmax=xrange[1])
              a.set_xlabel("Wavelength (micron)", fontsize=12)
              a.set_ylabel("Transmission", fontsize=12)

        if ( (self.selected_PlotWavelengthRange.get() == 'User set') & (self.selected_FluxORmag.get() == 'Use Line Flux') ):
              
#              if ((len(xrange) == 1) and (xrange[0].item == 0)):
              xrange = np.array([ float(self.Entry_lambdamin.get()), float(self.Entry_lambdamax.get())]) 
              index = np.where( (wave_grid > xrange[0]) & (wave_grid < xrange[1]) )
       
              x = wave_grid
              y = signalSpecObs/max(signalSpecObs)     
              fig = Figure(figsize=(16,6))
              a = fig.add_subplot()#111)
              fig.subplots_adjust(top=0.98, bottom=0.18, left=0.04, right=0.96) 
              
              a.plot(x[index], y[index],color='white') #no lines shown              
              #a.axis(xmin=xrange[0],xmax=xrange[1])
              a.axis(xmin=min(x[index]), xmax=max(x[index]))
              a.set_xlabel("Wavelength (micron)", fontsize=12)
              a.set_ylabel("Transmission", fontsize=12)
     
        signalSpecObs = []
        noseSpecObs = []
        snSpecObs = []        
        for i in range(8):
            signalSpecObs = np.append(signalSpecObs, DICT_signalSpecObs[i]) 
            noiseSpecObs  = np.append(noiseSpecObs,DICT_noiseSpecObs[i])
            snSpecObs  = np.append(snSpecObs,DICT_snSpecObs[i])

        import matplotlib.pyplot as plt 
        
        fig = Figure(figsize=(16,6))
        host = fig.add_subplot()#111)
        fig.subplots_adjust(top=0.98, bottom=0.18, left=0.04, right=0.96) 
        #fig, host = plt.subplots(figsize=(6,6)) # (width, height) in inches
        
        par1 = host.twinx()
        host.set_xlim( (x[index])[0], (x[index])[-1] ) 
        host.set_ylim(0, 1.3*max(snSpecObs[index]))
        par1.set_ylim(0, 2*max(signalSpecObs[index]))

        host.set_xlabel("Wavelength (micron)", fontsize=12)
        host.set_ylabel("S/N per pixel")
        par1.set_ylabel("photons/pixel")

        color1 = "green" # plt.cm.viridis(0)
        color2 = "blue"  # plt.cm.viridis(0.5)
        color3 = "red"   # plt.cm.viridis(.9)

# =============================================================================
#         p1, = host.plot( wave_grid[index], snSpecObs[index], color=color1, label="S/N")
#         p2, = par1.plot( wave_grid[index], signalSpecObs[index], color=color2, label="signal")
#         p3, = par1.plot( wave_grid[index], noiseSpecObs[index], color=color3, label="noise")
# =============================================================================

        p1, = host.plot( DICT_wave_grid[0], DICT_snSpecObs[0], color=color1, label="S/N")
        p2, = par1.plot( DICT_wave_grid[0], DICT_signalSpecObs[0], color=color2, label="signal")
        p3, = par1.plot( DICT_wave_grid[0], DICT_noiseSpecObs[0], color=color3, label="noise")

        for i in range(1,8):
            p1, = host.plot( DICT_wave_grid[i], DICT_snSpecObs[i], color=color1, label="S/N")
            p2, = par1.plot( DICT_wave_grid[i], DICT_signalSpecObs[i], color=color2, label="signal")
            p3, = par1.plot( DICT_wave_grid[i], DICT_noiseSpecObs[i], color=color3, label="noise")

        lns = [p1, p2, p3]
        host.legend(handles=lns, loc='best')

#        fig.tight_layout()
            
        canvas = FigureCanvasTkAgg(fig, master=self.frame_out)
        canvas.get_tk_widget().place(x=2, y=410, width=1780, height=245)#pack()
        canvas.draw()
        
        self.printed_atmtrans = tranSpecObs[index]
        self.printed_background = bkSpecObs[index]     
        self.printed_throughput = tpSpecObs[index]
        self.printed_signal = signalSpecObs[index]
        self.printed_wavegrid = wave_grid[index]
        self.printed_noise = noiseSpecObs[index]
        self.printed_snr = snSpecObs[index]

       

# =============================================================================
    def PrintToFile(self):
        values = [(ingredient, var.get()) for ingredient, var in  self.buttons.items()]
        if ( (values[0])[1] ) == 1:
            np.savetxt(self.results_path+'Throughput.txt', np.transpose([self.printed_wavegrid,self.printed_throughput]),fmt='%.3f, %.3f')
        if ( (values[1])[1] ) == 1:
            np.savetxt(self.results_path+'Transmission.txt', np.transpose([self.printed_wavegrid,self.printed_atmtrans]),fmt='%.3f, %.3f')
        if ( (values[2])[1] ) == 1:
            np.savetxt(self.results_path+'Background.txt', np.transpose([self.printed_wavegrid,self.printed_background]),fmt='%.3f, %.3f')
        if ( (values[3])[1] ) == 1:
            np.savetxt(self.results_path+'Signal.txt', np.transpose([self.printed_wavegrid,self.printed_signal]),fmt='%.3f, %.3f')
        if ( (values[4])[1] ) == 1:
            np.savetxt(self.results_path+'Noise.txt', np.transpose([self.printed_wavegrid,self.printed_noise]),fmt='%.3f, %.3f')
        if ( (values[5])[1] ) == 1:
            np.savetxt(self.results_path+'SNR.txt', np.transpose([self.printed_wavegrid,self.printed_snr]),fmt='%.3f, %.3f')


# =============================================================================
# # =============================================================================
# # =============================================================================
# =============================================================================



    def XTcalc(self):
        all_parameters = self.collect_all_parameters()
        WaterVapor_Value = self.selected_WaterVapor.get()
        ready_to_go = self.validate(all_parameters)
        
        self.button_Calculate = Button(self.frame6, text="Calculate", command=self.XTcalc, bg="black")

# =============================================================================
# =============================================================================
# # Convert all_parameters entries to more manageable entities
#
#        band = all_parameters["bandpass"]
        slit_width = float(all_parameters["slit"])         #slit width in arcsec
        Entry_NrOfDithers = float(all_parameters["NofDithers"])
        theta = float(all_parameters["AngularExt"])  #source angular extent in arcsec 
        Nreads = 1   #int(all_parameters["NrFowlerPairs"])
        lineWl = float(all_parameters["CentralWl"])   #Central Wl (in AA or micron)
        FWHM = float(all_parameters["FWHM"])
        z_line = float(all_parameters["LineRedshift"])
        mag =float(all_parameters["SourceMagnitude"])   
        z_spec = float(all_parameters["MagnitudeRedshift"])
        Vega_band = all_parameters["Vega_band"]
        SN = float(all_parameters["DesiredSNR"])
        time = float(all_parameters["TotalExpTime"])
        lineF = float(all_parameters['LineFlux'])
        
        line_width  = FWHM  #initial value, prevents crash when using magnitudes (i.e. no line width)
        
#        print(self.slit_selected.get())
# =============================================================================
# =============================================================================
#       put everything in micron
#
        if ( (all_parameters["FluxORMag"] == "Use Line Flux") and (all_parameters["LineWlUnits"] == "Angstrom")):
           lineWl=lineWl/10000.0
#   
# =============================================================================
# =============================================================================
#   if the number of exposures is greater than 1, assume two dither positions
#
##        if (Entry_NrOfDithers >1 ) :
#           dither=2.0
#        else: 
#           dither=1.0   

# =============================================================================
# =============================================================================
#          the location of the code and the data spectra
#
        homedir = os.getcwd() 
        XTcalc_dir = os.getcwd() + '/XTcalc_dir'
        Paranal_sky_path = homedir + '/Paranal_sky_VIS/'
        CerroPachon_sky_path =  homedir+ '/CerroPachon_sky/'
        self.results_path = homedir + '/SCORPIO_Results/'
 
# =============================================================================
# =============================================================================
#          MOSIFRE Linearity Limits
#
#          2.15 e/ADU gain
#          1% non linearity 26K ADU= 55900 electrons
#          5% non linearity 37K ADUs = 79550 e-
#          saturation 43K ADUs = 92450 e-
# # =============================================================================
# =============================================================================
#         one_per_limit = 55900   #to be revised
#         five_per_limit = 79550  #to be revised
        sat_limit_IR = 92450       #to be revised
        sat_limit_VIS = 92450       #to be revised
# =============================================================================
#       
# =============================================================================
# if the magnitude is entered in Vega, change it to AB.
# conversions for J,H,Ks from Blanton et al 2005
# K from ccs
# Y from CFHT WIRCam
#
# =============================================================================   
        if ( (all_parameters["FluxORMag"] == 'Use magnitude') and (all_parameters["Magnitude System"] == "Vega")):                                                                            
           if Vega_band == 'U': 
               iVega = 0
               mag=mag+0.79
           elif Vega_band == 'B':
               iVega = 1
               mag=mag-0.09 
           elif Vega_band == 'V':
               iVega = 2
               mag=mag+0.02 
           elif Vega_band == 'R':
               iVega = 3
               mag=mag+0.21 
           elif Vega_band == 'I':
               iVega = 4
               mag=mag+0.45
           elif Vega_band== 'Y': 
               iVega = 5
               mag=mag+0.66
           elif Vega_band == 'J':
               iVega = 6
               mag=mag+0.91 
           elif Vega_band == 'H':
               iVega = 7
               mag=mag+1.39 
           elif Vega_band == 'K':
               iVega = 8
               mag=mag+1.95 
           elif Vega_band == 'Ks':
               iVega = 9
               mag=mag+1.85
        
        
# =============================================================================
# *************************************
# *************************************
#          CONSTANTS
# *************************************
# *************************************
#     
# =============================================================================
    #the speed of light in cm/s
        logc = np.log10(29979245800.)
    
    #planck's constant in erg*s
        logh = np.log10(6.626068)-27
    
    #in log(erg cm)
        loghc = logc+logh
    
        f_nu_AB=48.59
    
    #area of the telescope in cm^2
        AT=(800/2.)**2 * np.pi  # Area of the telescope ((800/2.)**2 * np.pi) [cm2]
        
    #slit width used in arcsec to measure R_theta
        slit_W=0.18*3	# SCORPIO scale is 0.18". Nominal slit width is 3 mirrors = 0.54"
    
    #spatial pixel scale in arcseconds/pixel
        pix_scale=0.18	# spatial pixel scale [arcsec/px]; corresponds to 3'x3' FoV over 1000x1000 pixels
    
#    #pixel size inthe dispersion direction
        pix_disp=0.18  #arcsecond/pixel
    
    #Number of pixels in dispersion direction on the detector
        tot_Npix_VIS=4096.
        tot_Npix_IR=2048.
    
    #Detector readnoise in electrons/pix CDS (correlated double sampling)
        self.det_RN_SingleFrame = 12
        det_RN_IR=12.  # "virtual" single sampling, 
        det_RN_VIS=5.  #, TBC
    
    
    
# =============================================================================
# *************************************
# *************************************
#          SKY CONSTANTS
# *************************************
# *************************************
# =============================================================================

# =============================================================================
# read in the atmospheric transparency
# From Gemini Observatory: Lord, S. D., 1992, NASA Technical Memorandum 103957
# default is 1.6mm water vapor column
# airmass=1
#      
# =============================================================================
# =============================================================================
        #1.3 Atmospheric Transmission
        #==============================================================================
        sky_transmission_VIS = np.loadtxt(os.path.join(Paranal_sky_path,"GenericTransmission_VIS.txt"),skiprows=1) #lambda[micron], transmission
        sky_transmission_VIS[:,0] = sky_transmission_VIS[:,0] *1E-4 # A => [micron]
        sky_transmission_VIS_Wave = sky_transmission_VIS[:,0].astype(float)
        sky_transmission_VIS_Flux = sky_transmission_VIS[:,1].astype(float)
#
        loghc = -15.701922659
        sky_spectrum_VIS = np.loadtxt(os.path.join(Paranal_sky_path, "UVES_Fluxed_SkyALL.txt")) #lambda [A]; [erg/sec/cm2/A/arcsec2]
        sky_spectrum_VIS[:,0] = sky_spectrum_VIS[:,0] * 1E-4 #A -> [micron]
        sky_spectrum_VIS[:,1] = sky_spectrum_VIS[:,1] * (10.**(-loghc) * sky_spectrum_VIS[:,0] * 1E-4) # erg/sec/cm2/A/arcsec2 => [ph/sec/cm2/A/arcsec2]
        sky_spectrum_VIS[:,1] = sky_spectrum_VIS[:,1] * 1E4 * 1E-1  # [ph/sec/cm2/nm/arcsec2] => ph/sec/m2/nm/arcsec2
        sky_spectrum_VIS[:,1] = sky_spectrum_VIS[:,1] * 1E3 # ph/sec/m2/nm/arcsec2 => [ph/sec/m2/micron/arcsec2
        sky_spectrum_VIS_Wave = sky_spectrum_VIS[:,0].astype(float)
        sky_spectrum_VIS_Flux = sky_spectrum_VIS[:,1].astype(float)

# 
# =============================================================================

        vp = str( int( float(all_parameters["WaterVapor"])*10) )  # "1.0" => "10..."
        am = str( int( float(all_parameters["Airmass"])*10) )
        if all_parameters["AirmassORWaterVapor"] != "Use Default":
             transpec_IR='cptrans_zm_'+vp+'_'+am+'.dat'            
             sky_spec_IR='cp_skybg_zm_' + vp +'_'+ am +'_ph.dat'
        else: # => DEFAULT
             transpec_IR='cptrans_zm_43_10.dat'  
             sky_spec_IR='cp_skybg_zm_43_10_ph.dat'
        sky_transmission_IR = np.loadtxt(CerroPachon_sky_path+transpec_IR)
        sky_transmission_IR_Wave = sky_transmission_IR[:,0].astype(float)   #wl in micron, ok
        sky_transmission_IR_Flux = sky_transmission_IR[:,1].astype(float)   # throughput 0-1, ok
    
#         # Infrared spectrum at  CP
        sky_spectrum_IR = np.loadtxt(CerroPachon_sky_path+sky_spec_IR)
        sky_spectrum_IR_Wave = sky_spectrum_IR[:,0].astype(float)   #wl in Angstrom, bad...
        sky_spectrum_IR_Wave = sky_spectrum_IR_Wave/1000            #wl in micron, GOOD
        sky_spectrum_IR_Flux = sky_spectrum_IR[:,1].astype(float)   # throughput 0-1, ok
#         #unuts are  photons/sec/arcsec^2/nm/m^2
# 
# =============================================================================
        #MOSFIRE USES DIFFERENT BACKGROUND SPECTRA    
#        sky_spectrum = np.loadtxt(sky_path+band+'sky_cal_pA.sav.dat')
#        sky_spectrum_Wave = sky_spectrum[:,0].astype(float)   #wl in Angstrom, bad...
#        sky_spectrum_Flux = sky_spectrum[:,1].astype(float)   # throughput 0-1, ok

        # lam = sky_spectrum_Wave   #consistent with IDL
        #mksky = sky_spectrum_Flux 
                
        
# =============================================================================
#     *************************************
#     *************************************
#            MOSIFRE Throughput
#     *************************************
#     *************************************
#     
#     ;elem_AR = elment AR per surface
#     ;ref_mir = mirror reflectance
#     ;win_AR = window AR per surface
#     ;grat_eff: grating effciency
#     ;fil_tran: filter transmission
#     ;qe: quantum efficiency
#     ;disp: dispersion in angstroms/pixel
#     ;cent: central wavelength in micron
#     ;background in magnitudes per arcsecond^2
#     ;f_not: log of magnitude zero point in erg/s/cm^2/micron
#     ;dark current in electrons per second
#     ;rt: R-theta product: multiply by slit width to get resolution
#     ;SMRef: SOAR Mirror reflectance (placeholder only, as it is included in Silver throughput)
#     
# =============================================================================
    
        g_grism_stat={
# =============================================================================
#             "elem_AR" :0.99, 
#             "ref_mir" :0.98, 
#             "win_AR": 0.988, 
#             "grat_eff": 0.72,
#             "fil_trans": 0.93, 
#             "qe": 0.88, 
#             "disp": 2.170, 
#             "lambda": 2.2, 
#             "background": 16, 
#             "f_not": np.log10(3.8)-7, 
            "dark": 0.005, 
#             "rt": 3620.0*slit_width, 
#             "SMRef":1.00 
# =============================================================================
            "disp": 0.375818,	# dispersion [angstrom/px]
            "lambda": 0.4600,		# central wavelength [microns]
            "rt" : 4000 * 0.18*3        # instrument [Rxslit_W]
            }
    
        r_grism_stat={
# =============================================================================
#             "elem_AR": 0.992, 
#             "ref_mir": 0.985, 
#             "win_AR": 0.985,  
#             "grat_efF": 0.65, 
#             "fil_trans": 0.95, 
#             "qe": 0.88, 
#             "disp": 1.629, 
#             "lambda": 1.65, 
#             "background": 16.6, 
#             "f_not": np.log10(1.08)-6, 
            "dark": 0.005, 
#             "rt": 3660.0*slit_width, 
#             "SMRef": 1.00
# =============================================================================
            "disp":  0.388345,	# dispersion [angstrom/px]
            "lambda": 0.6115,		# central wavelength [microns]
            "rt" : 4600 * 0.18*3        # instrument [Rxslit_W]
            }
    
        i_grism_stat={ 
# =============================================================================
#             "elem_AR": 0.985, 
#             "ref_mir": 0.98, 
#             "win_AR": 0.985, 
#             "grat_eff": 0.8,
#             "fil_trans": 0.9, 
#             "qe": 0.8, 
#             "disp": 1.303, 
#             "lambda": 1.25, 
#             "background": 16.8, 
#             "f_not": np.log10(2.90)-6, 
            "dark": 0.005, 
#             "rt":3310.0*slit_width, 
#             "SMRef": 1.00
# =============================================================================
            "disp":0.425926,	# dispersion [angstrom/px]
            "lambda":0.7400,		# central wavelength [microns]
            "rt": 4503 * 0.18*3        # instrument [Rxslit_W]
            }
    
        z_grism_stat={
# =============================================================================
#             "elem_AR": 0.985, 
#             "ref_mir": 0.98, 
#             "win_AR": 0.985, 
#             "grat_eff": 0.8,
#             "fil_trans": 0.9, 
#             "qe": 0.8, 
#             "disp": 1.086, 
#             "lambda": 1.05, 
#             "background": 17.3, 
#             "f_not": np.log10(7.45)-6, 
            "dark": 0.005, 
#             "rt": 3380.0*slit_width, 
#             "SMRef": 1.00 
# =============================================================================
            "disp": 0.506101,	# dispersion [angstrom/px]
            "lambda": 0.8750,		# central wavelength [microns]
            "rt": 4511 * 0.18*3        # instrument [Rxslit_W]
            }

        Y_grism_stat={
# =============================================================================
#             "elem_AR" :0.99, 
#             "ref_mir" :0.98, 
#             "win_AR": 0.988, 
#             "grat_eff": 0.72,
#             "fil_trans": 0.93, 
#             "qe": 0.88, 
#             "disp": 2.170, 
#             "lambda": 2.2, 
#             "background": 16, 
#             "f_not": np.log10(3.8)-7, 
            "dark": 0.005, 
#             "rt": 3620.0*slit_width, 
#             "SMRef":1.00 
# =============================================================================
            "disp": 0.847700,	# dispersion [angstrom/px]
            "lambda": 1.0400,		# central wavelength [microns]
            "rt" : 4055 * 0.18*3        # instrument [Rxslit_W]
            }
    
        J_grism_stat={
# =============================================================================
#             "elem_AR": 0.992, 
#             "ref_mir": 0.985, 
#             "win_AR": 0.985,  
#             "grat_efF": 0.65, 
#             "fil_trans": 0.95, 
#             "qe": 0.88, 
#             "disp": 1.629, 
#             "lambda": 1.65, 
#             "background": 16.6, 
#             "f_not": np.log10(1.08)-6, 
            "dark": 0.005, 
#             "rt": 3660.0*slit_width, 
#             "SMRef": 1.00
# =============================================================================
            "disp":  1.03271,	# dispersion [angstrom/px]
            "lambda":  1.2500,		# central wavelength [microns]
            "rt" : 4006* 0.18*3        # instrument [Rxslit_W]
            }
    
        H_grism_stat={ 
# =============================================================================
#             "elem_AR": 0.985, 
#             "ref_mir": 0.98, 
#             "win_AR": 0.985, 
#             "grat_eff": 0.8,
#             "fil_trans": 0.9, 
#             "qe": 0.8, 
#             "disp": 1.303, 
#             "lambda": 1.25, 
#             "background": 16.8, 
#             "f_not": np.log10(2.90)-6, 
            "dark": 0.005, 
#             "rt":3310.0*slit_width, 
#             "SMRef": 1.00
# =============================================================================
            "disp":1.34252,	# dispersion [angstrom/px]
            "lambda":1.6300,		# central wavelength [microns]
            "rt":4019 * 0.18*3        # instrument [Rxslit_W]
            }
    
        K_grism_stat={
# =============================================================================
#             "elem_AR": 0.985, 
#             "ref_mir": 0.98, 
#             "win_AR": 0.985, 
#             "grat_eff": 0.8,
#             "fil_trans": 0.9, 
#             "qe": 0.8, 
#             "disp": 1.086, 
#             "lambda": 1.05, 
#             "background": 17.3, 
#             "f_not": np.log10(7.45)-6, 
            "dark": 0.005, 
#             "rt": 3380.0*slit_width, 
#             "SMRef": 1.00 
# =============================================================================
            "disp": 1.77502,	# dispersion [angstrom/px]
            "lambda": 2.1750,		# central wavelength [microns]
            "rt": 4927 * 0.18*3        # instrument [Rxslit_W]
            }
   
# =============================================================================
        grism_list = [g_grism_stat, r_grism_stat, 
                      i_grism_stat, z_grism_stat, 
                      Y_grism_stat, J_grism_stat, 
                      H_grism_stat, K_grism_stat]
        SCORPIO_throughput_list = [self.SCORPIO_throughput_g,self.SCORPIO_throughput_r, 
                                   self.SCORPIO_throughput_i,self.SCORPIO_throughput_z,
                                   self.SCORPIO_throughput_Y ,self.SCORPIO_throughput_J,
                                   self.SCORPIO_throughput_H,self.SCORPIO_throughput_K]

        GeminiTel_wl_list = [self.GeminiTel_wl_g,self.GeminiTel_wl_r, 
                             self.GeminiTel_wl_i,self.GeminiTel_wl_z,
                             self.GeminiTel_wl_Y ,self.GeminiTel_wl_J,
                             self.GeminiTel_wl_H,self.GeminiTel_wl_K]
        GeminiTel_th_list = [self.GeminiTel_th_g,self.GeminiTel_th_r, 
                             self.GeminiTel_th_i,self.GeminiTel_th_z,
                             self.GeminiTel_th_Y ,self.GeminiTel_th_J,
                             self.GeminiTel_th_H,self.GeminiTel_th_K]
# =============================================================================

# =============================================================================
# # =============================================================================
# # # STAR TMAIN LOOP ON BANDPASSES

# =============================================================================
#         SCORPIO_tpSpecObs = np.empty(0)
#         SCORPIO_wave_grid = np.empty(0)
#         SCORPIO_raw_bkSpecObs = np.empty(0)
#         SCORPIO_fltSpecObs      = np.empty(0)
#         SCORPIO_tranSpecObs     = np.empty(0)
#         SCORPIO_bkSpecObs       = np.empty(0)
#         SCORPIO_signalSpecObs   = np.empty(0)
#         SCORPIO_noiseSpecObs    = np.empty(0)
#         SCORPIO_snSpecObs       = np.empty(0)
# =============================================================================

        SCORPIO_tpSpecObs = {}
        SCORPIO_wave_grid = {}
        SCORPIO_raw_bkSpecObs = {}
        SCORPIO_fltSpecObs      = {}
        SCORPIO_tranSpecObs     = {}
        SCORPIO_bkSpecObs       = {}
        SCORPIO_signalSpecObs   = {}
        SCORPIO_noiseSpecObs    = {}
        SCORPIO_snSpecObs       = {}
        SCORPIO_sn_index       = {}

        SCORPIO_summary_struct = []#
        
#        filt_index = np.empty(8, dtype=object)


# =============================================================================

# =============================================================================

        if ( (all_parameters["TypeOfSpectrum"] == "My own spectrum") & (all_parameters["FluxORMag"] != 'Use Line Flux')) : 
            self.read_SourceSpectrum()
            #Redshift is applied only to the wavelenghts
            self.user_Wave=self.user_Wave*(1+z_spec)
            Vega_lambda  = [0.36, 0.438,0.545,0.798,1.04,1.25,1.63,2.175]
            i_center_lambda = np.where(abs(self.user_Wave - Vega_lambda[iVega])==min(abs(self.user_Wave - Vega_lambda[iVega]))) 
            mean_Flux = np.mean(self.user_Flux[i_center_lambda])





# # =============================================================================
# #  => LEVEL 9: LOOP ON FILTERS  =============================================================================
        for i in range(8):
            print(i)

            if i == 0:
                NExp = self.init_NExp_gr.get() * self.init_Entry_NrOfDitheredPairs.get() * 2
            if i == 1:
                NExp = self.init_NExp_gr.get() * self.init_Entry_NrOfDitheredPairs.get() * 2
            if i == 2:
                NExp = self.init_NExp_iz.get() * self.init_Entry_NrOfDitheredPairs.get() * 2
            if i == 3:
                NExp = self.init_NExp_iz.get() * self.init_Entry_NrOfDitheredPairs.get() * 2
            if i == 4:
                NExp = self.init_NExp_Y.get() * self.init_Entry_NrOfDitheredPairs.get() * 2
            if i == 5:
                NExp = self.init_NExp_J.get() * self.init_Entry_NrOfDitheredPairs.get() * 2
            if i == 6:
                NExp = self.init_NExp_H.get() * self.init_Entry_NrOfDitheredPairs.get() * 2
            if i == 7:
                NExp = self.init_NExp_K.get() * self.init_Entry_NrOfDitheredPairs.get() * 2

            print('NExp: ', NExp)
# =============================================================================
            if i<=3:   # PARAMS for VIS  vs. IR channels go here
                tot_Npix = tot_Npix_VIS #VIS channels
                sky_transmission_Wave = sky_transmission_VIS_Wave
                sky_transmission_Flux = sky_transmission_VIS_Flux
                sky_spectrum_Wave = sky_spectrum_VIS_Wave   
                sky_spectrum_Flux = sky_spectrum_VIS_Flux   
                det_RN = det_RN_VIS
                sat_limit = sat_limit_VIS
            else: #IR Channels
                tot_Npix = tot_Npix_IR
                sky_transmission_Wave = sky_transmission_IR_Wave
                sky_transmission_Flux = sky_transmission_IR_Flux
                sky_spectrum_Wave = sky_spectrum_IR_Wave   
                sky_spectrum_Flux = sky_spectrum_IR_Flux   
                det_RN = det_RN_IR
                sat_limit = sat_limit_IR
            stat=grism_list[i]
# =============================================================================
# **************************
#      passband THROUGHPUT
# **************************
            th_SCORPIO = SCORPIO_throughput_list[i]
            th_SCORPIO_wl = np.array(th_SCORPIO[:,0])  # Already in micron
            th_SCORPIO_th = np.array(th_SCORPIO[:,1])
            
            th_GeminiTel_wl = np.array(GeminiTel_wl_list[i]) /1000.0 # now in micron
            th_GeminiTel_th = np.array(GeminiTel_th_list[i])
            
            th = np.array(th_SCORPIO_th) 
            th_wave = np.array(th_SCORPIO_wl) #now in micron
            throughput = th 
            filt_wave = th_wave
            
# =============================================================================
#     real FWHM resolution
            R=stat["rt"]/slit_width
# =============================================================================
#     slit width in pixels along the dispersion direction
            swp=slit_width/pix_disp
# =============================================================================
#     spectral coverage in micron)
            cov=tot_Npix*(stat["disp"]/10000.)
# =============================================================================
# *************************************
# *************************************
#      IF using a specific line flux
# *************************************
# *************************************
            if all_parameters["FluxORMag"] == 'Use Line Flux':
#  =============================================================================
# =============================================================================
#         figure out the relavant wavelength range
#       
#           the observed line wavelength in micron
                center = lineWl * (1+z_line)   #lineWl*(1+z)
                filter_limit_0 = min(filt_wave)
                filter_limit_1 = max(filt_wave)
                if ( (i == 7) and (center > filter_limit_1 ) ):
                    messagebox.showerror(
                        title=None, message="Central Wavelength " + str(center ) + " is out of bandpass \n changing redshift to match bandpass center")
                if ( (center >= filter_limit_0) and (center < filter_limit_1 ) ):                
#           resolution at the central wavelength in micron
                    res = center/R    
#           the width of the spectral line before going through the spectrograph
                    real_width = center*FWHM*10**(-logc+5)      
#           the line width in micron that would be observed
                    line_width = np.sqrt(real_width**2+res**2)
                else:
                    res=0
                    real_seidth=0
                    line_width=0

# =============================================================================      
# =============================================================================

            else: #   BROAD BAND FILTERS
    
# =============================================================================
#      we are calculating for a broad band flux: 
# =============================================================================
                center=stat["lambda"]
#       resolution at the central wavelength in micron
                res=center/R

# =============================================================================
# # =============================================================================
# #
# #          DEGRADE RESOLUTION
# # 
# #     convolve the filter with bandpass resolution
# # =============================================================================
# # =============================================================================
# =============================================================================
# =============================================================================
            bandpass_degrade = self.degrade_resolution(wavelengths=th_wave, 
                                    flux=throughput, 
                                    center_wave=stat["lambda"], 
                                    spec_res=R, 
                                    disp = stat["disp"],
                                    px_tot = tot_Npix)
        

#        band_index = np.where(bandpass_degrade['flux'] > 0.01)[0]
            band_index = np.where( (bandpass_degrade["lam"] >= filt_wave[1]) & (bandpass_degrade["lam"] <= filt_wave[-2]) )
            fltSpecObs = np.array(bandpass_degrade["flux"][band_index])
        
#            tpSpecObs = fltSpecObs
#            tpSpecObs = np.array(bandpass_degrade["flux"][band_index])  #2251 values
#            v = tpSpecObs
#            v2 = [0 if i < 0 else i for i in v]
#            tpSpecObs = np.array(v2)
        
#       a tighter selection of the indexes with high throuhgput for the S/N
            filt_index=np.where(fltSpecObs > 0.05)[0]
        
            wave_grid = np.array(bandpass_degrade["lam"][band_index])
#            wave_grid  = np.insert(wave_grid,0,float(wave_grid[0]*0.9999))
#            wave_grid  = np.append(wave_grid,float(wave_grid[-1]*1.0001))
#            fltSpecObs  = np.insert(fltSpecObs,0,0.00)
#            fltSpecObs  = np.append(fltSpecObs,0.00)
            tpSpecObs = fltSpecObs

# 
# =============================================================================

# =============================================================================
# =============================================================================
        
            th_GeminiTel_degrade = self.degrade_resolution(wavelengths=th_GeminiTel_wl, 
                                    flux = th_GeminiTel_th, 
                                    center_wave=stat["lambda"], 
                                    spec_res=R, 
                                    disp = stat["disp"],
                                    px_tot = tot_Npix)
#        th_tel_degrade_SpecObs = np.array(bandpass_degrade["flux"][band_index])
#        th_GeminiTel_degrade_Wave = th_GeminiTel_degrade["lam"][band_index]
            th_GeminiTel_degrade_Flux = th_GeminiTel_degrade["flux"][band_index]
 #           th_GeminiTel_degrade_Flux  = np.insert(th_GeminiTel_degrade_Flux,0,0.00)
 #           th_GeminiTel_degrade_Flux  = np.append(th_GeminiTel_degrade_Flux,0.00)

# =============================================================================
# =============================================================================
        
            th_ADC_degrade = self.degrade_resolution(wavelengths=np.array(self.SCORPIO_throughput_ADC[:,0]),
                                    flux = np.array(self.SCORPIO_throughput_ADC[:,1]), 
                                    center_wave=stat["lambda"], 
                                    spec_res=R, 
                                    disp = stat["disp"],
                                    px_tot = tot_Npix)
#        th_tel_degrade_SpecObs = np.array(bandpass_degrade["flux"][band_index])
#        th_GeminiTel_degrade_Wave = th_GeminiTel_degrade["lam"][band_index]
            th_ADC_degrade_Flux = th_ADC_degrade["flux"][band_index]
 #           th_ADC_degrade_Flux  = np.insert(th_ADC_degrade_Flux,0,0.00)
 #           th_ADC_degrade_Flux  = np.append(th_ADC_degrade_Flux,0.00)

# =============================================================================
# =============================================================================
#       the relavant portion of the spectrum
#        bandpass_index = np.where(fltSpecObs > 0.1)[0]
#        fltSpecObs=fltSpecObs[bandpass_index]
# =============================================================================
# =============================================================================
# #    
# =============================================================================
# =============================================================================
#       convolve the atm_Transmission spectrum with the resolution
#
            atmtrans_degrade = self.degrade_resolution(wavelengths=sky_transmission_Wave, 
                                        flux= sky_transmission_Flux, 
                                        center_wave=stat["lambda"],  
                                        spec_res=R, 
                                        disp = stat["disp"], 
                                        px_tot = tot_Npix)
            tranSpecObs = np.array(atmtrans_degrade["flux"][band_index])   #2251 values    
 #           tranSpecObs = np.insert(tranSpecObs,0,0.00)
 #           tranSpecObs = np.append(tranSpecObs,0.00)
            
# =============================================================================
# =============================================================================
# =============================================================================
# #       convolve the throughput spectrum with the resolution
# #
# #        good = np.logical_and(th_wave >= wave_grid[0],th_wave <= wave_grid[-1])
# #       th_wave_selected = th_wave#[good]
# #        throughput_selected = throughput#[good]
#         throughput_degrade = self.degrade_resolution(wavelengths=th_wave,#_selected, 
#                                         flux=throughput,#,_selected, 
#                                         center_wave=stat["lambda"],  
#                                         spec_res=R, 
#                                         disp = stat["disp"], 
#                                         px_tot = tot_Npix)
#         tpSpecObs = np.array(throughput_degrade["flux"][band_index])  #2251 values
#         v = tpSpecObs
#         v2 = [0 if i < 0 else i for i in v]
#         tpSpecObs = np.array(v2)
# 
# =============================================================================

# =============================================================================
#         SAMI_throughput_degrade = self.degrade_resolution(wavelengths=self.SAMI_CCD_throughput_Wave,#_selected, 
#                                         flux=self.SAMI_CCD_throughput_Flux,#,_selected, 
#                                         center_wave=stat["lambda"],  
#                                         spec_res=R, 
#                                         disp = stat["disp"], 
#                                         px_tot = tot_Npix)
#         SAMISpecObs = np.array(SAMI_throughput_degrade["flux"][band_index])  #2251 values
# #        v = tpSpecObs
# =============================================================================
#        v2 = [0 if i < 0 else i for i in v]
#        tpSpecObs = np.array(v2)


# =============================================================================
# =============================================================================
#       convolve the background spectrum with the resolution
#
# =============================================================================
#        ;background in phot/sec/arcsec^2/nm/m^2

        #sky_spectrum_Flux = sky_spectrum_Flux/(0.7*pix_scale*10.**(loghc+4.0))*sky_spectrum_Wave*10**(4.+1.)
 
#        sky_spectrum_Wave_selected = sky_spectrum_Wave#[good]
#        sky_spectrum_Flux_selected = sky_spectrum_Flux#[good]
            background_degrade = self.degrade_resolution(wavelengths=sky_spectrum_Wave,#_selected, 
                                        flux=sky_spectrum_Flux,#_selected, 
                                        center_wave=stat["lambda"],  
                                        spec_res=R, 
                                        disp = stat["disp"], 
                                        px_tot = tot_Npix)
        #for now - sent the filt_index to be the NONzero_index
            background_degrade["flux"][background_degrade["flux"]<0]=0
            raw_bkSpecObs  = background_degrade["flux"][band_index]  #2251
        #filt_index = np.where(raw_bkSpecObs>0)[0]
        #filt_index = band_index  #used later, to keep consistency...
 #           raw_bkSpecObs = np.insert(raw_bkSpecObs,0,0.00)
 #           raw_bkSpecObs = np.append(raw_bkSpecObs,0.00)
 
  # =============================================================================
  # # =============================================================================
  # #      Final THROGHPUT    
  # #  
  # # =============================================================================
            tpSpecObs = tranSpecObs * th_GeminiTel_degrade_Flux * tpSpecObs     
            if self.ADCon.get() == 1:
                print('AC on')
                tpSpecObs =  tpSpecObs * th_ADC_degrade_Flux   
  
 

# 
# =============================================================================
#     *************************************
#     *************************************
#     ;     Using a specific line flux
#     *************************************
#     *************************************
#
            if all_parameters["FluxORMag"] == 'Use Line Flux':
# =   
#           the location inside the FWHM of the line
                line_index = np.where(abs(wave_grid - center) < 0.5*line_width)[0]
#           the area used to calcclate the S/N
# =============================================================================
                if line_index.size == 0:    #SKIP if the line is not in the passband
                    lineF = 0 
#                     bkSpecObs = 0
#                     mkBkgd = 0
#                     mag_back = 0
#                     signalATM = 0
#                     sigma = 0
                    signal = 0
                    background = 0
                    dark = 0
                    RN = 0
                    noise = 0
#                     sn_index = 0
#                     signal_spec = 0
                    #now a convoluted way to create ab array of zero's 
                    sig_rateSpecObs = np.array(wave_grid)*0.#(tuple(map(operator.sub,band_index,band_index))   
                    nPixSpatial = 1
                    nPixSpec = 1
#                     eppSpec = 0
# =============================================================================

                if line_index.size != -1:    #SKIP if the line is not in the passband
                    sn_index=line_index
#           ;now send the background spectrum through the telescope by
#           ;multiplying the throughput, the
#           ;slit_width, the angular extent (theta), the area of the
#           ;telescope, and the pixel scale in nm
#     
#           ;this gives phot/sec/pixel
                    bkSpecObs = raw_bkSpecObs * tpSpecObs * slit_width * theta * (AT*10.**(-4)) * (stat["disp"]/10.0)
# =         ;determine the average background
#           ;within the FWHM of the line
#           ;in photons per second per arcsec^2 per nm per m^2
                    mkBkgd=np.mean(sky_spectrum_Flux[np.where(abs(sky_spectrum_Wave - center) <= 0.5*line_width)])
#   #       ;fv_back=mkBkgd*(center)^2*10^(-4+3-4-c)
    #       ;what does this correspond to in AB mags/arcsec^2
    #       ;go to erg/s/cm^2/Hz
    #       ;10^-4 for m^2 to cm^2
    #       ;10^3 for micron to nm
    #       ;lam^2/c to covert from d(lam) to d(nu) (per Hz instead of per nm)
    #       ;hc/lam to convert photons to ergs
                    mag_back=-2.5*(np.log10(mkBkgd*center)-4+3+logh)-f_nu_AB
#       ; the signal in electrons per second that will hit the telsecope
#       ; as it hits the atmosphere (ie need
#       ; to multiply by the throughput and
#       ; the atmospheric transparency
                if line_index.size != 0:    #
                    lineF = float(self.Entry_LineFlux.get()) 
                    signalATM = lineF * 10**(-17-loghc-4) * center * AT
#       ;the width of the line in sigma - not FWHM
#       ;in micron
                    sigma=line_width/(2*np.sqrt(2*np.log(2)))
#       ;a spectrum version of the signal
#       ;phot per second per pixel (without atm or telescope)
#       ; ie total(signal_spec/signal) with
#       ; equal resolution of wave_grid /
#       ; stat.disp in micron
                    signal_spec=signalATM*(1/(np.sqrt(2*np.pi)*sigma))*np.exp(-0.5*(wave_grid-center)**2/sigma**2)*stat["disp"]/10.**4
#       ; the spectrum of the signal as detected
                    sig_rateSpecObs=signal_spec * tpSpecObs * tranSpecObs
# =============================================================================
# =============================================================================x
# # #       SLIT LOSSES
# # =============================================================================
# =============================================================================
 #               if self.selected_GLAO.get() == "SAM": 
 #                  beta = 3.   # ;appropriate from SAM, e-mail from Tokovinin; set =3 for VLT/FORS1 and =100 for a Gaussian profile
 #               else:
                    beta = 10. 
                    Nslit_X = round(float(self.slit_selected.get())/0.1667)
                    Nslit_Y = round(theta*2/0.1667)
            #print(Nslit_X,Nslit_Y)
                    slit_loss = self.slit_loss(theta,beta,Nslit_X,Nslit_Y)            
            #print(slit_loss)
                    sig_rateSpecObs = sig_rateSpecObs * slit_loss
#       ; the number of pixels in the spectral direction
                nPixSpec = (line_width*10000.0)/stat["disp"]
#       ;the spatial pixel scale
                nPixSpatial=theta/pix_scale
#       ;The number of pixels per FWHM observed
                Npix= nPixSpec * nPixSpatial
#       
# =============================================================================
# =============================================================================

#       ;*************************************
#       ;*************************************
#       ; we are calculating for a broad band flux
#       ;*************************************
#       ;*************************************
#       
            #=> 13: BEGIN BROAD BAND CALCULATION
            else: #use 

#       ; the area used to calculate the S/N
                sn_index=filt_index
                mag_back=-2.5*(np.log10(np.mean(raw_bkSpecObs)*center)-4+3+logh)-f_nu_AB
#       ;now send the background spectrum through the telescope by
#       ;multiplying the throughput, the
#       ;slit_width, the angular extent, the area of the
#       ;telescope, and the pixel scale in nm
#       ;this gives phot/sec/pixel
                bkSpecObs = raw_bkSpecObs * tpSpecObs * slit_width * theta * AT*1E-4 * (stat["disp"]/10.0)#       ;     bkSpecObs = raw_bkSpecObs * tpSpecObs * (0.5)^2 * (AT*10.^(-4)) * (stat.disp/10.0)


#          ;*************************************
#          ;*************************************
#          ; using the user input spectrum
#          ;*************************************
#          ;*************************************
                #=> 17: BEGIN MY OWN SPECTRUM
                if all_parameters["TypeOfSpectrum"] == "My own spectrum": 
#                    self.read_SourceSpectrum()
#                    #Redshift is applied only to the wavelenghts
#                    self.user_Wave=self.user_Wave*(1+z_spec)
#                   does the user spectrum cover the full band pass and are the wavelengths in micron?
                    #=> 21: BEGIN MESSAGE WARNING 
# =============================================================================
#                     if ((min(self.user_Wave) > min(filt_wave)) or (max(self.user_Wave) < max(filt_wave))):
#                         warning = 'The read-in spectrum from ' + str(self.source_filename) \
#                         + 'does not span the full wavelength coverage of the ', band,' band ' \
#                         + 'or is not in the proper format. The correct format is ' \
#                         + 'observed-frame wavelength in micron or Angstroms and flux in ' \
#                         + 'erg/s/cm2 in two column format with a space or comma ' \
#                         + 'as the delimiter. Also please check that you have choosen the correct ' \
#                         + 'wavelength units on the GUI.'
#                         messagebox.showinfo(
#                             title='Check spectrum',
#                             message=warning
#                             )       
#                     #<= 21: END MESSAGE WARNING 
# =============================================================================

                    userSig_degrade = self.degrade_resolution(wavelengths=self.user_Wave, 
                                        flux= self.user_Flux, 
                                        center_wave=stat["lambda"],  
                                        spec_res=R, 
                                        disp = stat["disp"], 
                                        px_tot = tot_Npix)
                    userSig = np.array(userSig_degrade["flux"][band_index])   #2251 values
                    
                    if max(userSig <= 0.0):
                        userSig = np.array(wave_grid)*0.00
#                  userSig = np.insert(userSig,0,0.00)
#                  userSig = np.append(userSig,0.)
#         ;multiply by the normalized filter transmission        
#                    filt_shape = fltSpecObs/max(fltSpecObs)
#                    userSig = userSig*filt_shape

                    #=> 21: BEGIN AB MAGS
                    if self.selected_MagnitudeSystem.get() == 'AB':
                        df = self.read_ABfilters()
                        wl_um = df[:,0] / 10000.0   #in micron
                        tp   = df[:,1]
                        good_index  = np.where(tp > 0.05)
                        AB_filter_degrade = self.degrade_resolution(wavelengths=wl_um,#[good_index], 
                                        flux= tp,#[good_index],  
                                        center_wave=np.mean(wl_um),#[good_index]),  
                                        spec_res=R, 
                                        disp = stat["disp"], 
                                        px_tot = tot_Npix)
                        AB_filter_degrade = np.array(AB_filter_degrade["flux"])#[good_index])   #2251 values
                        Source_filter_degrade = self.degrade_resolution(wavelengths=wl_um, #[good_index], 
                                        flux= self.user_Flux, #[good_index],  
                                        center_wave=np.mean(wl_um),#[good_index]),  
                                        spec_res=R, 
                                        disp = stat["disp"], 
                                        px_tot = tot_Npix)
                        Source_filter_degrade = np.array(Source_filter_degrade["flux"])#[good_index])   #2251 values
                        Source_filter_degrade = Source_filter_degrade * AB_filter_degrade
#         ;make the total match the broad band magnitude
                        scale=10.0**(-0.4*(mag+f_nu_AB))/np.mean(Source_filter_degrade)
                    #=> 21: END AB MAGS 
                    #=> 21: BEGIN JOHNSON MAGS 
                    else:
#         ;multiply by the normalized filter transmission        
#                        filt_shape = fltSpecObs/max(fltSpecObs)
#                        userSig = userSig*filt_shape
#         ;make the total match the broad band magnitude
                        scale=10.0**(-0.4*(mag+f_nu_AB))/mean_Flux
#         ;raw fv spec
                    #<=  21 END JOHNSON MAGS 
                    raw_fv_sig_spec = userSig*scale
#         ;convert to flux hitting the primary in flux hitting the primary in
#         ;phot/sec/micron (if the earth had no atmosphere)
#         ;phot/sec/micron = fnu * AT / lam / h
                    signal_spec=raw_fv_sig_spec*10.**(-1*logh)*AT / wave_grid
                #=> 17: END MY OWN SPECTRUM
  
#         
# =============================================================================        
# =============================================================================
#         ;*************************************
#         ;*************************************
#         ; using a flat F_nu spec (DEFAULT)
#         ;*************************************
#         ;*************************************
                #=> 17: BEGIN FLAT F_NU
                else:
             
#         ;fv=10^((-2/5)*MagAB-48.59) (erg/s/cm^2/Hz)
#         ;convert to flam: flam=fv*c/lam^2 (erg/s/cm^2/micron)
#         ;covert to photons: phot/sec/micron = fnu * AT / lam / h#         
#         ;flux hitting the primary in
#         ;phot/sec/micron (if the earth had no atmosphere)
                    signal_spec=10.0**(-0.4*(mag+f_nu_AB)-logh) * AT / wave_grid
                #=> 17: END FLAT F_NU#         
# =============================================================================        
# =============================================================================
#        ENDED DEFINION OF SIGNAL SPECTRUM (LINE FLUX OR SED)
# =============================================================================        
# =============================================================================

#       ;multiply by the atmospheric transparency
                signal_spec=signal_spec * tranSpecObs

#       ; now put it through the throughput of the telescope/instrument
#       ; phot/sec/micron
                sig_rateSpecObs= signal_spec * tpSpecObs
# =============================================================================
# =============================================================================
# # #       SLIT LOSSES (we are doing spectroscopy...)
# # =============================================================================
# =============================================================================
#           beta = 2.   # ;appropriate from SAM, e-mail from Tokovinin; set =3 for VLT/FORS1 and =100 for a Gaussian profile
#               if self.selected_GLAO.get() == "SAM": 
#                   beta = 3.   # ;appropriate from SAM, e-mail from Tokovinin; set =3 for VLT/FORS1 and =100 for a Gaussian profile
#               else:
                beta = 10. 
                Nslit_X = round(float(self.slit_selected.get())/0.1667)
                Nslit_Y = round(theta*2/0.1667)
                #print(Nslit_X,Nslit_Y)
                slit_loss = self.slit_loss(theta,beta,Nslit_X,Nslit_Y)            
                #print(slit_loss)
                sig_rateSpecObs = sig_rateSpecObs * slit_loss
#               now for phot/sec/pix multiply by micron/pix
                sig_rateSpecObs=sig_rateSpecObs * (stat["disp"]/10000.0)
#               number of pixels per resolution element in the spectral direction
                nPixSpec = (res*10000.0)/stat["disp"]
#               the spatial pixel scale
                nPixSpatial=theta/pix_scale
#               The number of pixels per FWHM observed
                Npix = nPixSpec * nPixSpatial     
            #<= 13: END BROAD BANDCALCULATION
#  =============================================================================
#   ;*************************************
#   ; END of calculation of SIGNAL
#   ;*************************************
# =============================================================================

      
      
# =============================================================================
#         ;*************************************
#         ;*************************************
#         ; Determine EXP TIME 
#         ;*************************************
#         ;*************************************         

            #=> 13: BEGIN EXP TIME CALCULATION
            if all_parameters["ExpTimeORSNR"] == 'Determine Exposure Time':

#             a) "SN" is known
#             b) "time" has to be found
#                
#       ; differentiate between total exposure time
#       ; and amount of time of individual exposures
#       
#       ;     ; figure out how long it takes
#       ;     qb=bkSpecObs + stat.dark*nPixSpatial + sig_rateSpecObs
#       ;     qa=-nPixSpec * sig_rateSpecObs^2/SN[0]^2
#       ;     qc=det_RN^2/Nreads*nPixSpatial
#       #       
#       ;if calulating with a line flux, assume S/N over the line
#       ; other wise, S/N per spectral pixel
                if i >= 4:
                    K1,K2,K3,time_IR= self.CalculateSamplingParameters()
                    det_RN = np.sqrt(K1[i-4])
                #=> 17: BEGIN ExpTime/LineFlux
                if all_parameters["FluxORMag"] == 'Use Line Flux':    #SKIP if the line is not in the passband 
                    if line_index.size != 0:
                        qa = -nPixSpec * sig_rateSpecObs[sn_index]**2/SN**2
#                        qb = NExp*bkSpecObs[sn_index] + NExp*stat["dark"]*nPixSpatial + sig_rateSpecObs[sn_index]
#                        qc = NExp*det_RN**2/Nreads*nPixSpatial*NExp
                        qb = bkSpecObs[sn_index] + stat["dark"]*nPixSpatial + sig_rateSpecObs[sn_index]
                        qc = det_RN**2/Nreads*nPixSpatial*NExp
                        timeSpec=(-qb -np.sqrt( qb**2 - 4*qa*qc ))/(2*qa)
                        time=np.median(timeSpec)
                        time=float(time)
                    else:
                        time = 0.0
                #=> 17: BEGIN ExpTime/SED
                else: # use CONTINUUM SED
                    qa=-sig_rateSpecObs**2/SN**2
#                    qb = NExp*bkSpecObs + NExp*stat["dark"]*nPixSpatial + sig_rateSpecObs
#                    qc = NExp*det_RN**2/Nreads*nPixSpatial*NExp
                    qb = bkSpecObs + stat["dark"]*nPixSpatial + sig_rateSpecObs
                    qc = det_RN**2/Nreads*nPixSpatial*NExp
                    timeSpec=(-qb -np.sqrt( qb**2 - 4*qa*qc ))/(2*qa)
                    time=np.median(timeSpec)
                    time=float(time)
                    
                signalSpecObs =  sig_rateSpecObs * time

                noiseSpecObs = np.sqrt(sig_rateSpecObs*time + (bkSpecObs +stat["dark"]*nPixSpatial)*time + det_RN**2/Nreads*nPixSpatial*NExp)


            #<= 13: END EXP TIME BANDCALCULATION
      
#     
# =============================================================================
#         ;*************************************
#         ;*************************************
#         ; Determine SIGNAL TO NOISE 
#         ;*************************************
#         ;*************************************         
       
#                a) time here is known, either set from the beginning o determined to find SNR
#                b) SN has to be found

#     ; noise contributions
#     ; poisson of background
#     ; poisson of dark current
#     ; poisson of the signal
#     ; read noise
#     ;the noise per slit length in the spatial direction
#     ; and per pixel in the spectral direction
#     ; the noise spectrum:
#     ; Poisson of the dark
#     ; current, signal, and background + the read noise"

            #=> 13: BEGIN EXP TIME CALCULATION
                
            else: 
                
                signalSpecObs =  sig_rateSpecObs * time

                if i<4: #BASIc CCD EQUATION...

                    noiseSpecObs = np.sqrt(sig_rateSpecObs*time + (bkSpecObs +stat["dark"]*nPixSpatial)*time + det_RN**2/Nreads*nPixSpatial*NExp)
                
#      MULTIACCUM SAMPLING IN THE IR CHANNELS
                if i >= 4:
                    K1,K2,K3,time_IR= self.CalculateSamplingParameters()
                    print('K1',K1,' K2',K2,' K3 ', K3,' time_R', time_IR)
                    Noise_Sig_tg = K2[i-4] * sig_rateSpecObs#*time_IR[i-4] 
                    Noise_Sig_tf = K3[i-4] * sig_rateSpecObs#*time_IR[i-4] 
                    Noise_Sig = K1[i-4] + Noise_Sig_tg + Noise_Sig_tf
                    Noise_Bg_tg = K2[i-4] * bkSpecObs#*time_IR[i-4]
                    Noise_Bg_tf = K3[i-4] * bkSpecObs#*time_IR[i-4]
                    Noise_Bg = K1[i-4] + Noise_Bg_tg + Noise_Bg_tf
                    Noise_Dark_tg = K2[i-4] * stat["dark"] #* time_IR[i-4]
                    Noise_Dark_tf = K3[i-4] * stat["dark"] #* time_IR[i-4]
                    Noise_Dark = K1[i-4] + Noise_Dark_tg + Noise_Dark_tf
                    NoiseVar = (Noise_Sig + Noise_Bg + Noise_Dark)*nPixSpatial
                    noiseSpecObs = np.sqrt(NoiseVar * NExp)

            snSpecObs = signalSpecObs / noiseSpecObs
    
            stn = np.mean(np.sqrt(nPixSpec) * snSpecObs)
    
#     ;the electron per pixel spectrum
#            eppSpec=(noiseSpecObs**2)/nPixSpatial
            eppSpec = (signalSpecObs + bkSpecObs + stat["dark"]) / nPixSpatial / NExp

# =============================================================================


# =============================================================================
#     ;*************************************
#     ;*************************************
#     ;       SCALAR values to be printed
#     ;*************************************
#     ;*************************************
#     
# =============================================================================
# =============================================================================
#     ;the mean instrument+telescope throughput in the same band pass
#        tp = np.mean( np.array(tpSpecObs)[sn_index.astype(int)])
            tp = np.mean(tpSpecObs)
#     
# =============================================================================
# =============================================================================
#     ;maximum electron per pixel
            print('i',i, np.round(np.max([eppSpec]),0), NExp)
#            max_epp=int(np.round(np.max([eppSpec])/NExp,0))
            max_epp=int(np.round(np.max([eppSpec]),0))
            print(max_epp)
#        
# =============================================================================
# =============================================================================
#     
#     ;if calulating a line flux, S/N per FWHM
#     ;ie S/N in the line
#     
            if all_parameters["FluxORMag"] == 'Use Line Flux':    #SKIP if the line is not in the passband
                if line_index.size != 0:    
#     
# =============================================================================
# =============================================================================
#       ;over the line (per FWHM)
                    stn = np.mean(np.sqrt(nPixSpec) * snSpecObs[sn_index])
#       
# =============================================================================
# =============================================================================
#       ;signal in e/FWHM
                    signal = np.mean(sig_rateSpecObs[sn_index])*nPixSpec*time
#       
# =============================================================================
# =============================================================================
#       ;sky background in e/sec/FWHM
                    background = np.mean(bkSpecObs[sn_index])*nPixSpec*time
#       
# =============================================================================
# =============================================================================
#       ;Read noise for multiple reads, electrons per FWHM
                    RN=det_RN/np.sqrt(Nreads)*np.sqrt(Npix)*np.sqrt(NExp)
#       
# =============================================================================
# =============================================================================
#       ;noise per FWHM
                    noise=np.mean(noiseSpecObs[sn_index])*np.sqrt(nPixSpec)
#       
# =============================================================================
# =============================================================================
#       ;e-
                    dark=stat["dark"]*Npix*time
#       
# =============================================================================
      
# =============================================================================
#         ;*************************************
#         ;*************************************
#         ; ...Determine SCALARS for SNR report
#         ;*************************************
#         ;*************************************         
      
            else:

# =============================================================================
# =============================================================================
#       ;we are computing S/N per pixel for a continuum source
#       
#       ;per spectral pixel
                stn = np.median(snSpecObs)
#       
# =============================================================================
# =============================================================================
#       ;signal in e/(spectral pixel)
                signal = np.median(sig_rateSpecObs)*time
#       
# =============================================================================
# =============================================================================
#       ;sky background in e/(spectral pixel)
                background = np.median(bkSpecObs)*time
#       
# =============================================================================
# =============================================================================
#       ;Read noise for multiple reads, electrons per spectral pixel
                RN=det_RN/np.sqrt(Nreads)*np.sqrt(nPixSpatial)*np.sqrt(NExp)
#       
# =============================================================================
# =============================================================================
#       ;noise per spectral pixel
                noise=np.median(noiseSpecObs)
#       
# =============================================================================
# =============================================================================
#       ;e- per spectral pixel
                dark=stat["dark"]*nPixSpatial*time
#       
# =============================================================================



# =============================================================================
#   ;*************************************
#   ;*************************************
#   ;      display the results
#   ;*************************************
#   ;*************************************
# 
# =============================================================================

    
# =============================================================================
#             SCORPIO_tpSpecObs       = np.append(SCORPIO_tpSpecObs, tpSpecObs)
#             SCORPIO_wave_grid       = np.append(SCORPIO_wave_grid, wave_grid)
#             SCORPIO_raw_bkSpecObs   = np.append(SCORPIO_raw_bkSpecObs, raw_bkSpecObs)
#             SCORPIO_fltSpecObs      = np.append(SCORPIO_fltSpecObs, fltSpecObs)
#             SCORPIO_tranSpecObs     = np.append(SCORPIO_tranSpecObs, tranSpecObs)
#             SCORPIO_bkSpecObs       = np.append(SCORPIO_bkSpecObs, bkSpecObs) 
#             SCORPIO_signalSpecObs   = np.append(SCORPIO_signalSpecObs,signalSpecObs)
#             SCORPIO_noiseSpecObs    = np.append(SCORPIO_noiseSpecObs, noiseSpecObs) 
#             SCORPIO_snSpecObs       = np.append(SCORPIO_snSpecObs, snSpecObs) 
# =============================================================================
            
            SCORPIO_tpSpecObs[i]       = tpSpecObs
            SCORPIO_wave_grid[i]       = wave_grid
            SCORPIO_raw_bkSpecObs[i]   = raw_bkSpecObs
            SCORPIO_fltSpecObs[i]      = fltSpecObs
            SCORPIO_tranSpecObs[i]     = tranSpecObs
            SCORPIO_bkSpecObs[i]       = bkSpecObs 
            SCORPIO_signalSpecObs[i]   = signalSpecObs
            SCORPIO_noiseSpecObs[i]    = noiseSpecObs 
            SCORPIO_snSpecObs[i]       = snSpecObs
            SCORPIO_sn_index[i]        = sn_index
 #SANITIZE
# =============================================================================
#         kill_indexes_YJ = np.where( (SCORPIO_wave_grid > 1.120) & (SCORPIO_wave_grid < 1.150) ) #Y/J gap
#         kill_indexes_JH = np.where( (SCORPIO_wave_grid > 1.350) & (SCORPIO_wave_grid < 1.500) ) #J/H gap
#         kill_indexes_HK = np.where( (SCORPIO_wave_grid > 1.760) & (SCORPIO_wave_grid < 2.000) ) #J/H gap
#         kill_indexes = np.concatenate(kill_indexes_YJ, kill_indexes_JH, kill_indexes_HK)
#  
#         SCORPIO_tpSpecObs[kill_indexes] = 0
#         SCORPIO_wave_grid[kill_indexes] = 0
#         SCORPIO_raw_bkSpecObs[kill_indexes] = 0
#         SCORPIO_fltSpecObs[kill_indexes] = 0
#         SCORPIO_tranSpecObs[kill_indexes] = 0
#         SCORPIO_bkSpecObs[kill_indexes] = 0
#         SCORPIO_signalSpecObs[kill_indexes] = 0
#         SCORPIO_noiseSpecObs[kill_indexes] = 0
#         SCORPIO_snSpecObs[kill_indexes] = 0
# # =============================================================================
# =============================================================================
#     ;*************************************
#     ;*************************************
#     ;      display the results
#     ;*************************************
#     ;*************************************
#     
# =============================================================================
    
            GUI = True
            if GUI == True:
                #Summary of results, in dictionary 
                summary_struct = dict()
                summary_struct["quant"] = ['Wavelength', 'Resolution','Dispersion', 'Throughput', 'Signal', 'Sky Background', 
                                       'Sky brightness', 'Dark Current', 'Read Noise', 'Total Noise','S/N', 
                                       'Total Exposure Time', 'Max e- per pixel']

                if ( (all_parameters["FluxORMag"] == "Line Flux") and (lineWl > 0) ):
                    summary_struct["unit"] = ['micron','FWHM in angstrom', 'angstrom/pixel', '',  'electrons per FWHM', 
                                          'electrons per FWHM', 'AB mag per sq. arcsec', 'electrons per FWHM', 
                                          'electrons per FWHM', 
                                          'electrons per FWHM',
                                          'per observed FWHM', 'seconds', 'electrons per pixel per exp']                                     
                else:
                    summary_struct["unit"] = ['micron','angstrom', 'angstrom/pixel', '',  'electrons per spectral pixel',
                                              'electrons per spectral pixel', 'AB mag per sq. arcsec', 'electrons per spectral pixel', 
                                              'electrons per spectral pixel', 'electrons per spectral pixel',
                                              'per spectral pixel', 'seconds', 'electrons per pixel']


                if max_epp >= 1e10:
                    max_epp_string = "> 1e10"
                else:
                    max_epp_string = max_epp
                
                #checking if the signal is saturating the detector
                if max_epp > sat_limit:
                    messagebox.showerror(title=None,message="Detector saturated! \n\n     Try to increase NExp...")
#                print("Detector Saturated!")
# =============================================================================
#     #
#     #for IR detector do a check on the non linearity thresholds
#     #---------------------------------------------------------------
#     #elif (max_epp > telescope["five_per_limit"]) & (max_epp < instrument["sat_limit"]):
#     #    print("Detector in >5 percent unlinear regime")
#     #elif (max_epp > telescope["one_per_limit"]) & (max_epp < instrument["five_per_limit"]):
#     #    print("Detector in 1 - 5 percent nonlinear regime")
                else:
                    pass
# 
# =============================================================================

                summary_struct["value"] = [np.round(center,4),#stat["lambda"],4),
                    np.round(res * 1e4,1),
                    np.round(stat['disp'],2),
                    np.round(tp,2),         #avg_throughput,
                    np.round(signal,2),      #signal_print,
                    np.round(background,2),             #background_print,
                    np.round(mag_back,2),      #bkg_mag,
                    np.round(dark,2),          #dark_print,
                    np.round(RN,2),            #RN_print,6),
                    np.round(noise,2),         #noise_print,6),
                    np.round(stn,2),
                    np.round(time,2),          #exp_time,6),
                    max_epp_string
                    ]

                SCORPIO_summary_struct.append(summary_struct["value"])  
 #               print(SCORPIO_summary_struct)
                

    ## Actual output containing the spectrum (for graphing purposes) --------------
                self.spec_struct = dict()
        
                self.spec_struct["wave"] = SCORPIO_wave_grid #background_degrade["lam"]
                self.spec_struct["center"] = center#stat["lambda"]
                self.spec_struct["sn_index"] = SCORPIO_sn_index
                self.spec_struct["filt_index"] = filt_index
                self.spec_struct["tp"] = SCORPIO_tpSpecObs #throughput_degrade["flux"]
                self.spec_struct["filt"] = SCORPIO_fltSpecObs #bandpass_degrade["flux"]
                self.spec_struct["tran"] = SCORPIO_tranSpecObs
        #    spec_struct["bk"] = background_degrade["flux"]
                self.spec_struct["bk"] = SCORPIO_bkSpecObs  #background_final [electrons/s/pixel]
        #    spec_struct["sig"] = signal_spectrum # phot/sec/micron #not needed
                self.spec_struct["signal"] =   SCORPIO_signalSpecObs # signal_final # electrons/pixel -> signal_space * exp_time
                self.spec_struct["noise"] = SCORPIO_noiseSpecObs  # noise 
                self.spec_struct["sn"] = SCORPIO_snSpecObs   #  SNR
                self.spec_struct["LineFlux"] = all_parameters["LineFlux"]
                self.spec_struct["time"] = time
            
                self.spec_struct["line_width"] = line_width

      
        
        
        
# =============================================================================
#           widget_control, GUI.table, set_value=out_struct
#           
#           ;turn the max e- per pixel red if the detector has saturated
#           color_bkgrd=fltarr(3,13*3)+255
#           if (max_epp gt sat_limit) then color_bkgrd[1:2,36:38]=0 else $
#             if (max_epp gt five_per_limit) then begin
#             color_bkgrd[2,36:38]=0
#             color_bkgrd[1,36:38]=140
#           endif else $
#             if (max_epp gt one_per_limit) then color_bkgrd[2,36:38]=0
#             
#           widget_control, GUI.table, BACKGROUND_COLOR=color_bkgrd
#           
                self.text_SCORPIO_Header.delete('1.0',END)
                if all_parameters["ExpTimeORSNR"] ==  'Determine Exposure Time':
                    Longstring = "Calculation for a signal to noise ratio of " + str(np.round(stn,3))  # + "\n"
                    Longstring=Longstring + "through a "+all_parameters["slit"]+" arcsecond slit"
                    self.text_SCORPIO_Header.insert(INSERT,Longstring)
                if all_parameters["ExpTimeORSNR"] ==  'Determine Signal to Noise':
                    Longstring2="Calculation for a " + all_parameters["TotalExpTime"] + " s total integration time " #\n"
                    Longstring2=Longstring2 + "through a "+all_parameters["slit"]+" arcsecond slit"
                    self.text_SCORPIO_Header.insert(INSERT,Longstring2)
                

#                
# =============================================================================

# =============================================================================
#                 for item in self.set.get_children():
#                     self.set.delete(item) 
#                 
#                 for j in  range(len(summary_struct["quant"])):
#                     self.set.insert(parent='',index='end',iid=j,text='',
#                                 values=(summary_struct["quant"][j],
#                                         summary_struct["value"][j],
#                                         summary_struct["unit"][j]) )  
#                 
# =============================================================================
                
# =============================================================================
#             #x= np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#             #v= np.array ([16,16.31925,17.6394,16.003,17.2861,17.3131,19.1259,18.9694,22.0003,22.81226])
#             #p= np.array ([16.23697,     17.31653,     17.22094,     17.68631,     17.73641 ,    18.6368,
#             #            19.32125,     19.31756 ,    21.20247  ,   22.41444   ,  22.11718  ,   22.12453])
# 
#             x=spec_struct["wave"] 
#             y=spec_struct["sn_index"]           
#             fig = Figure(figsize=(6,6))
#             a = fig.add_subplot(111)
#             #a.scatter(x,v,color='red')
#             a.plot(x, y,color='blue')
#             a.invert_yaxis()
# 
#            # a.set_title ("Estimation Grid", fontsize=16)
#             a.set_ylabel("transmission", fontsize=14)
#             a.set_xlabel("Wavelength (micron)", fontsize=14)
# 
#             canvas = FigureCanvasTkAgg(fig, master=self.frame_out)
#             canvas.get_tk_widget().place(x=2, y=450, width=490, height=250)#pack()
#             canvas.draw()
#     
# =============================================================================
    

# =============================================================================
                self.Entry_lambdamin.configure(state='normal')
                self.Entry_lambdamax.configure(state='normal')
                if self.selected_PlotWavelengthRange.get() == 'Default':
                    self.Entry_lambdamin.delete(0, END)
                    self.Entry_lambdamax.delete(0, END)
                    self.wl_0 = wave_grid[0] # background_degrade["lam"][0]
                    self.wl_0 = f"{self.wl_0:,{'.3f'}}"
                    self.wl_1 = wave_grid[-1] #background_degrade["lam"][-1]
                    self.wl_1 = f"{self.wl_1:,{'.3f'}}"
#            self.Entry_lambdamin.insert(0,self.wl_0) 
#            self.Entry_lambdamax.insert(0,self.wl_1) 
                    index = np.where(abs(wave_grid - center) < 10*line_width)[0]
                    lambdamin = f"{min(wave_grid):,{'.3f'}}"
                    lambdamax = f"{max(wave_grid):,{'.3f'}}"
                else: 
                    lambdamin  = float(self.Entry_lambdamin.get())
                    lambdamax  = float(self.Entry_lambdamax.get())
                    self.Entry_lambdamin.delete(0, END)
                    self.Entry_lambdamax.delete(0, END)
                self.Entry_lambdamin.insert(0,lambdamin) 
                self.Entry_lambdamax.insert(0,lambdamax) 
                self.Entry_lambdamin.configure(state='disabled')
                self.Entry_lambdamax.configure(state='disabled')
            

        for item in self.set.get_children():
            self.set.delete(item) 
                              
        for j in  range(len(summary_struct["quant"])):
                 summary_struct["value1"] =  SCORPIO_summary_struct[0]
                 summary_struct["value2"] =  SCORPIO_summary_struct[1]
                 summary_struct["value3"] =  SCORPIO_summary_struct[2]
                 summary_struct["value4"] =  SCORPIO_summary_struct[3]
                 summary_struct["value5"] =  SCORPIO_summary_struct[4]
                 summary_struct["value6"] =  SCORPIO_summary_struct[5]
                 summary_struct["value7"] =  SCORPIO_summary_struct[6]
                 summary_struct["value8"] =  SCORPIO_summary_struct[7]
                 self.set.insert(parent='',index='end',iid=j,text='',
                                values=(summary_struct["quant"][j],
                                        summary_struct["value1"][j],
                                        summary_struct["value2"][j],
                                        summary_struct["value3"][j],
                                        summary_struct["value4"][j],
                                        summary_struct["value5"][j],
                                        summary_struct["value6"][j],
                                        summary_struct["value7"][j],
                                        summary_struct["value8"][j],
                                        summary_struct["unit"][j]) )  

# 
# =============================================================================
        if self.selected_PlotObsORSNR.get() == "Plot Observations":
#           print( "Plot Observations")
           self.plot_obs()
        else:
           self.plot_snr()
               
        print('calculation completed')    

 
    def root_exit(self):
       root.quit()#destroy() 
# 
# =============================================================================


# Create a GUI root
root = Tk()
root.style = ttk.Style()
mywin=MainWindow(root)

# Give a title to your self
root.title("XTCak=lk")
# size of the window
root.geometry("1800x940")   

# Make the loop for displaying root
root.mainloop()
