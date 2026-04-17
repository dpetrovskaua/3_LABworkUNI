import pytest
from base import BuildingBlock

def test_block_initialization():
    block = BuildingBlock(name="Stone", category="Structural", hardness=1.5, blast_resistance=6.0, is_transparent=False)
    assert block.name == "Stone"
    assert block.category == "Structural"
    assert block.hardness == 1.5
    assert block.blast_resistance == 6.0
    assert block.is_transparent == False

def test_equality():
    block1 = BuildingBlock("Dirt", "Natural", 0.5, 0.5, False)
    block2 = BuildingBlock("Dirt", "Natural", 0.5, 0.5, False)
    block3 = BuildingBlock("Sand", "Natural", 0.5, 0.5, False)
    assert block1 == block2  # однаковий вміст тому мають бути рівні
    assert block1 != block3  # різні імена тому не рівні

def test_representation():
    block = BuildingBlock("Glass", "Ornamental", 0.3, 0.3, True)
    expected_repr = "BuildingBlock(name='Glass', hardness=0.3, blast_resistance=0.3)"
    assert repr(block) == expected_repr

def test_sorting_logic():
    # блоки спеціально для перевірки сортування
    b1 = BuildingBlock("Block A", "Test", 2.0, 10.0, False)
    b2 = BuildingBlock("Block B", "Test", 2.0, 50.0, False)  # твердість така ж, але опір вибухам більший
    b3 = BuildingBlock("Block C", "Test", 0.5, 1.0, False)  # найменш твердий

    blocks = [b1, b2, b3]
    blocks.sort(key=lambda b: (b.hardness, -b.blast_resistance))
    # очікуваний порядок:
        # 1. Block C (найменший hardness: 0.5)
        # 2. Block B (hardness: 2.0, але blast_resistance 50.0 > 10.0, тому він іде перед A)
        # 3. Block A (hardness: 2.0, blast_resistance 10.0)
    assert blocks == [b3, b2, b1]

def test_not_equal_different_types():
    block = BuildingBlock("Obsidian", "Natural", 50.0, 1200.0, False)
    assert block != "Рядок"
    assert block != 123
