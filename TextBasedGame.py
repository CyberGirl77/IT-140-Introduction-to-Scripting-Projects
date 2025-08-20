# TextBasedGame.py
# Author: Davanna Scroggins

# Function to display game instructions
def show_instructions():
    print("Enchanted Forest Adventure Game")
    print("Collect all 6 enchanted relics to break the magician's curse.")
    print("Move commands: go North, go South, go East, go West")
    print("Add to Inventory: get [item name]\n")

# Function to show the player's current status
def show_status(current_room, inventory, rooms):
    print("---------------------------")
    print(f"You are in the {current_room}")
    print(f"Inventory: {inventory}")
    item = rooms[current_room].get("item", None)
    if item and item not in inventory:
        print(f"You see a {item}")
    print("---------------------------")

simulated_inputs = [
    "go North",             # Crystal Lake
    "get Crystal ball",
    "go East",              # Moonlit Grove
    "get Moonstone Necklace",
    "go East",              # Shimmering Falls
    "get Waterfall Tear",
    "go North",             # Sunstone Cavern
    "get Sunstone Bracelet",
    "go East",              # Rosebud Sanctuary
    "get Rosebud Elixir",
    "go West",              # go back
    "go South",             # Shimmering Falls
    "go West",              # Moonlit Grove
    "go South",             # Hissing Meadow
    "get Hissing Feather",
    "go North",             # Moonlit Grove
    "go West",              # Crystal Lake
    "go South",             # Fairy Circle
    "go East",              # Hissing Meadow (again)
    "go North",             # Moonlit Grove
    "go East",              # Shimmering Falls
    "go North",             # Sunstone Cavern
    "go East",              # Rosebud Sanctuary
    "go North"              # Shadowy Void (final boss)
]
input_index = 0

def safe_input(prompt):
    global input_index
    if input_index < len(simulated_inputs):
        command = simulated_inputs[input_index]
        print(f"{prompt}{command}")
        input_index += 1
        return command
    else:
        raise RuntimeError("No more simulated inputs available.")

# Main function containing gameplay logic
def main():
    rooms = {
        'Fairy Circle': {'North': 'Crystal Lake', 'East': 'Hissing Meadow'},
        'Crystal Lake': {'South': 'Fairy Circle', 'East': 'Moonlit Grove', 'item': 'Crystal ball'},
        'Hissing Meadow': {'West': 'Fairy Circle', 'North': 'Moonlit Grove', 'item': 'Hissing Feather'},
        'Moonlit Grove': {'South': 'Hissing Meadow', 'West': 'Crystal Lake', 'East': 'Shimmering Falls', 'item': 'Moonstone Necklace'},
        'Shimmering Falls': {'West': 'Moonlit Grove', 'North': 'Sunstone Cavern', 'item': 'Waterfall Tear'},
        'Sunstone Cavern': {'South': 'Shimmering Falls', 'East': 'Rosebud Sanctuary', 'item': 'Sunstone Bracelet'},
        'Rosebud Sanctuary': {'West': 'Sunstone Cavern', 'North': 'Shadowy Void', 'item': 'Rosebud Elixir'},
        'Shadowy Void': {'South': 'Rosebud Sanctuary'}  # Villain room
    }

    inventory = []
    current_room = 'Fairy Circle'

    show_instructions()

    while True:
        show_status(current_room, inventory, rooms)

        try:
            move = safe_input("Enter your move: ").strip().split(" ", 1)
        except RuntimeError as e:
            print(e)
            break

        command = move[0].lower()

        if command == 'go':
            if len(move) > 1:
                direction = move[1].capitalize()
                if direction in rooms[current_room]:
                    current_room = rooms[current_room][direction]
                else:
                    print("You can't go that way!")
            else:
                print("Please specify a direction.")

        elif command == 'get':
            if len(move) > 1:
                item = move[1]
                room_item = rooms[current_room].get("item", None)
                if room_item and item.lower() == room_item.lower() and item not in inventory:
                    inventory.append(room_item)
                    print(f"{room_item} added to inventory.")
                else:
                    print("Can't get that item.")
            else:
                print("Please specify what item to get.")

        else:
            print("Invalid command.")

        # Check for win/lose condition
        if current_room == 'Shadowy Void':
            if len(inventory) == 6:
                print("\nCongratulations! You have collected all enchanted relics and defeated the Shadow Beast!")
                print("Thanks for playing the game. Hope you enjoyed it.")
            else:
                print("\nThe Shadow Beast has trapped you in eternal darkness. GAME OVER!")
                print("Thanks for playing the game. Hope you enjoyed it.")
            break

# Run the game
if __name__ == "__main__":
    main()
