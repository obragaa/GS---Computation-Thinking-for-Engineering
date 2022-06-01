# This Python file uses the following encoding: utf-8

def electric_car_average():
    # De acordo com a General Motors, o Chevrolet Bolt tem uma bateria de 66 kWh e autonomia de 416 km.

    reference = 100
    try:
        electric_car_battery = int(input("Digite o valor da bateria (kWh) do carro elétrico: "))

        electric_car_autonomy = int(input("Digite a autonomia do veículo (km) do carro elétrico: "))
    except:
        print("Digite valores coerentes.")
        exit()

    average_consumption = round(float((reference * electric_car_battery)/electric_car_autonomy), 2)

    print(average_consumption)

def average_car_combustion():

    a = input()


def init():
    electric_car_average()


init()