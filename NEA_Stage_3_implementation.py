# NEA Stage 3: Implementation
class NEA(object):
    def implementation(self):
        # Predefined process: Input
        def input_data():

            invalid = True

            # While validity is not true...
            while invalid:
                v_name, coin_type, bag_weight = input("Name: "), int(input("Coin Type: ")), int(input("Bag Weight: "))

                coin_types = [2,    1,    0.5, 0.2, 0.1,  0.05, 0.02, 0.01]  # In pounds
                bag_values = [20,   20,   10,  10,  5,    5,    1,    1]  # In pounds
                coin_weights = [12, 8.75, 8,   5,   6.5,  3.25, 7.12, 3.56]  # In grams

                # if coin_type is not a valid one...
                if coin_type not in coin_types:
                    # Not changing validity
                    print("Incorrect coin type. Please try again.")

                elif not v_name.isalpha():
                    # Not changing validity
                    print("Invalid name. Please try again.")

                elif coin_type in coin_types:
                    invalid = False
                    print("Valid")

            # coin type AND name has been validated!

            # Predefined process: Calculations
            def calculations():
                # Connecting all the three values.
                mega_pos = coin_types.index(coin_type)

                # Correct bag weight
                cbw = 0
                bag_value = bag_values[mega_pos]
                coin_weight = coin_weights[mega_pos]

                cbw += (bag_value/coin_type) * coin_weight
                print(bag_weight)

                weight_diff = bag_weight - cbw

                coin_diff = weight_diff/coin_weight

                # calculation function has been done!

                if coin_diff == 0:
                    print("Donated successfully")
                    bags += 1

            calculations()
        input_data()

        if coin_diff == 0:
            print("Donated successfully")
            bags += 1

my_NEA = NEA()
my_NEA.implementation()
