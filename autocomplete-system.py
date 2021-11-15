class Node:
    def __init__(self, val = None, children = None, leaf = True):
        if not children: children = [None] * 27
        self.val = val
        self.children = children
        self.leaf = leaf

def autocomplete(s, strs_set):
    if len(s) == 0: return strs_set

    solution = []
    root = Node()

    def trie_insert(query, i, node):
        if i >= len(query):
            node.leaf = False
            node.children[26] = Node('')
            return
        child_index = ord(query[i]) - ord('a')
        if node.children[child_index]:
            trie_insert(query, i + 1, node.children[child_index])
        else:
            node.children[child_index] = Node(query[i])
            node.leaf = False
            trie_insert(query, i + 1, node.children[child_index])

    for query_str in strs_set:
        trie_insert(query_str, 0, root)

    def trie_dfs(prefix, i, node, curr_prefix):
        if node.leaf:
            if i >= len(prefix):
                solution.append(curr_prefix)
            return

        if i == len(prefix):
            for child in node.children:
                if child:
                    trie_dfs(prefix, i, child, curr_prefix + child.val)
            return

        child_index = ord(prefix[i]) - ord('a')
        child = node.children[child_index]
        if child:
                trie_dfs(prefix, i + 1, child, curr_prefix + child.val)

    trie_dfs(s, 0, root, '')
    return solution

assert str(sorted(autocomplete('de', ['dog', 'deer', 'deal']))) == str(sorted(['deer', 'deal']))
assert str(sorted(autocomplete('a', ['a', 'ab', 'abc']))) == str(sorted(['a', 'ab', 'abc']))
