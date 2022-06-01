# This Python file uses the following encoding: utf-8

def electric_car_average():

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

    reference = 100

    car_combustion_liter_per_km = int(input("Média de quilômetros percorridos por litro gasto (exemplo: 1L == 1km): "))
    car_combustion_liter_price = float(input("Digite o valor da gasolina (exemplo: 4,0): "))
    car_combustion_liter_per_100km = car_combustion_liter_price * car_combustion_liter_per_km

    print(car_combustion_liter_per_100km)

def init():
    electric_car_average()
    average_car_combustion()


init()