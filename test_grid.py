def test_grid_initialization(empty_grid):
    assert empty_grid.num_rows == 20
    assert empty_grid.num_cols == 10
    for row in empty_grid.grid:
        assert all(cell == 0 for cell in row)

def test_grid_is_inside(empty_grid):
    assert empty_grid.is_inside(0, 0)
    assert empty_grid.is_inside(19, 9)
    assert not empty_grid.is_inside(-1, 0)
    assert not empty_grid.is_inside(20, 0)
    assert not empty_grid.is_inside(0, 10)

def test_grid_is_empty(empty_grid):
    assert empty_grid.is_empty(0, 0)
    empty_grid.grid[0][0] = 1
    assert not empty_grid.is_empty(0, 0)

def test_grid_clear_row(empty_grid):
    row = 5
    for col in range(empty_grid.num_cols):
        empty_grid.grid[row][col] = 3
    empty_grid.clear_row(row)
    assert all(empty_grid.grid[row][col] == 0 for col in range(empty_grid.num_cols))

def test_clear_full_rows(full_row_grid):
    rows_cleared = full_row_grid.clear_full_rows()
    assert rows_cleared == 1
    assert all(full_row_grid.grid[19][col] == 0 for col in range(full_row_grid.num_cols))
