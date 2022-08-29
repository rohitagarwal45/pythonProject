# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.children = []
#         self.parent = None
#
#     def add_child(self, child):
#         child.parent = self
#         self.children.append(child)
#
#     def level(self):
#         count = 0
#         while self.parent:
#             count += 1
#             self = self.parent
#         return count
#
#     def display_tree(self):
#         height = self.level()
#         space = ' ' * height * 2
#         pattern = space + '|__' if self.parent else ""
#         print(f"{pattern}{self.data}")
#         if len(self.children) > 0:
#             for child in self.children:
#                 # print(child.data)
#                 child.display_tree()
#
#
# def build_product_tree():
#     root = TreeNode("Electronics")
#
#     laptop = TreeNode("Laptop")
#     root.add_child(laptop)
#
#     cell_phone = TreeNode("Cellphone")
#     root.add_child(cell_phone)
#
#     television = TreeNode("Television")
#     root.add_child(television)
#
#     macbook = TreeNode("macbook")
#     laptop.add_child(macbook)
#     microsoft_surface = TreeNode("Microsoft surface")
#     laptop.add_child(microsoft_surface)
#     thinkpad = TreeNode("Thinkpad")
#     laptop.add_child(thinkpad)
#
#     iphone = TreeNode("iphone")
#     cell_phone.add_child(iphone)
#     google_pixcel = TreeNode("Google Pixel")
#     cell_phone.add_child(google_pixcel)
#     vivo = TreeNode("vivo")
#     cell_phone.add_child(vivo)
#
#     samsung = TreeNode("samsung")
#     television.add_child(samsung)
#     lg = TreeNode("LG")
#     television.add_child(lg)
#
#     return root
#
# if __name__ == '__main__':
#     root = build_product_tree()
#     root.display_tree()


# https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/7_Tree/7_tree_exercise.md

class TreeNode:
    def __init__(self, data1, data2):
        self.position = data1
        self.emp_name = data2
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def level(self):
        count = 0
        while self.parent:
            count += 1
            self = self.parent
        return count

    def display_tree(self,flag):
        height = self.level()
        space = ' ' * height * 2
        pattern = space + '|__' if self.parent else ""
        if flag == "name":
            print(f"{pattern}{self.emp_name}")
        elif flag == "position":
            print(f"{pattern}{self.position}")
        else:
            print(f"{pattern}{self.emp_name} ({self.position})")
        if len(self.children) > 0:
            for child in self.children:
                # print(child.data)
                child.display_tree(flag)

    def display_level_wise(self, level):
        height = self.level()
        space = ' ' * height
        pattern = space + "|__" if self.parent else ""
        print(f"{pattern}{self.emp_name}")
        if level > height and self.children:
            for child in self.children:
                child.display_level_wise(level)


def build_product_tree():
    root = TreeNode("CEO", "Nilupul")

    cto = TreeNode("CTO", "Chinmay")
    root.add_child(cto)

    hr_head = TreeNode("HR head", "Gels")
    root.add_child(hr_head)

    infa_head = TreeNode("Infastructure Head", "Vishwa")
    cto.add_child(infa_head)

    appl_head = TreeNode("Application Head", "Aamir")
    cto.add_child(appl_head)

    cloud_manager = TreeNode("Cloud Manager", "Dhaval")
    infa_head.add_child(cloud_manager)
    app_manager = TreeNode("Application Manger", "Abhijeet")
    infa_head.add_child(app_manager)

    recruitment_manager = TreeNode("Recruitment Manager", "Peter")
    hr_head.add_child(recruitment_manager)
    policy_manager = TreeNode("Policy Manager", "Waqar")
    hr_head.add_child(policy_manager)

    return root

if __name__ == '__main__':
    root = build_product_tree()
    # root.display_tree("name")
    # root.display_tree("position")
    # root.display_tree("both")
    root.display_level_wise(4)

