import matplotlib.pyplot as plt
import numpy as np

print("Welcom. Today you will create and customize a visual graph!")
print("Your requested number of random values will be generated.")
print("Then you will customize your graph. At the end, you can see your grap!")

countOfNumbers = int(input("Enter the count of random numbers you want: "))
randomNumbers = np.random.randint(0, 100, countOfNumbers)
numbersXAxis = np.array(range(countOfNumbers))

colorOfLine = input("Enter the color of the lines (r, g, b, y): ")
styleOfLine = input("Enter the style of line (--, *-, :, -.)")
markersOfLine = input("Enter the marker of line (.,ov^><1234): ")

(myFigure, myAxes) = plt.subplots()
myAxes.plot(numbersXAxis, randomNumbers, color=colorOfLine, linestyle = styleOfLine, marker = markersOfLine)
plt.show()