class ExpNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class ExpressionTree:
    def build_from_postfix(self, expression):
        """
        Build expression tree from postfix expression.
        Example postfix: "23+5*"
        """
        stack = []

        for char in expression:
            if char.isdigit():
                stack.append(ExpNode(char))
            else:
                node = ExpNode(char)
                node.right = stack.pop()
                node.left = stack.pop()
                stack.append(node)

        return stack[-1]

    def evaluate(self, root):
        """
        Evaluate recursively.
        """
        if not root.left and not root.right:
            return int(root.value)

        left = self.evaluate(root.left)
        right = self.evaluate(root.right)

        return eval(f"{left}{root.value}{right}")

    def inorder(self, root):
        if not root:
            return ""
        return f"({self.inorder(root.left)} {root.value} {self.inorder(root.right)})"


# Optional demonstration
if __name__ == "__main__":
    expr = "23+5*"  # (2 + 3) * 5
    et = ExpressionTree()
    root = et.build_from_postfix(expr)

    print("Inorder Expression:", et.inorder(root))
    print("Evaluation:", et.evaluate(root))
