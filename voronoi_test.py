from PIL import Image
import random
import math

Rt = [(5,25),(20,10),(20,20),(20,30),(20,40),(26,10),(26,20),(26,30),(26,40),(32,20),(32,30),(38,20),(38,30),(44,10),(44,20),(44,30),
(44,40),(50,10),(50,20),(50,30),(50,40),(65,25)]

def generate_voronoi_diagram(width, height, num_cells):
  image = Image.new("RGB", (width, height))
  putpixel = image.putpixel
  imgx, imgy = image.size
  nx = []
  ny = []
  nr = []
  ng = []
  nb = []
  for i in range(num_cells):
    nr.append(random.randrange(50,256))
    nb.append(random.randrange(50,256))

  jj=-1
  for y in range(imgy):
    for x in range(imgx):
      dmin = math.hypot(imgx, imgy)

      j=-1
      for i in range(num_cells):
        d = math.hypot(Rt[i][0]-x, Rt[i][1]-y)  

        if d < dmin:
          dmin = d
          j = i

        if(x == Rt[j][0] and y == Rt[j][1] and j<11):
          putpixel((x, y), (255, 0, 0))
        elif(x == Rt[j][0] and y == Rt[j][1] and j>=11):
          putpixel((x, y), (0, 0, 255))
        '''elif(jj!=j):
          putpixel((x,y),(0,0,0))
          jj=j
          '''
        else:
          putpixel((x,y),(255,255,255))

  image.save("VoronoiDiagram.png", "PNG")
  image.show()


generate_voronoi_diagram(70, 50, len(Rt))


