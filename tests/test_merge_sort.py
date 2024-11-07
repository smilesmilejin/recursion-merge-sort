from activity.merge_sort import merge_sort

def test_merge_sort_sorts_data():
    # arrange
    data = [5, 3, 2, 6, 4, 7, 1, 8]

    # act
    sorted_data = merge_sort(data)

    # assert
    assert sorted_data == [1, 2, 3, 4, 5, 6, 7, 8]

def test_merge_sort_sorts_empty_data():
    # arrange
    data = []

    # act
    sorted_data = merge_sort(data)

    # assert
    assert sorted_data == []

def test_merge_sort_sorts_single_data():
    # arrange
    data = [5]

    # act
    sorted_data = merge_sort(data)

    # assert
    assert sorted_data == [5]
