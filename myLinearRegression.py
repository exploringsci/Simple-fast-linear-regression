class regression:
    def favgxy(self, vals):
        sumx = 0
        sumy = 0
        for a in range(len(vals)):
            sumx += vals[a][0]
            sumy += vals[a][1]
        avgx = sumx / len(vals)
        avgy = sumy / len(vals)
        return [avgx, avgy]
    def main(self, inputsarr):
        avxy = self.favgxy(inputsarr)
        slopesum = 0
        for a in range(len(inputsarr)):
            if avxy[0] != inputsarr[a][0]:
                slopesum += (inputsarr[a][1] - avxy[1])/(inputsarr[a][0] - avxy[0])
        avgslope = slopesum / len(inputsarr)
        return "y - " + str(avxy[1]) + " = " + str(avgslope) + "(x - " + str(avxy[0]) + ")"
regr = regression()
inputList = input('Enter the x and y values of each point in the format x1,y1 x2,y2 x3,y3 etc. Space between points, comma only between x and y ')
inputList = inputList.split()
for x in range(len(inputList)):
    inputList[x] = inputList[x].split(",")
inputList = [list(map(int, point)) for point in inputList]
equ = regr.main(inputList)
print (equ)