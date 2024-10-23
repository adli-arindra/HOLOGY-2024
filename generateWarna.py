from matplotlib import pyplot as plt
import numpy as np

fcsv = open("warna.csv", "w")
fcsv.write("id, r, g, b\n")

path = "processed/"

for id in range(1, 778):
    img = plt.imread(path + f"{id}.jpg")

    print(id)

    try:
        r = []
        g = []
        b = []

        for i in range(200):
            for j in range(200):
                current = img[i][j]
                if current[0] != 255 or current[1] != 0 or current[2] != 200:
                    b.append(current[0])
                    g.append(current[1])
                    r.append(current[2])
    
        fcsv.write(f"{id},{np.median(r)},{np.median(g)},{np.median(b)}\n")
    except:
        fcsv.write(f"{id},0,0,0\n")

fcsv.close()