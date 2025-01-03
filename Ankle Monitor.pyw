# Developed by Steven Kotowski
# Last Updated: 12-21-2024

# Import Modules
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import pickle
import os

# Import Variable Files
import Configurations.EmployeeInfo as Emp
import Configurations.Config as Config
import Configurations.DestinationChoices as Dest

# Theme Color and Font Settings
global Theme
Theme = Config.ThemeEnabled
if (Theme == "DarkMode"):
    LightingBackGroundSetting = 'Gray25'
    LightingButtonBGSetting = 'Gray35'
    FontColorLabelSetting = 'snow'
    FontColorHeaderSetting = 'snow'
    FontColorButtonSetting = 'snow'
    headerFontSetting = "Garamond 16 bold"
    SubHeaderFontSetting = "Garamond 12 bold"
    labelFontSetting = "Georgia 10 bold"
    ButtonFontSetting = "Georgia 8"
elif (Theme == "DOTNavy"):
    LightingBackGroundSetting = 'dodgerblue3'
    LightingButtonBGSetting = 'blue2'
    FontColorLabelSetting = 'snow'
    FontColorHeaderSetting = 'snow'
    FontColorButtonSetting = 'snow'
    headerFontSetting = "Garamond 16 bold"
    SubHeaderFontSetting = "Garamond 12 bold"
    labelFontSetting = "Georgia 10 bold"
    ButtonFontSetting = "Georgia 8"
elif (Theme == "ConstructionZone"):
    LightingBackGroundSetting = 'orangered'
    LightingButtonBGSetting = 'orangered3'
    FontColorLabelSetting = 'snow'
    FontColorHeaderSetting = 'snow'
    FontColorButtonSetting = 'snow'
    headerFontSetting = "Garamond 16 bold"
    SubHeaderFontSetting = "Garamond 12 bold"
    labelFontSetting = "Georgia 10 bold"
    ButtonFontSetting = "Georgia 8"
elif (Theme == "SystemDefault"):
    LightingBackGroundSetting = '#F0F0F0'
    LightingButtonBGSetting = '#F0F0F0'
    FontColorLabelSetting = 'black'
    FontColorHeaderSetting = 'black'
    FontColorButtonSetting = 'black'
    headerFontSetting = "Garamond 16 bold"
    SubHeaderFontSetting = "Garamond 12 bold"
    labelFontSetting = "Georgia 10 bold"
    ButtonFontSetting = "Georgia 8"
elif (Theme == "Seahawks"):
    LightingBackGroundSetting = '#002A5C'
    LightingButtonBGSetting = '#7AC142'
    FontColorLabelSetting = '#7AC142'
    FontColorHeaderSetting = '#7AC142'
    FontColorButtonSetting = 'black'
    headerFontSetting = "Garamond 16 bold"
    SubHeaderFontSetting = "Garamond 12 bold"
    labelFontSetting = "Georgia 10 bold"
    ButtonFontSetting = "Georgia 8"

# Determine Employee Amount for Resizing
EmployeeCount = Config.EmployeeQuantity
if (EmployeeCount == 8):
    MainWindowGeometry = "750x600"
    Emp.Employee9Enabled = False
    Emp.Employee10Enabled = False
    Emp.Employee11Enabled = False
    Emp.Employee12Enabled = False    
    Emp.Employee13Enabled = False
    Emp.Employee14Enabled = False
    Emp.Employee15Enabled = False
    Emp.Employee16Enabled = False    
    Emp.Employee17Enabled = False
    Emp.Employee18Enabled = False
    Emp.Employee19Enabled = False
    Emp.Employee20Enabled = False
elif (EmployeeCount == 12):
    MainWindowGeometry = "750x800"
    Emp.Employee13Enabled = False
    Emp.Employee14Enabled = False
    Emp.Employee15Enabled = False
    Emp.Employee16Enabled = False    
    Emp.Employee17Enabled = False
    Emp.Employee18Enabled = False
    Emp.Employee19Enabled = False
    Emp.Employee20Enabled = False
elif (EmployeeCount == 16):
    MainWindowGeometry = "750x985"
    Emp.Employee17Enabled = False
    Emp.Employee18Enabled = False
    Emp.Employee19Enabled = False
    Emp.Employee20Enabled = False    
elif (EmployeeCount == 20):
    MainWindowGeometry = "925x985"

# Destination Window Resizing
DestinationWindowGeometry = "675x500"

