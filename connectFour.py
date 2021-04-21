from tkinter import*
from tkinter import messagebox

root = Tk()
root.title('Darsh Shah - Ruthav Sadali')

#x starts so true
clicked = True
count = 0


def disable_all_buttons():
    b1.config(state = DISABLED)
    b2.config(state = DISABLED)
    b3.config(state = DISABLED)
    b4.config(state = DISABLED)
    b5.config(state = DISABLED)
    b6.config(state = DISABLED)
    b7.config(state = DISABLED)
    b8.config(state = DISABLED)
    b9.config(state = DISABLED)
    b10.config(state = DISABLED)
    b12.config(state = DISABLED)
    b13.config(state = DISABLED)
    b14.config(state = DISABLED)
    b15.config(state = DISABLED)
    b16.config(state = DISABLED)
    b17.config(state = DISABLED)
    b18.config(state = DISABLED)
    b19.config(state = DISABLED)
    b20.config(state = DISABLED)
    b21.config(state = DISABLED)
    b22.config(state = DISABLED)
    b23.config(state = DISABLED)
    b24.config(state = DISABLED)
    b25.config(state = DISABLED)
    b26.config(state = DISABLED)
    b27.config(state = DISABLED)
    b28.config(state = DISABLED)
    b29.config(state = DISABLED)
    b30.config(state = DISABLED)
    b31.config(state = DISABLED)
    b32.config(state = DISABLED)
    b33.config(state = DISABLED)
    b34.config(state = DISABLED)
    b35.config(state = DISABLED)
    b36.config(state = DISABLED)
    b37.config(state = DISABLED)
    b38.config(state = DISABLED)
    b39.config(state = DISABLED)
    b40.config(state = DISABLED)
    b41.config(state = DISABLED)
    b42.config(state = DISABLED)
##CHECKIFWONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
def checkifwon():
    global winner
    winner = False
    #ACCROSS FIRST ROW ---------------------------------------------------------------------------------------------------------------------------------
    if b1["text"] == "red" and b2["text"] == "red" and b3["text"] == "red" and b4["text"] == "red":
        b1.config(bg = "lawngreen")
        b2.config(bg = "lawngreen")
        b3.config(bg = "lawngreen")
        b4.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b2["text"] == "red" and b3["text"] == "red" and b4["text"] == "red" and b5["text"] == "red":
        b2.config(bg = "lawngreen")
        b3.config(bg = "lawngreen")
        b4.config(bg = "lawngreen")
        b5.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b3["text"] == "red" and b4["text"] == "red" and b5["text"] == "red" and b6["text"] == "red":
        b3.config(bg = "lawngreen")
        b4.config(bg = "lawngreen")
        b5.config(bg = "lawngreen")
        b6.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b4["text"] == "red" and b5["text"] == "red" and b6["text"] == "red" and b7["text"] == "red":
        b2.config(bg = "lawngreen")
        b3.config(bg = "lawngreen")
        b4.config(bg = "lawngreen")
        b5.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
        #ACCROSS SECOND ROW ---------------------------------------------------------------------------------------------------------------------------------
    elif b8["text"] == "red" and b9["text"] == "red" and b10["text"] == "red" and b11["text"] == "red":
        b8.config(bg = "lawngreen")
        b9.config(bg = "lawngreen")
        b10.config(bg = "lawngreen")
        b11.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b9["text"] == "red" and b10["text"] == "red" and b11["text"] == "red" and b12["text"] == "red":
        b9.config(bg = "lawngreen")
        b10.config(bg = "lawngreen")
        b11.config(bg = "lawngreen")
        b12.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b10["text"] == "red" and b11["text"] == "red" and b12["text"] == "red" and b13["text"] == "red":
        b10.config(bg = "lawngreen")
        b11.config(bg = "lawngreen")
        b12.config(bg = "lawngreen")
        b13.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b11["text"] == "red" and b12["text"] == "red" and b13["text"] == "red" and b14["text"] == "red":
        b12.config(bg = "lawngreen")
        b13.config(bg = "lawngreen")
        b14.config(bg = "lawngreen")
        b11.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    #ACCROSS THIRD ROW ---------------------------------------------------------------------------------------------------------------------------------
    elif b15["text"] == "red" and b16["text"] == "red" and b17["text"] == "red" and b18["text"] == "red":
        b15.config(bg = "lawngreen")
        b16.config(bg = "lawngreen")
        b17.config(bg = "lawngreen")
        b18.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b16["text"] == "red" and b17["text"] == "red" and b18["text"] == "red" and b19["text"] == "red":
        b16.config(bg = "lawngreen")
        b17.config(bg = "lawngreen")
        b18.config(bg = "lawngreen")
        b19.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b17["text"] == "red" and b18["text"] == "red" and b19["text"] == "red" and b20["text"] == "red":
        b17.config(bg = "lawngreen")
        b18.config(bg = "lawngreen")
        b19.config(bg = "lawngreen")
        b20.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b18["text"] == "red" and b19["text"] == "red" and b20["text"] == "red" and b21["text"] == "red":
        b18.config(bg = "lawngreen")
        b19.config(bg = "lawngreen")
        b20.config(bg = "lawngreen")
        b21.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    #ACCROSS FOURTH ROW ---------------------------------------------------------------------------------------------------------------------------------
    elif b22["text"] == "red" and b23["text"] == "red" and b24["text"] == "red" and b25["text"] == "red":
        b22.config(bg = "lawngreen")
        b23.config(bg = "lawngreen")
        b24.config(bg = "lawngreen")
        b25.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b23["text"] == "red" and b24["text"] == "red" and b25["text"] == "red" and b26["text"] == "red":
        b23.config(bg = "lawngreen")
        b24.config(bg = "lawngreen")
        b25.config(bg = "lawngreen")
        b26.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b24["text"] == "red" and b25["text"] == "red" and b26["text"] == "red" and b27["text"] == "red":
        b24.config(bg = "lawngreen")
        b25.config(bg = "lawngreen")
        b26.config(bg = "lawngreen")
        b27.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b25["text"] == "red" and b26["text"] == "red" and b27["text"] == "red" and b28["text"] == "red":
        b25.config(bg = "lawngreen")
        b26.config(bg = "lawngreen")
        b27.config(bg = "lawngreen")
        b28.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    #ACCROSS FIFTH ROW ---------------------------------------------------------------------------------------------------------------------------------
    elif b29["text"] == "red" and b30["text"] == "red" and b31["text"] == "red" and b32["text"] == "red":
        b29.config(bg = "lawngreen")
        b30.config(bg = "lawngreen")
        b31.config(bg = "lawngreen")
        b32.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b30["text"] == "red" and b31["text"] == "red" and b32["text"] == "red" and b33["text"] == "red":
        b30.config(bg = "lawngreen")
        b31.config(bg = "lawngreen")
        b32.config(bg = "lawngreen")
        b33.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b31["text"] == "red" and b32["text"] == "red" and b33["text"] == "red" and b34["text"] == "red":
        b31.config(bg = "lawngreen")
        b32.config(bg = "lawngreen")
        b33.config(bg = "lawngreen")
        b34.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b32["text"] == "red" and b33["text"] == "red" and b34["text"] == "red" and b35["text"] == "red":
        b32.config(bg = "lawngreen")
        b33.config(bg = "lawngreen")
        b34.config(bg = "lawngreen")
        b35.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    #ACCROSS SIXTH ROW ---------------------------------------------------------------------------------------------------------------------------------
    elif b36["text"] == "red" and b37["text"] == "red" and b38["text"] == "red" and b39["text"] == "red":
        b36.config(bg = "lawngreen")
        b37.config(bg = "lawngreen")
        b38.config(bg = "lawngreen")
        b39.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b37["text"] == "red" and b38["text"] == "red" and b39["text"] == "red" and b40["text"] == "red":
        b37.config(bg = "lawngreen")
        b38.config(bg = "lawngreen")
        b39.config(bg = "lawngreen")
        b40.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b38["text"] == "red" and b39["text"] == "red" and b40["text"] == "red" and b41["text"] == "red":
        b38.config(bg = "lawngreen")
        b39.config(bg = "lawngreen")
        b40.config(bg = "lawngreen")
        b41.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b39["text"] == "red" and b40["text"] == "red" and b41["text"] == "red" and b42["text"] == "red":
        b39.config(bg = "lawngreen")
        b40.config(bg = "lawngreen")
        b41.config(bg = "lawngreen")
        b42.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    
    

    #DOWN FIRST COLUMN===================================================================================================
    elif b1["text"] == "red" and b8["text"] == "red" and b15["text"] == "red" and b22["text"] == "red":
        b1.config(bg = "lawngreen")
        b8.config(bg = "lawngreen")
        b15.config(bg = "lawngreen")
        b22.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b8["text"] == "red" and b15["text"] == "red" and b22["text"] == "red" and b29["text"] == "red":
        b29.config(bg = "lawngreen")
        b8.config(bg = "lawngreen")
        b15.config(bg = "lawngreen")
        b22.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b36["text"] == "red" and b15["text"] == "red" and b22["text"] == "red" and b29["text"] == "red":
        b29.config(bg = "lawngreen")
        b36.config(bg = "lawngreen")
        b15.config(bg = "lawngreen")
        b22.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    #DOWN SECOND COLUMN===================================================================================================
    elif b2["text"] == "red" and b9["text"] == "red" and b16["text"] == "red" and b23["text"] == "red":
        b2.config(bg = "lawngreen")
        b9.config(bg = "lawngreen")
        b16.config(bg = "lawngreen")
        b23.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b9["text"] == "red" and b16["text"] == "red" and b23["text"] == "red" and b30["text"] == "red":
        b30.config(bg = "lawngreen")
        b9.config(bg = "lawngreen")
        b16.config(bg = "lawngreen")
        b23.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b37["text"] == "red" and b16["text"] == "red" and b23["text"] == "red" and b30["text"] == "red":
        b30.config(bg = "lawngreen")
        b37.config(bg = "lawngreen")
        b16.config(bg = "lawngreen")
        b23.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    #DOWN THIRD COLUMN===================================================================================================
    elif b3["text"] == "red" and b10["text"] == "red" and b17["text"] == "red" and b24["text"] == "red":
        b3.config(bg = "lawngreen")
        b10.config(bg = "lawngreen")
        b17.config(bg = "lawngreen")
        b24.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b10["text"] == "red" and b17["text"] == "red" and b24["text"] == "red" and b31["text"] == "red":
        b31.config(bg = "lawngreen")
        b10.config(bg = "lawngreen")
        b17.config(bg = "lawngreen")
        b24.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b38["text"] == "red" and b17["text"] == "red" and b24["text"] == "red" and b31["text"] == "red":
        b31.config(bg = "lawngreen")
        b38.config(bg = "lawngreen")
        b17.config(bg = "lawngreen")
        b24.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    #DOWN FOURTH COLUMN===================================================================================================
    elif b4["text"] == "red" and b11["text"] == "red" and b18["text"] == "red" and b25["text"] == "red":
        b4.config(bg = "lawngreen")
        b11.config(bg = "lawngreen")
        b18.config(bg = "lawngreen")
        b25.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b11["text"] == "red" and b18["text"] == "red" and b25["text"] == "red" and b32["text"] == "red":
        b32.config(bg = "lawngreen")
        b11.config(bg = "lawngreen")
        b18.config(bg = "lawngreen")
        b25.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b39["text"] == "red" and b18["text"] == "red" and b25["text"] == "red" and b32["text"] == "red":
        b32.config(bg = "lawngreen")
        b39.config(bg = "lawngreen")
        b18.config(bg = "lawngreen")
        b25.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    #DOWN FIFTH COLUMN===================================================================================================
    elif b5["text"] == "red" and b12["text"] == "red" and b19["text"] == "red" and b26["text"] == "red":
        b5.config(bg = "lawngreen")
        b12.config(bg = "lawngreen")
        b19.config(bg = "lawngreen")
        b26.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b12["text"] == "red" and b19["text"] == "red" and b26["text"] == "red" and b33["text"] == "red":
        b33.config(bg = "lawngreen")
        b12.config(bg = "lawngreen")
        b19.config(bg = "lawngreen")
        b26.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b40["text"] == "red" and b19["text"] == "red" and b26["text"] == "red" and b33["text"] == "red":
        b33.config(bg = "lawngreen")
        b40.config(bg = "lawngreen")
        b19.config(bg = "lawngreen")
        b26.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    #DOWN SIXTH COLUMN===================================================================================================
    elif b6["text"] == "red" and b13["text"] == "red" and b20["text"] == "red" and b27["text"] == "red":
        b6.config(bg = "lawngreen")
        b13.config(bg = "lawngreen")
        b20.config(bg = "lawngreen")
        b27.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b13["text"] == "red" and b20["text"] == "red" and b27["text"] == "red" and b34["text"] == "red":
        b34.config(bg = "lawngreen")
        b13.config(bg = "lawngreen")
        b20.config(bg = "lawngreen")
        b27.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b41["text"] == "red" and b20["text"] == "red" and b27["text"] == "red" and b34["text"] == "red":
        b34.config(bg = "lawngreen")
        b41.config(bg = "lawngreen")
        b20.config(bg = "lawngreen")
        b27.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    #DOWN SEVENTH COLUMN===================================================================================================
    elif b7["text"] == "red" and b14["text"] == "red" and b21["text"] == "red" and b28["text"] == "red":
        b7.config(bg = "lawngreen")
        b14.config(bg = "lawngreen")
        b21.config(bg = "lawngreen")
        b28.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b14["text"] == "red" and b21["text"] == "red" and b28["text"] == "red" and b35["text"] == "red":
        b35.config(bg = "lawngreen")
        b14.config(bg = "lawngreen")
        b21.config(bg = "lawngreen")
        b28.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b42["text"] == "red" and b21["text"] == "red" and b28["text"] == "red" and b35["text"] == "red":
        b35.config(bg = "lawngreen")
        b42.config(bg = "lawngreen")
        b21.config(bg = "lawngreen")
        b28.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()

    #CROSSES
    elif b1["text"] == "red" and b9["text"] == "red" and b17["text"] == "red" and b25["text"] == "red":
        b1.config(bg = "lawngreen")
        b17.config(bg = "lawngreen")
        b9.config(bg = "lawngreen")
        b25.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b33["text"] == "red" and b9["text"] == "red" and b17["text"] == "red" and b25["text"] == "red":
        b33.config(bg = "lawngreen")
        b17.config(bg = "lawngreen")
        b9.config(bg = "lawngreen")
        b25.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b33["text"] == "red" and b41["text"] == "red" and b17["text"] == "red" and b25["text"] == "red":
        b33.config(bg = "lawngreen")
        b17.config(bg = "lawngreen")
        b41.config(bg = "lawngreen")
        b25.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()

    elif b2["text"] == "red" and b10["text"] == "red" and b18["text"] == "red" and b26["text"] == "red":
        b2.config(bg = "lawngreen")
        b18.config(bg = "lawngreen")
        b10.config(bg = "lawngreen")
        b26.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b34["text"] == "red" and b10["text"] == "red" and b18["text"] == "red" and b26["text"] == "red":
        b34.config(bg = "lawngreen")
        b18.config(bg = "lawngreen")
        b10.config(bg = "lawngreen")
        b26.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b34["text"] == "red" and b42["text"] == "red" and b18["text"] == "red" and b26["text"] == "red":
        b34.config(bg = "lawngreen")
        b18.config(bg = "lawngreen")
        b42.config(bg = "lawngreen")
        b26.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    
    elif b3["text"] == "red" and b11["text"] == "red" and b19["text"] == "red" and b27["text"] == "red":
        b3.config(bg = "lawngreen")
        b19.config(bg = "lawngreen")
        b11.config(bg = "lawngreen")
        b27.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b35["text"] == "red" and b11["text"] == "red" and b19["text"] == "red" and b27["text"] == "red":
        b35.config(bg = "lawngreen")
        b19.config(bg = "lawngreen")
        b11.config(bg = "lawngreen")
        b27.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()

    elif b4["text"] == "red" and b12["text"] == "red" and b20["text"] == "red" and b28["text"] == "red":
        b28.config(bg = "lawngreen")
        b20.config(bg = "lawngreen")
        b4.config(bg = "lawngreen")
        b12.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()

    elif b8["text"] == "red" and b16["text"] == "red" and b24["text"] == "red" and b32["text"] == "red":
        b8.config(bg = "lawngreen")
        b16.config(bg = "lawngreen")
        b24.config(bg = "lawngreen")
        b32.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b40["text"] == "red" and b16["text"] == "red" and b24["text"] == "red" and b32["text"] == "red":
        b40.config(bg = "lawngreen")
        b16.config(bg = "lawngreen")
        b24.config(bg = "lawngreen")
        b32.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    
    elif b15["text"] == "red" and b23["text"] == "red" and b31["text"] == "red" and b39["text"] == "red":
        b15.config(bg = "lawngreen")
        b23.config(bg = "lawngreen")
        b31.config(bg = "lawngreen")
        b39.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    
    elif b4["text"] == "red" and b22["text"] == "red" and b16["text"] == "red" and b10["text"] == "red":
        b16.config(bg = "lawngreen")
        b22.config(bg = "lawngreen")
        b4.config(bg = "lawngreen")
        b10.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    
    elif b21["text"] == "red" and b27["text"] == "red" and b33["text"] == "red" and b39["text"] == "red":
        b33.config(bg = "lawngreen")
        b21.config(bg = "lawngreen")
        b39.config(bg = "lawngreen")
        b27.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    
    elif b5["text"] == "red" and b11["text"] == "red" and b17["text"] == "red" and b23["text"] == "red":
        b5.config(bg = "lawngreen")
        b11.config(bg = "lawngreen")
        b17.config(bg = "lawngreen")
        b23.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b11["text"] == "red" and b17["text"] == "red" and b23["text"] == "red" and b29["text"] == "red":
        b11.config(bg = "lawngreen")
        b17.config(bg = "lawngreen")
        b23.config(bg = "lawngreen")
        b29.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    
    elif b14["text"] == "red" and b20["text"] == "red" and b26["text"] == "red" and b32["text"] == "red":
        b14.config(bg = "lawngreen")
        b20.config(bg = "lawngreen")
        b26.config(bg = "lawngreen")
        b32.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b20["text"] == "red" and b26["text"] == "red" and b32["text"] == "red" and b38["text"] == "red":
        b20.config(bg = "lawngreen")
        b26.config(bg = "lawngreen")
        b32.config(bg = "lawngreen")
        b38.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    
    elif b6["text"] == "red" and b12["text"] == "red" and b18["text"] == "red" and b24["text"] == "red":
        b6.config(bg = "lawngreen")
        b12.config(bg = "lawngreen")
        b18.config(bg = "lawngreen")
        b24.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b12["text"] == "red" and b18["text"] == "red" and b24["text"] == "red" and b30["text"] == "red":
        b12.config(bg = "lawngreen")
        b18.config(bg = "lawngreen")
        b24.config(bg = "lawngreen")
        b30.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b18["text"] == "red" and b24["text"] == "red" and b30["text"] == "red" and b36["text"] == "red":
        b18.config(bg = "lawngreen")
        b24.config(bg = "lawngreen")
        b30.config(bg = "lawngreen")
        b36.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    
    elif b7["text"] == "red" and b13["text"] == "red" and b19["text"] == "red" and b25["text"] == "red":
        b7.config(bg = "lawngreen")
        b13.config(bg = "lawngreen")
        b19.config(bg = "lawngreen")
        b25.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b13["text"] == "red" and b19["text"] == "red" and b25["text"] == "red" and b31["text"] == "red":
        b12.config(bg = "lawngreen")
        b18.config(bg = "lawngreen")
        b24.config(bg = "lawngreen")
        b30.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()
    elif b19["text"] == "red" and b25["text"] == "red" and b31["text"] == "red" and b37["text"] == "red":
        b19.config(bg = "lawngreen")
        b25.config(bg = "lawngreen")
        b31.config(bg = "lawngreen")
        b37.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "red wins")
        disable_all_buttons()

    #ACCROSS FIRST ROW ---------------------------------------------------------------------------------------------------------------------------------
    if b1["text"] == "yellow" and b2["text"] == "yellow" and b3["text"] == "yellow" and b4["text"] == "yellow":
        b1.config(bg = "lawngreen")
        b2.config(bg = "lawngreen")
        b3.config(bg = "lawngreen")
        b4.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b2["text"] == "yellow" and b3["text"] == "yellow" and b4["text"] == "yellow" and b5["text"] == "yellow":
        b2.config(bg = "lawngreen")
        b3.config(bg = "lawngreen")
        b4.config(bg = "lawngreen")
        b5.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b3["text"] == "yellow" and b4["text"] == "yellow" and b5["text"] == "yellow" and b6["text"] == "yellow":
        b3.config(bg = "lawngreen")
        b4.config(bg = "lawngreen")
        b5.config(bg = "lawngreen")
        b6.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b4["text"] == "yellow" and b5["text"] == "yellow" and b6["text"] == "yellow" and b7["text"] == "yellow":
        b2.config(bg = "lawngreen")
        b3.config(bg = "lawngreen")
        b4.config(bg = "lawngreen")
        b5.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
        #ACCROSS SECOND ROW ---------------------------------------------------------------------------------------------------------------------------------
    elif b8["text"] == "yellow" and b9["text"] == "yellow" and b10["text"] == "yellow" and b11["text"] == "yellow":
        b8.config(bg = "lawngreen")
        b9.config(bg = "lawngreen")
        b10.config(bg = "lawngreen")
        b11.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b9["text"] == "yellow" and b10["text"] == "yellow" and b11["text"] == "yellow" and b12["text"] == "yellow":
        b9.config(bg = "lawngreen")
        b10.config(bg = "lawngreen")
        b11.config(bg = "lawngreen")
        b12.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b10["text"] == "yellow" and b11["text"] == "yellow" and b12["text"] == "yellow" and b13["text"] == "yellow":
        b10.config(bg = "lawngreen")
        b11.config(bg = "lawngreen")
        b12.config(bg = "lawngreen")
        b13.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b11["text"] == "yellow" and b12["text"] == "yellow" and b13["text"] == "yellow" and b14["text"] == "yellow":
        b12.config(bg = "lawngreen")
        b13.config(bg = "lawngreen")
        b14.config(bg = "lawngreen")
        b11.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    #ACCROSS THIRD ROW ---------------------------------------------------------------------------------------------------------------------------------
    elif b15["text"] == "yellow" and b16["text"] == "yellow" and b17["text"] == "yellow" and b18["text"] == "yellow":
        b15.config(bg = "lawngreen")
        b16.config(bg = "lawngreen")
        b17.config(bg = "lawngreen")
        b18.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b16["text"] == "yellow" and b17["text"] == "yellow" and b18["text"] == "yellow" and b19["text"] == "yellow":
        b16.config(bg = "lawngreen")
        b17.config(bg = "lawngreen")
        b18.config(bg = "lawngreen")
        b19.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b17["text"] == "yellow" and b18["text"] == "yellow" and b19["text"] == "yellow" and b20["text"] == "yellow":
        b17.config(bg = "lawngreen")
        b18.config(bg = "lawngreen")
        b19.config(bg = "lawngreen")
        b20.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b18["text"] == "yellow" and b19["text"] == "yellow" and b20["text"] == "yellow" and b21["text"] == "yellow":
        b18.config(bg = "lawngreen")
        b19.config(bg = "lawngreen")
        b20.config(bg = "lawngreen")
        b21.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    #ACCROSS FOURTH ROW ---------------------------------------------------------------------------------------------------------------------------------
    elif b22["text"] == "yellow" and b23["text"] == "yellow" and b24["text"] == "yellow" and b25["text"] == "yellow":
        b22.config(bg = "lawngreen")
        b23.config(bg = "lawngreen")
        b24.config(bg = "lawngreen")
        b25.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b23["text"] == "yellow" and b24["text"] == "yellow" and b25["text"] == "yellow" and b26["text"] == "yellow":
        b23.config(bg = "lawngreen")
        b24.config(bg = "lawngreen")
        b25.config(bg = "lawngreen")
        b26.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b24["text"] == "yellow" and b25["text"] == "yellow" and b26["text"] == "yellow" and b27["text"] == "yellow":
        b24.config(bg = "lawngreen")
        b25.config(bg = "lawngreen")
        b26.config(bg = "lawngreen")
        b27.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b25["text"] == "yellow" and b26["text"] == "yellow" and b27["text"] == "yellow" and b28["text"] == "yellow":
        b25.config(bg = "lawngreen")
        b26.config(bg = "lawngreen")
        b27.config(bg = "lawngreen")
        b28.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    #ACCROSS FIFTH ROW ---------------------------------------------------------------------------------------------------------------------------------
    elif b29["text"] == "yellow" and b30["text"] == "yellow" and b31["text"] == "yellow" and b32["text"] == "yellow":
        b29.config(bg = "lawngreen")
        b30.config(bg = "lawngreen")
        b31.config(bg = "lawngreen")
        b32.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b30["text"] == "yellow" and b31["text"] == "yellow" and b32["text"] == "yellow" and b33["text"] == "yellow":
        b30.config(bg = "lawngreen")
        b31.config(bg = "lawngreen")
        b32.config(bg = "lawngreen")
        b33.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b31["text"] == "yellow" and b32["text"] == "yellow" and b33["text"] == "yellow" and b34["text"] == "yellow":
        b31.config(bg = "lawngreen")
        b32.config(bg = "lawngreen")
        b33.config(bg = "lawngreen")
        b34.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b32["text"] == "yellow" and b33["text"] == "yellow" and b34["text"] == "yellow" and b35["text"] == "yellow":
        b32.config(bg = "lawngreen")
        b33.config(bg = "lawngreen")
        b34.config(bg = "lawngreen")
        b35.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    #ACCROSS SIXTH ROW ---------------------------------------------------------------------------------------------------------------------------------
    elif b36["text"] == "yellow" and b37["text"] == "yellow" and b38["text"] == "yellow" and b39["text"] == "yellow":
        b36.config(bg = "lawngreen")
        b37.config(bg = "lawngreen")
        b38.config(bg = "lawngreen")
        b39.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b37["text"] == "yellow" and b38["text"] == "yellow" and b39["text"] == "yellow" and b40["text"] == "yellow":
        b37.config(bg = "lawngreen")
        b38.config(bg = "lawngreen")
        b39.config(bg = "lawngreen")
        b40.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b38["text"] == "yellow" and b39["text"] == "yellow" and b40["text"] == "yellow" and b41["text"] == "yellow":
        b38.config(bg = "lawngreen")
        b39.config(bg = "lawngreen")
        b40.config(bg = "lawngreen")
        b41.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b39["text"] == "yellow" and b40["text"] == "yellow" and b41["text"] == "yellow" and b42["text"] == "yellow":
        b39.config(bg = "lawngreen")
        b40.config(bg = "lawngreen")
        b41.config(bg = "lawngreen")
        b42.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    
    

    #DOWN FIRST COLUMN===================================================================================================
    elif b1["text"] == "yellow" and b8["text"] == "yellow" and b15["text"] == "yellow" and b22["text"] == "yellow":
        b1.config(bg = "lawngreen")
        b8.config(bg = "lawngreen")
        b15.config(bg = "lawngreen")
        b22.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b8["text"] == "yellow" and b15["text"] == "yellow" and b22["text"] == "yellow" and b29["text"] == "yellow":
        b29.config(bg = "lawngreen")
        b8.config(bg = "lawngreen")
        b15.config(bg = "lawngreen")
        b22.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b36["text"] == "yellow" and b15["text"] == "yellow" and b22["text"] == "yellow" and b29["text"] == "yellow":
        b29.config(bg = "lawngreen")
        b36.config(bg = "lawngreen")
        b15.config(bg = "lawngreen")
        b22.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    #DOWN SECOND COLUMN===================================================================================================
    elif b2["text"] == "yellow" and b9["text"] == "yellow" and b16["text"] == "yellow" and b23["text"] == "yellow":
        b2.config(bg = "lawngreen")
        b9.config(bg = "lawngreen")
        b16.config(bg = "lawngreen")
        b23.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b9["text"] == "yellow" and b16["text"] == "yellow" and b23["text"] == "yellow" and b30["text"] == "yellow":
        b30.config(bg = "lawngreen")
        b9.config(bg = "lawngreen")
        b16.config(bg = "lawngreen")
        b23.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b37["text"] == "yellow" and b16["text"] == "yellow" and b23["text"] == "yellow" and b30["text"] == "yellow":
        b30.config(bg = "lawngreen")
        b37.config(bg = "lawngreen")
        b16.config(bg = "lawngreen")
        b23.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    #DOWN THIRD COLUMN===================================================================================================
    elif b3["text"] == "yellow" and b10["text"] == "yellow" and b17["text"] == "yellow" and b24["text"] == "yellow":
        b3.config(bg = "lawngreen")
        b10.config(bg = "lawngreen")
        b17.config(bg = "lawngreen")
        b24.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b10["text"] == "yellow" and b17["text"] == "yellow" and b24["text"] == "yellow" and b31["text"] == "yellow":
        b31.config(bg = "lawngreen")
        b10.config(bg = "lawngreen")
        b17.config(bg = "lawngreen")
        b24.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b38["text"] == "yellow" and b17["text"] == "yellow" and b24["text"] == "yellow" and b31["text"] == "yellow":
        b31.config(bg = "lawngreen")
        b38.config(bg = "lawngreen")
        b17.config(bg = "lawngreen")
        b24.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    #DOWN FOURTH COLUMN===================================================================================================
    elif b4["text"] == "yellow" and b11["text"] == "yellow" and b18["text"] == "yellow" and b25["text"] == "yellow":
        b4.config(bg = "lawngreen")
        b11.config(bg = "lawngreen")
        b18.config(bg = "lawngreen")
        b25.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b11["text"] == "yellow" and b18["text"] == "yellow" and b25["text"] == "yellow" and b32["text"] == "yellow":
        b32.config(bg = "lawngreen")
        b11.config(bg = "lawngreen")
        b18.config(bg = "lawngreen")
        b25.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b39["text"] == "yellow" and b18["text"] == "yellow" and b25["text"] == "yellow" and b32["text"] == "yellow":
        b32.config(bg = "lawngreen")
        b39.config(bg = "lawngreen")
        b18.config(bg = "lawngreen")
        b25.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    #DOWN FIFTH COLUMN===================================================================================================
    elif b5["text"] == "yellow" and b12["text"] == "yellow" and b19["text"] == "yellow" and b26["text"] == "yellow":
        b5.config(bg = "lawngreen")
        b12.config(bg = "lawngreen")
        b19.config(bg = "lawngreen")
        b26.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b12["text"] == "yellow" and b19["text"] == "yellow" and b26["text"] == "yellow" and b33["text"] == "yellow":
        b33.config(bg = "lawngreen")
        b12.config(bg = "lawngreen")
        b19.config(bg = "lawngreen")
        b26.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b40["text"] == "yellow" and b19["text"] == "yellow" and b26["text"] == "yellow" and b33["text"] == "yellow":
        b33.config(bg = "lawngreen")
        b40.config(bg = "lawngreen")
        b19.config(bg = "lawngreen")
        b26.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    #DOWN SIXTH COLUMN===================================================================================================
    elif b6["text"] == "yellow" and b13["text"] == "yellow" and b20["text"] == "yellow" and b27["text"] == "yellow":
        b6.config(bg = "lawngreen")
        b13.config(bg = "lawngreen")
        b20.config(bg = "lawngreen")
        b27.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b13["text"] == "yellow" and b20["text"] == "yellow" and b27["text"] == "yellow" and b34["text"] == "yellow":
        b34.config(bg = "lawngreen")
        b13.config(bg = "lawngreen")
        b20.config(bg = "lawngreen")
        b27.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b41["text"] == "yellow" and b20["text"] == "yellow" and b27["text"] == "yellow" and b34["text"] == "yellow":
        b34.config(bg = "lawngreen")
        b41.config(bg = "lawngreen")
        b20.config(bg = "lawngreen")
        b27.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    #DOWN SEVENTH COLUMN===================================================================================================
    elif b7["text"] == "yellow" and b14["text"] == "yellow" and b21["text"] == "yellow" and b28["text"] == "yellow":
        b7.config(bg = "lawngreen")
        b14.config(bg = "lawngreen")
        b21.config(bg = "lawngreen")
        b28.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b14["text"] == "yellow" and b21["text"] == "yellow" and b28["text"] == "yellow" and b35["text"] == "yellow":
        b35.config(bg = "lawngreen")
        b14.config(bg = "lawngreen")
        b21.config(bg = "lawngreen")
        b28.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b42["text"] == "yellow" and b21["text"] == "yellow" and b28["text"] == "yellow" and b35["text"] == "yellow":
        b35.config(bg = "lawngreen")
        b42.config(bg = "lawngreen")
        b21.config(bg = "lawngreen")
        b28.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()

    #CROSSES
    elif b1["text"] == "yellow" and b9["text"] == "yellow" and b17["text"] == "yellow" and b25["text"] == "yellow":
        b1.config(bg = "lawngreen")
        b17.config(bg = "lawngreen")
        b9.config(bg = "lawngreen")
        b25.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b33["text"] == "yellow" and b9["text"] == "yellow" and b17["text"] == "yellow" and b25["text"] == "yellow":
        b33.config(bg = "lawngreen")
        b17.config(bg = "lawngreen")
        b9.config(bg = "lawngreen")
        b25.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b33["text"] == "yellow" and b41["text"] == "yellow" and b17["text"] == "yellow" and b25["text"] == "yellow":
        b33.config(bg = "lawngreen")
        b17.config(bg = "lawngreen")
        b41.config(bg = "lawngreen")
        b25.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()

    elif b2["text"] == "yellow" and b10["text"] == "yellow" and b18["text"] == "yellow" and b26["text"] == "yellow":
        b2.config(bg = "lawngreen")
        b18.config(bg = "lawngreen")
        b10.config(bg = "lawngreen")
        b26.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b34["text"] == "yellow" and b10["text"] == "yellow" and b18["text"] == "yellow" and b26["text"] == "yellow":
        b34.config(bg = "lawngreen")
        b18.config(bg = "lawngreen")
        b10.config(bg = "lawngreen")
        b26.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b34["text"] == "yellow" and b42["text"] == "yellow" and b18["text"] == "yellow" and b26["text"] == "yellow":
        b34.config(bg = "lawngreen")
        b18.config(bg = "lawngreen")
        b42.config(bg = "lawngreen")
        b26.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    
    elif b3["text"] == "yellow" and b11["text"] == "yellow" and b19["text"] == "yellow" and b27["text"] == "yellow":
        b3.config(bg = "lawngreen")
        b19.config(bg = "lawngreen")
        b11.config(bg = "lawngreen")
        b27.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b35["text"] == "yellow" and b11["text"] == "yellow" and b19["text"] == "yellow" and b27["text"] == "yellow":
        b35.config(bg = "lawngreen")
        b19.config(bg = "lawngreen")
        b11.config(bg = "lawngreen")
        b27.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()

    elif b4["text"] == "yellow" and b12["text"] == "yellow" and b20["text"] == "yellow" and b28["text"] == "yellow":
        b28.config(bg = "lawngreen")
        b20.config(bg = "lawngreen")
        b4.config(bg = "lawngreen")
        b12.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()

    elif b8["text"] == "yellow" and b16["text"] == "yellow" and b24["text"] == "yellow" and b32["text"] == "yellow":
        b8.config(bg = "lawngreen")
        b16.config(bg = "lawngreen")
        b24.config(bg = "lawngreen")
        b32.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b40["text"] == "yellow" and b16["text"] == "yellow" and b24["text"] == "yellow" and b32["text"] == "yellow":
        b40.config(bg = "lawngreen")
        b16.config(bg = "lawngreen")
        b24.config(bg = "lawngreen")
        b32.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    
    elif b15["text"] == "yellow" and b23["text"] == "yellow" and b31["text"] == "yellow" and b39["text"] == "yellow":
        b15.config(bg = "lawngreen")
        b23.config(bg = "lawngreen")
        b31.config(bg = "lawngreen")
        b39.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    
    elif b4["text"] == "yellow" and b22["text"] == "yellow" and b16["text"] == "yellow" and b10["text"] == "yellow":
        b16.config(bg = "lawngreen")
        b22.config(bg = "lawngreen")
        b4.config(bg = "lawngreen")
        b10.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    
    elif b21["text"] == "yellow" and b27["text"] == "yellow" and b33["text"] == "yellow" and b39["text"] == "yellow":
        b33.config(bg = "lawngreen")
        b21.config(bg = "lawngreen")
        b39.config(bg = "lawngreen")
        b27.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    
    elif b5["text"] == "yellow" and b11["text"] == "yellow" and b17["text"] == "yellow" and b23["text"] == "yellow":
        b5.config(bg = "lawngreen")
        b11.config(bg = "lawngreen")
        b17.config(bg = "lawngreen")
        b23.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b11["text"] == "yellow" and b17["text"] == "yellow" and b23["text"] == "yellow" and b29["text"] == "yellow":
        b11.config(bg = "lawngreen")
        b17.config(bg = "lawngreen")
        b23.config(bg = "lawngreen")
        b29.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    
    elif b14["text"] == "yellow" and b20["text"] == "yellow" and b26["text"] == "yellow" and b32["text"] == "yellow":
        b14.config(bg = "lawngreen")
        b20.config(bg = "lawngreen")
        b26.config(bg = "lawngreen")
        b32.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b20["text"] == "yellow" and b26["text"] == "yellow" and b32["text"] == "yellow" and b38["text"] == "yellow":
        b20.config(bg = "lawngreen")
        b26.config(bg = "lawngreen")
        b32.config(bg = "lawngreen")
        b38.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    
    elif b6["text"] == "yellow" and b12["text"] == "yellow" and b18["text"] == "yellow" and b24["text"] == "yellow":
        b6.config(bg = "lawngreen")
        b12.config(bg = "lawngreen")
        b18.config(bg = "lawngreen")
        b24.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b12["text"] == "yellow" and b18["text"] == "yellow" and b24["text"] == "yellow" and b30["text"] == "yellow":
        b12.config(bg = "lawngreen")
        b18.config(bg = "lawngreen")
        b24.config(bg = "lawngreen")
        b30.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b18["text"] == "yellow" and b24["text"] == "yellow" and b30["text"] == "yellow" and b36["text"] == "yellow":
        b18.config(bg = "lawngreen")
        b24.config(bg = "lawngreen")
        b30.config(bg = "lawngreen")
        b36.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    
    elif b7["text"] == "yellow" and b13["text"] == "yellow" and b19["text"] == "yellow" and b25["text"] == "yellow":
        b7.config(bg = "lawngreen")
        b13.config(bg = "lawngreen")
        b19.config(bg = "lawngreen")
        b25.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b13["text"] == "yellow" and b19["text"] == "yellow" and b25["text"] == "yellow" and b31["text"] == "yellow":
        b12.config(bg = "lawngreen")
        b18.config(bg = "lawngreen")
        b24.config(bg = "lawngreen")
        b30.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    elif b19["text"] == "yellow" and b25["text"] == "yellow" and b31["text"] == "yellow" and b37["text"] == "yellow":
        b19.config(bg = "lawngreen")
        b25.config(bg = "lawngreen")
        b31.config(bg = "lawngreen")
        b37.config(bg = "lawngreen")
        winner = True
        messagebox.showinfo("Connect 4", "yellow wins")
        disable_all_buttons()
    
    if count >= 42:
        messagebox.showerror("Connect 4", "Tie")
        disable_all_buttons()


