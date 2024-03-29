#converts kilo to miles
import tkinter

class KiloConvertGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame =tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        
        self.prompt_label =tkinter.Label(self.top_frame,text='Enter a distance in kilometers: ')
        self.kilo_entry = tkinter.Entry(self.top_frame,width=10)
        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')

        self.descr_label = tkinter.Label(self.mid_frame,text='Converted to miles:')
        self.value = tkinter.StringVar() #StringVar object associated w/ an output label
        self.miles_label = tkinter.Label(self.mid_frame, textvariable=self.value) #label associated w/ StringVar
        self.descr_label.pack(side='left')
        
        self.miles_label.pack(side='left')
        self.calc_button = tkinter.Button(self.bottom_frame,text='Convert',command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,text='Quit',command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()
    
    def convert(self):
        kilo = float(self.kilo_entry.get())
        miles = kilo *0.6214
        self.value.set(miles) #convert miles to a string and store it in the StringVar object

if __name__ == '__main__':
    kilo_conv = KiloConvertGUI()