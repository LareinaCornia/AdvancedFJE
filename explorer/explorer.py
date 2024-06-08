import json
from .components import Container, Leaf
from .visitor import ConcreteVisitor

class FunnyJsonExplorer:
    def __init__(self, style, icon):
        self.style = style
        self.icon = icon
        self.root = None

    def _load(self, json_data):
        def build_component(data):
            icon = data.get('icon', f"default_{self.icon}")
            name = data.get('name', 'Unnamed')
            level = data.get('level', 0)
            if 'children' in data:
                container = Container(name, level, self.style, self.icon)
                for child_data in data['children']:
                    container.add(build_component(child_data))
                return container
            else:
                return Leaf(name, self.style, self.icon)

        parsed_data = json.loads(json_data)
        self.root = build_component(parsed_data)

    def show(self):
        if self.root:
            print(f"Showing JSON with style {self.style} and icon family {self.icon}")
            visitor = ConcreteVisitor()
            self.root.draw(visitor)
        else:
            print("No data loaded.")
