from Part1_Trees.bst import BinarySearchTree, Building
from Part1_Trees.avl import AVLTree
from Part2_Graphs.graph_matrix import GraphMatrix
from Part2_Graphs.graph_list import GraphList
from Part2_Graphs.bfs_dfs import BFS_DFS
from Part2_Graphs.dijkstra import Dijkstra
from Part2_Graphs.kruskal import Kruskal
from ExpressionTree.expression_tree import ExpressionTree


# ---------------- MAIN DRIVER PROGRAM ---------------- #

if __name__ == "__main__":

    print("\n=== PART 1: TREE IMPLEMENTATION ===\n")

    bst = BinarySearchTree()
    avl = AVLTree()
    avl_root = None

    # Sample Building Data
    buildings = [
        Building(10, "Admin Block", "Center Campus"),
        Building(5, "Library", "North Wing"),
        Building(15, "CSE Department", "South Wing"),
        Building(2, "Hostel A", "East Side"),
        Building(7, "Cafeteria", "West Side"),
    ]

    # Insert into BST & AVL
    for b in buildings:
        bst.insert(b)
        avl_root = avl.insert(avl_root, b)

    # --- BST Traversals ---
    print("BST Inorder:", bst.inorder())
    print("BST Preorder:", bst.preorder())
    print("BST Postorder:", bst.postorder())

    # AVL Height comparison
    print("\nHeight of AVL Tree (Balanced):", avl_root.height)

    print("\n=== PART 2: GRAPH IMPLEMENTATION ===\n")

    # GRAPH MATRIX DEMO
    print("Adjacency Matrix Representation:\n")
    matrix_graph = GraphMatrix(5)
    matrix_graph.add_edge(0, 1, 4)
    matrix_graph.add_edge(0, 2, 2)
    matrix_graph.add_edge(1, 3, 5)
    matrix_graph.add_edge(2, 3, 8)
    matrix_graph.add_edge(3, 4, 6)

    for row in matrix_graph.display():
        print(row)

    # GRAPH LIST DEMO
    list_graph = GraphList(5)
    list_graph.add_edge(0, 1, 4)
    list_graph.add_edge(0, 2, 2)
    list_graph.add_edge(1, 3, 5)
    list_graph.add_edge(2, 3, 8)
    list_graph.add_edge(3, 4, 6)

    print("\nAdjacency List Representation:")
    print(list_graph.display())

    # BFS & DFS
    bfs_dfs = BFS_DFS(list_graph.display())
    print("\nBFS from 0:", bfs_dfs.bfs(0))
    print("DFS from 0:", bfs_dfs.dfs(0))

    # DIJKSTRA
    dijkstra_obj = Dijkstra(list_graph.display())
    shortest_paths = dijkstra_obj.shortest_path(0)
    print("\nDijkstra Shortest Paths from 0:", shortest_paths)

    # KRUSKAL
    kruskal_obj = Kruskal(list_graph.display())
    mst = kruskal_obj.minimum_spanning_tree()
    print("\nKruskal Minimum Spanning Tree:", mst)

    print("\n=== PART 3: EXPRESSION TREE (Energy Bill Example) ===\n")

    postfix_expr = "23+5*"  # (2 + 3) * 5
    et = ExpressionTree()
    root_expr = et.build_from_postfix(postfix_expr)

    print("Inorder Expression:", et.inorder(root_expr))
    print("Evaluation Result:", et.evaluate(root_expr))

    print("\n=== END OF PROGRAM ===")