def b_click(b, num):

    if num == 1 or num == 8 or num == 15 or num == 22 or num == 29 or num == 36:
        first()
    elif num == 2 or num == 9 or num == 16 or num == 23 or num == 30 or num == 37:
        second()
    elif num == 3 or num == 10 or num == 17 or num == 24 or num == 31 or num == 38:
        third()
    elif num == 4 or num == 11 or num == 18 or num == 25 or num == 32 or num == 39:
        fourth()
    elif num == 5 or num == 12 or num == 19 or num == 26 or num == 33 or num == 40:
        fifth()
    elif num == 6 or num == 13 or num == 20 or num == 27 or num == 34 or num == 41:
        sixth()
    elif num == 7 or num == 14 or num == 21 or num == 28 or num == 35 or num == 42:
        seventh()

def first():
    if b36["text"] == " ":
        fillInBut(b36)
    elif b29["text"] == " ":
        fillInBut(b29)
    elif b22["text"] == " ":
        fillInBut(b22)
    elif b15["text"] == " ":
        fillInBut(b15)
    elif b8["text"] == " ":
        fillInBut(b8)
    elif b1["text"] == " ":
        fillInBut(b1)
    else:
        messagebox.showerror("Connect 4", "Column is already full")

def second():
    if b37["text"] == " ":
        fillInBut(b37)
    elif b30["text"] == " ":
        fillInBut(b30)
    elif b23["text"] == " ":
        fillInBut(b23)
    elif b16["text"] == " ":
        fillInBut(b16)
    elif b9["text"] == " ":
        fillInBut(b9)
    elif b2["text"] == " ":
        fillInBut(b2)
    else:
        messagebox.showerror("Connect 4", "Column is already full")

