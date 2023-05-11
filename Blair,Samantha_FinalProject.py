"""
    Samantha Blair
    Final Project
    Wagging Tail Rescue GUI Application
    
    This program is an online pet adoption application.
    The program allows for the user to apply to adopt either a cat or dog.
    Once the user has made a decision it will take them to the application
    to fill our neccessary information such as name, address, email,
    and telephone number.
 """

#Import libraries
from tkinter import *
from tkinter import messagebox
import os
from PIL import Image, ImageTk

#create Second Window
def App():
    parent=Tk()
    parent.title("Wagging Tail Rescuse Application")
    parent.geometry("550x600")
    parent.configure(bg="Light Blue")
   
    
    #Create a label to display name instruction
    nameLabel=Label(parent, text="Enter your first and last name:", bg="Light Blue")
    nameLabel.pack()
    
    #Validate name
    def validation():
        n=nameEntry.get()
        
        try:
            if len(n) == 0:
                msg.configure(text='Name cannot be empty!')
            elif any(ch.isdigit() for ch in n):
                msg.configure(text="Name cannot have numerics!")
            elif len(n) <=2:
                msg.configure(text="Minimum 3 characters!")
            elif len(n) >300:
                msg.configure(text="Name is too long!")
        except Exception as ep:
            messagebox.showerror('error',ep)
            
        
            
        
    #Create an entry widget for user to input name
    nameEntry=Entry(parent, validate='focusout', validatecommand=validation)
    nameEntry.pack()
    
    #Create message label
    msg=Label(parent, text='', bg= "Light Blue")
    msg.pack()
    
    #Create a label to display email address instruction
    emailLabel=Label(parent,text="Enter your email address:", bg="Light Blue")
    emailLabel.pack()
    
    #Validate email
    def validation2():
        e=emailEntry.get()
        
        try:
            if len(e) == 0:
                msg2.configure(text='Email cannot be empty!')
            elif len(e) <=2:
                msg2.configure(text="Minimum 3 characters!")
            elif len(e) >300:
                msg2.configure(text="Email is too long!")
        except Exception as ep:
            messagebox.showerror('error',ep)
        
    
    
    #Create an entry widget for user to input email
    emailEntry=Entry(parent,validate='focusout',validatecommand=validation2)
    emailEntry.pack()
    
    #Create message label
    msg2=Label(parent, text='', bg= "Light Blue")
    msg2.pack()
    
    #Create a label to display phone number instruction
    phoneNumLabel=Label(parent,text="Enter your phone number:", bg="Light Blue")
    phoneNumLabel.pack()
    
    #Validate phone number 
    def validation3():
        ph=phoneNumEntry.get()
        
        try:
            if len(ph) == 0:
                msg3.configure(text='Phpne number cannot be empty!')
            elif len(ph) <=2:
                msg3.configure(text="Minimum 3 characters!")
            elif len(ph) >10:
                msg3.configure(text="Phone number is too long!")
        except Exception as ep:
            messagebox.showerror('error',ep)
    
    #Create an entry widget for user to input phone number
    phoneNumEntry=Entry(parent, validate='focusout', validatecommand=validation3)
    phoneNumEntry.pack()
    
    #Create message label
    msg3=Label(parent, text='', bg= "Light Blue")
    msg3.pack()
    
    #Create a label to display address instruction
    addressLabel=Label(parent,text="Enter your address:", bg="Light Blue")
    addressLabel.pack()
    
    #Create validation for address
    def validation4():
        a=addressEntry.get()
        
        try:
            if len(a) == 0:
                msg4.configure(text='Address cannot be empty!')
            elif len(a) <=2:
                msg4.configure(text="Minimum 3 characters!")
            elif len(a) >300:
                msg4.configure(text="Address is too long!")
        except Exception as ep:
            messagebox.showerror('error',ep)
            
    #Create an entry widget for user to enter address
    addressEntry=Entry(parent,validate='focusout', validatecommand=validation4)
    addressEntry.pack()
    
    #Create a label for validation check
    msg4=Label(parent,text='', bg="Light Blue")
    msg4.pack()
    
    #Create a label to display the city instruction
    cityLabel=Label(parent,text="Enter your city:", bg="Light Blue")
    cityLabel.pack()
    
    #Create validation for city 
    def validation5():
        c=cityEntry.get()
        
        try:
            if len(c) == 0:
                msg5.configure(text='City cannot be empty!')
            elif any(ch.isdigit() for ch in c):
                msg5.configure(text="City cannot have numerics!")
            elif len(c) <=2:
                msg5.configure(text="Minimum 3 characters!")
            elif len(c) >30:
                msg.configure(text="City is too long!")
        except Exception as ep:
            messagebox.showerror('error',ep)
            
            
    #Create an entry widget for user to input city
    cityEntry=Entry(parent,validate='focusout',validatecommand=validation5)
    cityEntry.pack()
    
    #Create label for validation message
    msg5=Label(parent, text='', bg="Light Blue")
    msg5.pack()
    
    #Create a label to display state instruction
    stateLabel=Label(parent,text="Enter your State:", bg="Light Blue")
    stateLabel.pack()
    
    #Create validation for state entry
    def validation6():
        s=stateEntry.get()
        
        try:
            if len(s) == 0:
                msg6.configure(text='State cannot be empty!')
            elif any(ch.isdigit() for ch in s):
                msg6.configure(text="State cannot have numerics!")
            elif len(s) <=2:
                msg6.configure(text="Minimum 3 characters!")
            elif len(s) >30:
                msg6.configure(text="Name is too long!")
        except Exception as ep:
            messagebox.showerror('error',ep)
            
    #Create an entry widget for user to input state
    stateEntry=Entry(parent, validate='focusout',validatecommand=validation6)
    stateEntry.pack()
    
    #Create label for state validation message
    msg6=Label(parent, text='', bg='Light Blue')
    msg6.pack()
    
    #Create a label to display zip code instruction
    zipCodeLabel=Label(parent,text="Enter your zip code:", bg="Light Blue")
    zipCodeLabel.pack()
    
    #Create validation for zip code
    def validation7():
        zc=zipCodeEntry.get()
        
        try:
            if len(zc) == 0:
                msg7.configure(text='Zip code cannot be empty!')
            elif len(zc) <5:
                msg7.configure(text="Minimum 5 characters!")
            elif len(zc) >5:
                msg7.configure(text="Zip code is too long!")
        except Exception as ep:
            messagebox.showerror('error',ep)
            
    #Create an entry widget for user to input zip code
    zipCodeEntry=Entry(parent,validate='focusout',validatecommand=validation7)
    zipCodeEntry.pack()
    
    #Create label for zip code validation message
    msg7=Label(parent, text='',bg='Light Blue')
    msg7.pack()
    
    #Create button to submit application for a cat
    submitButton=Button(parent, text="Click to submit an application!", bg="Blue", fg= "White", command = succession)
    submitButton.pack(pady= 10)
    

    
