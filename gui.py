import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

class Gui(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520
    #CTK = customtkinter.CTk()

    def __init__(self):
        super().__init__()
        
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{Gui.WIDTH}x{Gui.HEIGHT}")

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self, width=180, corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")
        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        #----Text ("Entry") Input
        self.entry = customtkinter.CTkEntry(
            master=self.frame_right,
            width=120,
            placeholder_text="Enter Stock Ticker Symbol")
        self.entry.grid(row=1, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        #----Button----
        self.button_1 = customtkinter.CTkButton(
            master=self.frame_right,
            text="Search",
            command=self.button_event)
        self.button_1.grid(row=2, column=0, pady=10, padx=20)

    def button_event(self):
        print("Searching...")

if __name__ == "__main__":
    app = Gui()
    app.mainloop()