# Functions
def MainMenu():

    DefaultStatusText = Dest.DefaultStatusText
    TitleMainWindow = Config.TitleMainWindow

    # Main Menu Form Control
    global mainWindow
    mainWindow = tk.Tk()
    mainWindow.title(TitleMainWindow)
    mainWindow.geometry(MainWindowGeometry)
    mainWindow.resizable(True, False)
    mainWindow.configure(background = LightingBackGroundSetting)

    # Labels - Status Indicator Texts
    if (Emp.Employee1Enabled == True):
        global labelEmployee1
        labelEmployee1 = Label(mainWindow, text = DefaultStatusText, font=labelFontSetting, width=20, height=1, background=LightingBackGroundSetting, foreground=FontColorLabelSetting)
        labelEmployee1.place(x=20, y=270)

    if (Emp.Employee2Enabled == True):
        global labelEmployee2
        labelEmployee2 = Label(mainWindow, text = DefaultStatusText, font=labelFontSetting, width=20, height=1, background=LightingBackGroundSetting, foreground=FontColorLabelSetting)
        labelEmployee2.place(x=190, y=270)
    
    if (Emp.Employee3Enabled == True):   
        global labelEmployee3
        labelEmployee3 = Label(mainWindow, text = DefaultStatusText, font=labelFontSetting, width=20, height=1, background=LightingBackGroundSetting, foreground=FontColorLabelSetting)
        labelEmployee3.place(x=365, y=270)

    if (Emp.Employee4Enabled == True): 
        global labelEmployee4
        labelEmployee4 = Label(mainWindow, text = DefaultStatusText, font=labelFontSetting, width=20, height=1, background=LightingBackGroundSetting, foreground=FontColorLabelSetting)
        labelEmployee4.place(x=540, y=270)

    if (Emp.Employee5Enabled == True):  
        global labelEmployee5
        labelEmployee5 = Label(mainWindow, text = DefaultStatusText, font=labelFontSetting, width=20, height=1, background=LightingBackGroundSetting, foreground=FontColorLabelSetting)
        labelEmployee5.place(x=20, y=495)

    if (Emp.Employee6Enabled == True):
        global labelEmployee6
        labelEmployee6 = Label(mainWindow, text = DefaultStatusText, font=labelFontSetting, width=20, height=1, background=LightingBackGroundSetting, foreground=FontColorLabelSetting)
        labelEmployee6.place(x=190, y=495)

    if (Emp.Employee7Enabled == True):
        global labelEmployee7
        labelEmployee7 = Label(mainWindow, text = DefaultStatusText, font=labelFontSetting, width=20, height=1, background=LightingBackGroundSetting, foreground=FontColorLabelSetting)
        labelEmployee7.place(x=365, y=495)

    if (Emp.Employee8Enabled == True):
        global labelEmployee8
        labelEmployee8 = Label(mainWindow, text = DefaultStatusText, font=labelFontSetting, width=20, height=1, background=LightingBackGroundSetting, foreground=FontColorLabelSetting)
        labelEmployee8.place(x=540, y=495)            

    if (Emp.Employee9Enabled == True):
        global labelEmployee9
        labelEmployee9 = Label(mainWindow, text = DefaultStatusText, font=labelFontSetting, width=20, height=1, background=LightingBackGroundSetting, foreground=FontColorLabelSetting)
        labelEmployee9.place(x=20, y=720)    

    if (Emp.Employee10Enabled == True):
        global labelEmployee10
        labelEmployee10 = Label(mainWindow, text = DefaultStatusText, font=labelFontSetting, width=20, height=1, background=LightingBackGroundSetting, foreground=FontColorLabelSetting)
        labelEmployee10.place(x=190, y=720)    

    if (Emp.Employee11Enabled == True):
        global labelEmployee11
        labelEmployee11 = Label(mainWindow, text = DefaultStatusText, font=labelFontSetting, width=20, height=1, background=LightingBackGroundSetting, foreground=FontColorLabelSetting)
        labelEmployee11.place(x=365, y=720)    

    if (Emp.Employee12Enabled == True):
        global labelEmployee12
        labelEmployee12 = Label(mainWindow, text = DefaultStatusText, font=labelFontSetting, width=20, height=1, background=LightingBackGroundSetting, foreground=FontColorLabelSetting)
        labelEmployee12.place(x=540, y=720)

    if (Emp.Employee13Enabled == True):
        global labelEmployee13
        labelEmployee13 = Label(mainWindow, text = DefaultStatusText, font=labelFontSetting, width=20, height=1, background=LightingBackGroundSetting, foreground=FontColorLabelSetting)
        labelEmployee13.place(x=20, y=945) 

    if (Emp.Employee14Enabled == True):
        global labelEmployee14
        labelEmployee14 = Label(mainWindow, text = DefaultStatusText, font=labelFontSetting, width=20, height=1, background=LightingBackGroundSetting, foreground=FontColorLabelSetting)
        labelEmployee14.place(x=190, y=945) 

    if (Emp.Employee15Enabled == True):
        global labelEmployee15
        labelEmployee15 = Label(mainWindow, text = DefaultStatusText, font=labelFontSetting, width=20, height=1, background=LightingBackGroundSetting, foreground=FontColorLabelSetting)
        labelEmployee15.place(x=365, y=945) 

    if (Emp.Employee16Enabled == True):
        global labelEmployee16
        labelEmployee16 = Label(mainWindow, text = DefaultStatusText, font=labelFontSetting, width=20, height=1, background=LightingBackGroundSetting, foreground=FontColorLabelSetting)
        labelEmployee16.place(x=540, y=945) 

    if (Emp.Employee17Enabled == True):
        global labelEmployee17
        labelEmployee17 = Label(mainWindow, text = DefaultStatusText, font=labelFontSetting, width=20, height=1, background=LightingBackGroundSetting, foreground=FontColorLabelSetting)
        labelEmployee17.place(x=715, y=270) 

    if (Emp.Employee18Enabled == True):
        global labelEmployee18
        labelEmployee18 = Label(mainWindow, text = DefaultStatusText, font=labelFontSetting, width=20, height=1, background=LightingBackGroundSetting, foreground=FontColorLabelSetting)
        labelEmployee18.place(x=715, y=495) 

    if (Emp.Employee19Enabled == True):
        global labelEmployee19
        labelEmployee19 = Label(mainWindow, text = DefaultStatusText, font=labelFontSetting, width=20, height=1, background=LightingBackGroundSetting, foreground=FontColorLabelSetting)
        labelEmployee19.place(x=715, y=720) 

    if (Emp.Employee20Enabled == True):
        global labelEmployee20
        labelEmployee20 = Label(mainWindow, text = DefaultStatusText, font=labelFontSetting, width=20, height=1, background=LightingBackGroundSetting, foreground=FontColorLabelSetting)
        labelEmployee20.place(x=715, y=945) 

    # Header Labels
    PrimaryHeaderText = Config.PrimaryHeader
    PrimaryHeader = Label(mainWindow, text = PrimaryHeaderText, font = headerFontSetting, width = 50, height = 2, background=LightingBackGroundSetting, foreground=FontColorHeaderSetting)
    PrimaryHeader.place(x=80, y=10)

    SecondaryHeaderText = Config.SecondaryHeader
    SecondaryHeader = Label(mainWindow, text = SecondaryHeaderText, font = headerFontSetting, width = 50, height = 2, background=LightingBackGroundSetting, foreground=FontColorHeaderSetting)
    SecondaryHeader.place(x=80, y=45)

    if (EmployeeCount == 20):
        PrimaryHeader.place(x=160, y=10)
        SecondaryHeader.place(x=160, y=45)

    # Buttons
    global ButtonID

    if (Emp.Employee1Enabled == True):
        EmployeeName1 = Emp.EmployeeName1
        buttonEmployee1 = Button(mainWindow, text = EmployeeName1, height=1, width=16, command=lambda: SubMenuSelect(ButtonID = 1), background=LightingButtonBGSetting, foreground=FontColorButtonSetting, font=ButtonFontSetting)
        buttonEmployee1.place(x=51, y=232)

    if (Emp.Employee2Enabled == True): 
        EmployeeName2 = Emp.EmployeeName2
        buttonEmployee2 = Button(mainWindow, text = EmployeeName2, height=1, width=16, command=lambda: SubMenuSelect(ButtonID = 2), background=LightingButtonBGSetting, foreground=FontColorButtonSetting, font=ButtonFontSetting)
        buttonEmployee2.place(x=226, y=232)

    if (Emp.Employee3Enabled == True):
        EmployeeName3 = Emp.EmployeeName3
        buttonEmployee3 = Button(mainWindow, text = EmployeeName3, height=1, width=16, command=lambda: SubMenuSelect(ButtonID = 3), background=LightingButtonBGSetting, foreground=FontColorButtonSetting, font=ButtonFontSetting) 
        buttonEmployee3.place(x=401, y=232)

    if (Emp.Employee4Enabled == True):   
        EmployeeName4 = Emp.EmployeeName4
        buttonEmployee4 = Button(mainWindow, text = EmployeeName4, height=1, width=16, command=lambda: SubMenuSelect(ButtonID = 4), background=LightingButtonBGSetting, foreground=FontColorButtonSetting, font=ButtonFontSetting)
        buttonEmployee4.place(x=576, y=232)

    if (Emp.Employee5Enabled == True):  
        EmployeeName5 = Emp.EmployeeName5
        buttonEmployee5 = Button(mainWindow, text = EmployeeName5, height=1, width=16, command=lambda: SubMenuSelect(ButtonID = 5), background=LightingButtonBGSetting, foreground=FontColorButtonSetting, font=ButtonFontSetting)
        buttonEmployee5.place(x=51, y=457)

    if (Emp.Employee6Enabled == True):
        EmployeeName6 = Emp.EmployeeName6
        buttonEmployee6 = Button(mainWindow, text = EmployeeName6, height=1, width=16, command=lambda: SubMenuSelect(ButtonID = 6), background=LightingButtonBGSetting, foreground=FontColorButtonSetting, font=ButtonFontSetting)
        buttonEmployee6.place(x=226, y=457)

    if (Emp.Employee7Enabled == True): 
        EmployeeName7 = Emp.EmployeeName7
        buttonEmployee7 = Button(mainWindow, text = EmployeeName7, height=1, width=16, command=lambda: SubMenuSelect(ButtonID = 7), background=LightingButtonBGSetting, foreground=FontColorButtonSetting, font=ButtonFontSetting)
        buttonEmployee7.place(x=401, y=457)

    if (Emp.Employee8Enabled == True): 
        EmployeeName8 = Emp.EmployeeName8
        buttonEmployee8 = Button(mainWindow, text = EmployeeName8, height=1, width=16, command=lambda: SubMenuSelect(ButtonID = 8), background=LightingButtonBGSetting, foreground=FontColorButtonSetting, font=ButtonFontSetting)
        buttonEmployee8.place(x=576, y=457)

    if (Emp.Employee9Enabled == True): 
        EmployeeName9 = Emp.EmployeeName9
        buttonEmployee9 = Button(mainWindow, text = EmployeeName9, height=1, width=16, command=lambda: SubMenuSelect(ButtonID = 9), background=LightingButtonBGSetting, foreground=FontColorButtonSetting, font=ButtonFontSetting)
        buttonEmployee9.place(x=51, y=682)

    if (Emp.Employee10Enabled == True):
        EmployeeName10 = Emp.EmployeeName10
        buttonEmployee10 = Button(mainWindow, text = EmployeeName10, height=1, width=16, command=lambda: SubMenuSelect(ButtonID = 10), background=LightingButtonBGSetting, foreground=FontColorButtonSetting, font=ButtonFontSetting)
        buttonEmployee10.place(x=226, y=682)

    if (Emp.Employee11Enabled == True): 
        EmployeeName11 = Emp.EmployeeName11
        buttonEmployee11 = Button(mainWindow, text = EmployeeName11, height=1, width=16, command=lambda: SubMenuSelect(ButtonID = 11), background=LightingButtonBGSetting, foreground=FontColorButtonSetting, font=ButtonFontSetting)
        buttonEmployee11.place(x=401, y=682)

    if (Emp.Employee12Enabled == True):
        EmployeeName12 = Emp.EmployeeName12
        buttonEmployee12 = Button(mainWindow, text = EmployeeName12, height=1, width=16, command=lambda: SubMenuSelect(ButtonID = 12), background=LightingButtonBGSetting, foreground=FontColorButtonSetting, font=ButtonFontSetting)
        buttonEmployee12.place(x=576, y=682)

    if (Emp.Employee13Enabled == True):  
        EmployeeName13 = Emp.EmployeeName13
        buttonEmployee13 = Button(mainWindow, text = EmployeeName13, height=1, width=16, command=lambda: SubMenuSelect(ButtonID = 13), background=LightingButtonBGSetting, foreground=FontColorButtonSetting, font=ButtonFontSetting)
        buttonEmployee13.place(x=51, y=907)

    if (Emp.Employee14Enabled == True): 
        EmployeeName14 = Emp.EmployeeName14
        buttonEmployee14 = Button(mainWindow, text = EmployeeName14, height=1, width=16, command=lambda: SubMenuSelect(ButtonID = 14), background=LightingButtonBGSetting, foreground=FontColorButtonSetting, font=ButtonFontSetting)
        buttonEmployee14.place(x=226, y=907)

    if (Emp.Employee15Enabled == True):  
        EmployeeName15 = Emp.EmployeeName15
        buttonEmployee15 = Button(mainWindow, text = EmployeeName15, height=1, width=16, command=lambda: SubMenuSelect(ButtonID = 15), background=LightingButtonBGSetting, foreground=FontColorButtonSetting, font=ButtonFontSetting)
        buttonEmployee15.place(x=401, y=907)

    if (Emp.Employee16Enabled == True):
        EmployeeName16 = Emp.EmployeeName16
        buttonEmployee16 = Button(mainWindow, text = EmployeeName16, height=1, width=16, command=lambda: SubMenuSelect(ButtonID = 16), background=LightingButtonBGSetting, foreground=FontColorButtonSetting, font=ButtonFontSetting)
        buttonEmployee16.place(x=576, y=907)

    if (Emp.Employee17Enabled == True):
        EmployeeName17 = Emp.EmployeeName17
        buttonEmployee17 = Button(mainWindow, text = EmployeeName17, height=1, width=16, command=lambda: SubMenuSelect(ButtonID = 17), background=LightingButtonBGSetting, foreground=FontColorButtonSetting, font=ButtonFontSetting)
        buttonEmployee17.place(x=751, y=232)

    if (Emp.Employee18Enabled == True):
        EmployeeName18 = Emp.EmployeeName18
        buttonEmployee18 = Button(mainWindow, text = EmployeeName18, height=1, width=16, command=lambda: SubMenuSelect(ButtonID = 18), background=LightingButtonBGSetting, foreground=FontColorButtonSetting, font=ButtonFontSetting)
        buttonEmployee18.place(x=751, y=457)

    if (Emp.Employee19Enabled == True):
        EmployeeName19 = Emp.EmployeeName19
        buttonEmployee19 = Button(mainWindow, text = EmployeeName19, height=1, width=16, command=lambda: SubMenuSelect(ButtonID = 19), background=LightingButtonBGSetting, foreground=FontColorButtonSetting, font=ButtonFontSetting)
        buttonEmployee19.place(x=751, y=682)

    if (Emp.Employee20Enabled == True):
        EmployeeName20 = Emp.EmployeeName20
        buttonEmployee20 = Button(mainWindow, text = EmployeeName20, height=1, width=16, command=lambda: SubMenuSelect(ButtonID = 20), background=LightingButtonBGSetting, foreground=FontColorButtonSetting, font=ButtonFontSetting)
        buttonEmployee20.place(x=751, y=907)

    # Images
    ImagesRelief = "sunken"
    if (Emp.Employee1Enabled == True):
        EmployeeImg1 = Emp.EmployeeImg1
        EmployeeImage1Processing = Image.open(EmployeeImg1)
        EmployeeImage1Resize = EmployeeImage1Processing.resize((120,120))
        EmployeeImagePhoto1 = ImageTk.PhotoImage(EmployeeImage1Resize)
        EmployeeImagePhotoFrame1 = Label(mainWindow, image=EmployeeImagePhoto1, relief=ImagesRelief)
        EmployeeImagePhotoFrame1.place(x=50, y=105)

    if (Emp.Employee2Enabled == True):    
        EmployeeImg2 = Emp.EmployeeImg2
        EmployeeImage2Processing = Image.open(EmployeeImg2)
        EmployeeImage2Resize = EmployeeImage2Processing.resize((120,120))
        EmployeeImagePhoto2 = ImageTk.PhotoImage(EmployeeImage2Resize)
        EmployeeImagePhotoFrame2 = Label(mainWindow, image=EmployeeImagePhoto2, relief=ImagesRelief)
        EmployeeImagePhotoFrame2.place(x=225, y=105)

    if (Emp.Employee3Enabled == True): 
        EmployeeImg3 = Emp.EmployeeImg3
        EmployeeImage3Processing = Image.open(EmployeeImg3)
        EmployeeImage3Resize = EmployeeImage3Processing.resize((120,120))
        EmployeeImagePhoto3 = ImageTk.PhotoImage(EmployeeImage3Resize)
        EmployeeImagePhotoFrame3 = Label(mainWindow, image=EmployeeImagePhoto3, relief=ImagesRelief)
        EmployeeImagePhotoFrame3.place(x=400, y=105)
    
    if (Emp.Employee4Enabled == True):    
        EmployeeImg4 = Emp.EmployeeImg4
        EmployeeImage4Processing = Image.open(EmployeeImg4)
        EmployeeImage4Resize = EmployeeImage4Processing.resize((120,120))
        EmployeeImagePhoto4 = ImageTk.PhotoImage(EmployeeImage4Resize)
        EmployeeImagePhotoFrame4 = Label(mainWindow, image=EmployeeImagePhoto4, relief=ImagesRelief)
        EmployeeImagePhotoFrame4.place(x=575, y=105)

    if (Emp.Employee5Enabled == True):    
        EmployeeImg5 = Emp.EmployeeImg5
        EmployeeImage5Processing = Image.open(EmployeeImg5)
        EmployeeImage5Resize = EmployeeImage5Processing.resize((120,120))
        EmployeeImagePhoto5 = ImageTk.PhotoImage(EmployeeImage5Resize)
        EmployeeImagePhotoFrame5 = Label(mainWindow, image=EmployeeImagePhoto5, relief=ImagesRelief)
        EmployeeImagePhotoFrame5.place(x=50, y=330)

    if (Emp.Employee6Enabled == True):    
        EmployeeImg6 = Emp.EmployeeImg6
        EmployeeImage6Processing = Image.open(EmployeeImg6)
        EmployeeImage6Resize = EmployeeImage6Processing.resize((120,120))
        EmployeeImagePhoto6 = ImageTk.PhotoImage(EmployeeImage6Resize)
        EmployeeImagePhotoFrame6 = Label(mainWindow, image=EmployeeImagePhoto6, relief=ImagesRelief)
        EmployeeImagePhotoFrame6.place(x=225, y=330)

    if (Emp.Employee7Enabled == True):  
        EmployeeImg7 = Emp.EmployeeImg7
        EmployeeImage7Processing = Image.open(EmployeeImg7)
        EmployeeImage7Resize = EmployeeImage7Processing.resize((120,120))
        EmployeeImagePhoto7 = ImageTk.PhotoImage(EmployeeImage7Resize)
        EmployeeImagePhotoFrame7 = Label(mainWindow, image=EmployeeImagePhoto7, relief=ImagesRelief)
        EmployeeImagePhotoFrame7.place(x=400, y=330)

    if (Emp.Employee8Enabled == True): 
        EmployeeImg8 = Emp.EmployeeImg8
        EmployeeImage8Processing = Image.open(EmployeeImg8)
        EmployeeImage8Resize = EmployeeImage8Processing.resize((120,120))
        EmployeeImagePhoto8 = ImageTk.PhotoImage(EmployeeImage8Resize)
        EmployeeImagePhotoFrame8 = Label(mainWindow, image=EmployeeImagePhoto8, relief=ImagesRelief)
        EmployeeImagePhotoFrame8.place(x=575, y=330)

    if (Emp.Employee9Enabled == True):   
        EmployeeImg9 = Emp.EmployeeImg9
        EmployeeImage9Processing = Image.open(EmployeeImg9)
        EmployeeImage9Resize = EmployeeImage9Processing.resize((120,120))
        EmployeeImagePhoto9 = ImageTk.PhotoImage(EmployeeImage9Resize)
        EmployeeImagePhotoFrame9 = Label(mainWindow, image=EmployeeImagePhoto9, relief=ImagesRelief)
        EmployeeImagePhotoFrame9.place(x=50, y=555)

    if (Emp.Employee10Enabled == True):   
        EmployeeImg10 = Emp.EmployeeImg10
        EmployeeImage10Processing = Image.open(EmployeeImg10)
        EmployeeImage10Resize = EmployeeImage10Processing.resize((120,120))
        EmployeeImagePhoto10 = ImageTk.PhotoImage(EmployeeImage10Resize)
        EmployeeImagePhotoFrame10 = Label(mainWindow, image=EmployeeImagePhoto10, relief=ImagesRelief)
        EmployeeImagePhotoFrame10.place(x=225, y=555)

    if (Emp.Employee11Enabled == True): 
        EmployeeImg11 = Emp.EmployeeImg11
        EmployeeImage11Processing = Image.open(EmployeeImg11)
        EmployeeImage11Resize = EmployeeImage11Processing.resize((120,120))
        EmployeeImagePhoto11 = ImageTk.PhotoImage(EmployeeImage11Resize)
        EmployeeImagePhotoFrame11 = Label(mainWindow, image=EmployeeImagePhoto11, relief=ImagesRelief)
        EmployeeImagePhotoFrame11.place(x=400, y=555)

    if (Emp.Employee12Enabled == True):  
        EmployeeImg12 = Emp.EmployeeImg12
        EmployeeImage12Processing = Image.open(EmployeeImg12)
        EmployeeImage12Resize = EmployeeImage12Processing.resize((120,120))
        EmployeeImagePhoto12 = ImageTk.PhotoImage(EmployeeImage12Resize)
        EmployeeImagePhotoFrame12 = Label(mainWindow, image=EmployeeImagePhoto12, relief=ImagesRelief)
        EmployeeImagePhotoFrame12.place(x=575, y=555)

    if (Emp.Employee13Enabled == True):    
        EmployeeImg13 = Emp.EmployeeImg13
        EmployeeImage13Processing = Image.open(EmployeeImg13)
        EmployeeImage13Resize = EmployeeImage13Processing.resize((120,120))
        EmployeeImagePhoto13 = ImageTk.PhotoImage(EmployeeImage13Resize)
        EmployeeImagePhotoFrame13 = Label(mainWindow, image=EmployeeImagePhoto13, relief=ImagesRelief)
        EmployeeImagePhotoFrame13.place(x=50, y=780)

    if (Emp.Employee14Enabled == True):   
        EmployeeImg14 = Emp.EmployeeImg14
        EmployeeImage14Processing = Image.open(EmployeeImg14)
        EmployeeImage14Resize = EmployeeImage14Processing.resize((120,120))
        EmployeeImagePhoto14 = ImageTk.PhotoImage(EmployeeImage14Resize)
        EmployeeImagePhotoFrame14 = Label(mainWindow, image=EmployeeImagePhoto14, relief=ImagesRelief)
        EmployeeImagePhotoFrame14.place(x=225, y=780)

    if (Emp.Employee15Enabled == True):    
        EmployeeImg15 = Emp.EmployeeImg15
        EmployeeImage15Processing = Image.open(EmployeeImg15)
        EmployeeImage15Resize = EmployeeImage15Processing.resize((120,120))
        EmployeeImagePhoto15 = ImageTk.PhotoImage(EmployeeImage15Resize)
        EmployeeImagePhotoFrame15 = Label(mainWindow, image=EmployeeImagePhoto15, relief=ImagesRelief)
        EmployeeImagePhotoFrame15.place(x=400, y=780)

    if (Emp.Employee16Enabled == True):   
        EmployeeImg16 = Emp.EmployeeImg16
        EmployeeImage16Processing = Image.open(EmployeeImg16)
        EmployeeImage16Resize = EmployeeImage16Processing.resize((120,120))
        EmployeeImagePhoto16 = ImageTk.PhotoImage(EmployeeImage16Resize)
        EmployeeImagePhotoFrame16 = Label(mainWindow, image=EmployeeImagePhoto16, relief=ImagesRelief)
        EmployeeImagePhotoFrame16.place(x=575, y=780)

    if (Emp.Employee17Enabled == True):   
        EmployeeImg17 = Emp.EmployeeImg17
        EmployeeImage17Processing = Image.open(EmployeeImg17)
        EmployeeImage17Resize = EmployeeImage17Processing.resize((120,120))
        EmployeeImagePhoto17 = ImageTk.PhotoImage(EmployeeImage17Resize)
        EmployeeImagePhotoFrame17 = Label(mainWindow, image=EmployeeImagePhoto17, relief=ImagesRelief)
        EmployeeImagePhotoFrame17.place(x=750, y=105)

    if (Emp.Employee18Enabled == True):   
        EmployeeImg18 = Emp.EmployeeImg18
        EmployeeImage18Processing = Image.open(EmployeeImg18)
        EmployeeImage18Resize = EmployeeImage18Processing.resize((120,120))
        EmployeeImagePhoto18 = ImageTk.PhotoImage(EmployeeImage18Resize)
        EmployeeImagePhotoFrame18 = Label(mainWindow, image=EmployeeImagePhoto18, relief=ImagesRelief)
        EmployeeImagePhotoFrame18.place(x=750, y=330)

    if (Emp.Employee19Enabled == True):   
        EmployeeImg19 = Emp.EmployeeImg19
        EmployeeImage19Processing = Image.open(EmployeeImg19)
        EmployeeImage19Resize = EmployeeImage19Processing.resize((120,120))
        EmployeeImagePhoto19 = ImageTk.PhotoImage(EmployeeImage19Resize)
        EmployeeImagePhotoFrame19 = Label(mainWindow, image=EmployeeImagePhoto19, relief=ImagesRelief)
        EmployeeImagePhotoFrame19.place(x=750, y=555)

    if (Emp.Employee20Enabled == True):   
        EmployeeImg20 = Emp.EmployeeImg20
        EmployeeImage20Processing = Image.open(EmployeeImg20)
        EmployeeImage20Resize = EmployeeImage20Processing.resize((120,120))
        EmployeeImagePhoto20 = ImageTk.PhotoImage(EmployeeImage20Resize)
        EmployeeImagePhotoFrame20 = Label(mainWindow, image=EmployeeImagePhoto20, relief=ImagesRelief)
        EmployeeImagePhotoFrame20.place(x=750, y=780)

    MainLogo = 'Assets\\Logo.png'
    MainLogoProcessing = Image.open(MainLogo)
    MainLogoResize = MainLogoProcessing.resize((80,80))
    MainLogoImg = ImageTk.PhotoImage(MainLogoResize)
    MainLogoFrame = Label(mainWindow, image=MainLogoImg, background=LightingBackGroundSetting, relief='flat')
    MainLogoFrame.place(x=25, y=5)

    mainWindow.mainloop()

