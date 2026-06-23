# Binary Search Tree (BST) - Inventory Management System with GUI

* [🇧🇷 Versão em Português](README-PTBR.md)

This project is the final assignment for the Data Structures course. It features an interactive Product Inventory Management System built upon a **Binary Search Tree (BST)** algorithm from scratch, complete with a graphical user interface (GUI) using `CustomTkinter`.

## 📌 Project Overview
The main goal of this project is to demonstrate the practical application of a Binary Search Tree. By simulating an inventory, the BST efficiently manages product names, automatically sorting them alphabetically and ensuring optimized search and retrieval operations.

## ⚙️ Technical Deep Dive

### 1. Data Structure Implementation
The core logic resides in the `Tree` and `Node` classes, strictly following OOP principles. The system handles standard BST operations:
*   **Insertion (`add`):** Recursively traverses the tree to place new items based on alphabetical comparison.
*   **Search (`search`):** Navigates left or right branches, providing an average time complexity of **O(log n)**, making it highly efficient for inventory lookups.
*   **Deletion (`remove`):** This is the most complex algorithm implemented, gracefully handling the three classic BST deletion scenarios:
    *   *Case 1 (Leaf Node):* Simply removes the node.
    *   *Case 2 (One Child):* Bypasses the node, linking the parent directly to the child.
    *   *Case 3 (Two Children):* Finds the **In-Order Successor** (the minimum value in the right subtree), replaces the target node's data with it, and then deletes the successor.

### 2. Tree Traversals
The system allows real-time visualization of the tree using three traversal methods:
*   **In-Order (Left-Root-Right):** Outputs the inventory in a strictly sorted alphabetical order (A-Z).
*   **Pre-Order (Root-Left-Right):** Useful for structural analysis or creating a copy of the tree.
*   **Post-Order (Left-Right-Root):** Typically used for safe deletion of the entire tree structure from the bottom up.

### 3. Graphical Interface
The GUI strictly separates the visual layer (`InventoryApp`) from the business logic layer (`Tree`). It offers real-time status updates (success/error messages) and dynamically redraws the tree contents when mutations occur.

## 🚀 How to Run

**Requirements:**
*   Python 3.x
*   CustomTkinter

**Installation & Execution:**
1. Clone this repository.
2. Install the GUI library:
```bash
   pip install customtkinter
```
1. Run the application:
```bash
    python main_gui.py
```
## 🎥 Demonstration
A detailed explanation of the logic and a demonstration of the software can be found on my LinkedIn: 
[Click here to watch the demonstration video on LinkedIn](https://www.linkedin.com/posts/matheus-concesso-095870301_python-softwareengineering-datastructures-ugcPost-7475155158700797952-Hhmk/)