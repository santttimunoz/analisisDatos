import matplotlib.pyplot as ptl

def crearGrafico():
    labels = ["ventas medellin", "ventas bogota", "ventas cali"]
    values = [200, 100, 50]
    fig, ax = ptl.subplots()
    ax.pie(values, labels)
    ptl.show()
    ptl.close()