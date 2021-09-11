import tkinter as tk
import random

from PIL import Image, ImageTk

window = tk.Tk()
window.geometry("960x690")

topFrame = tk.Frame(window)
topFrame.grid(row=0, column=0)
midFrame = tk.Frame(window)
midFrame.grid(row=1, column=0)
bottomFrame = tk.Frame(window)
bottomFrame.grid(row=2, column=0)
window.title("Slot Machine")

window.grid_rowconfigure(1, weight=2)
window.grid_columnconfigure(0, weight=3)

balance = 100
winAmount = 0
betAmount = 1
allSymbols = ["Bar1", "Bar2", "Bar3", "Bell", "Cherries", "Clover", "Heart", "Horseshoe", "Lemon", "Lucky7", "Melon"]
strBalance = tk.StringVar()
strBalance.set("Balance: $" + str(balance))
strWinAmount = tk.StringVar()
strWinAmount.set("Win: $" + str(winAmount))
strBetAmount = tk.StringVar()
strBetAmount.set("Bet: $" + str(betAmount))
firstReel = ""
# strFirstReel = tk.StringVar()
# strFirstReel.set(firstReel)
secondReel = ""
# strSecondReel = tk.StringVar()
# strSecondReel.set(secondReel)
thirdReel = ""
# strThirdReel = tk.StringVar()
# strThirdReel.set(thirdReel)

symbols = ["Lemon", "Cherries", "Heart", "Bell", "Clover", "Lucky7"]
# Load images here
img_spinButton = ImageTk.PhotoImage(Image.open("C:/Users/jtfra/PycharmProjects/Slots/media/Slot_Machine/Bare_Bones_Slot_Machine_Frame/spin.png"))
img_spinButton_pressed = ImageTk.PhotoImage(Image.open("C:/Users/jtfra/PycharmProjects/Slots/media/Slot_Machine/Bare_Bones_Slot_Machine_Frame/spin_pressed.png"))
img_betButton = ImageTk.PhotoImage(Image.open("C:/Users/jtfra/PycharmProjects/Slots/media/Slot_Machine/Bare_Bones_Slot_Machine_Frame/bet.png"))
img_betButton_pressed = ImageTk.PhotoImage(Image.open("C:/Users/jtfra/PycharmProjects/Slots/media/Slot_Machine/Bare_Bones_Slot_Machine_Frame/bet_pressed.png"))
payline_frame = ImageTk.PhotoImage(Image.open("C:/Users/jtfra/PycharmProjects/Slots/media/Slot_Machine/Bare_Bones_Slot_Machine_Frame/paylineframe.png"))

img_lemon = ImageTk.PhotoImage(Image.open("C:/Users/jtfra/PycharmProjects/Slots/media/Slot_Machine/lemon.png"))
img_cherries = ImageTk.PhotoImage(Image.open("C:/Users/jtfra/PycharmProjects/Slots/media/Slot_Machine/cherries.png"))
img_heart = ImageTk.PhotoImage(Image.open("C:/Users/jtfra/PycharmProjects/Slots/media/Slot_Machine/heart.png"))
img_bell = ImageTk.PhotoImage(Image.open("C:/Users/jtfra/PycharmProjects/Slots/media/Slot_Machine/bell.png"))
img_clover = ImageTk.PhotoImage(Image.open("C:/Users/jtfra/PycharmProjects/Slots/media/Slot_Machine/clover.png"))
img_lucky7 = ImageTk.PhotoImage(Image.open("C:/Users/jtfra/PycharmProjects/Slots/media/Slot_Machine/Lucky7_rainbow.png"))
symbols_imgs = [img_lemon, img_cherries, img_heart, img_bell, img_clover, img_lucky7]

balanceLabel = tk.Label(topFrame, textvariable=strBalance)
balanceLabel.pack()

reelOneLabel = tk.Label(midFrame, image=img_lucky7)
reelOneLabel.grid(row=0, column=0)
reelTwoLabel = tk.Label(midFrame, image=img_lucky7)
reelTwoLabel.grid(row=0, column=1)
reelThreeLabel = tk.Label(midFrame, image=img_lucky7)
reelThreeLabel.grid(row=0, column=2)

# Function that runs when the user spins the slot
def spin():
    # spinButton.configure(image=img_spinButton_pressed)
    global balance, firstReel, secondReel, thirdReel

    # reelSpinAnimation()

    firstReel, firstReelImg = spinReel()
    reelOneLabel.configure(image=firstReelImg)
    secondReel, secondReelImg = spinReel()
    reelTwoLabel.configure(image=secondReelImg)
    thirdReel, thirdReelImg = spinReel()
    reelThreeLabel.configure(image=thirdReelImg)
    calcWinnings()
    # spinButton.configure(image=img_spinButton)

betAmountLabel = tk.Label(bottomFrame, textvariable=strBetAmount)
betAmountLabel.grid(row=0, column=0)
spinButton = tk.Button(bottomFrame, command=spin, image=img_spinButton)
# spinButton.pack()
spinButton.grid(row=0, column=1)
winAmountLabel = tk.Label(bottomFrame, textvariable=strWinAmount)
winAmountLabel.grid(row=0, column=2)

def calcWinnings():
    global balance, strBalance, firstReel, secondReel, thirdReel
    balance -= 1
    strBalance.set("Balance: $" + str(balance))

    if ((firstReel == "Lemon") and (secondReel != "Lemon")):
        win = 2
    elif ((firstReel == "Cherries") and (secondReel == "Cherries") and (thirdReel == "Cherries")):
        win = 5
    elif ((firstReel == "Heart") and (secondReel == "Heart") and ((thirdReel == "Heart") or (thirdReel == "Lucky7"))):
        win = 10
    elif ((firstReel == "Bell") and (secondReel == "Bell") and ((thirdReel == "Bell") or (thirdReel == "Lucky7"))):
        win = 14
    elif ((firstReel == "Clover") and (secondReel == "Clover") and ((thirdReel == "Clover") or (thirdReel == "Lucky7"))):
        win = 20
    elif ((firstReel == "Lucky7") and (secondReel == "Lucky7") and (thirdReel == "Lucky7")):
        win = 250
    else:
        win = 0
    strWinAmount.set("Win: $" + str(win))
    balance += win
    print(firstReel + " - " + secondReel + " - " + thirdReel)
    print("Win: $" + str(win))

def spinReel():
    randNum = random.randint(0, len(symbols)-1)
    return (symbols[randNum], symbols_imgs[randNum])


window.mainloop()