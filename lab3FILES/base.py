class BuildingBlock:
    def __init__(self, name: str,  category: str, hardness: float, blast_resistance: float, is_transparent: bool):
        self.name = name
        self.category = category
        self.hardness = hardness  # за зростанням
        self.blast_resistance = blast_resistance  # за спаданням
        self.is_transparent = is_transparent

    def __repr__(self) -> str:
       return f"{self.name}, with hardness of {self.hardness} and blast_resistance of {self.blast_resistance}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BuildingBlock):
            return NotImplemented

        return (self.name == other.name and
                self.category == other.category and
                self.hardness == other.hardness and
                self.blast_resistance == other.blast_resistance and
                self.is_transparent == other.is_transparent)
