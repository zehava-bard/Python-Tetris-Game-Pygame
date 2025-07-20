# Tests/test_game_logic.py
def test_game_initial(game_instance):
    assert game_instance.grid is not None
    assert game_instance.current_block is not None
    assert game_instance.next_block is not None
    assert game_instance.score == 0
    assert not game_instance.game_over


def test_block_inside_on_start(game_instance):
    assert game_instance.block_inside()

def test_rotate_block_keeps_inside(game_instance):
    block_before = game_instance.current_block
    game_instance.rotate()
    assert game_instance.block_inside()
    assert game_instance.current_block == block_before

def test_block_can_move_left(game_instance):
    col_before = game_instance.current_block.column_offset
    game_instance.move_left()
    col_after = game_instance.current_block.column_offset
    assert col_after <= col_before

def test_block_can_move_right(game_instance):
    col_before = game_instance.current_block.column_offset
    game_instance.move_right()
    col_after = game_instance.current_block.column_offset
    assert col_after >= col_before

def test_move_left_and_back(game_instance):
    old_pos = game_instance.current_block.column_offset, game_instance.current_block.column_offset
    game_instance.move_left()
    game_instance.move_right()
    new_pos = game_instance.current_block.column_offset, game_instance.current_block.column_offset
    assert new_pos == old_pos

def test_score_after_line_clear(game_instance, monkeypatch):
    row_to_clear = game_instance.grid.num_rows - 1
    for col in range(game_instance.grid.num_cols):
        game_instance.grid.grid[row_to_clear][col] = 1

    game_instance.lock_block()
    assert game_instance.score >= 100


def test_rotate_plays_sound(game_instance, monkeypatch):
    played = {"called": False}

    def fake_play():
        played["called"] = True

    monkeypatch.setattr(game_instance.rotate_sound, "play", fake_play)
    game_instance.rotate()
    assert played["called"]
