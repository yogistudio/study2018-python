"""
邮校学习
0425
TK
"""
# from tkinter import Label
#
# widget = Label(None, text='hello')
# widget.pack()
# widget.mainloop()


from tkinter import Label, Frame, Tk, Button, Entry
from tkinter import RIGHT, LEFT

from tkinter.filedialog import askopenfilename

tk = Tk()


# 创建一个tk实例,并在tk.mainloop()运行


def cmd():
    aStr = askopenfilename()
    aFloat = float(entryList[0].get())
    bFloat = float(entryList[1].get())
    entryList[2].delete(0, len(entryList[2].get()))
    entryList[2].insert(0, round(aFloat + bFloat, 2))


nameList = ['NumberA', 'NumberB', 'NumberC']
frameList = [Frame(tk) for i in nameList]
labelList = [Label(i, text=j) for i, j in zip(frameList, nameList)]
# alist=[1,2,3]
# blist=[4,5,6]
# list(zip(alist,blist))
# [(1, 4), (2, 5), (3, 6)]
entryList = [Entry(i) for i in frameList]

for lable, entry, frame in zip(labelList, entryList, frameList):
    lable.pack(side=LEFT)
    entry.pack(side=RIGHT)
    frame.pack()

btn = Button(tk, text="Add", command=cmd)
#
btn.pack(side=RIGHT)

tk.mainloop()
