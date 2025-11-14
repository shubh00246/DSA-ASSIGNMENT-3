class Building:
    def __init__(self, building_id, name, location):
        self.id = building_id
        self.name = name
        self.location = location

    def __str__(self):
        return f"{self.id} - {self.name} ({self.location})"


class BSTNode:
    def __init__(self, building):
        self.building = building
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, building):
        self.root = self._insert(self.root, building)

    def _insert(self, node, building):
        if not node:
            return BSTNode(building)
        if building.id < node.building.id:
            node.left = self._insert(node.left, building)
        else:
            node.right = self._insert(node.right, building)
        return node

    def search(self, building_id):
        return self._search(self.root, building_id)

    def _search(self, node, building_id):
        if not node:
            return None
        if node.building.id == building_id:
            return node.building
        if building_id < node.building.id:
            return self._search(node.left, building_id)
        return self._search(node.right, building_id)

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(str(node.building))
            self._inorder(node.right, result)

    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        if node:
            result.append(str(node.building))
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(str(node.building))
