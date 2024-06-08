from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit_leaf(self, leaf, indent, is_last):
        pass

    @abstractmethod
    def visit_container(self, container, indent, is_last, first_call):
        pass

class ConcreteVisitor(Visitor):
    def visit_leaf(self, leaf, indent, is_last):
        icon = ''
        if leaf.icon == 'poker-face':
            icon = '♣'
        elif leaf.icon == 'star':
            icon = '✩'

        if leaf.style == 'tree':
            print(f"{indent}{'└─ ' if is_last else '├─ '}{icon} {leaf.name}")
        elif leaf.style == 'rectangle':
            connector = '└─ ' if is_last else '├─ '
            print(f"{indent}{connector}{icon} {leaf.name} {'─' * (30 - len(indent) - len(leaf.name) - len(connector) - 2)}┤" if not is_last else f"{indent}{connector}{icon} {leaf.name} {'─' * (30 - len(indent) - len(leaf.name) - len(connector) - 2)}┘")

    def visit_container(self, container, indent, is_last, first_call):
        icon = ' '
        if container.icon == 'poker-face':
            icon = '♠' 
        elif container.icon == 'star':
            icon = '✪'

        if container.style == 'tree':
            print(f"{indent}{'└─ ' if is_last else '├─ '}{icon} {container.name}")
            indent += "    " if is_last else "|   "
        elif container.style == 'rectangle':
            if first_call:
                print(f"{indent}┌─ {icon} {container.name} {'─' * (27 - len(indent) - len(container.name) - 2)}┐")
            else:
                connector = '└──' if is_last else '├─ '
                print(f"{indent}{connector}{icon} {container.name} {'─' * (30 - len(indent) - len(container.name) - len(connector) - 2)}┤" if not is_last else f"{indent}{connector}{icon} {container.name} {'─' * (30 - len(indent) - len(container.name) - len(connector) - 2)}┘")
            if not first_call:
                indent += "────" if is_last else "└── "
            else:
                indent += "└───"
