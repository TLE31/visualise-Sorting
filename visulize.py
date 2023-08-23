from tkinter import *
from tkinter import ttk
import random
from time import sleep
# importing our designed algorithms from the algorithms folder




#to store the array/heights of rectangle
data = []
#to store the colour of respective rectangles
colorData = []



def startBubbleSort(data, drawData,stepTime):

    colorData=['grey' for x in range(len(data))]
    for i in range(len(data)-1):
        for j in range(len(data)-i-1):
            colorData[j]=colorData[j+1]='white'
            drawData(data,colorData)
            colorData[j]=colorData[j+1]='grey'
            sleep(stepTime)
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
                colorData[j]=colorData[j+1]='red'
                drawData(data,colorData)
                colorData[j]=colorData[j+1]='grey'
                sleep(stepTime)
        colorData[len(data)-1-i]='green'
        drawData(data,colorData)
    colorData[0]='green'
    drawData(data,colorData)

from time import sleep
colorData=[]

def startQuickSort(data, drawData,stepTime):
    global colorData
    colorData=['grey' for x in range(len(data))]
    quickSort(data,0,len(data)-1,drawData,stepTime)
    colorData=['green' for x in range(len(data))]
    # drawData(data,colorData)

def quickSort(data,start,end,drawData,stepTime):
    if start>=end:
        return
    
    pivot=partition(data,start,end)
    quickSort(data,start,pivot-1,drawData,stepTime)
    quickSort(data,pivot+1,end,drawData,stepTime)

def partition(data,start,end):
    i=start-1
    pivot=data[end]
    for j in range(start,end):
        if data[j]<=pivot:
            i+=1
            data[i],data[j]=data[j],data[i]
    data[i+1],data[end]=data[end],data[i+1]
    return i+1

data=[434243,34,23,2323,121]
startQuickSort(data,0,0)
print(data)

def startMergeSort(data, drawData,stepTime):
    global colorData
    colorData=['grey' for x in range(len(data))]
    mergeSort(data,0,len(data)-1,drawData,stepTime)
    colorData=['green' for x in range(len(data))]
    drawData(data,colorData)


def merge(data,start,end,drawData,stepTime):
    i=start
    j=(start+end)//2+1
    a=[]
    while i<=(start+end)//2 and j<=end:
        colorData[i]=colorData[j]='blue'
        drawData(data,colorData)
        colorData[i]=colorData[j]='grey'
        sleep(stepTime)
        if data[i]<data[j]:
            colorData[i]='green'
            drawData(data,colorData)
            sleep(stepTime)
            colorData[i]='grey'
            a.append(data[i])
            i+=1
        else:
            colorData[j]='green'
            drawData(data,colorData)
            sleep(stepTime)
            colorData[j]='grey'
            a.append(data[j])
            j+=1
    
    while i<=(start+end)//2:
        colorData[i]='green'
        drawData(data,colorData)
        sleep(stepTime)
        colorData[i]='grey'
        a.append(data[i])
        i+=1
    
    while j<=end:
        colorData[j]='green'
        drawData(data,colorData)
        sleep(stepTime)
        colorData[j]='grey'
        a.append(data[j])
        j+=1
    for x in range(start,end+1):
        data[x]=a[x-start]




