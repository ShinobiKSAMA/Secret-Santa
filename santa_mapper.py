import random

class SantaMapper:
    def __init__(self, names: list) -> None:
        """
        Initializes the SantaMapper with a list of names.

        Parameters:
        - names (list): A list of tuples containing names and addresses.
        """
        
        self.names = names

    def map_santas(self) -> dict:
        """
        Generates Santa mappings based on the provided list of names.

        Returns:
        - dict: A dictionary where each name is mapped to another name, forming Santa pairings.
        """
        
        # Create a shuffled copy of the names list
        shuffled: list = self.names.copy()

        # Ensure the shuffled list has an even number of elements by adding "No Mapping" if necessary
        if len(shuffled) % 2 != 0:
            shuffled.append(("No Mapping", "No Mapping"))
        
        # Shuffle the list randomly
        random.shuffle(shuffled)

        # Initialize an empty dictionary to store Santa mappings
        santa_mappings: dict = {}

        # Iterate through each name in the original list
        for name, address in self.names:
            # Create a list of potential matches excluding the current name and already mapped names
            canBe: list = [(x,y) for x,y in shuffled if x != name and not santa_mappings.keys().__contains__(name)]
            
            # Choose a random match from the potential matches
            match: tuple = random.choice(canBe)
            
            # Remove the selected match from the shuffled list
            shuffled.remove(match)

            # Add the mapping to the dictionary
            santa_mappings[name] = match

        # Return the final dictionary of Santa mappings
        return santa_mappings