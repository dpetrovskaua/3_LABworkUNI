from base import BuildingBlock
def main():
    blocks = [
        BuildingBlock("Stone", "Structural", 1.5, 6.0, False),
        BuildingBlock("Cobblestone", "Structural", 2, 6.0, False),
        BuildingBlock("Dirt", "Natural", 0.5, 0.5, False),
        BuildingBlock("Glass", "Ornamental", 0.3, 0.3, True),
        BuildingBlock("Obsidian", "Natural", 50.0, 1200.0, False),
        BuildingBlock("Wood", "Structural", 2.0, 2.0, False),
        BuildingBlock("Sand", "Natural", 0.5, 0.5, False),    ]

    print("Оригінальний порядок:")
    for block in blocks:
        print(block)
    # сортування; мінус перед b.blast_resistance дає спадання.
    blocks.sort(key=lambda b: (b.hardness, -b.blast_resistance))
    print("\nВідсортований порядок (За зростанням по hardness, За спаданням по Blast resistance):")

    for block in blocks:
        print(block)
    # пошук ідент об'єктів; створюємо об'єкт з такими ж характеристиками, як у скла
    target_block = BuildingBlock("Glass", "Ornamental", 0.3, 0.3, True)

    print(f"\nПошук: {target_block}")
    if target_block in blocks:
        index = blocks.index(target_block)
        print(f"Успіх! Ідентичний блок знайдено за номером: {index+1}")
    else:
        print("Блок не знайдено.")

if __name__ == "__main__":
    main()
