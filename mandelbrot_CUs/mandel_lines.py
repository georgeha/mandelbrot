
__author__    = "George Chantzialexiou"
__copyright__ = "Copyright 2012-2013, The SAGA Project"
__license__   = "MIT"



import sys
from PIL import Image

################################################################################
##
def makemandel(mandelx, xbeg, xend, ybeg, yend, cy, y):

    # drawing area (xa < xb and ya < yb)
    xa = -2.0
    xb =  1.0

    # maximum iterations
    maxIt = 128 

    # the output image
    image = Image.new("RGB", (xend-xbeg, yend-ybeg))
    for x in range(xbeg, xend):
        cx = x * (xb - xa) / (mandelx - 1) + xa
        c = complex(cx, cy)
        z = 0
        for i in range(maxIt):
            if abs(z) > 2.0: break 
            z = z * z + c 
        r = i % 4 * 16
        g = i % 6 * 16
        b = i % 16 * 16
        image.putpixel((x-xbeg, y-ybeg), b * 65536 + g * 256 + r)
 
    image.save("mandel_%d.gif" % y, "GIF")
    
    return image

################################################################################
##
if __name__ == "__main__":

    args = sys.argv[1:]

    imgX = int(sys.argv[1])
    xBeg = int(sys.argv[2])
    xEnd = int(sys.argv[3])
    yBeg = int(sys.argv[4])
    yEnd = int(sys.argv[5])
    cy = float(sys.argv[6])
    y = int(sys.argv[7])


    makemandel(imgX, xBeg, xEnd, yBeg, yEnd, cy, y)
    sys.exit(0)
