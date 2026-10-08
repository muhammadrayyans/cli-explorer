import environment.environment as env
from explorer.directory_list import pass_target, explore_target
from input_parser.navigate import folder_navigation, folder_nav_backwards

# explore_target(env.root)
# return_val = folder_navigation([x.name for x in pass_target(rf"{env.root}")], env.root)
# if return_val == "break-x01238bsk032k09sda(*&^)":
#     print("Worked")
# else: explore_target(env.root)
print(env.root)
folder_nav_backwards()
print(env.root)

