import customtkinter as ctk

# --- BST LOGIC ---
class Node:
    def __init__(self, content: str):
        self.left: Node = None   
        self.right: Node = None
        self.content: str = content
    
class Tree:
    def __init__(self):
        self.root: Node = None
    
    def add(self, content: str, root: Node = None):
        if self.root is None:
            self.root = Node(content)
            return
        
        if root is None:
            root = self.root
        
        if content > root.content:
            if root.right is None:
                root.right = Node(content)
            else:
                self.add(content, root.right)
        else:
            if root.left is None:
                root.left = Node(content)
            else:
                self.add(content, root.left)

    def search(self, content: str, root: Node = None) -> bool:
        if root is None:
            root = self.root
            if root is None:
                return False

        if content == root.content:
            return True
        elif content < root.content and root.left:
            return self.search(content, root.left)
        elif content > root.content and root.right:
            return self.search(content, root.right)
        return False

    def remove(self, content: str):
        self.root = self._remove_node(self.root, content)

    def _remove_node(self, root: Node, content: str) -> Node:
        if root is None:
            return root

        if content < root.content:
            root.left = self._remove_node(root.left, content)
        elif content > root.content:
            root.right = self._remove_node(root.right, content)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            root.content = self._get_min_value(root.right)
            root.right = self._remove_node(root.right, root.content)

        return root

    def _get_min_value(self, root: Node) -> str:
        current = root
        while current.left is not None:
            current = current.left
        return current.content

    # Modified Traversals to return lists for the GUI
    def get_inorder(self, root: Node, result: list):
        if root:
            if root.left: self.get_inorder(root.left, result)
            result.append(root.content)
            if root.right: self.get_inorder(root.right, result)

    def get_preorder(self, root: Node, result: list):
        if root:
            result.append(root.content)
            if root.left: self.get_preorder(root.left, result)
            if root.right: self.get_preorder(root.right, result)

    def get_postorder(self, root: Node, result: list):
        if root:
            if root.left: self.get_postorder(root.left, result)
            if root.right: self.get_postorder(root.right, result)
            result.append(root.content)


# --- CUSTOM TKINTER GUI ---
class InventoryApp(ctk.CTk):
    def __init__(self, tree: Tree):
        super().__init__()

        self.tree = tree
        
        # Window setup
        self.title("BST Inventory Manager")
        self.geometry("700x500")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Grid Layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- LEFT FRAME (Controls) ---
        self.frame_left = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nsew")

        self.label_title = ctk.CTkLabel(self.frame_left, text="Inventory Controls", font=ctk.CTkFont(size=20, weight="bold"))
        self.label_title.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.entry_product = ctk.CTkEntry(self.frame_left, placeholder_text="Product Name")
        self.entry_product.grid(row=1, column=0, padx=20, pady=10)

        self.btn_add = ctk.CTkButton(self.frame_left, text="Add Product", command=self.add_product)
        self.btn_add.grid(row=2, column=0, padx=20, pady=5)

        self.btn_remove = ctk.CTkButton(self.frame_left, text="Remove Product", fg_color="#C0392B", hover_color="#922B21", command=self.remove_product)
        self.btn_remove.grid(row=3, column=0, padx=20, pady=5)

        self.btn_search = ctk.CTkButton(self.frame_left, text="Search Product", fg_color="#27AE60", hover_color="#1E8449", command=self.search_product)
        self.btn_search.grid(row=4, column=0, padx=20, pady=5)

        self.label_status = ctk.CTkLabel(self.frame_left, text="System Ready.", text_color="gray")
        self.label_status.grid(row=5, column=0, padx=20, pady=(20, 10))

        # --- RIGHT FRAME (Display) ---
        self.frame_right = ctk.CTkFrame(self)
        self.frame_right.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.frame_right.grid_rowconfigure(1, weight=1)
        self.frame_right.grid_columnconfigure((0, 1, 2), weight=1)

        self.btn_inorder = ctk.CTkButton(self.frame_right, text="In-Order (A-Z)", command=lambda: self.update_display("inorder"))
        self.btn_inorder.grid(row=0, column=0, padx=5, pady=10)

        self.btn_preorder = ctk.CTkButton(self.frame_right, text="Pre-Order", command=lambda: self.update_display("preorder"))
        self.btn_preorder.grid(row=0, column=1, padx=5, pady=10)

        self.btn_postorder = ctk.CTkButton(self.frame_right, text="Post-Order", command=lambda: self.update_display("postorder"))
        self.btn_postorder.grid(row=0, column=2, padx=5, pady=10)

        self.textbox = ctk.CTkTextbox(self.frame_right, font=ctk.CTkFont(size=14))
        self.textbox.grid(row=1, column=0, columnspan=3, padx=10, pady=(0, 10), sticky="nsew")

        # Initial display update
        self.update_display("inorder")

    # --- BUTTON CALLBACKS ---
    def add_product(self):
        product = self.entry_product.get().strip().capitalize()
        if not product:
            self.set_status("Please enter a product name.", "orange")
            return
            
        if self.tree.search(product):
            self.set_status(f"'{product}' already exists.", "orange")
        else:
            self.tree.add(product)
            self.set_status(f"'{product}' added successfully.", "green")
            self.entry_product.delete(0, 'end')
            self.update_display("inorder")

    def remove_product(self):
        product = self.entry_product.get().strip().capitalize()
        if not product:
            self.set_status("Please enter a product name.", "orange")
            return

        if self.tree.search(product):
            self.tree.remove(product)
            self.set_status(f"'{product}' removed.", "green")
            self.entry_product.delete(0, 'end')
            self.update_display("inorder")
        else:
            self.set_status(f"'{product}' not found.", "red")

    def search_product(self):
        product = self.entry_product.get().strip().capitalize()
        if not product:
            self.set_status("Please enter a product name.", "orange")
            return

        if self.tree.search(product):
            self.set_status(f"'{product}' is in stock!", "green")
        else:
            self.set_status(f"'{product}' is OUT of stock.", "red")

    def update_display(self, traversal_type: str):
        self.textbox.delete("1.0", "end")
        result_list = []

        if self.tree.root is None:
            self.textbox.insert("end", "[Inventory is empty]")
            return

        if traversal_type == "inorder":
            self.tree.get_inorder(self.tree.root, result_list)
            self.textbox.insert("end", "--- IN-ORDER TRAVERSAL (A-Z) ---\n\n")
        elif traversal_type == "preorder":
            self.tree.get_preorder(self.tree.root, result_list)
            self.textbox.insert("end", "--- PRE-ORDER TRAVERSAL ---\n\n")
        elif traversal_type == "postorder":
            self.tree.get_postorder(self.tree.root, result_list)
            self.textbox.insert("end", "--- POST-ORDER TRAVERSAL ---\n\n")

        for item in result_list:
            self.textbox.insert("end", f"📦 {item}\n")

    def set_status(self, message: str, color: str):
        self.label_status.configure(text=message, text_color=color)


if __name__ == "__main__":
    # Initialize the BST and add some dummy data
    my_tree = Tree()
    initial_products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Desk", "Headset"]
    for p in initial_products:
        my_tree.add(p)

    # Run the App
    app = InventoryApp(my_tree)
    app.mainloop()