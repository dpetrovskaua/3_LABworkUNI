from base import BuildingBlock

def main():
    blocks = [
        BuildingBlock("Stone", "Structural", 1.5, 6.0, False),
        BuildingBlock("Cobblestone", "Structural", 2, 6.0, False),
        BuildingBlock("Dirt", "Natural", 0.5, 0.5, False),
        BuildingBlock("Glass", "Ornamental", 0.3, 0.3, True),
        BuildingBlock("Obsidian", "Natural", 50.0, 1200.0, False),
        BuildingBlock("Wood", "Structural", 2.0, 2.0, False),
        BuildingBlock("Sand", "Natural", 0.5, 0.5, False),
    ]

    print("--- Original Array ---")
    for block in blocks:
        print(block)
    # сортування
    # мінус перед b.blast_resistance дає спадання.
    blocks.sort(key=lambda b: (b.hardness, -b.blast_resistance))

    print("\n--- Sorted Array (Hardness ASC, Blast resistance DESC) ---")
    for block in blocks:
        print(block)
    # пошук ідент об'єктів
    # беремо рандом об'єкт: скло
    target_block = BuildingBlock("Glass", "Ornamental", 0.3, 0.3, True)

    print(f"\n--- Searching for: {target_block} ---")
    # через __eq__ в класі, 'in' порівняє всі поля, а не адреси в пам'яті
    if target_block in blocks:
        index = blocks.index(target_block)
        print(f"Success! Identical object found at index: {index}")
    else:
        print("Object not found in the array.")

if __name__ == "__main__":
    main()
