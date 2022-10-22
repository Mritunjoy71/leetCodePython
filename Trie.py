from typing import List


class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.links = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.links:
                node.links[ch] = TrieNode()
            node = node.links[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.links:
                return False
            node = node.links[ch]
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.links:
                return False
            node = node.links[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        obj = Trie()
        for i in range(len(strs) - 1):
            # if strs[i] == '':
            #     return ''
            obj.insert(strs[i])
        # if strs[len(strs) - 1] == '':
        #     return ''
        prefix = ''
        node = obj.root
        for ch in strs[len(strs) - 1]:
            if ch in node.links and len(node.links.keys()) == 1 and node.isEnd is False:
                prefix += ch
                node = node.links[ch]
            else:
                return prefix
        return prefix


def main():
    print("Hello World!")
    # obj = Trie()
    # obj.insert(word)
    # param_2 = obj.search(word)
    # param_3 = obj.startsWith(prefix)


if __name__ == "__main__":
    main()
