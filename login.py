from twilio.rest import Client
from tkinter import *
from tkinter import messagebox
import random


class OtpLogin(Tk):
    """
    This class holds the logic to create UI , send otp and validate otp.
    """
    def __init__(self):
        """
        This is constructor method.
        """
        super().__init__()
        self.geometry("600x550")
        self.resizable(False, False)
        self.otp = random.randint(100000, 999999)
        # keys nad mobile number can be used below to send otp to provided mobile number using twilio service.
        # we can sign up on twilio for getting the keys and mbie number.
        self.client = Client("", "")
        self.client.messages.create(to=[""], from_="", body=self.b)

    def labels(self):
        """
        This method is used to create the labels on canvas.
        :return: None
        """
        self.canvas = Canvas(self, bg="white", width=400, height=280)
        self.canvas.place(x=100, y=60)
        self.title = Label(self, text="OTP Verfication", font="bold, 20", bg="#38ACEC")
        self.title.place(x=210, y=90)

    def input(self):
        """
        This method will be used to take the input.
        :return: None
        """
        self.user_name = Text(self, borderwidth=2, wrap="word", width=29, height=2)
        self.user_name.place(x=190, y=160)

    def buttons(self):
        """
        This method will initialize buttons
        :return: None
        """
        self.submit_image = PhotoImage(file="submit.png")
        self.submit_btn = Button(self, image=self.submit_image, command=self.check_otp, border=0)
        self.submit_btn.place(x=200, y=240)

        self.resend_image = PhotoImage(file="resent.png")
        self.resend_btn = Button(self, image=self.resend_image, border=0)
        self.resend_btn.place(x=250, y=350)

    def resend_otp(self):
        """
        This method will be used to resend the otp.
        :return: None
        """
        self.otp = random.randint(100000, 999999)
        self.client = Client("", "")
        self.client.messages.create(to=[""], from_="", body=self.b)

    def check_otp(self):
        """
        This methos will be used to validate the OTP.
        :return: None
        """
        try:
            self.user_input = int(self.user_name.get(1.0, "end-1c"))
            if self.user_input == self.otp:
                messagebox.showinfo("showinfo", "Login Success")
                self.otp = "Done"
            elif self.otp == "Done":
                messagebox.showinfo("showinfo", "already entered the otp")
            else:
                messagebox.showinfo("showinfo", "Wrong otp")
        except:
            messagebox.showinfo("showinfo", "invalid otp")


if __name__ == "__main__":
    ui = OtpLogin()
    ui.labels()
    ui.input()
    ui.buttons()
    ui.mainloop()

