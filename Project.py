import random

class PirateGame:
    def __init__(self):
        pass

    def start_game(self):
        print("Welcome to the Pirate Adventure!")
        print("You are a pirate on a quest for treasure. Choose wisely!")
        print("You find yourself on a deserted island with multiple paths ahead of you.")

    def choose_path(self):
        print("\nWhich path will you choose?")
        print("1. The path through the dense jungle.")
        print("2. The path along the rocky cliffs.")
        print("3. The path through the dark cave.")
        print("4. The path along the sandy beach.")

        choice = input("Enter your choice (1, 2, 3, or 4): ")

        if choice == "1":
            self.path_jungle()
        elif choice == "2":
            self.path_cliffs()
        elif choice == "3":
            self.path_cave()
        elif choice == "4":
            self.path_beach()
        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")
            self.choose_path()

    def path_jungle(self):
        print("\nYou chose the path through the dense jungle.")
        print("As you hack through the thick foliage, you encounter a wild boar.")

        decision = input("Will you (a) try to sneak past it, (b) fight it, or (c) try to tame it? (a/b/c): ")

        if decision.lower() == "a":
            print("\nYou manage to sneak past the boar and continue on your journey.")
            print("You come across an abandoned campsite.")
            self.explore_campsite()
        elif decision.lower() == "b":
            print("\nYou engage the boar in combat but are severely injured. Game over!")
        elif decision.lower() == "c":
            print("\nYou attempt to tame the boar but it doesn't seem interested. You continue on your journey.")
            print("You find a hidden cave entrance.")
            self.explore_cave()
        else:
            print("Invalid choice! Please enter 'a', 'b', or 'c'.")
            self.path_jungle()

    def explore_campsite(self):
        print("\nYou find various supplies at the campsite.")
        print("You also find a map with mysterious markings.")
        print("Do you (a) follow the map or (b) ignore it? (a/b): ")
        decision = input()
        if decision.lower() == "a":
            print("\nYou follow the map and discover a buried treasure!")
            self.treasure()
        elif decision.lower() == "b":
            print("\nYou ignore the map and continue on your journey.")
            print("You encounter a group of friendly monkeys.")
            print("You can (a) play with the monkeys or (b) move on. (a/b): ")
            decision = input()
            if decision.lower() == "a":
                print("\nThe monkeys cheerfully play with you for a while.")
                print("Feeling refreshed, you continue your adventure.")
            elif decision.lower() == "b":
                print("\nYou decide to move on and continue your adventure.")
            else:
                print("Invalid choice! Please enter 'a' or 'b'.")
                self.explore_campsite()
        else:
            print("Invalid choice! Please enter 'a' or 'b'.")
            self.explore_campsite()

    def explore_cave(self):
        print("\nYou enter the cave and find it filled with glittering gems.")
        print("You can (a) collect the gems or (b) leave them and continue. (a/b): ")
        decision = input()
        if decision.lower() == "a":
            print("\nYou collect the gems and continue on your journey.")
            print("You emerge from the cave and find a breathtaking waterfall.")
        elif decision.lower() == "b":
            print("\nYou decide to leave the gems untouched and continue on your journey.")
            print("You emerge from the cave and find a breathtaking waterfall.")
        else:
            print("Invalid choice! Please enter 'a' or 'b'.")
            self.explore_cave()

    def path_cliffs(self):
        print("\nYou chose the path along the rocky cliffs.")
        print("As you navigate the treacherous terrain, you slip and fall.")

        decision = input("Do you (a) try to climb back up, (b) search for another way, or (c) take a leap of faith? (a/b/c): ")

        if decision.lower() == "a":
            print("\nYou manage to climb back up and continue your journey.")
            print("You spot a shipwreck in the distance.")
            self.explore_shipwreck()
        elif decision.lower() == "b":
            print("\nYou search for another way but encounter a dead end. Game over!")
        elif decision.lower() == "c":
            print("\nYou take a leap of faith and land safely on a hidden ledge.")
            print("You find a chest containing valuable treasures.")
            self.treasure()
        else:
            print("Invalid choice! Please enter 'a', 'b', or 'c'.")
            self.path_cliffs()

    def explore_shipwreck(self):
        print("\nYou reach the shipwreck and explore its remains.")
        print("You find a damaged but salvageable boat.")
        print("Do you (a) repair the boat and sail away, or (b) search for more treasures? (a/b): ")
        decision = input()
        if decision.lower() == "a":
            print("\nYou repair the boat and sail away from the island, victorious!")
        elif decision.lower() == "b":
            print("\nYou search the shipwreck for more treasures but find nothing of value.")
            print("You decide to continue exploring the island.")
        else:
            print("Invalid choice! Please enter 'a' or 'b'.")
            self.explore_shipwreck()

    def path_cave(self):
        print("\nYou chose the path through the dark cave.")
        print("Inside the cave, you hear strange noises echoing from the depths.")

        decision = input("Do you (a) venture deeper into the cave, (b) turn back, or (c) light a torch? (a/b/c): ")

        if decision.lower() == "a":
            print("\nYou venture deeper into the cave and encounter a hidden chamber.")
            print("You find an ancient artifact.")
            self.treasure()
        elif decision.lower() == "b":
            print("\nYou decide to turn back, but you trip and injure yourself. Game over!")
        elif decision.lower() == "c":
            print("\nYou light a torch and explore further into the cave.")
            print("You find a secret passage leading to a pirate's hideout.")
            self.explore_hideout()
        else:
            print("Invalid choice! Please enter 'a', 'b', or 'c'.")
            self.path_cave()

    def explore_hideout(self):
        print("\nYou explore the pirate's hideout and find a stash of gold coins.")
        print("Do you (a) take the gold or (b) leave it and continue? (a/b): ")
        decision = input()
        if decision.lower() == "a":
            print("\nYou take the gold and become even richer!")
            self.treasure()
        elif decision.lower() == "b":
            print("\nYou decide to leave the gold untouched and continue on your adventure.")
            print("You exit the hideout and return to the cave entrance.")
        else:
            print("Invalid choice! Please enter 'a' or 'b'.")
            self.explore_hideout()

    def path_beach(self):
        print("\nYou chose the path along the sandy beach.")
        print("As you stroll along the beach, you notice a shipwreck in the distance.")

        decision = input("Do you (a) investigate the shipwreck, (b) search for seashells, or (c) build a sandcastle? (a/b/c): ")

        if decision.lower() == "a":
            print("\nYou investigate the shipwreck and find valuable artifacts!")
            print("You also find a message in a bottle.")
            self.read_message()
        elif decision.lower() == "b":
            print("\nYou search for seashells and find a rare pearl!")
            print("You continue along the beach.")
        elif decision.lower() == "c":
            print("\nYou build a magnificent sandcastle and admire your handiwork.")
            print("You feel refreshed and ready to continue your adventure.")
        else:
            print("Invalid choice! Please enter 'a', 'b', or 'c'.")
            self.path_beach()

    def read_message(self):
        print("\nThe message in the bottle contains a map to buried treasure!")
        print("Do you (a) follow the map or (b) discard it? (a/b): ")
        decision = input()
        if decision.lower() == "a":
            print("\nYou follow the map and discover a buried treasure!")
            self.treasure()
        elif decision.lower() == "b":
            print("\nYou discard the map and continue your journey.")
            print("You encounter a friendly dolphin swimming in the ocean.")
        else:
            print("Invalid choice! Please enter 'a' or 'b'.")
            self.read_message()

    def treasure(self):
        print("\nCongratulations! You found the treasure and became rich beyond your wildest dreams!")
        print("You have successfully completed your pirate adventure.")

    def play_again(self):
        choice = input("\nDo you want to play again? (yes/no): ")
        return choice.lower() == "yes"


def main():
    while True:
        game = PirateGame()
        game.start_game()
        game.choose_path()
        if not game.play_again():
            break

if __name__ == "__main__":
    main()
