
APPROVED_BREEDS = [
        "Mastiff",
        "Chihuahua",
        "Corgi",
        "Shar Pei",
        "Beagle",
        "French Bulldog",
        "Pug",
        "Pointer"
    ]

class Dog:
    def __init__(self, name="", breed="Mutt"):
        assert isinstance(name, str) and 0 < len(name) <= 25, "Name must be a string between 1 and 25 characters."
        self.name = name

        assert isinstance(breed, str), "Breed must be a string."
        assert breed in Dog.APPROVED_BREEDS, "Breed must be in the list of approved breeds."
        self.breed = breed