#Create submission successful window
def succession():
    

    
    # Define photo2 as a global variable
    photo2 = None

    def load_image():
        global photo2
        image = Image.open("lastphoto.jpg")
        resized_image = image.resize((300, 300))
        photo2 = ImageTk.PhotoImage(resized_image)

    def show_image():
        global photo2
        child = Toplevel()
        child.configure(bg="Light Blue")
        
        #Create label for image
        label2 = Label(child, image=photo2, bg="Light Blue")
        label2.pack()
        
        #Create window title
        sucTitleWindow=Label(child, text="Application Successfully Submitted!", font=("Arial Bold",16), bg="Light Blue")
        sucTitleWindow.pack(pady=50)
    
        #Create hear from us soon label
        contact=Label(child, text="Thank you for submitting your application to Wagging Tail Rescue.", bg="Light Blue")
        contact.pack(pady=30)
    
         #Set width of the label 
        width=200
    
         #Set the long text 
        longText= "Your application has been submitted and will be reviewed by a Wagging Tail Rescue employee shortly. Once your application is reviewed,we will reach out to you about adopting your new furry friend!"    
    
        #Create info label
        info=Label(child,text= longText, wraplength= width, bg="Light Blue")
        info.pack()

        
        #Create a button to close the window
        convertButton=Button(child, text="Exit", command=quit)
        convertButton.pack()

    load_image()
    show_image()

    
    
    

#Create First Window  
def main():
    
    #Create the main application window 
    root=Tk()
    
    #Create the title and background color of window
    root.title("Wagging Tail Rescue")
    root.configure(bg="Light Blue")
    
    
    #Create itnro label
    titleWindow=Label(root, text="Welcome to Wagging Tails Rescue!",font=("Arial bold",26), bg="Light Blue")
    titleWindow.pack(pady=30)
    
    #Create a introduction label
    intro=Label(root, text = "Where Pets Find Their People", font= ("Lucida Handwriting",20), bg="Light Blue")
    intro.pack()
    
    #Open image and resize it 
    image=Image.open("adoptapet.jpg")
    resizeImage= image.resize((500,300))
    
    #Convert the resized image to a photoimage object 
    photo=ImageTk.PhotoImage(resizeImage)
    
    #Create a label
    photoLabel=Label(root, image=photo)
    photoLabel.pack(pady=60)
    
    #Create adopt buttons to access application
    adoptButton=Button (root, text="Click here to fill out an application!", fg="White",bg="Blue", command = App)
    adoptButton.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
    
