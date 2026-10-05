from pathlib import Path as path

def explore_target(target: str) -> str:
    """A folder inspecting and content printing function
    
    Args:
        Target : The directory path or name to be inspected
    """
    

    target_folder = path(target)
    counter = 0
    for index, files in enumerate(target_folder.iterdir()):
        
        if files.is_file():
            print(f"{index}. 📝 "+files.name, end="   ")
        elif files.is_dir():
            print(f"{index}. 📁 "+files.name, end="   ")
        else:
            print(index+" "+files.name, end="  ")
        
        if counter == 4:
            print("\n")
            counter = 0
            
        counter+=1

def pass_target(target: str) -> list:
    """A folder content passing function
    
    Args:
        Target : The directory path or name to be inspected
    """
    

    target_folder = path(target)
    return target_folder.iterdir()