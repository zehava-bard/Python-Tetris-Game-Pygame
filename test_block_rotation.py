def test_tblock_rotation_cycles(t_block):
    original_positions = t_block.get_cell_positions()
    for _ in range(4):
        t_block.rotate()
    cycled_positions = t_block.get_cell_positions()
    # אחרי 4 סיבובים זה אמור לחזור למצב ההתחלתי
    for p1, p2 in zip(original_positions, cycled_positions):
        assert p1.row == p2.row
        assert p1.column == p2.column

def test_tblock_move_and_undo(t_block):
    original = [(pos.row, pos.column) for pos in t_block.get_cell_positions()]
    t_block.move(1, -2)
    moved = [(pos.row, pos.column) for pos in t_block.get_cell_positions()]
    assert any(o != m for o, m in zip(original, moved))

    t_block.move(-1, 2)
    restored = [(pos.row, pos.column) for pos in t_block.get_cell_positions()]
    assert original == restored
