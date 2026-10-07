import environment.environment as env
from pathlib import Path as path

def folder_navigation(content_list: list, root: str) -> str:
    """Used for retuning path of navigation 
    
    Args:
        content_list: the content list
    """
    
    user_input = input("Enter the name of the folder or select the index : ")
    if int(user_input) == -1:
        return "break-x01238bsk032k09sda(*&^)"
    
    if user_input.isdigit():
        if path(rf"{root+"\\"+content_list[int(user_input)]}").is_dir():
            root = rf"{root+"\\"+content_list[int(user_input)]}"
            env.update_root(root)
            return root
    else:
        if rf"{root+"\\"+content_list[int(user_input)]}".is_dir():
            root = rf"{root+'\\'+user_input}"
            env.update_root(root)
            return root
    
    
        