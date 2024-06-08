from abc import ABC, abstractmethod
from typing import List, Iterator

class Component(ABC):
    def __init__(self, style, icon):
        self.style = style
        self.icon = icon

    @abstractmethod
    def draw(self, visitor, indent="", is_last=True, first_call=False):
        pass

    @abstractmethod
    def __iter__(self) -> Iterator:
        pass

class Leaf(Component):
    def __init__(self, name, style, icon):
        super().__init__(style, icon)
        self.name = name

    def draw(self, visitor, indent="", is_last=True, first_call=False):
        visitor.visit_leaf(self, indent, is_last)

    def __iter__(self) -> Iterator:
        yield self

class Container(Component):
    def __init__(self, name, level, style, icon):
        super().__init__(style, icon)
        self.name = name
        self.level = level
        self.children: List[Component] = []

    def add(self, component: Component):
        self.children.append(component)

    def remove(self, component: Component):
        self.children.remove(component)

    def draw(self, visitor, indent="", is_last=True, first_call=True):
        visitor.visit_container(self, indent, is_last, first_call)
        indent += "    " if is_last else "|   "
        for i, child in enumerate(self.children):
            is_last_child = i == len(self.children) - 1
            child.draw(visitor, indent, is_last_child, first_call=False)

    def __iter__(self) -> Iterator:
        yield self
        for child in self.children:
            yield from child
