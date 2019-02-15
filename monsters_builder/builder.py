"""
Author:  PH01L
Email:   phoil@osrsbox.com
Website: https://www.osrsbox.com

Copyright (c) 2019, PH01L

###############################################################################
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################
"""

import os
import json

from monsters_builder import monster_builder


if __name__ == "__main__":
    # Delete old log file
    if os.path.exists("builder.log"):
        os.remove("builder.log")

    # # Load the current database contents
    # items_complete_path = os.path.join("..", "docs", "items-complete.json")
    # with open(items_complete_path) as f:
    #     current_db = json.load(f)

    # Set data input directories
    extraction_path_wiki = os.path.join("..", "extraction_tools_wiki", "")
    extraction_path_other = os.path.join("..", "extraction_tools_other", "")

    # Load the wiki text file
    with open(extraction_path_wiki + "extract_page_text_monsters.json") as wiki_text_file:
        wiki_text = json.load(wiki_text_file)

    # Start processing every item!
    for monster_name in wiki_text:
        json_data = wiki_text[monster_name]
        # Initialize the BuildItem class
        builder = monster_builder.BuildMonster(monster_name,
                                               json_data)
        # Start the build item population function
        builder.find_monster()
        # builder.populate()
