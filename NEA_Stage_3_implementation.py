# NEA Stage 3: Implementation
class NEA(object):
    def __init__(self):
        self.bags = 0

    def implementation(self):
        def main():
            def main_menu():
                print("██████████████████")
                print("█ > Donate to charity(1)     █")
                print("█ > Open stats(2)             █")
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

                        incorrect = True

                        while incorrect:
                            v_name, coin_type, bag_weight = input("Name: "), float(input("Coin Type: ")),\
                                                                float(input("Bag Weight: "))
                            if ValueError:
                                pass
                                #Ill work on this later


                        # Now incorrect is False

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
                    cbw = 0
                    bag_value = bag_values[mega_pos]

                    global coin_weight
                    coin_weight = coin_weights[mega_pos]

                    cbw += (bag_value/coin_type) * coin_weight
                    print('bag weight: ' + str(bag_weight))
                    print('cbw: ' + str(cbw))

                    global weight_diff
                    weight_diff = bag_weight - cbw
                    print('weight_diff: ' + str(weight_diff))

                    # calculation function has been done!

                    thingy = 'on'

                    # Wacky loop, ^^ is related to the loop
                    while thingy == 'on':
                        if weight_diff == 0:
                            print("Donated successfully")
                            self.bags += 1
                            more_bags = input("Do you wish to add more bags? (y/n) ")
                            if more_bags == 'n':
                                thingy = 'off'

                            # Go back to menu.
                            elif more_bags == 'y':

                                self.implementation()

                        elif weight_diff < 0:
                            print("Your submitted bag weight is %s grams lighter than the real value. Add %s coin"
                                  "s." % abs(weight_diff), round(weight_diff/coin_weight))
                            add_or_no = input("Add %s grams? (y/n)" % abs(weight_diff))
                            if add_or_no == 'y':
                                print("Adding %s grams..." % abs(weight_diff))
                                weight_diff = 0
                                print("Added!")

                calculations()
            main_menu()

            invalid = True

            while invalid:
                if option == str(1):
                    input_data()
                    invalid = False
                elif option == str(2):
                    pass
                    # Show logs
                    invalid = False
                elif option == str(3):
                    # Close program
                    exit()
                    invalid = False
                else:
                    # Keeping invalid the way it is. True
                    pass
        main()

    def coin_count_stuff(self):
        increment = 1
        with open('CoinCount.txt', 'r+') as coin_count:
            coin_count.write('ENTRY ' + str(increment) + ': Volunteer Name: ' + v_name + ', Donated amount: ' +
                             str(coin_type * bag_weight/coin_weight) + 'Accuracy: ')
            increment += 1
my_NEA = NEA()
my_NEA.implementation()
