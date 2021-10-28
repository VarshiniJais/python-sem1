#importing required modules
from tkinter import *
import sys
import qrcode
import pyqrcode
from PIL import Image,ImageTk
from tkinter.font import Font
import re

#Creating a window
root=Tk()
root.title("QR Generator")
root.resizable(width=False,height=False)

#Function to generate QR code
def generate(lg,bw,fc,bc,content):
	logo=Image.open(lg)
	basewidth=bw
	wpercent = (basewidth/float(logo.size[0]))
	hsize = int((float(logo.size[1])*float(wpercent)))
	logo=logo.resize((basewidth,hsize),Image.ANTIALIAS)
	qr_big = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
	qr_big.add_data(content)
	qr_big.make()
	qr=qr_big.make_image(fill_color=fc, back_color=bc).convert('RGB')
	pos=((qr.size[0] - logo.size[0])//2,(qr.size[1]- logo.size[1])//2)
	qr.paste(logo,pos)
	qr.save("QR.png")
	
#Function to display the generated QR code	
def display():
	global photo
	global check
	photo=Image.open("QR.png")
	photo=photo.resize((260,260),Image.ANTIALIAS)
	photo=ImageTk.PhotoImage(photo)
	global lb
	lb=Label(frame2,image=photo)
	lb.grid(row=3,column=1)
	check=True
    
#Function to handle errors
def error():
	global photo
	global check
	if check==True:
		global lb
		lb.grid_forget()
	photo=Image.open("error.png")
	photo=photo.resize((250,80),Image.ANTIALIAS)
	photo=ImageTk.PhotoImage(photo)
	lb=Label(frame2,image=photo)
	lb.grid(row=3,column=1)

#Function to check the validity of URLs  
def url_check(content,type=None):
	if type!=None:
		if type in content and ' ' not in content:
			return True
		else:
			return False
	format_URL = re.compile(r'https?://www\.[a-z0-9]+\.[^\s]', re.IGNORECASE)
	if(re.match(format_URL,content)):
		return True
	else:
		return False
		
		
#Function to check validity of an email
def email_check(content):
	if re.match(r"[a-zA-z0-9]+@[a-zA-z]+\.[a-zA-z]+", content):
		return True
	else:
		return False
		
		
#Generating QR code for plain text
def text(content):
	qr= pyqrcode.create(content)
	qr.png("QR.png", scale=6)
	display()
	
#Generating QR code for youtube url
def youtube(content):
	val=url_check(content,"https://www.youtube.com")
	if val:
		generate("yt.png",175,"#aa0000","white",content)
		display()
	else:
		error()

#Generating QR code for instagram url
def instagram(content):
	val=url_check(content,"https://www.instagram.com")
	if val:
		generate("insta.png",140,"#9955ff","white",content)
		display()
	else:
		error()

#Generating QR code for twitter url
def twitter(content):
	val=url_check(content,"https://twitter.com")
	if val:
		generate("twitter.png",130,"#224488","#eeeeee",content)
		display()
	else:
		error()
		
#Generating QR code for general url
def url(content):
	val=url_check(content)
	if val:
		generate("google.png",140,"white","blue",content)
		display()
	else:
		error()

#Generating QR code to write a mail the email address
def email(content):
	val=email_check(content)
	if val:
		generate("email.png",180,"white","#cc0000","mailto:"+content)
		display()
	else:
		error()
		
#Generating QR code to dial the phone number
def phone(content):
    p=re.compile(r"\d{10}")
    if re.match(p,content):
        generate("phone.png",90,"green","white","tel:"+content)		
        display()
    else:
        error()
#Defining the first frame
def F1():
	frame1=LabelFrame(root,padx=50,pady=70,bg="#f4ac84")#449999
	frame1.grid(row=0,column=0,padx=10,pady=10)
	
	btxt = Button(frame1,width=10, text="Text",bg="#f4e484",font=Font(family="Georgia", size=14),command=lambda:(F4(),F2(text,"Enter Text")))#weight??
	btxt.grid(row=2, column=1, padx=5, pady=7)
    
	byt=Button(frame1,width=10,text="YouTube",bg="#f4e484",font=Font(family="Georgia", size=14),command=lambda:(F4(),F2(youtube,"Enter YouTube URL")))
	byt.grid(row=3,column=1,padx=5,pady=7)
    
	binsta=Button(frame1,width=10,text="Instagram",bg="#f4e484",font=Font(family="Georgia", size=14),command=lambda:(F4(),F2(instagram,"Enter Instagram URL")))
	binsta.grid(row=4,column=1,padx=5,pady=7)

	btwitter=Button(frame1,width=10,text="Twitter",bg="#f4e484",font=Font(family="Georgia", size=14),command=lambda:(F4(),F2(twitter,"Enter Twitter URL")))
	btwitter.grid(row=5,column=1,padx=5,pady=7)
    
	burl=Button(frame1,width=10,text="URL",bg="#f4e484",font=Font(family="Georgia", size=14),command=lambda:(F4(),F2(url,"Enter Website URL")))
	burl.grid(row=6,column=1,padx=5,pady=7)

	bemail=Button(frame1,width=10,text="Email",bg="#f4e484",font=Font(family="Georgia", size=14),command=lambda:(F4(),F2(email,"Enter Email ID")))
	bemail.grid(row=7,column=1,padx=5,pady=7)

	bphone=Button(frame1,width=10,text="Phone",bg="#f4e484",font=Font(family="Georgia", size=14),command=lambda:(F4(),F2(phone,"Enter Phone Number to Dial")))
	bphone.grid(row=8,column=1,padx=5,pady=7)

#Defining the second frame
def F2(name,display):
	global frame2
	frame2=LabelFrame(root,padx=50,pady=30,width=700,height=500,bg="#f4ac84")
	frame2.grid(padx=10,pady=10,row=0,column=1)
	label = Label(frame2,text=display, bg="#f4ac84",font=Font(family="Georgia", size=15))
	label.grid(row=1, column=0, padx=5, pady=5)
	global entry
	entry = Entry(frame2,width=40)
	entry.grid(row=1, column=1, padx=5, pady=7)
	bgen = Button(frame2,width=10, text="Generate",bg="#f4e484",font=Font(family="Georgia", size=11),command=lambda:name(entry.get()))
	bgen.grid(row=2, column=8, padx=5, pady=7)
	bbck = Button(frame2,width=10, text="Back",bg="#f4e484",font=Font(family="Georgia", size=11),command=F4)
	bbck.grid(row=4, column=8, padx=5, pady=7)

#Defining the third frame	
def F3():
	global frame3
	frame3=LabelFrame(root,padx=153,pady=5,width=700,height=450,bg="#caa5a9")
	frame3.grid(padx=10,pady=10,row=1,column=0,columnspan=2)
	label = Label(frame3,text="Created By:", bg="#caa5a9",font=Font(family="Georgia", size=13))
	label.grid(row=0,column=0,padx=5, pady=5)
	label = Label(frame3,text="  Shreyas S Pawar  ", bg="#caa5a9",font=Font(family="Georgia", size=13))
	label.grid(row=0,column=1,padx=5, pady=5)
	label = Label(frame3,text="  Vaishnavi V B  ", bg="#caa5a9",font=Font(family="Georgia", size=13))
	label.grid(row=0,column=2,padx=5, pady=5)
	label = Label(frame3,text="  Varshini Jayasankar  ", bg="#caa5a9",font=Font(family="Georgia", size=13))
	label.grid(row=0,column=3,padx=5, pady=5)

#Defining the fourth frame
def F4():
	global frame4
	frame4=LabelFrame(root,padx=200,pady=205,width=700,height=450,bg="#f3d9a4")
	frame4.grid(padx=10,pady=10,row=0,column=1)
	label = Label(frame4,text="QR Code Generator", bg="#f3d9a4",font=Font(family="Georgia", size=30, weight="normal"))
	label.grid(padx=5, pady=5)
	label = Label(frame4,text="Select the options on the left to generate your own QR", bg="#f3d9a4",font=Font(family="Georgia", size=15, weight="normal"))
	label.grid(padx=5, pady=5)

#Defining a main function and calling it
def main():
	F1()
	F3()
	F4()
	global check
	check=False
main()

#sample cases
#text : this is our project
#youtube : https://www.youtube.com/watch?v=FGTv9-oQhIg&list=RDu-FaTNxrWhw&index=8
#instagram : https://www.instagram.com/aliaabaat/?hl=en
#twitter : https://twitter.com/narendramodi?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor
#url : https://www.pes.edu/
#email : belikerevaishnavi@gmail.com
#phone : +918618932551

root.mainloop()
#End of the project


