from tkinter import *
from tkinter import ttk

class interface:

    def interface():

        #main windows Section
        mainWindow = Tk()
        mainWindow.title('Hash Tables Vizualizator')
        mainWindow.geometry('600x600')
        mainWindow.resizable(0,0)
        mainWindow.config(bg='white')

        #menu frame Section
        recordFound = StringVar()
        hashValue = StringVar()
        codeValue = StringVar()
        nameValue = StringVar()
        def recordFoundFunction():
            information = contains(int(inputNumber.get()),int(hashTableSize.get()))
            if(len(information)>1):
                recordFound.set('Record Found')
                hashValue.set(information[0])
                codeValue.set(information[1])
                nameValue.set(information[2])
                dataset = open('dataset.txt', 'r', encoding= 'utf-8')
                treeview.delete(*treeview.get_children())
                for element in dataset:
                    if(int(element.split(';')[0]) >= int(information[0]) and int(element.split(';')[0]) <= int(element.split(';')[0]) + 10):
                        treeview.insert('', END,text=element.split(';')[0], values=(element.split(';')[1],element.split(';')[2]))
            else:
                recordFound.set('Record Not Found')
                hashValue.set('')
                codeValue.set('')
                nameValue.set('')
                treeview.delete(*treeview.get_children())

            
            

        menuFrame = Frame(mainWindow)
        menuFrame.grid(row=2, column=0, padx=10,pady=0)
        menuFrame.config(bg='white')
        menuFrame.config(width=800, height=350)
        menuLabel = Label(menuFrame, text='Menu Section')
        menuLabel.grid(row=0, column=1, padx=10,pady=10)
        inputNumber = Entry(menuFrame)
        inputNumber.grid(row=1, column=1, padx=10,pady=10)
        inputLabel = Label(menuFrame, text='Code: ')
        inputLabel.grid(row=1, column=0, padx=10,pady=10)
        findButton = Button(menuFrame, text='Find', command=recordFoundFunction)
        findButton.grid(row=2, column=0)
        hashLabel = Label(menuFrame, text= 'Hash')
        hashLabel.grid(row=0, column=2)
        codeLabel = Label(menuFrame, text= 'Code')
        codeLabel.grid(row=0, column=3)
        nameLabel = Label(menuFrame, text= 'Name')
        nameLabel.grid(row=0, column=4)
        hashValueLabel = Label(menuFrame, textvariable=hashValue)
        hashValueLabel.grid(row=1, column=2)
        codeValueLabel = Label(menuFrame, textvariable=codeValue)
        codeValueLabel.grid(row=1, column=3)
        nameValueLabel = Label(menuFrame, textvariable=nameValue)
        nameValueLabel.grid(row=1, column=4)
        recordFoundLabel= Label(menuFrame, textvariable=recordFound)
        recordFoundLabel.grid(row=2, column=2, padx=10,pady=10)


        #table Frame Section
        collisionsAmounth = StringVar()
        collisionsAmounth.set(collisions)
        def collisionsAmounthFunction():
            run(int(hashTableSize.get()))
            collisionsAmounth.set(collisions)

        tableFrame = Frame(mainWindow)
        tableFrame.grid(row=0, column=0, padx=10,pady=0)
        tableFrame.config(bg='white')
        tableFrameLabel = Label(tableFrame, text='Table Hash Section')
        tableFrameLabel.grid(row=0, column=0, padx=10,pady=10)
        hashTableSize =StringVar(tableFrame)
        hashTableSize.set('103')
        options = ['103','113','131','163','199','251','311']
        dropDown = OptionMenu(tableFrame, hashTableSize, *options)
        dropDown.grid(row=1, column=0)
        reportButton = Button(tableFrame, text='Re - Hash Table', command=collisionsAmounthFunction)
        reportButton.grid(row=2, column=0)
        reportLabel = Label(tableFrame, text='----- Report -----')
        reportLabel.grid(row=0, column=2, padx=10,pady=10)
        collisionsLabel= Label(tableFrame, text='collisions: ')
        collisionsLabel.grid(row=1, column=2, padx=10,pady=10)
        collisionsAmounthLabel= Label(tableFrame, textvariable=collisionsAmounth)
        collisionsAmounthLabel.grid(row=2, column=2, padx=10,pady=10)

        #Dataset Frame Section this section contains 10 registers above the find register 

        datasetFrame = Frame(mainWindow)
        datasetFrame.grid(row=1, column= 0, padx=10, pady=10)
        datasetFrame.config(bg='white', width=300)
        datasetFrameLabel = Label(datasetFrame, text='Dataset Information (10 registers)')
        datasetFrameLabel.grid(row=0, column=0, padx=10, pady=10)
        treeview = ttk.Treeview(datasetFrame, columns=('col1','col2'))
        treeview.column('#0', width=50, anchor=CENTER)
        treeview.column('col1', width=50, anchor=CENTER)
        treeview.column('col2', width=200, anchor=CENTER)
        treeview.heading('#0', text='HASH', anchor=CENTER)
        treeview.heading('col1', text='CODE', anchor=CENTER)
        treeview.heading('col2', text='NAME', anchor=CENTER)
        treeview.grid(row=1)
        mainWindow.mainloop()