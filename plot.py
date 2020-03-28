import matplotlib.pyplot as plt
import numpy as np
import sys

filename = sys.argv[1]        # Stores ARG1 in filename, as in: $ python plot.py ARG1 ARG2 
data = np.loadtxt(filename, delimiter=",", skiprows=32)   # Attempts to load filename into local variable data.
#"Time sec","Extension mm","Load N","Stress MPa","Cycle Count ","Total Cycle Count ","Repetitions Count ","Strain [Exten.] %","Tenacity gf/tex"

range = (len(data))
stress = data[:,3]
strain = data[:,7]
plt.plot(strain, stress, color='c', linestyle='-', label='line')
plt.xlabel("Strain [Exten.] %")
plt.ylabel("Stress [MPa]")
plt.title("Stress vs Strain")
plt.legend(loc='best')

first, second =np.polyfit(stress,strain,1)
line_x=np.linespace(min(stress),max(stress))
line_y=np.polyval([first,second] ,line_x)
plt.plot(line_x,line_y, color='b', linestyle='--', label='Linear Regression')
plt.savefig(filename+'.pdf')
plt.show()

print("Young's Modulus : "+str(first)+ str('Mpa'))


## Part 0
# Figure out what arguments to add to the loadtxt function call
# so that numbers are loaded into the local function 'data'.
# Hint: look for arguments like 'skiprows' and 'delimiter'
# Check by running:
#   $ python plot.py raw-data/Sp15_245L_sect-001_group-1_glass.raw
# at the command line.


## Part 1
# Figure out what columns and rows of data we need to plot
# Stress (y-axis) vs Strain (x-axis)
# plot raw-data/Sp15_245L_sect-001_group-1_glass.raw
# Make sure to include axis labels and units!
# plt.plot(xdata,ydata, arguments-to-make-plot-pretty)


## Part 2
# Check to see if your code in part 1 will plot all of the files in raw-data/
# Edit the files (use git liberally here!) to make them more usable


## Part 3
# Use linear regression to calculate the slope of the linear part of
# the stress-strain data. Plot your line against the data to make 
# sure it makes sense! Use the slope of this line to calculate and print
# the Young's modulus (with units!)


## Part 4
# Modify your code to save your plots to a file and see if you can generate
# plots and Young's moduli for all of the cleaned up files in your data 
# directory. If you haven't already, this is a good time to add text to 
# your .gitignore file so you're not committing the figures to your repository.


# LIL JOKE FOR YOU WHILE YOU READ MY BORING CODE
## Why did the programmer quit his job?
#### Because he didnt get arrays
