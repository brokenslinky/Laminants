import Laminants
from Laminants import *

if __name__=="__main__":
    print("Lay fabrics from bottom to top.")
    fabrics = []
    tmp = select_fabric()
    while tmp:
        fabrics.append(tmp)
        tmp = select_fabric()
    layers = []
    for fabric in fabrics:
        layers.append(Layer(fabric=fabric, matrix=epoxy, ratio=0.5))
    laminant = Laminant(layers)

    laminant.bend_to_failure()
