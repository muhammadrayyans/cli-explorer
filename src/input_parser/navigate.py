import environment.environment as env

def folder_navigation(content_list: list, root: str) -> str:
    """Used for retuning path of navigation 
    
    Args:
        content_list: the content list
    """
    user_input = input("Enter the name of the folder or select the index : ")
    if user_input.isdigit() and rf"{root+"\\"+content_list[int(user_input)]}".is_dir():
        root = rf"{root+"\\"+content_list[int(user_input)]}"
        env.update_root(root)
        return root
    else:
        if rf"{root+"\\"+content_list[int(user_input)]}".is_dir():
            root = rf"{root+'\\'+user_input}"
            env.update_root(root)
            return root
    
    
        