def SubMenuSelect(ButtonID):
    
    TitleDestinationWindow = Config.TitleDestinationWindow

    # Destination Window Form Controls
    global DestinationSelectWindow
    DestinationSelectWindow = tk.Toplevel(mainWindow)
    DestinationSelectWindow.title(TitleDestinationWindow)
    DestinationSelectWindow.geometry(DestinationWindowGeometry)
    DestinationSelectWindow.configure(background = LightingBackGroundSetting)
    DestinationSelectWindow.resizable(False, False)

    global ChosenEmployee
    ChosenEmployee = ButtonID

    # Headers
    SubHeader1 = Config.SubHeader1
    SubHeaderStatuses1 = Label(DestinationSelectWindow, text = SubHeader1, font=SubHeaderFontSetting, foreground=FontColorHeaderSetting, background=LightingBackGroundSetting)
    SubHeaderStatuses1.place(x=15, y=10)

    SubHeader2 = Config.SubHeader2
    SubHeaderStatuses2 = Label(DestinationSelectWindow, text = SubHeader2, font=SubHeaderFontSetting, foreground=FontColorHeaderSetting, background=LightingBackGroundSetting)
    SubHeaderStatuses2.place(x=15, y=95)

    SubHeader3 = Config.SubHeader3
    SubHeaderStatuses3 = Label(DestinationSelectWindow, text = SubHeader3, font=SubHeaderFontSetting, foreground=FontColorHeaderSetting, background=LightingBackGroundSetting)
    SubHeaderStatuses3.place(x=15, y=230)

    SubHeader4 = Config.SubHeader4
    SubHeaderStatuses4 = Label(DestinationSelectWindow, text = SubHeader4, font=SubHeaderFontSetting, foreground=FontColorHeaderSetting, background=LightingBackGroundSetting)
    SubHeaderStatuses4.place(x=15, y=315)

    SubHeader5 = Config.SubHeader5
    SubHeaderStatuses4 = Label(DestinationSelectWindow, text = SubHeader5, font=SubHeaderFontSetting, foreground=FontColorHeaderSetting, background=LightingBackGroundSetting)
    SubHeaderStatuses4.place(x=15, y=400)

    # Buttons
    global SubSelection

    if (Dest.Destination1Enabled == True):
        global Destination1
        Destination1 = Dest.Destination1
        SubButton1 = Button(DestinationSelectWindow, text=Destination1, height=2, width=15, command=lambda: ChangeStatus(SubSelection = 1), foreground=FontColorButtonSetting, background=LightingButtonBGSetting, font=ButtonFontSetting)
        SubButton1.place(x=25, y=40)

    if (Dest.Destination2Enabled == True):
        global Destination2
        Destination2 = Dest.Destination2
        SubButton2 = Button(DestinationSelectWindow, text=Destination2, height=2, width=15, command=lambda: ChangeStatus(SubSelection = 2), foreground=FontColorButtonSetting, background=LightingButtonBGSetting, font=ButtonFontSetting)
        SubButton2.place(x=150, y=40)

    if (Dest.Destination3Enabled == True):
        global Destination3
        Destination3 = Dest.Destination3
        SubButton3 = Button(DestinationSelectWindow, text=Destination3, height=2, width=15, command=lambda: ChangeStatus(SubSelection = 3), foreground=FontColorButtonSetting, background=LightingButtonBGSetting, font=ButtonFontSetting)
        SubButton3.place(x=275, y=40)

    if (Dest.Destination4Enabled == True):
        global Destination4
        Destination4 = Dest.Destination4
        SubButton4 = Button(DestinationSelectWindow, text=Destination4, height=2, width=15, command=lambda: ChangeStatus(SubSelection = 4), foreground=FontColorButtonSetting, background=LightingButtonBGSetting, font=ButtonFontSetting)
        SubButton4.place(x=400, y=40)

    if (Dest.Destination5Enabled == True):
        global Destination5
        Destination5 = Dest.Destination5
        SubButton5 = Button(DestinationSelectWindow, text=Destination5, height=2, width=15, command=lambda: ChangeStatus(SubSelection = 5), foreground=FontColorButtonSetting, background=LightingButtonBGSetting, font=ButtonFontSetting)
        SubButton5.place(x=525, y=40)

    if (Dest.Destination6Enabled == True):
        global Destination6
        Destination6 = Dest.Destination6
        SubButton6 = Button(DestinationSelectWindow, text=Destination6, height=2, width=15, command=lambda: ChangeStatus(SubSelection = 6), foreground=FontColorButtonSetting, background=LightingButtonBGSetting, font=ButtonFontSetting)
        SubButton6.place(x=25, y=125)

    if (Dest.Destination7Enabled == True):
        global Destination7
        Destination7 = Dest.Destination7
        SubButton7 = Button(DestinationSelectWindow, text=Destination7, height=2, width=15, command=lambda: ChangeStatus(SubSelection = 7), foreground=FontColorButtonSetting, background=LightingButtonBGSetting, font=ButtonFontSetting)
        SubButton7.place(x=150, y=125)

    if (Dest.Destination8Enabled == True):
        global Destination8
        Destination8 = Dest.Destination8
        SubButton8 = Button(DestinationSelectWindow, text=Destination8, height=2, width=15, command=lambda: ChangeStatus(SubSelection = 8), foreground=FontColorButtonSetting, background=LightingButtonBGSetting, font=ButtonFontSetting)
        SubButton8.place(x=275, y=125)

    if (Dest.Destination9Enabled == True):
        global Destination9
        Destination9 = Dest.Destination9
        SubButton9 = Button(DestinationSelectWindow, text=Destination9, height=2, width=15, command=lambda: ChangeStatus(SubSelection = 9), foreground=FontColorButtonSetting, background=LightingButtonBGSetting, font=ButtonFontSetting)
        SubButton9.place(x=400, y=125)

    if (Dest.Destination10Enabled == True):
        global Destination10
        Destination10 = Dest.Destination10
        SubButton10 = Button(DestinationSelectWindow, text=Destination10, height=2, width=15, command=lambda: ChangeStatus(SubSelection = 10), foreground=FontColorButtonSetting, background=LightingButtonBGSetting, font=ButtonFontSetting)
        SubButton10.place(x=525, y=125)

    if (Dest.Destination11Enabled == True):
        global Destination11
        Destination11 = Dest.Destination11
        SubButton11 = Button(DestinationSelectWindow, text=Destination11, height=2, width=15, command=lambda: ChangeStatus(SubSelection = 11), foreground=FontColorButtonSetting, background=LightingButtonBGSetting, font=ButtonFontSetting)
        SubButton11.place(x=25, y=175)

    if (Dest.Destination12Enabled == True):
        global Destination12
        Destination12 = Dest.Destination12
        SubButton12 = Button(DestinationSelectWindow, text=Destination12, height=2, width=15, command=lambda: ChangeStatus(SubSelection = 12), foreground=FontColorButtonSetting, background=LightingButtonBGSetting, font=ButtonFontSetting)
        SubButton12.place(x=150, y=175)

    if (Dest.Destination13Enabled == True):
        global Destination13
        Destination13 = Dest.Destination13
        SubButton13 = Button(DestinationSelectWindow, text=Destination13, height=2, width=15, command=lambda: ChangeStatus(SubSelection = 13), foreground=FontColorButtonSetting, background=LightingButtonBGSetting, font=ButtonFontSetting)
        SubButton13.place(x=275, y=175)

    if (Dest.Destination14Enabled == True):
        global Destination14
        Destination14 = Dest.Destination14
        SubButton14 = Button(DestinationSelectWindow, text=Destination14, height=2, width=15, command=lambda: ChangeStatus(SubSelection = 14), foreground=FontColorButtonSetting, background=LightingButtonBGSetting, font=ButtonFontSetting)
        SubButton14.place(x=400, y=175)

    if (Dest.Destination15Enabled == True):
        global Destination15
        Destination15 = Dest.Destination15
        SubButton15 = Button(DestinationSelectWindow, text=Destination15, height=2, width=15, command=lambda: ChangeStatus(SubSelection = 15), foreground=FontColorButtonSetting, background=LightingButtonBGSetting, font=ButtonFontSetting)
        SubButton15.place(x=525, y=175) 

    if (Dest.Destination16Enabled == True):
        global Destination16
        Destination16 = Dest.Destination16
        SubButton16 = Button(DestinationSelectWindow, text=Destination16, height=2, width=15, command=lambda: ChangeStatus(SubSelection = 16), foreground=FontColorButtonSetting, background=LightingButtonBGSetting, font=ButtonFontSetting)
        SubButton16.place(x=25, y=260)

    if (Dest.Destination17Enabled == True):
        global Destination17
        Destination17 = Dest.Destination17
        SubButton17 = Button(DestinationSelectWindow, text=Destination17, height=2, width=15, command=lambda: ChangeStatus(SubSelection = 17), foreground=FontColorButtonSetting, background=LightingButtonBGSetting, font=ButtonFontSetting)
        SubButton17.place(x=150, y=260)

    if (Dest.Destination18Enabled == True):
        global Destination18
        Destination18 = Dest.Destination18
        SubButton18 = Button(DestinationSelectWindow, text=Destination18, height=2, width=15, command=lambda: ChangeStatus(SubSelection = 18), foreground=FontColorButtonSetting, background=LightingButtonBGSetting, font=ButtonFontSetting)
        SubButton18.place(x=275, y=260)

    if (Dest.Destination19Enabled == True):
        global Destination19
        Destination19 = Dest.Destination19
        SubButton19 = Button(DestinationSelectWindow, text=Destination19, height=2, width=15, command=lambda: ChangeStatus(SubSelection = 19), foreground=FontColorButtonSetting, background=LightingButtonBGSetting, font=ButtonFontSetting)
        SubButton19.place(x=400, y=260)

    if (Dest.Destination20Enabled == True):
        global Destination20
        Destination20 = Dest.Destination20
        SubButton20 = Button(DestinationSelectWindow, text=Destination20, height=2, width=15, command=lambda: ChangeStatus(SubSelection = 20), foreground=FontColorButtonSetting, background=LightingButtonBGSetting, font=ButtonFontSetting)
        SubButton20.place(x=525, y=260)

    if (Dest.Destination21Enabled == True):
        global Destination21
        Destination21 = Dest.Destination21
        SubButton21 = Button(DestinationSelectWindow, text=Destination21, height=2, width=15, command=lambda: ChangeStatus(SubSelection = 21), foreground=FontColorButtonSetting, background=LightingButtonBGSetting, font=ButtonFontSetting)
        SubButton21.place(x=25, y=345)

    if (Dest.Destination22Enabled == True):
        global Destination22
        Destination22 = Dest.Destination22
        SubButton22 = Button(DestinationSelectWindow, text=Destination22, height=2, width=15, command=lambda: ChangeStatus(SubSelection = 22), foreground=FontColorButtonSetting, background=LightingButtonBGSetting, font=ButtonFontSetting)
        SubButton22.place(x=150, y=345)

    if (Dest.Destination23Enabled == True):
        global Destination23
        Destination23 = Dest.Destination23
        SubButton23 = Button(DestinationSelectWindow, text=Destination23, height=2, width=15, command=lambda: ChangeStatus(SubSelection = 23), foreground=FontColorButtonSetting, background=LightingButtonBGSetting, font=ButtonFontSetting)
        SubButton23.place(x=275, y=345)

    if (Dest.Destination24Enabled == True):
        global Destination24
        Destination24 = Dest.Destination24
        SubButton24 = Button(DestinationSelectWindow, text=Destination24, height=2, width=15, command=lambda: ChangeStatus(SubSelection = 24), foreground=FontColorButtonSetting, background=LightingButtonBGSetting, font=ButtonFontSetting)
        SubButton24.place(x=400, y=345)

    if (Dest.Destination25Enabled == True):
        global Destination25
        Destination25 = Dest.Destination25
        SubButton25 = Button(DestinationSelectWindow, text=Destination25, height=2, width=15, command=lambda: ChangeStatus(SubSelection = 25), foreground=FontColorButtonSetting, background=LightingButtonBGSetting, font=ButtonFontSetting)
        SubButton25.place(x=525, y=345)

    if (Dest.Destination26Enabled == True):
        global Destination26
        Destination26 = Dest.Destination26
        SubButton26 = Button(DestinationSelectWindow, text=Destination26, height=2, width=15, command=lambda: ChangeStatus(SubSelection = 26), foreground=FontColorButtonSetting, background=LightingButtonBGSetting, font=ButtonFontSetting)
        SubButton26.place(x=25, y=430)

    if (Dest.Destination27Enabled == True):
        global Destination27
        Destination27 = Dest.Destination27
        SubButton27 = Button(DestinationSelectWindow, text=Destination27, height=2, width=15, command=lambda: ChangeStatus(SubSelection = 27), foreground=FontColorButtonSetting, background=LightingButtonBGSetting, font=ButtonFontSetting)
        SubButton27.place(x=150, y=430)  

    if (Dest.Destination28Enabled == True):
        global Destination28
        Destination28 = Dest.Destination28
        SubButton28 = Button(DestinationSelectWindow, text=Destination28, height=2, width=15, command=lambda: ChangeStatus(SubSelection = 28), foreground=FontColorButtonSetting, background=LightingButtonBGSetting, font=ButtonFontSetting)
        SubButton28.place(x=275, y=430)  

    if (Dest.Destination29Enabled == True):
        global Destination29
        Destination29 = Dest.Destination29
        SubButton29 = Button(DestinationSelectWindow, text=Destination29, height=2, width=15, command=lambda: ChangeStatus(SubSelection = 29), foreground=FontColorButtonSetting, background=LightingButtonBGSetting, font=ButtonFontSetting)
        SubButton29.place(x=400, y=430)  

    if (Dest.Destination30Enabled == True):
        global Destination30
        Destination30 = Dest.Destination30
        SubButton30 = Button(DestinationSelectWindow, text=Destination30, height=2, width=15, command=lambda: ChangeStatus(SubSelection = 30), foreground=FontColorButtonSetting, background=LightingButtonBGSetting, font=ButtonFontSetting)
        SubButton30.place(x=525, y=430)  

    DestinationSelectWindow.mainloop()

