class TestAdventureAgeConfirmation(unittest.TestCase):
    def test_invalid_age_input(self):
        # Simulate user input for age confirmation
        user_input = ['n', 'N']

        # Redirect user input to a mock input stream
        with mock.patch('builtins.input', side_effect=user_input):
            # Run the code block that checks age confirmation
            your_age = input("are you 21 or older? Y or N")
            if your_age.upper() == "Y":
                print("you can proceed.")
            else:
                print("You are too young to proceed." + "go back to the forest and find the way to the river bed, and look for the lotus flower that shines in the dark.")
                if your_age.upper() == "y":
                    print("You decide to stay and watch the sunset over the mountain, and soon enough, you come across a small cave.")
                    cave_entrance = input("do you want to enter the cave? Y or N")

        # Assert that the code block prints the correct message for invalid age input
        self.assertEqual(
            "You are too young to proceed.go back to the forest and find the way to the river bed, and look for the lotus flower that shines in the dark.",
            capsys.readouterr().out.strip()
        )

if __name__ == '__main__':
    unittest.main()