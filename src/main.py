from environment.environment import root
from explorer.directory_list import pass_target, explore_target
from input_parser.navigate import folder_navigation

explore_target(root)
folder_navigation([x.name for x in pass_target(rf"{root}")], root)
explore_target(root)


