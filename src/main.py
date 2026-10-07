import environment.environment as env
from explorer.directory_list import pass_target, explore_target
from input_parser.navigate import folder_navigation

explore_target(env.root)
folder_navigation([x.name for x in pass_target(rf"{env.root}")], env.root)
explore_target(env.root)


