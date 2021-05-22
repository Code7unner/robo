import matplotlib.pyplot as plt
import pandas as pd


def run():
    df = pd.read_csv('nyc_robots.csv', sep=';')
    BBox = (-74.1263, -73.9575, 40.6828, 40.7875)

    plt.plot(df.get('end station longitude'), df.get('end station latitude'), '.r', markersize=5)
    plt.plot(df.get('start station longitude'), df.get('start station latitude'), '.g', markersize=5)

    plt.axis([BBox[0], BBox[1], BBox[2], BBox[3]])

    coors = list(
        set(zip(df.get('start station longitude'), df.get('start station latitude'), df.get('start station name'))))
    for i in coors:
        plt.text(i[0], i[1], i[2], fontsize=7)
    coors = list(set(zip(df.get('end station longitude'), df.get('end station latitude'), df.get('end station name'))))
    for i in coors:
        plt.text(i[0], i[1], i[2], fontsize=7)

    plt.axes([0, 0, 0, 0])

    plt.show()


if __name__ == '__main__':
    run()
