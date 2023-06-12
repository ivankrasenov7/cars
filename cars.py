"""
Author:     Ivan Kirov
Date:       07.06.23
Description: Json Car Reader
Version:     1.0
"""

import pandas as pd


class Cars:
    """
    Car object class

    Attributes
    ----------
    data : json string

    Methods
    -------
    car_counts()
        get unique car counts
    average_number()
        get average car numbers
    heaviest_cars()
        get 5 heaviest cars
    manufacturer()
        get number of cars of each producer
    year()
        get number of cars by each year
    save_csv
        save the file to a directory
    """
    def __init__(self, data):
        """
        :param data: str
            json data string
        """
        self.data = data

    def car_counts(self):
        """

        :return:
            non unique cars
        """
        unique_cars = self.data["Name"].nunique()
        return unique_cars

    def average_number(self):
        """

        :return:
            average horsepower
        """
        average_horsepower = self.data["Horsepower"].mean()
        return average_horsepower

    def heaviеst_cars(self):
        """

        :return:
            five heaviest cars
        """
        heaviest_five_car = self.data.nlargest(5, "Weight_in_lbs")
        return heaviest_five_car

    def manufacturer(self):
        """

        :return:
            produced cars by manufaturer
        """
        cars_manufacturer = self.data["Origin"].value_counts()
        return cars_manufacturer

    def year(self):
        """

        :return:
            produced cars by year
        """
        cars_by_year = self.data["Year"].value_counts()
        return cars_by_year

    def save_csv(self, output_file):
        """

        :param output_file:
        :return:
            csv data file
        """
        self.data.to_csv(output_file, index=False)


def main():
    try:
        df = pd.read_json("cars.json")
        print("Data has been succesfully uploaded")
    except FileNotFoundError:
        print("Fila was not found. Pleave provide valid information")
        return

    analysis = Cars(df)

    unique_cars = analysis.car_counts()
    print(f"The number of unique cars is relevant to {unique_cars}")

    average_horsepower = analysis.average_number()
    print(f"The average horsepower of the cars is {average_horsepower}")

    heaviest_five_car = analysis.heaviеst_cars()
    print(f"The five heaviest cars are: {heaviest_five_car}")

    cars_manufacturer = analysis.manufacturer()
    print("Number of cars produced by each manufacturer:" ,cars_manufacturer)

    cars_by_year = analysis.year()
    print(f"Number of cars produced by each year: {cars_by_year}")

    analysis.save_csv("Cars_output.csv")
    print("Data has been sucessfully upoloaded in Cars_output.csv")


if __name__ == "__main__":
    main()
