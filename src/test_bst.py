# coding=utf-8


def test_node_class():
    """Init node."""
    from bst import Node
    node = Node(5)
    assert node.value == 5
    assert node.right is None
    assert node.left is None
    assert node.parent is None


def test_insert():
    """Test if value inserted into the tree."""
    from bst import Bst
    new_bst = Bst()
    new_bst.insert(3)
    assert new_bst.head.value == 3


def test_insert_two_values():
    """Test insert works for two values."""
    from bst import Bst
    new_bst = Bst()
    new_bst.insert(3)
    new_bst.insert(4)
    assert new_bst.head.value == 3
    assert new_bst.head.right.value == 4
    assert new_bst.head.left is None


def test_insert_three_values():
    """Test three values."""
    from bst import Bst
    new_bst = Bst()
    new_bst.insert(3)
    new_bst.insert(5)
    new_bst.insert(4)
    assert new_bst.head.value == 3
    assert new_bst.head.right.value == 5
    assert new_bst.head.right.left.value == 4


def test_insert_value_already_exists():
    """Test if value exists it is ignored."""
    from bst import Bst
    new_bst = Bst()
    new_bst.insert(3)
    new_bst.insert(3)
    assert new_bst.head.right is None
    assert new_bst.head.left is None
    assert new_bst.head.value == 3


def test_contain_true():
    """Test if value in list return True."""
    from bst import Bst
    new_bst = Bst()
    new_bst.insert(3)
    assert new_bst.contains(3) is True


def test_contain_false():
    """Test if value in list return False."""
    from bst import Bst
    new_bst = Bst()
    new_bst.insert(3)
    assert new_bst.contains(4) is False