from balanced_binary_search_tree import Tree
import random as rdn
from chronometer import Chronometer

if __name__ == "__main__":
    tree_control = Tree()

    # Mean to go down -> 5.5 sec

    i = 0
    with Chronometer() as t:
        while i < 100000:
            tree_control.insert_in_tree(rdn.randint(1,1000000))
            i = i + 1
    print('To insert spend {:.5f} seconds'.format(float(t)))

    """with Chronometer() as t:
        print('\nin order: ', end='')
        tree_control.in_order()
    print('To print spend {:.5f} seconds'.format(float(t)))"""

    print('\n\nRight height of tree: ', tree_control.right_tree_height())
    print('\nLeft height of tree: ', tree_control.left_tree_height())