def third():
    if b38["text"] == " ":
        fillInBut(b38)
    elif b31["text"] == " ":
        fillInBut(b31)
    elif b24["text"] == " ":
        fillInBut(b24)
    elif b17["text"] == " ":
        fillInBut(b17)
    elif b10["text"] == " ":
        fillInBut(b10)
    elif b3["text"] == " ":
        fillInBut(b3)
    else:
        messagebox.showerror("Connect 4", "Column is already full")

def fourth():
    if b39["text"] == " ":
        fillInBut(b39)
    elif b32["text"] == " ":
        fillInBut(b32)
    elif b25["text"] == " ":
        fillInBut(b25)
    elif b18["text"] == " ":
        fillInBut(b18)
    elif b11["text"] == " ":
        fillInBut(b11)
    elif b4["text"] == " ":
        fillInBut(b4)
    else:
        messagebox.showerror("Connect 4", "Column is already full")

def fifth():
    if b40["text"] == " ":
        fillInBut(b40)
    elif b33["text"] == " ":
        fillInBut(b33)
    elif b26["text"] == " ":
        fillInBut(b26)
    elif b19["text"] == " ":
        fillInBut(b19)
    elif b12["text"] == " ":
        fillInBut(b12)
    elif b5["text"] == " ":
        fillInBut(b5)
    else:
        messagebox.showerror("Connect 4", "Column is already full")

