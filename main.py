import os
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

temps = pd.read_excel('CSVs/Temperatures Data.xlsx')

celsius = temps['Celsius']
farenheit = temps['Farenheit']
kelvin = temps['Kelvin']

def clear_terminal():
    if os.name == "nt":
        os.system("cls")

tf.get_logger().setLevel('ERROR')

print("Welcome to a temperature calculator")
print("\n")

# Create a list of model configurations
model_configs = [
    (celsius, kelvin),
    (celsius, farenheit),
    (kelvin, celsius),
    (kelvin, farenheit),
    (farenheit, celsius),
    (farenheit, kelvin)
]

# Create a list to store the models
models = []

# Create and compile 6 different models
for i, (input_data, output_data) in enumerate(model_configs):
    model_name = f"Model_{i+1}"
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(units=50, input_shape=[1]),
        tf.keras.layers.Dense(units=50),
        tf.keras.layers.Dense(units=1)
    ], name=model_name)  # Assign a distinct name to the model

    model.compile(
        optimizer=tf.keras.optimizers.Adam(0.1),
        loss='mean_squared_error'
    )

    models.append((model, input_data, output_data))

print("Please wait a little bit while the models train :D")
print("\n")

# Train each model in the list
for i, (model, input_data, output_data) in enumerate(models):
    print(f"Training Model {i+1}")
    model.fit(input_data, output_data, epochs=500, verbose=False)

clear_terminal()

print("All models have been trained!")

aux_while = 0

while aux_while == 0:

    print("Select a temperature unit to work with: ")
    print("\n")
    print("1 - Celsius")
    print("2 - Kelvin")
    print("3 - Farenheit")
    print("4 - Exit")
    print("\n")

    try:
        option = int(input('Option: '))
        print("\n")
    except ValueError:
        print("The input wasn't in the list")
        print("\n")

    clear_terminal()

    if option == 1:
        print("You choose Celsius")
        print("\n")
        aux_celsius = 0

        while aux_celsius == 0:
            print("Choose an action: ")
            print("\n")
            print("1 - Transform Celsius to Kelvin")
            print("2 - Transform Celsius to Farenheit")
            print("3 - Back to menu")
            print("4 - Exit")
            print("\n")

            try:
                option1 = int(input('Option: '))
                print("\n")
            except ValueError:
                print("The input wasn't in the list")
                print("\n")

            clear_terminal()

            if option1 == 1:
                aux_value = 0
                while aux_value == 0:

                    try:
                        value = int(input('Input the celsius value: '))
                        print("\n")
                        aux_value = 1
                    except ValueError:
                        print("The inserted value is not numeric")
                        print("\n")

                result = models[0][0].predict([value])
                print(str(value) + " Celsius, son: " + str(round(float(result[0]),2)) + " Kelvin")
                print("\n")

            if option1 == 2:
                aux_value = 0
                while aux_value == 0:

                    try:
                        value = int(input('Input the celsius value: '))
                        print("\n")
                        aux_value = 1
                    except ValueError:
                        print("The inserted value is not numeric")
                        print("\n")

                result = models[1][0].predict([value])
                print(str(value) + " Celsius, son: " + str(round(float(result[0]),2)) + " Farenheit")
                print("\n")

            if option1 == 3:
                aux_celsius = 1

            if option1 == 4:
                aux_while = 1
                break

            else:
                print("The input wasn't in the list")

    if option == 2:
        print("You choose Kelvin")
        print("\n")
        aux_kelvin = 0

        while aux_kelvin == 0:
            print("Choose an action: ")
            print("\n")
            print("1 - Transform Kelvin to Celsius")
            print("2 - Transform Kelvin to Farenheit")
            print("3 - Back to menu")
            print("4 - Exit")
            print("\n")

            try:
                option2 = int(input('Option: '))
                print("\n")
            except ValueError:
                print("The input wasn't in the list")
                print("\n")

            clear_terminal()

            if option2 == 1:
                aux_value = 0
                while aux_value == 0:

                    try:
                        value = int(input('Input the Kelvin value: '))
                        print("\n")
                        aux_value = 1
                    except ValueError:
                        print("The inserted value is not numeric")
                        print("\n")

                result = models[2][0].predict([value])
                print(str(value) + " Kelvin, son: " + str(round(float(result[0]),2)) + " Celsius")
                print("\n")

            if option2 == 2:
                aux_value = 0
                while aux_value == 0:

                    try:
                        value = int(input('Input the Kelvin value: '))
                        print("\n")
                        aux_value = 1
                    except ValueError:
                        print("The inserted value is not numeric")
                        print("\n")

                result = models[3][0].predict([value])
                print(str(value) + " Kelvin, son: " + str(round(float(result[0]),2)) + " Farenheit")
                print("\n")

            if option2 == 3:
                aux_kelvin = 1

            if option2 == 4:
                aux_while = 1
                break

            else:
                print("The input wasn't in the list")


    if option == 3:
        print("You choose Farenheit")
        print("\n")
        aux_farenheit = 0

        while aux_farenheit == 0:
            print("Choose an action: ")
            print("\n")
            print("1 - Transform Farenheit to Celsius")
            print("2 - Transform Farenheit to Kelvin")
            print("3 - Back to menu")
            print("4 - Exit")
            print("\n")

            try:
                option3 = int(input('Option: '))
                print("\n")
            except ValueError:
                print("The input wasn't in the list")
                print("\n")

            clear_terminal()

            if option3 == 1:
                aux_value = 0
                while aux_value == 0:

                    try:
                        value = int(input('Input the Farenheit value: '))
                        print("\n")
                        aux_value = 1
                    except ValueError:
                        print("The inserted value is not numeric")
                        print("\n")

                result = models[4][0].predict([value])
                print(str(value) + " Farenheit, son: " + str(round(float(result[0]),2)) + " Celsius")
                print("\n")

            if option3 == 2:
                aux_value = 0
                while aux_value == 0:

                    try:
                        value = int(input('Input the Farenheit value: '))
                        print("\n")
                        aux_value = 1
                    except ValueError:
                        print("The inserted value is not numeric")
                        print("\n")

                result = models[5][0].predict([value])
                print(str(value) + " Farenheit, son: " + str(round(float(result[0]),2)) + " Kelvin")
                print("\n")

            if option3 == 3:
                aux_farenheit = 1

            if option3 == 4:
                aux_while = 1
                break

            else:
                print("The input wasn't in the list")

    if option == 4:
        aux_while = 1










