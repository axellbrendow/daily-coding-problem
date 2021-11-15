'''
0 dir
1 \tsubdir1
2 \t\tfile1.ext // When I’m at this node, I need to know dir/subdir1/file1.ext
2 \t\tsubsubdir1  // While I have children on the same level
3 \t\t\tsubsubdir1 // Backtrack if number of \t’s of current element is greater or equal
1 \tsubdir2 <--
2 \t\tsubsubdir2
3 \t\t\tfile2.ext
'''

def get_longest_path_to_a_file(file_sys): # "dir\n\tleet.txt"
    tree_nodes = file_sys.split('\n')  # ["dir", "\tleet.txt"]
    tab_counts = [path.count('\t') for path in tree_nodes]  # [0, 1]
    pos = 0
    def dfs(prev_pos, path):  # prev_pos = 0, path = "dir"
        nonlocal pos
        if pos >= len(tree_nodes): return 0
        if tab_counts[pos] <= tab_counts[prev_pos]: return 0
        max_len = 0
        while pos < len(tab_counts) and tab_counts[pos] > tab_counts[prev_pos]:
            node_name = tree_nodes[pos][tab_counts[pos]:]
            if '.' in node_name:
                file_path = f'{path}/{node_name}'  # dir/leet.txt
                max_len = max(max_len, len(file_path))  # 12
                pos += 1
            else:
                pos += 1
                max_len = max(max_len, dfs(pos - 1, f'{path}/{node_name}'))
        return max_len

    root_max_len = 0
    while pos < len(tab_counts) and tab_counts[pos] == 0:
        node_name = tree_nodes[pos][tab_counts[pos]:]
        if '.' in node_name:
            root_max_len = max(root_max_len, len(node_name))
            pos += 1
        else:
            pos += 1
            root_max_len = max(root_max_len, dfs(pos - 1, node_name))
    return root_max_len

assert get_longest_path_to_a_file("dir") == 0
assert get_longest_path_to_a_file("dir\n\tleet.txt") == 12
assert get_longest_path_to_a_file("dir\n\tdirdir1\n\tleet.txt") == 12
assert get_longest_path_to_a_file("dir\n\tdirdir1\n\t\tleet.txt") == 20
assert get_longest_path_to_a_file("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext") == 32
assert get_longest_path_to_a_file("file.txt") == 8
assert get_longest_path_to_a_file("file.txt\nfile2.txt") == 9
assert get_longest_path_to_a_file("file.txt\nfile2.txt\n1234567890") == 9
assert get_longest_path_to_a_file("file.txt\nfile2.txt\n1234567890\n\tabcd.txt") == 19