def sixth():
    if b41["text"] == " ":
        fillInBut(b41)
    elif b34["text"] == " ":
        fillInBut(b34)
    elif b27["text"] == " ":
        fillInBut(b27)
    elif b20["text"] == " ":
        fillInBut(b20)
    elif b13["text"] == " ":
        fillInBut(b13)
    elif b6["text"] == " ":
        fillInBut(b6)
    else:
        messagebox.showerror("Connect 4", "Column is already full")

def seventh():
    if b42["text"] == " ":
        fillInBut(b42)
    elif b35["text"] == " ":
        fillInBut(b35)
    elif b28["text"] == " ":
        fillInBut(b28)
    elif b21["text"] == " ":
        fillInBut(b21)
    elif b14["text"] == " ":
        fillInBut(b14)
    elif b7["text"] == " ":
        fillInBut(b7)
    else:
        messagebox.showerror("Connect 4", "Column is already full")

def fillInBut(b):
    global clicked, count
    if b["text"] == " " and clicked == True:
        b["text"] = "red"
        b["bg"] = "red"
        clicked = False
        count += 1
        checkifwon()
    elif b["text"] == " " and clicked == False:
        b["text"] = "yellow"
        b["bg"] = "yellow"
        clicked = True
        count += 1
        checkifwon()

