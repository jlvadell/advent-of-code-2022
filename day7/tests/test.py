import unittest
from day7.src import main
from anytree import Node


class Day7TestCase(unittest.TestCase):

    def test_given_a_working_directory_and_destination__change_directory__should_update_cwd(self):
        # Given
        params = [
            ['/test', '..', '/', 'Test case: go back from /test to /'],
            ['/test/dir1', '..', '/test', 'Test case: go back from /test/dir1 to /test'],
            ['/', 'test', '/test', 'Test case: from / to /test'],
            ['/test', 'dir1', '/test/dir1', 'Test case: /test to /test/dir1'],

        ]
        for cwd, destination, expected, test_case in params:
            # When
            actual = main.change_directory(cwd, destination)
            # Then
            self.assertEqual(expected, actual, test_case)

    def test_given_terminal_output__parse_terminal_output__should_return_tree(self):
        """
        Given a terminal output function parse_terminal_output should be able to build tree and return root node
        """
        # Given
        input_file = 'data/test_input_1.txt'

        # When
        actual = main.parse_terminal_output(input_file)
        expected = Node("root", size=48381165, children=[
            Node("a", size=94853,  children=[
                Node("e", size=584)
            ]),
            Node("d", size=24933642)
        ])

        # Then
        self.assertEqual(expected.name, actual.name, 'Test case: same root name')
        self.assertEqual(expected.size, actual.size, 'Test case: same root size')
        self.assertEqual(len(expected.children), len(actual.children), 'Test case: same number of children')
        self.assertEqual(expected.children[0].size, actual.children[0].size, 'Test case: same children[0] size')


    def test_given_a_branch__add_size_to_branch__should_add_size_to_all_branch(self):
        # Given
        target_node = Node("some_directory", size=0)
        root = Node("root", size = 100, children=[
            Node("a", size=50),
            Node("things", size=0, children=[
                Node("folders", size=50, children=[target_node])
            ])
        ])

        # When
        main.add_size_to_branch(target_node, 900)

        # Then
        self.assertEqual(target_node.size, 900)
        self.assertEqual(target_node.parent.size, 950)
        self.assertEqual(root.size, 1000)

    def test_given_terminal_output__solve_part_1__should_return_solution(self):
        """
        Given a terminal output (test_input_data) function solve_part_1 should be able to find the solution
        """
        # Given
        input_file = 'data/test_input_1.txt'

        # When
        actual = main.solve_part_1(input_file)
        expected = 95437

        # Then
        self.assertEqual(expected, actual)

    def test_given_terminal_output__solve_part_2__should_return_solution(self):
        """
        Given a terminal output (test_input_data) function solve_part_2 should be able to find the solution
        """
        # Given
        input_file = 'data/test_input_1.txt'

        # When
        actual = main.solve_part_2(input_file)
        expected = 24933642

        # Then
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