def mergeSort(data,start,end,drawData,stepTime):
    
    if start>=end:
        return

    colorData[start:end+1]=['white' for x in range(start,end+1)]
    drawData(data,colorData)
    sleep(stepTime)
    colorData[start:end+1]=['grey' for x in range(start,end+1)]


    mergeSort(data,start,(start+end)//2,drawData,stepTime)
    mergeSort(data,(start+end)//2+1,end,drawData,stepTime)
    merge(data,start,end,drawData,stepTime)


    colorData[start:end+1]=['white' for x in range(start,end+1)]
    drawData(data,colorData)
    sleep(stepTime)
    colorData[start:end+1]=['grey' for x in range(start,end+1)]
    # for x in range(start,end+1):
    #     drawData(data,colorData)
    #     sleep(stepTime)


def startSelectionSort(data, drawData,stepTime):

    colorData=['grey' for x in range(len(data))]
    for i in range(len(data)):
        min=data[i]
        min_index=i
        colorData[i]='blue'
        for j in range(i+1,len(data)):
            colorData[j]='white'
            drawData(data,colorData)
            colorData[j]='grey'
            sleep(stepTime)
            if data[j]<min:
                colorData[min_index]='grey'
                min=data[j]
                min_index=j
                colorData[j]='blue'
                if j!=len(data)-1:
                    colorData[j+1]='white'
                drawData(data,colorData)
                # colorData[j]='blue'
                sleep(stepTime)
        data[min_index],data[i]=data[i],data[min_index]
        colorData[i+1:]=['grey' for x in range(i+1,len(data))]
        colorData[i]='green'
        drawData(data,colorData)
        sleep(stepTime)

def startInsertionSort(data, drawData,stepTime):

    colorData=['grey' for x in range(len(data))]
    for i in range(1,len(data)):
        key=data[i]
        j=i-1

        colorData[i]='blue'
        drawData(data,colorData)
        sleep(stepTime)
        
        while j>=0 and data[j]>key:

            colorData[j]='white'
            drawData(data,colorData)
            sleep(stepTime)
            colorData[j]='grey'

            data[j+1]=data[j]
            j-=1

        data[j+1]=key

        colorData[j+1]='red'
        drawData(data,colorData)
        sleep(stepTime)
        colorData[j+1]='grey'
        colorData[i]='grey'

    colorData=['green' for x in range(len(data))]
    drawData(data,colorData)

def visualize(algorithm,stepTime):
    stepTime/=10

    if algorithm=="Bubble Sort":
        startBubbleSort(data,drawData,stepTime)
    elif algorithm=="Merge Sort":
        startMergeSort(data,drawData,stepTime)
    elif algorithm=="Selection Sort":
        startSelectionSort(data,drawData,stepTime)
    elif algorithm=="Insertion Sort":
        startInsertionSort(data,drawData,stepTime)
    elif algorithm=="Quick Sort":
        startQuickSort(data,drawData,stepTime)
    elif algorithm=="Radix Sort":
        startMergeSort(data,drawData,stepTime)
    elif algorithm=="Heap Sort":
        startMergeSort(data,drawData,stepTime)
    #add your algorithm and call it here
    



#function to move the main window with the cursor drag
#implement when in need to eliminate the title bar and make a custom title bar
def get_pos(event):
    xwin = root.winfo_x()
    ywin = root.winfo_y()
    startx = event.x_root
    starty = event.y_root
    ywin = ywin - starty
    xwin = xwin - startx

    def move_window(event):
        root.geometry("{0}x{1}+{2}+{3}".format(width,height,event.x_root + xwin, event.y_root + ywin))
    startx = event.x_root
    starty = event.y_root

    titlef.bind('<B1-Motion>', move_window)



#function to generate random data for visualization
def genData(data_size):
    global data,colorData
    data=colorData=[]

    #set initial color of elements
    colorData=['grey' for x in range(int(float(data_size)))]
    for _ in range(int(float(data_size))):
        data.append(random.randrange(1,100))

    #draw the elemets on canvas
    drawData(data,colorData)
    sizel.config(text=str(format(int(float(data_size)),"0>3d")))



#function to draw rectangles, 'data' is a list of rectangle heights and 'colorData' the respective colors
def drawData(data,colorData):
    global height,width

    #clears canvas before drawing new data
    canvas.delete("all")

    #setting canvas height,width
    canvas_h=height-20
    canvas_w=width

    #setting the spacing between 2 rectangle
    spacing=2

    #set the width of 1 rectangle
    rectangle_w=(canvas_w-spacing*(len(data)-1))/len(data)

    #normalizing the data
    for i in range(len(data)):
        data[i]=data[i]/max(data)
 
    #drawing the normalized data
    for i,rect_height in enumerate(data):
        x0=i*rectangle_w+(i+1)*spacing
        y0=canvas_h-rect_height*(canvas_h-20)
        x1=(i+1)*rectangle_w+(i+1)*spacing
        y1=canvas_h
        canvas.create_rectangle(x0,y0,x1,y1,fill=colorData[i])
        # canvas.create_text(x0+2,y0-2,text=str(i),fill='white')
    root.update_idletasks()



#to change display delay on the label
def dispDelay(delay):
    delayl.config(text=str(format(float(delay)/10,">03.1f")+" sec"))



#starts the visualizer GUI
def main():

    #set width and height of window
    global width,height
    width=1000
    height=610

    global root
    root=Tk()
    root.title(" SORTING VISULAIZER")
    style=ttk.Style()
    style.configure('TScale',background='black')
    # root.overrideredirect(1)
    # root.maxsize(width,height)
    root.resizable(0,0)
    root.config(bg='black')
    # root.attributes('-topmost',1)

    #to store the selected algorithm from combobox
    algorithm=StringVar()

    global titlef,delayl,sizel
    titlef=Frame(root,width=width,height=height,bg='black')
    titlef.grid(row=0,column=0)
    # titlef.bind('<Button-1>', get_pos)
    sizel=Label(titlef,text="50",bg='black',fg='white',font=('Helvetica',25,'bold'))
    sizel.pack(side=LEFT,padx=(10,200))
    Label(titlef,text="Sorting Visualizer",bg='black',fg='white',font=('Helvetica',25,'bold')).pack(pady=10,side=LEFT)
    delayl=Label(titlef,text="0.0 sec",bg='black',fg='white',font=('Helvetica',25,'bold'))
    delayl.pack(side=LEFT,padx=(190,10))


    #top frame for user input
    topf=Frame(root,width=width, height=250 , bg='black')
    topf.grid(row=1,column=0,padx=10,pady=5)

    global size,speed
    size=IntVar()
    speed=IntVar()
    #row 1 of topf
    # Button(topf,text='x',command=exitGui).grid(row=0,column=5,sticky=E)
    Label(topf,text="Step Delay (sec)",bg='black',fg='white',font=('Helvetica',13,'bold')).grid(row=0,column=0,padx=5,pady=5,sticky=E)
    speed_scale=ttk.Scale(topf,variable=speed,from_=0,to=10,command=dispDelay)
    speed_scale.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    Label(topf,text="Select Algorithm",bg='black',fg='white',font=('Helvetica',13,'bold')).grid(row=0,column=3,padx=(50,0),pady=5,sticky=E)
    algorithm_menu=ttk.Combobox(topf,textvariable=algorithm,state='readonly',values=['Bubble Sort','Selection Sort','Insertion Sort','Merge Sort'])
    algorithm_menu.grid(row=0,column=4,padx=5,pady=5,sticky=W)
    algorithm_menu.current(0)

    #row 2 of topf 
    Label(topf,text="Size",bg='black',fg='white',font=('Helvetica',13,'bold')).grid(row=1,column=0,padx=5,pady=5,sticky=E)
    size_scale=ttk.Scale(topf,variable=size,from_=3,to=100,command=genData)
    size_scale.grid(row=1,column=1,padx=5,pady=5,sticky=W)
    size.set(50)
    Button(topf,text="Visualise",bg='white',command=lambda : visualize(algorithm.get(),speed.get())).grid(row=1,column=3,padx=(50,0),pady=5,ipadx=10,sticky=W)
    


    #canvas for visualisation
    global canvas
    canvas = Canvas(root,width=width,height=height-25,bg='black')
    canvas.grid(row=2,column=0,padx=10,pady=5)

    #generate 50 elements on gui startup
    genData(50)
    
     
    root.mainloop()

if __name__ == "__main__":
    main()
