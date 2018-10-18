# NEA Stage 3: Implementation
class NEA(object):
    def implementation(self):
        cbw = 0
        # Predefined process: Input

        def input_data():
            # All the different types of coin, bags, coin weights. All these values are linked.
            coin_types = [2,    1,    0.5, 0.2, 0.1,  0.05, 0.02, 0.01]  # In pounds
            bag_values = [20,   20,   10,  10,  5,    5,    1,    1]  # In pounds
            coin_weights = [12, 8.75, 8,   5,   6.5,  3.25, 7.12, 3.56]  # In grams

            # Predefined process: Calculations
            def calculations(value):
                # Connecting all the three values. Mega because it's important. Pos because it's the position in list.
                mega_pos = coin_types.index(coin_type)

                bag_value = bag_values[mega_pos]
                coin_weight = coin_weights[mega_pos]

                value += (bag_value/coin_type) * coin_weight

            calculations(cbw)
            # calculation function has been done!

            validity = False

            # While validity is not true...
            while not validity:
                v_name, coin_type, bag_weight = input("Name: "), int(input("Coin Type: ")), int(input("Bag Weight: "))

                # if coin_type is not a valid one...
                if coin_type not in coin_types:
                    # Not changing validity
                    print("Incorrect coin type. Please try again.")

                elif not v_name.isalpha():
                    # Not changing validity
                    print("Invalid name. Please try again.")

                elif coin_type in coin_types:
                    validity = True

            # coin type AND name has been validated!

        input_data()

        def main_menu():
            print("")

my_NEA = NEA()
my_NEA.implementation()