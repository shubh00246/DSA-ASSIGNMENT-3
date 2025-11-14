class Building:
    def __init__(self, building_id, name, location):
        self.id = building_id
        self.name = name
        self.location = location

    def __str__(self):
        return f"{self.id} - {self.name} ({self.location})"


class AVLNode:
    def __init__(self, building):
        self.building = building
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def insert(self, root, building):
        """
        Insert `building` into AVL tree rooted at `root`.
        Returns new root after insertion and rebalancing.
        """
        if not root:
            return AVLNode(building)

        if building.id < root.building.id:
            root.left = self.insert(root.left, building)
        else:
            root.right = self.insert(root.right, building)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # LL case
        if balance > 1 and building.id < root.left.building.id:
            return self.right_rotate(root)

        # RR case
        if balance < -1 and building.id > root.right.building.id:
            return self.left_rotate(root)

        # LR case
        if balance > 1 and building.id > root.left.building.id:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RL case
        if balance < -1 and building.id < root.right.building.id:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        t2 = y.left

        # perform rotation
        y.left = z
        z.right = t2

        # update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        t3 = y.right

        # perform rotation
        y.right = z
        z.left = t3

        # update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right)

    # traversal helpers (return list of string representations)
    def inorder(self, root):
        res = []
        self._inorder(root, res)
        return res

    def _inorder(self, node, res):
        if node:
            self._inorder(node.left, res)
            res.append(str(node.building))
            self._inorder(node.right, res)

    def preorder(self, root):
        res = []
        self._preorder(root, res)
        return res

    def _preorder(self, node, res):
        if node:
            res.append(str(node.building))
            self._preorder(node.left, res)
            self._preorder(node.right, res)

    def postorder(self, root):
        res = []
        self._postorder(root, res)
        return res

    def _postorder(self, node, res):
        if node:
            self._postorder(node.left, res)
            self._postorder(node.right, res)
            res.append(str(node.building))


# Optional small demo when running this file directly
if __name__ == "__main__":
    avl = AVLTree()
    root = None
    sample = [
        Building(10, "Admin Block", "Center"),
        Building(5, "Library", "North Wing"),
        Building(15, "CSE Dept", "South Wing"),
        Building(2, "Hostel A", "East"),
        Building(7, "Cafeteria", "West"),
    ]

    for b in sample:
        root = avl.insert(root, b)

    print("AVL Inorder:", avl.inorder(root))
    print("AVL Preorder:", avl.preorder(root))
    print("AVL Postorder:", avl.postorder(root))
    print("AVL Height (root):", root.height if root else 0)
