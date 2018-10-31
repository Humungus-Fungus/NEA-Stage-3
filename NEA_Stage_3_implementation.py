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
                    print("ERROR: Invalid coin type (2nd input). Please try again.")

                elif not v_name.isalpha():
                    # Not changing validity
                    print("ERROR: Invalid name (1st input). Please refrain from using numbers/symbols in your name and"
                          " try again.")

                elif coin_type in coin_types:
                    invalid = False
                    print("✓\n")

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
                print('bag weight: ' + str(bag_weight))
                print('cbw: ' + str(cbw))

                weight_diff = bag_weight - cbw
                print('weight_diff: ' + str(weight_diff))
                coin_diff = weight_diff/coin_weight
                print('coin_diff: ' + str(coin_diff))
                # calculation function has been done!

                bags = 0

                if coin_diff == 0:
                    print("Donated successfully")
                    bags += 1

            calculations()
        input_data()


my_NEA = NEA()
my_NEA.implementation()
