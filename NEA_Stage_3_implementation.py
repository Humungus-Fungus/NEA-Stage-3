# NEA Stage 3: Implementation
class NEA(object):
    def __init__(self):
        self.bags = 0

    def implementation(self):
        def main():
            def main_menu():
                print("██████████████████")
                print("█ > Donate to charity(1)     █")
                print("█ > Open stats(2)            █")
                print("█ > Quit(3)                  █")
                print("██████████████████\n")

                global option
                option = input("Choose an option: ")

            # Predefined process: Input
            def input_data():

                def inputs():
                    global invalid
                    invalid = True

                    # While validity is not true...
                    while invalid:
                        global v_name
                        global coin_type
                        global bag_weight
                        global coin_types
                        global bag_values
                        global coin_weights

                        increment = 1

                        for i in range(increment):
                            try:
                                v_name, coin_type, bag_weight = input("Name: "), float(input("Coin Type: ")),\
                                                                float(input("Bag Weight: "))
                            except ValueError:
                                # Constantly increasing the size of the list, so the above code is run until correct.
                                increment += 1

                        coin_types = [2,    1,    0.5, 0.2, 0.1,  0.05, 0.02, 0.01]  # In pounds
                        bag_values = [20,   20,   10,  10,  5,    5,    1,    1]  # In pounds
                        coin_weights = [12, 8.75, 8,   5,   6.5,  3.25, 7.12, 3.56]  # In grams

                        # if coin_type is not a valid one...

                        if coin_type not in coin_types:
                            # Not changing validity
                            print("ERROR: Invalid coin type (2nd input). Please try again.")

                        elif not v_name.isalpha():
                            # Not changing validity
                            print("ERROR: Invalid name (1st input). Please refrain from using numbers/symbols in your"
                                  " name and try again.")

                        elif coin_type in coin_types:
                            invalid = False
                            print("✓\n")

                inputs()

                # coin type AND name has been validated!

                # Predefined process: Calculations
                def calculations():
                    # Connecting all the three values.
                    mega_pos = coin_types.index(coin_type)

                    # Correct bag weight
                    global cbw
                    cbw = 0
                    bag_value = bag_values[mega_pos]

                    global coin_weight
                    coin_weight = coin_weights[mega_pos]

                    cbw += (bag_value/coin_type) * coin_weight

                    global weight_diff
                    weight_diff = bag_weight - cbw
                    print('weight_diff: ' + str(weight_diff))

                    # calculation function has been done!

                    # This is for altering weight diff without altering wait diff
                    new_weight_diff = weight_diff
                    while True:
                        if new_weight_diff == 0:
                            print("Donated successfully")
                            self.bags += 1
                            more_bags = input("Do you wish to add more bags? (y/n) ")
                            if more_bags == 'n':
                                break

                            # Go back to menu.
                            elif more_bags == 'y':

                                input_data()

                        elif new_weight_diff < 0:
                            abs_weight_diff = abs(int(weight_diff))
                            coin_weight = int(coin_weight)
                            print("Your submitted bag weight is %d grams lighter than the real value. Add %d grams."
                                  % (abs_weight_diff, abs_weight_diff))
                            add_or_no = input("Added %d grams yet? (y/n)" % abs_weight_diff)

                            while True:
                                if add_or_no == 'y':
                                    print('Great coin slotting skills!')
                                    new_weight_diff = 0
                                    break
                                elif add_or_no == 'n':
                                    print('Well get on with it!')
                                    add_or_no = input("Added %d grams yet? (y/n) " % abs_weight_diff)
                                    # Keeping the loop alive (no -break-s)

                        elif new_weight_diff > 0:
                            abs_weight_diff = abs(int(weight_diff))
                            coin_weight = int(coin_weight)
                            print("Your submitted bag weight is %d grams heavier than the real value. Remove %d grams."
                                  % (weight_diff, abs_weight_diff))
                            remove_or_no = input("Removed %d grams yet? (y/n) " % abs_weight_diff)

                            while True:
                                if remove_or_no == 'y':
                                    print("Great coin pulling skills!")
                                    new_weight_diff = 0
                                    break
                                elif remove_or_no == 'n':
                                    print('Well get on with it!')
                                    remove_or_no = input('Removed %d grams yet? (y/n) ' % abs_weight_diff)
                                    # Keeping the loop alive (notice the lack of -break-ing)

                calculations()
            main_menu()

            while True:
                if option == str(1):
                    input_data()
                    break
                elif option == str(2):
                    with open('CoinCount.txt', 'r') as coin_count:
                        cc_lines = coin_count.readlines()
                        while '\n' in cc_lines:
                            cc_lines.remove('\n')
                        for i in cc_lines:
                            i += '\n'
                            print(i)
                    break
                elif option == str(3):
                    # Close program
                    exit()
                    break
                else:
                    # Keeping invalid the way it is. True
                    pass
        main()


def coin_count_stuff():
        with open('CoinCount.txt', 'a') as coin_count:
            try:
                coin_count.write('\nENTRY : Volunteer Name: ' + v_name + ', Donated amount (submitted): ' +
                                 str(bag_weight) + ', Donated amount(actual):' + str(cbw) + ' grams. Accuracy: ' +
                                 str((bag_weight/cbw) * 100) + '%')
            except NameError:
                pass

my_NEA = NEA()

while True:
    my_NEA.implementation()
    coin_count_stuff()
