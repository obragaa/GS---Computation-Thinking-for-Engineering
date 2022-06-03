# This Python file uses the following encoding: utf-8
def input_value_universal():
    global reference, price_param

    try:
        #distance_param = int(input("Digite uma distância para ser usada como parâmetro (exemplo: 100 km): "))
        print("-----------------------------------------------------------------------------")
        price_param = float(input("Digite um valor para ser comparado entre o carro elétrico e o carro a combustão (exemplo: 7.8 reais): "))
    except:
        print("Digite valores coerentes.")
        exit()
    print("-----------------------------------------------------------------------------")

    reference = 100


def electric_car_average():

    try:
        print("-----------------------------------------------------------------------------")

        electric_car_battery = int(input("Digite o valor da bateria (kWh) do carro elétrico: "))

        electric_car_autonomy = int(input("Digite a autonomia do veículo (km) do carro elétrico: "))
        print("-----------------------------------------------------------------------------\n")
    except:
        print("Digite valores coerentes.")
        exit()

    average_consumption = round(float((reference * electric_car_battery)/electric_car_autonomy), 2)
    car_electric_price_per_reference = round(average_consumption * 0.50, 2)
    car_electric_liter_per_reference = round(price_param / car_combustion_liter_price, 2)
    how_much_better_is = round(car_combustion_price_per_reference / car_electric_price_per_reference)

    print(f"Preço gasto com o carro elétrico: "
          f"R${car_electric_price_per_reference}\n")

    print(f"Preço gasto com o carro a combustão: : "
          f"R${car_combustion_price_per_reference}\n")

    print(f"O quão econômico o carro elétrico é: "
          f"{how_much_better_is} vezes menos do valor do carro a combustão")


def average_car_combustion():
    global car_combustion_liter_price, car_combustion_price_per_reference

    try:
        car_combustion_km_per_liter = int(input("Média de quilômetros percorridos por litro gasto (exemplo: 10km por litro): "))
        car_combustion_liter_price = float(input("Digite o valor da gasolina (exemplo: 5 por litro): "))
    except:
        print("Digite valores coerentes.")
        exit()

    car_combustion_price_per_reference = car_combustion_liter_price * car_combustion_km_per_liter


def verify_loop():
    global aux

    print("-----------------------------------------------------------------------------")
    verify = input("Gostaria de calcular o consumo novamente? ").upper()

    if verify != "SIM":
        aux = False


def init():
    global aux

    aux = True

    while aux:
        input_value_universal()
        average_car_combustion()
        electric_car_average()
        verify_loop()


init()