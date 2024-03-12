import pandas as pd
import matplotlib.pyplot as plt
import cv2
import soap_bar
import shower_head


def soap_in_a_tub(soap_file="assets/bar_of_soap3.png", number_of_droplets=1000):
    """
    Simulate a bar of soap being eroded by a shower.

    :param soap_file:
    :param number_of_droplets:
    :return:
    """

    soap = soap_bar.SoapBar(soap_file)

    shower = shower_head.ShowerHead()
    data = []

    while soap.size() > 0:
        shower.generate_droplet(soap.soap, number_of_droplets)

        shower.update_droplets(soap.soap)

        droplet_impact = soap.erode(shower.droplets)

        shower.remove_droplets(droplet_impact)

        data.append([shower.total_droplets, soap.percentage_remaining()])

        animate_simulation(soap, shower)


    df = pd.DataFrame(data, columns=['Droplets', 'Soap Remaining'])

    graph_simulation(df)

    export_simulation_data_csv(df)


def graph_simulation(df):
    """
    Plot the simulation data. Number of droplets vs % soap remaining.
    :param df:
    :return:
    """
    df.plot(x='Droplets', y='Soap Remaining', kind='line')
    plt.plot(df['Droplets'], df['Soap Remaining'])
    plt.xlabel('Droplets')
    plt.ylabel('Soap Remaining')
    plt.title('Soap Erosion')
    plt.show()


def export_simulation_data_csv(df):
    """
    Export the simulation data to a csv file.
    :param df:
    :return:
    """
    df.to_csv('soap_simulation.csv', index=False)


def animate_simulation(soap, shower):
    """
    Animate the soap erosion simulation.
    :param soap:
    :param shower:
    :return:
    """
    display_soap = soap.soap.copy()

    shower.draw_droplets(display_soap, shower.droplets)

    cv2.imshow('Shower Simulation', display_soap)
    cv2.waitKey(30)


def main():
    soap_in_a_tub("assets/bar_of_soap3.png", 10000)


if __name__ == "__main__":
    main()