def ChangeStatus(SubSelection):

    global SelectedStatusText
    
    if (SubSelection == 1):
        SelectedStatusText = Destination1
    elif (SubSelection == 2):
        SelectedStatusText = Destination2
    elif (SubSelection == 3):
        SelectedStatusText = Destination3
    elif (SubSelection == 4):
        SelectedStatusText = Destination4
    elif (SubSelection == 5):
        SelectedStatusText = Destination5
    elif (SubSelection == 6):
        SelectedStatusText = Destination6
    elif (SubSelection == 7):
        SelectedStatusText = Destination7
    elif (SubSelection == 8):
        SelectedStatusText = Destination8
    elif (SubSelection == 9):
        SelectedStatusText = Destination9
    elif (SubSelection == 10):
        SelectedStatusText = Destination10
    elif (SubSelection == 11):
        SelectedStatusText = Destination11
    elif (SubSelection == 12):
        SelectedStatusText = Destination12
    elif (SubSelection == 13):
        SelectedStatusText = Destination13
    elif (SubSelection == 14):
        SelectedStatusText = Destination14
    elif (SubSelection == 15):
        SelectedStatusText = Destination15
    elif (SubSelection == 16):
        SelectedStatusText = Destination16
    elif (SubSelection == 17):
        SelectedStatusText = Destination17
    elif (SubSelection == 18):
        SelectedStatusText = Destination18
    elif (SubSelection == 19):
        SelectedStatusText = Destination19
    elif (SubSelection == 20):
        SelectedStatusText = Destination20
    elif (SubSelection == 21):
        SelectedStatusText = Destination21
    elif (SubSelection == 22):
        SelectedStatusText = Destination22
    elif (SubSelection == 23):
        SelectedStatusText = Destination23
    elif (SubSelection == 24):
        SelectedStatusText = Destination24
    elif (SubSelection == 25):
        SelectedStatusText = Destination25
    elif (SubSelection == 26):
        SelectedStatusText = Destination26        
    elif (SubSelection == 27):
        SelectedStatusText = Destination27
    elif (SubSelection == 28):
        SelectedStatusText = Destination28
    elif (SubSelection == 29):
        SelectedStatusText = Destination29
    elif (SubSelection == 30):
        SelectedStatusText = Destination30

    if (ChosenEmployee == 1):
        labelEmployee1.config(text = SelectedStatusText)
    elif (ChosenEmployee == 2):
        labelEmployee2.config(text = SelectedStatusText)
    elif (ChosenEmployee == 3):
        labelEmployee3.config(text = SelectedStatusText)
    elif (ChosenEmployee == 4):
        labelEmployee4.config(text = SelectedStatusText)
    elif (ChosenEmployee == 5):
        labelEmployee5.config(text = SelectedStatusText)
    elif (ChosenEmployee == 6):
        labelEmployee6.config(text = SelectedStatusText)   
    elif (ChosenEmployee == 7):
        labelEmployee7.config(text = SelectedStatusText)
    elif (ChosenEmployee == 8):
        labelEmployee8.config(text = SelectedStatusText)
    elif (ChosenEmployee == 9):
        labelEmployee9.config(text = SelectedStatusText)
    elif (ChosenEmployee == 10):
        labelEmployee10.config(text = SelectedStatusText)    
    elif (ChosenEmployee == 11):
        labelEmployee11.config(text = SelectedStatusText)
    elif (ChosenEmployee == 12):
        labelEmployee12.config(text = SelectedStatusText)
    elif (ChosenEmployee == 13):
        labelEmployee13.config(text = SelectedStatusText)
    elif (ChosenEmployee == 14):
        labelEmployee14.config(text = SelectedStatusText)
    elif (ChosenEmployee == 15):
        labelEmployee15.config(text = SelectedStatusText)
    elif (ChosenEmployee == 16):
        labelEmployee16.config(text = SelectedStatusText)
    elif (ChosenEmployee == 17):
        labelEmployee17.config(text = SelectedStatusText)
    elif (ChosenEmployee == 18):
        labelEmployee18.config(text = SelectedStatusText)
    elif (ChosenEmployee == 19):
        labelEmployee19.config(text = SelectedStatusText)
    elif (ChosenEmployee == 20):
        labelEmployee20.config(text = SelectedStatusText)    

    DestinationSelectWindow.destroy()

MainMenu()