from pathlib import Path as path

def explore_target(target: str) -> str:
    """A folder inspecting and content printing function
    
    Args:
        Target : The directory path or name to be inspected
    """
    
    target_folder = path(target)
    counter = 0
    if target_folder.is_dir():
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
        else: print(target_folder.name)

def pass_target(target: str) -> list:
    """A folder content passing function
    
    Args:
        Target : The directory path or name to be inspected
    """
    

    target_folder = path(target)
    if target_folder.is_dir():
        return target_folder.iterdir()
    else:
        return [target_folder.name]