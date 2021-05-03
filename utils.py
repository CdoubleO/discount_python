from typing import Any, Callable, List


class Nameable():
    def __init__(self, name: str=''):
        pass

    def name(self) -> str:
        pass

    def set_name(self, name: str):
        pass


class Taggable():
    def __init__(self, tags: List[str]):
        pass

    def tags(self) -> List[str]:
        pass

    def has_tag(self, tag: str) -> bool:
        pass

    def has_tags(self, tags: List[str]) -> bool:
        pass



class Manager:
    def __init__(self):
        pass

    def objects(self) -> List[Any]:
        pass

    def add(self, obj: Any) -> bool:
        pass

    def remove(self, obj: Any) -> bool:
        pass

    def remove_at(self, index: int) -> bool:
        pass

    def remove_all(self):
        pass

    def find(self, prop_method: Callable, compare_to: Any) -> Any:
        pass

    def at(self, idx: int) -> Any:
        pass

    def random(self) -> Any:
        pass


class ManagerKey(Manager):
    def __init__(self, obj_get_key_method: Callable=None):
        pass

    def get(self, key: Any) -> Any:
        pass

    def __getitem__(self, key: Any) -> Any:
        pass
