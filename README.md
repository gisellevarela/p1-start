Project 1
Software Used: Cisco Anyconnect (VPN), Terminal Window, XQuartz, numpy, github, and matplotlib

Accessing the Code: In order to access this code you will need to open up a terminal. Now Mac has a built in terminal and to access that you can search for it in the launch pad. If you are operating in windows you will have to download MobaXterm.
Then you will need to have VPN access either through Boise State oncampus or off campus which can be used by using your My Boise State login. Mac users will need to download XQuarts and if you are using Windows this step is unnecessary. 
Once you have a terminal open login in my typing in "ssh -Y USERNAME@coen-bascottie". After logging in you will want to cd into the "p1-start" folder. In this folder you will be able to access the code which is in "plot.py". 

How to Run: Locate the raw-data file to input your own data! Then open plot.py with vim to make any adjustments to the code so that it fits your data. Once you have made any adjustments necessary go back to your terminal with bascottie in the p1-start and type in "python plot.py". This will tell python to plot your data and a window should open up displaying a graph and Young's modulus.

Example of Running the Code: 
  ssh -Y JohnAdams@coen-bascottie
  cd p1-start
    vim raw-data
      #this will show you all the folders of data that are already in the code, remember to add your data!
    vim plot.py
      #view code and make adjustments
        #to make adjustments type "i" to insert any characters and ":wq" to exit vim
     python plot.py
        #graph should appear as well as Young's Modulus
        
Helpuful Notes: 
  If you were to mess up anytime while using this code and delete or type something by mistake just push the "u" key to undo.
  Tab Completion can be used to navigate between folders faster. Just hit the tab button when typing folders names! If you cant remember your options hit tab twice and python will display all possible folder names.
  
What I learned: To be quite blunt I had NO IDEA on how to code a single thing before this project. It was quite different to implement all the things we learned in class into one single project. Throughout this process I was able to understand the importance of staying organized while moving and rearranging files in python. I was also able to understand how important and pretty cool the program git is. Git was like a cloud that stored all information while making your code. I found it really helpful to refer back to a couple of my commits on git after I had deleted some information or misplaced it. This project was a challenge, but I feel like I have learned so much throughout the entire process. I was able to look back through ether pads and python notebooks to re jog my memory and finally see a WHOLE PICTURE to the world of coding. 
