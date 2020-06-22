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
equ = regr.main([[1, 1], [2, 1], [3, 2], [4, 3], [5, 3]])
print (equ)