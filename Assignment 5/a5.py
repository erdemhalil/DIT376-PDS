from typing import Optional, Dict

class Trie():
    def __init__(self) -> None:
        self.value: Optional[Value] = None
        self.endOfWord: bool = False
        self.active: bool = True
        self.children: Dict[Key, Trie] = {}
    
    def insert(self, path: str, val: int) -> None:
        print("TODO")
    
    def fetch(self, path: str) -> Optional[int]:
        print("TODO")
    
    def delete(self, path: str) -> Optional[int]:
        print("TODO")
