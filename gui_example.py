from tkinter import *    # standard binging to TK (tk-inter(face))
from tkinter import ttk  # binding to newer "themed widgets"
from tkinter import messagebox
from PIL import ImageTk, Image


def design_window():

    def ok_button():
        msg_out = "You have entered {} with blood type {}{}.\n" \
                  "Do you want to save this information?" \
                .format(donor_name.get(), blood_letter.get(), rh_factor.get())
        response = messagebox.askyesno(message=msg_out, icon="question")
        if response is False:
            return
        # to get field value of entry, there are two ways:
        # name_entry.delete(0, 'end')
        # name_entry.insert(0, 'Modified')
        print("Donor name: {}".format(donor_name.get()))
        # print("Donor name: {}".format(name_entry.get()))
        print("Blood letter: {}".format(blood_letter.get()))
        print("Rh factor: {}".format(rh_factor.get()))
        donor_name.set("")
        blood_letter.set("")
        rh_factor.set("-")
        # do_other_stuff()
        return

    def cancel_button():
        root.destroy()
        return

    def checkbox_change():
        if rh_factor.get() == "+":
            rh_check["text"] = "Rh factor - Selected"
            # rh_check.configure(text="Rh factor - Selected")
        elif rh_factor.get() == "-":
            rh_check["text"] = "Rh factor - Not Selected"

    def activate_btn1():
        new_btn0.state(["!disabled"])
        # do not include ()
        # or it would run while compiling
        new_btn0.instate(["!disabled"], do_other_stuff)
        return

    def disactivate_btn1():
        new_btn0.state(["disabled"])
        # if no second parameter exists, this function checks for flags in list
        new_btn0.instate(["!disabled"], do_other_stuff)
        return

    def combo_disp(event):  # remember to include event
        print("Center location chosen: {}-{}".format(
            donor_center_combo.current(), donor_center.get()))
        return

    root = Tk()  # sets up the main window
    root.title("Blood Donor Database")
    root.columnconfigure(0, pad=5)
    root.columnconfigure(1, pad=5)
    root.columnconfigure(2, pad=5)
    # root.rowconfigure(4, pad=20)

    # Add Blood Donor Database Label
    top_label = ttk.Label(root, text="Blood Donor Database")
    top_label.grid(column=0, row=0, columnspan=2, sticky=W)
    # resultsContents = StringVar()
    # top_label['textvariable'] = resultsContents
    # resultsContents.set('New value to display')

    # Add Name Label and Entry
    name_label = ttk.Label(root, text="Name:")
    name_label.grid(column=0, row=1)
    donor_name = StringVar()
    # donor_name.set("Enter name here...")
    # width indicates # of chars or pixels
    name_entry = ttk.Entry(root, textvariable=donor_name, width=30, show="*")
    name_entry.grid(column=1, row=1)  # , padx=5

    # Add Radiobuttons
    blood_letter = StringVar()
    # button1 = ttk.Radiobutton(root, text="A", variable=blood_letter,
    #                           value="A")
    # button1.grid(column=0, row=2)  # depends on whether you change later
    ttk.Radiobutton(root, text="A", variable=blood_letter,
                    value="A").grid(column=0, row=2, sticky=W)
    ttk.Radiobutton(root, text="B", variable=blood_letter,
                    value="B").grid(column=0, row=3, sticky=W)
    ttk.Radiobutton(root, text="AB", variable=blood_letter,
                    value="AB").grid(column=0, row=4, sticky=W)
    ttk.Radiobutton(root, text="O", variable=blood_letter,
                    value="O").grid(column=0, row=5, sticky=W)

    # Add Rh Factor Checkbox
    rh_factor = StringVar()
    rh_factor.set("-")  # init value
    rh_check = ttk.Checkbutton(root, text="Rh Positive", variable=rh_factor,
                               onvalue="+", offvalue="-",
                               command=checkbox_change)
    rh_check.grid(column=1, row=3)

    # Add buttons
    ok_btn = ttk.Button(root, text="OK", command=ok_button)
    ok_btn.grid(column=1, row=5)
    cancel_btn = ttk.Button(root, text="Cancel", command=cancel_button)  # no ()
    cancel_btn.grid(column=2, row=5)

    # Add Donation Center Dropdown
    ttk.Label(root, text="Nearest Donor Center").grid(column=2, row=0)
    donor_center = StringVar()
    donor_center_combo = ttk.Combobox(root, textvariable=donor_center)
    donor_center_combo.grid(column=2, row=1)  # , padx=5
    donor_center_combo["values"] = ("Durham", "Rayleigh", "Cary", "Apex")
    donor_center_combo.state(["readonly"])
    donor_center_combo.current(0)
    donor_center_combo.bind('<<ComboboxSelected>>', combo_disp)

    # Frame
    # The content Frame is placed in root
    content = ttk.Frame(root, width='10c', height='20c')  # if no in-widgets
    content.grid(column=1, row=6, pady=10)
    content['padding'] = (10, 10)  # for in-widgets

    content['borderwidth'] = 2    # these two call together
    content['relief'] = 'groove'  # these two call together

    # The ok_btn button is placed in the content Frame
    new_btn0 = ttk.Button(content, text="Btn 1")
    new_btn0.grid(column=0, row=0, sticky=E)
    new_btn0.state(["disabled"])
    new_btn1 = ttk.Button(content, text="Btn 2", command=activate_btn1)
    new_btn1.grid(column=0, row=1, padx=10)
    new_btn2 = ttk.Button(content, text="Btn 3", command=disactivate_btn1)
    new_btn2.grid(column=0, row=2, sticky=W)

    # Add image
    # my_image = PhotoImage(file="~/Downloads/20Spring/lab/20200310_12KPa_PWC"
    #                            "/MPSA/20200310_154146911_SWvelocities.gif")
    # my_img_label = Label(root, image=my_image)
    # my_img_label.grid(column=1, row=7)
    # Or use Pillow:
    # image_obj = Image.open("/Users/yangpeiliu/Desktop/Huahua.png")
    # my_image = ImageTk.PhotoImage(image_obj)
    # my_img_label = Label(root, image=my_image)
    # my_img_label.grid(column=1, row=7)

    # print("Before mainloop")
    root.mainloop()
    # print("After mainloop")
    return


def do_other_stuff():
    print("This function will do lots of things")
    return


if __name__ == '__main__':
    design_window()