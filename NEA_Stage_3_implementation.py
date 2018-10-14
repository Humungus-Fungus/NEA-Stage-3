# NEA Stage 3: Implementation
class NEA(object):
    def implementation():
        # Predefined process: Input
        def input():
            # All the different types of coin, bags, coin weights. All these values are linked.
            coin_types = [2,  1,  0.5, 0.2, 0.1,  0.05, 0.02, 0.01] # In pounds
            bag_values = [20, 20,  10, 10,  5,    5,    1,    1] # In pounds
            coin_weights=[12, 8.75, 8, 5,   6.5,  3.25, 7.12, 3.56] # In grams

            validity = False

            # While validity is not true...
            while not validity:
                v_name, coin_type, bag_weight = input("Name: "), input("Coin Type: "), input("Bag Weigth: ")

                if coin_type not in coin_types:
                    # Not changing validity
                    pass
                elif coin_type in coin_types:
                    validity = True

            # A way to connect all the three values. Mega because it's important. Pos because it's the position in the list.
            mega_pos = coin_types.index()

            bag_value = bag_values[mega_pos]
            coin_weight = coin_weights[mega_pos]
        
        # coin type has been validated!

        #Predefined process: Calculations
        def calculations():
            # Correct Bag Weight (cbw)
            cbw = (bag_value/coin_type) * coin_weight
        
