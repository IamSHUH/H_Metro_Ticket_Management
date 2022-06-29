from tkinter import *
import webbrowser

#creating a window
root = Tk()
root.title('About Developer')
root.geometry('1160x652')

#providing developer portfolio link to the button
new = 1
url = "https://shuhportfolio.netlify.app/"

def openbrowser():
    webbrowser.open(url,new=new)

#adding background image
bg = PhotoImage(file = 'images/mts.png')

canvas = Canvas(
	root, 
	width = 500,
	height = 400
	)

canvas.pack(fill='both', expand = True)

canvas.create_image(
	0, 
	0, 
	image=bg,
	anchor = "nw"
	)
''''
canvas.create_text(
	250, 
	150, 
	text = 'About Developer',
	font=('Arial', 50),
	)
'''
#creating button for portfolio link
btn = Button(
	root, 
	text = 'EXPLORE MORE ABOUT DEVELOPER',
	command=openbrowser,
	width=35,
	height=2,
	#relief=SOLID,
	font=('arial', 12)
	)
	
#window sizing
btn_canvas = canvas.create_window(
	500, 
	300,
	anchor = "nw",
	window = btn,
	)


root.mainloop()