import queue
import random
import matplotlib.pyplot as plt
import networkx as nx

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def dfs_traversal(root, graph, pos, colors, level=0):
    if root is None:
        return
    print(root.val, end=" ")

    color = (random.random(), random.random(), random.random())
    colors[root.val] = color  

    graph.add_node(root.val, color=color)  
    pos[root.val] = (level, level) 

    if root.left:
        graph.add_edge(root.val, root.left.val)  
        dfs_traversal(root.left, graph, pos, colors, level=level + 1)
    if root.right:
        graph.add_edge(root.val, root.right.val)  
        dfs_traversal(root.right, graph, pos, colors, level=level + 1)

def bfs_traversal(root, graph, pos, colors):
    if root is None:
        return
    q = queue.Queue()
    q.put((root, 0))
    level = 0
    while not q.empty():
        node, level = q.get()
        print(node.val, end=" ")

        color = (random.random(), random.random(), random.random())
        colors[node.val] = color  

        graph.add_node(node.val, color=color)  
        pos[node.val] = (level, level)  

        if node.left:
            q.put((node.left, level + 1))
            graph.add_edge(node.val, node.left.val)  
        if node.right:
            q.put((node.right, level + 1))
            graph.add_edge(node.val, node.right.val)  
        level += 1

def draw_tree(root, traversal_type):
    tree = nx.DiGraph()
    pos = {}
    colors = {}

    if traversal_type == "DFS":
        dfs_traversal(root, tree, pos, colors)
    elif traversal_type == "BFS":
        bfs_traversal(root, tree, pos, colors)
    else:
        print("Invalid type (choose 'DFS' or 'BFS')")

    plt.figure(figsize=(8, 6))
    nx.draw(tree, pos, with_labels=True, node_size=1500, font_size=12, node_color=[colors[n] for n in tree.nodes()])
    plt.title(f"{traversal_type} Traversal")
    plt.show()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

draw_tree(root, "DFS")
draw_tree(root, "BFS")