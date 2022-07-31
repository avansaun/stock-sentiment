import tkinter
import customtkinter
import request

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        #self = customtkinter.CTk()  # create CTk window like you do with the Tk window
        self.title("Stock Sentiment self")
        self.geometry("900x600")

        

        #====== Create Panels ======

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Left Panel
        self.frame_left = customtkinter.CTkFrame(master=self, width=250, corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing

        self.leftColTitle = customtkinter.CTkLabel(master=self.frame_left, text="Search For Company", text_font=("Roboto Medium", -16))
        self.leftColTitle.grid(row=1, column=0, pady=10, padx=10)

        self.tickerInput = customtkinter.CTkEntry(master=self.frame_left, width=220, placeholder_text="Company Name or Ticker")
        self.tickerInput.grid(row=2, column=0, pady=10, padx=20)

        self.searchBtn = customtkinter.CTkButton(master=self.frame_left, text="Search", command=self.button_event)
        self.searchBtn.grid(row=3, column=0, pady=5, padx=20)

        #Right Panel
        self.frame_right = customtkinter.CTkFrame(master=self)


    def button_event(self):
        print("Searching for " + self.tickerInput.get())

if __name__ == "__main__":
    app = App()
    app.mainloop()