from tkinter import *
from tkinter import filedialog
from pytube import YouTube
import os
import time
import customtkinter

# Modes: system (default), light, dark
customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("green")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("640x380")
        self.title("YouTube downloader v 2.0 ")
        self.iconbitmap(os.getcwd()+"\img\icona.ico")
        self.resizable(False, False)
        self.main_font = ("Helvetica", 12)
        self.button_font = ("Helvetica", 15, "bold")
        self.yt = None
        self.choice = 0
        self.check_var = StringVar()
        self.output_dir = os.getcwd()+"\output"
        

        #frames
        self.input_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.text_frame = customtkinter.CTkFrame(self)
        self.progress_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.progress_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.browser_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.button_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.help_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.input_frame.pack()
        self.text_frame.pack()
        self.progress_frame.pack()
        self.browser_frame.pack()
        self.button_frame.pack()
        self.help_frame.pack()
     
        #frame input_frame
        self.user_input = customtkinter.CTkEntry(self.input_frame, 
                                                  width=340, 
                                                  font=self.main_font
                                                  )
        self.user_input.grid(row=0, column=0, padx=5, pady=15)

        self.chackbox_mp3 = customtkinter.CTkCheckBox(self.input_frame,
                                                      text="mp3",
                                                      width=40, 
                                                      variable=self.check_var,
                                                      onvalue="1", 
                                                      offvalue="0",
                                                      command=self.checkbox_event
                                                      )
        self.chackbox_mp3.grid(row=0, column=1, padx=(2,10))

        self.button_add = customtkinter.CTkButton(self.input_frame,
                                                  text="add to download", 
                                                  width=140, 
                                                  font=self.button_font, 
                                                  command=self.add_link
                                                  )
        self.button_add.grid(row=0, column=2, padx=5, pady=5, ipadx=5)
       
       
        #frame text_frame
        self.label_title = customtkinter.CTkLabel(self.text_frame,
                                                  text="info about video/mp3", 
                                                  width=560,
                                                  justify="right",
                                                  anchor="e",
                                                  font=("", 12, "bold")
                                                  )
        self.label_title.grid(row=0, column=0, padx=(0,10))

        self.label_name = customtkinter.CTkLabel(self.text_frame, 
                                                 text="", 
                                                 width=580,
                                                 justify="left",
                                                 anchor="w"
                                                 )
        self.label_name.grid(row=1, column=0, padx=5)
        self.label_author = customtkinter.CTkLabel(self.text_frame, 
                                                   text="", 
                                                   width=580,
                                                   justify="left",
                                                   anchor="w"
                                                   )
        self.label_author.grid(row=2, column=0, padx=5)
        self.label_views = customtkinter.CTkLabel(self.text_frame, 
                                                  text="", 
                                                  width=580,
                                                  justify="left",
                                                  anchor="w"
                                                  )
        self.label_views.grid(row=3, column=0, padx=5)
        self.label_file_size = customtkinter.CTkLabel(self.text_frame, 
                                                  text="", 
                                                  width=580,
                                                  justify="left",
                                                  anchor="w"
                                                  )
        self.label_file_size.grid(row=4, column=0, padx=5)

        #frame button_frame
        self.button_down = customtkinter.CTkButton(self.button_frame, 
                                                   text="download", 
                                                   width=480, 
                                                   font=self.button_font, 
                                                   command=self.download_link
                                                   )
        self.button_down.grid(row=0, column=1, padx=5, pady=5, ipadx=5)

        self.button_close = customtkinter.CTkButton(self.button_frame, 
                                                    text="close", 
                                                    width=85, 
                                                    font=self.button_font, 
                                                    command=self.close_window
                                                    )
        self.button_close.grid(row=0, column=2, padx=4, pady=4)

        #frame browser_frame
        self.button_browser = customtkinter.CTkButton(self.browser_frame, 
                                                      text="path to save", 
                                                      font=self.button_font, 
                                                      command=self.brows_directory
                                                      )
        self.button_browser.grid(row=0, column=2,  padx=4, pady=4)

        self.label_path = customtkinter.CTkLabel(self.browser_frame, 
                                                 text=self.output_dir, 
                                                 justify="left", 
                                                 anchor="w", 
                                                 width=440
                                                 )
        self.label_path.grid(row=0, column=0, padx=(4,0))


        #frame progress_frame
        self.bar = customtkinter.CTkProgressBar(self.progress_frame, 
                                                width=500, 
                                                mode='determinate'
                                                )
        self.bar.grid(row=0, column=0, pady=15)
        self.bar.set(value=0)
      
        self.label_percent = customtkinter.CTkLabel(self.progress_frame, 
                                                    text="0 %",  
                                                    width=80, 
                                                    font=("", 15, "bold")
                                                    )
        self.label_percent.grid(row=0, column=1)

        self.label_streams = customtkinter.CTkLabel(self.help_frame, 
                                                  text="", 
                                                  width=580,
                                                  justify="left",
                                                  anchor="w",
                                                  wraplength=550
                                                 )
        self.label_streams.grid(row=0, column=0, pady=(10,0))

    #video or audio
    def checkbox_event(self):
        self.choice = int(self.check_var.get())

    #select directory for saving
    def brows_directory(self):
        hlp = filedialog.askdirectory()
        if hlp !="":
            self.output_dir = hlp
        self.label_path.configure(text=self.output_dir)

    #on_progress_callback function will run whenever a chunk is downloaded from a video
    def progress_check(self, chunk, file_handle, remaining):
        percent = round(100*(self.yd.filesize - remaining)/self.yd.filesize, 1)
        self.label_percent.configure(text=f"{percent} %")
        self.bar.set(value = float(percent/100))
        self.update()      

    #add link for downloading
    def add_link(self):
        link = self.user_input.get()
        self.bar.set(value=0)
        self.label_percent.configure(text="0 %")
        self.label_streams.configure(text="")
        self.label_author.configure(text="")
        self.label_views.configure(text="")
        self.label_file_size.configure(text="")
        try:
            self.yt = YouTube(link, on_progress_callback=self.progress_check)
            
            if self.choice == 0:   
                self.yd = self.yt.streams.get_highest_resolution()  
            else:
                # [print(one_stream) for one_stream in self.yt.streams.filter(only_audio=True)]
                self.yd = self.yt.streams.get_audio_only()
    
            self.label_name.configure(text=f"title: {self.yt.title}")
            self.label_author.configure(text=f"author: {self.yt.author}")
            self.label_views.configure(text=f"views: {self.yt.views}")
            self.label_file_size.configure(text=f"file size: {round(self.yd.filesize/1024/1024,2)} MB")
        except:
            print("Connection Error")
            self.label_name.configure(text=f"Connection Error, check the link and try it again")
    
    #start downloading process from link
    def download_link(self):
        print("start download")
        prefix_name = round(time.time())
        try:
            if self.choice == 1:
                out_file = self.yd.download(output_path=self.output_dir, filename=str(prefix_name)+self.yt.title)
                base, ext = os.path.splitext(out_file)
                new_file = base + ".mp3"
                os.rename(out_file, new_file)
            else:
                new_file = self.yd.download(output_path=self.output_dir, filename_prefix=str(prefix_name))

            self.label_streams.configure(text=f"download complete:\n{new_file}")
        except:
            print("download error")
            self.label_streams.configure(text="download error, try it again")

    def close_window(self):
        self.destroy()
    

app = App()
app.mainloop()

#test youtube links
#https://www.youtube.com/watch?v=-bTdbOiN6y8
#https://www.youtube.com/watch?v=iM3kjbbKHQU