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
import glob
from typing import Dict
from typing import List
from typing import Generator

from osrsbox.items_api.item_definition import ItemDefinition


class AllItems:
    """This class handles loading of the osrsbox-db items database.

    :param input_data_file_or_directory: The osrsbox-db items folder of JSON files, or single JSON file.
    """
    def __init__(self, input_data_file_or_directory: str):
        self.all_items: List[ItemDefinition] = list()
        self.all_items_dict: Dict[int, ItemDefinition] = dict()
        self.load_all_items(input_data_file_or_directory)

    def __iter__(self) -> Generator[str, None, None]:
        """Iterate (loop) over each ItemDefinition object."""
        for item_id in self.all_items:
            yield item_id

    def __getitem__(self, id_number: int) -> ItemDefinition:
        """Return the item definition object for a loaded item.

        :param id_number: The item ID number.
        :return: The item definition object linked to a specific ID number.
        """
        return self.all_items_dict[id_number]

    def __len__(self) -> int:
        """Return the count of the total number of items.

        :return: The total number of items.
        """
        return len(self.all_items)

    def load_all_items(self, input_data_file_or_directory: str) -> None:
        """Load the items database via a JSON file, or directory of JSON files.

        :param input_data_file_or_directory: The path to the data input.
        """
        if os.path.isdir(input_data_file_or_directory):

            if input_data_file_or_directory.endswith("/"):
                path = input_data_file_or_directory + "*"
            else:
                path = os.path.join(input_data_file_or_directory, "*")

            self._load_items_from_directory(path_to_directory=path)

        elif os.path.isfile(input_data_file_or_directory):
            self._load_items_from_file(input_data_file_or_directory)

    def _load_items_from_directory(self, path_to_directory: str) -> None:
        """Load item database from a directory of JSON files (`items-json`).

        :param path_to_directory: The path to the `items-json` directory.
        """
        # Loop through every item file
        for json_file in glob.glob(path_to_directory):

            if os.path.isdir(json_file):
                continue

            with open(json_file) as input_json_file:
                temp = json.load(input_json_file)

            self._load_item(temp)

    def _load_items_from_file(self, path_to_json_file: str) -> None:
        """Load item database from a single JSON file (`items-complete.json`).

        :param path_to_json_file: The path to the `items-complete.json` file.
        """
        with open(path_to_json_file) as input_json_file:
            temp = json.load(input_json_file)

        for entry in temp:
            self._load_item(temp[entry])

    def _load_item(self, item_json: Dict) -> None:
        """Convert the `item_json` into a :class:`ItemDefinition` and store it."""
        # Load the item using the ItemDefinition class
        item_def = ItemDefinition()
        item_def.load_item_definition_from_file(item_json)

        # Add item to list
        self.all_items.append(item_def)
        self.all_items_dict[item_def.id] = item_def
