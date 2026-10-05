from environment.environment import update_root

def folder_navigation(content_list: list, root: str) -> str:
    """Used for retuning path of navigation 
    
    Args:
        content_list: List of items in current folder
    """
    user_input = input("Enter the name of the folder or select the index : ")
    if user_input.isdigit():
        print(f"old root = {root}")
        root = rf"{root+"/"+content_list[int(user_input)]}"
        print(f"new root = {root}")
        update_root(root)
        return root
    else:
        root = rf"{root+"/"+user_input}"
        update_root(root)
        return root
    
    
        