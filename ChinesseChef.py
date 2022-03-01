from Chef import Chef

# Now the chinessChef has the qualities of the Chef plus this ones
class ChinesseChef(Chef):


    def make_fried_rice(self):
        print("I made fried rice")

    # overrides the function of the Chef
    def make_special_dish(self):
        print("My chinesse special dish")
