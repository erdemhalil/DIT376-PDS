# Group A5 5
# Group members: Erdem Halil

from typing import Optional, Dict, List

class Trie():
    def __init__(self) -> None:
        self.value: Optional[str] = None
        self.endOfWord: bool = False
        self.active: bool = True
        self.children: Dict[str, Trie] = {}

    def insert(self, path: List[str], val: str) -> None:
        node = self
        for part in path:
            if part not in node.children:
                node.children[part] = Trie()  # Create a new node if the part doesn't exist
            node = node.children[part]  # Move to the next node
        node.value = val
        node.endOfWord = True

    def fetch(self, path: List[str]) -> Optional[str]:
        node = self
        for part in path:
            if part not in node.children:
                return None
            node = node.children[part]  # Move to the next node
        
        if node.endOfWord:
            return node.value  # Return the date if the file path is found, else return None
        else:
            return None

    def delete(self, path: List[str]) -> Optional[str]:
        node = self
        nodes_to_delete = []    # Can also make use of stack to eliminate reversing later on?
        for part in path:
            if part not in node.children:
                return None
            nodes_to_delete.append((part, node))
            node = node.children[part]  # Move to the next node

        if not node.endOfWord:
            return None

        deleted_value = node.value  # Store the value of the node to be deleted
        node.endOfWord = False  # Mark the last node as not the end of a word

        # Traverse back and remove unnecessary nodes
        for part, current_node in reversed(nodes_to_delete):
            if not current_node.children[part].endOfWord and len(current_node.children[part].children) == 0:
                del current_node.children[part]  # Remove the node if it's safe to do so
            else:
                break  # Stop when we reach a node with other children or active values
        return deleted_value

# Tests
print("------------------")
print("Tests #1")
print("------------------")
t = Trie()
for word, val in zip(["alphabet", "beta", "gamma"], [1, 2, 3]):
    t.insert(word, val)

print(f'Should output None -> {t.fetch("alpha")}') # None
print(f'Should output 2 -> {t.fetch ("beta")}') # 2
print(f'Should output 1 -> {t.fetch("alphabet")}') # 1
print(f'Should output None -> {t.fetch("Gamma")}') # None
print(f'Should output 3 -> {t.fetch("gamma")}') # 3

print("------------------")
print("Tests #2")
print("------------------")
t = Trie()
t.insert("alpha", 10)
a = t.delete("alpha")
print(f'Should output 10 -> {a}')  # a = 10
print(f'Should output None -> {t.fetch("alpha")}')  # None

t.insert("alpha", 10)
t.insert("alphabet", 22)
a = t.delete("alpha")
print(f'Should output 10 -> {a}')  # a = 10
print(f'Should output 22 -> {t.fetch("alphabet")}')  # 22
print(f'Should output None -> {t.fetch("alpha")}')  # None

print("------------------")
print("Tests #3")
print("------------------")
t = Trie()
path1 = ["/", "home", "/", "user", "/", "folder1", "/", "file1"]
path2 = ["/", "home", "/", "user", "/", "folder1", "/", "file2"]
path3 = ["/", "home", "/", "user", "/", "folder2", "/", "file3"]

t.insert(path1, "2022-09-22")
t.insert(path2, "2023-01-19")
t.insert(path3, "2021-04-01")

print(f'Should output 2022-09-22 -> {t.fetch(path1)}')  # 2022-09-22
print(f'Should output 2022-09-22 -> {t.delete(path1)}')  # 2022-09-22
print(f'Should output 2022-01-19 -> {t.fetch(path2)}')  # 2023-01-19
print(f'Should output None -> {t.fetch(path1)}')  # None
print(f'Should output None -> {t.fetch(["/", "home"])}')  # None
print(f'Should output 2021-04-01 -> {t.fetch(path3)}')  # 2021-04-01