def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23, b24, b25, b26, b27, b28, b29, b30, b31, b32, b33, b34, b35, b36, b37, b38, b39, b40, b41, b42
    global clicked, count
    clicked = True
    count = 0
    #buttons
    b1 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b1, 1))
    b2 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b2, 2))
    b3 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b3, 3))
    b4 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b4, 4))
    b5 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b5, 5))
    b6 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b6, 6))
    b7 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b7, 7))

    b8 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b8, 8))
    b9 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b9, 9))
    b10 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b10, 10))
    b11 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b11, 11))
    b12 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b12, 12))
    b13 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b13, 13))
    b14 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b14, 14))

    b15 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b15, 15))
    b16 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b16, 16))
    b17 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b17, 17))
    b18 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b18, 18))
    b19 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b19, 19))
    b20 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b20, 20))
    b21 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b21, 21))
    
    b22 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b22, 22))
    b23 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b23, 23))
    b24 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b24, 24))
    b25 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b25, 25))
    b26 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b26, 26))
    b27 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b27, 27))
    b28 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b28, 28))

    b29 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b29, 29))
    b30 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b30, 30))
    b31 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b31, 31))
    b32 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b32, 32))
    b33 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b33, 33))
    b34 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b34, 34))
    b35 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b35, 35))

    b36 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b36, 36))
    b37 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b37, 37))
    b38 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b38, 38))
    b39 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b39, 39))
    b40 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b40, 40))
    b41 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b41, 41))
    b42 = Button(root, text = " ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda:b_click(b42, 42))

    #grid
    b1.grid(row=0, column = 0)
    b2.grid(row=0, column = 1)
    b3.grid(row=0, column = 2)
    b4.grid(row=0, column = 3)
    b5.grid(row=0, column = 4)
    b6.grid(row=0, column = 5)
    b7.grid(row=0, column = 6)

    b8.grid(row=1, column = 0)
    b9.grid(row=1, column = 1)
    b10.grid(row=1, column = 2)
    b11.grid(row=1, column = 3)
    b12.grid(row=1, column = 4)
    b13.grid(row=1, column = 5)
    b14.grid(row=1, column = 6)
    
    b15.grid(row=2, column = 0)
    b16.grid(row=2, column = 1)
    b17.grid(row=2, column = 2)
    b18.grid(row=2, column = 3)
    b19.grid(row=2, column = 4)
    b20.grid(row=2, column = 5)
    b21.grid(row=2, column = 6)

    b22.grid(row=3, column = 0)
    b23.grid(row=3, column = 1)
    b24.grid(row=3, column = 2)
    b25.grid(row=3, column = 3)
    b26.grid(row=3, column = 4)
    b27.grid(row=3, column = 5)
    b28.grid(row=3, column = 6)

    b29.grid(row=4, column = 0)
    b30.grid(row=4, column = 1)
    b31.grid(row=4, column = 2)
    b32.grid(row=4, column = 3)
    b33.grid(row=4, column = 4)
    b34.grid(row=4, column = 5)
    b35.grid(row=4, column = 6)

    b36.grid(row=5, column = 0)
    b37.grid(row=5, column = 1)
    b38.grid(row=5, column = 2)
    b39.grid(row=5, column = 3)
    b40.grid(row=5, column = 4)
    b41.grid(row=5, column = 5)
    b42.grid(row=5, column = 6)

my_Menu = Menu(root)
root.config(menu = my_Menu)

options_menu = Menu(my_Menu, tearoff = FALSE)
my_Menu.add_cascade(label = "Options", menu = options_menu)
options_menu.add_command(label = "Reset Game", command=reset)


reset()

root.mainloop()