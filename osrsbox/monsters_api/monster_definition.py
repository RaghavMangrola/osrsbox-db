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
from collections import OrderedDict
from typing import Dict

from osrsbox.monsters_api.monster_stats import MonsterStats


class MonsterDefinition:
    """This class defines the object structure and properties for an OSRS monster.

    The MonsterDefinition class is the object that retains all properties and stats
    for one specific monster. Every monster has the properties defined in this class,
    as well as the stats contained in the MonstersStats class.
    """

    def __init__(self):
        self.monster_id = None
        self.name = None
        self.members = None
        self.release_date = None
        self.combat_level = None
        self.examine = None
        self.hit_points = None
        self.max_hit = None
        self.aggressive = None
        self.poison = None
        self.weakness = None
        self.attack_type = None
        self.attack_style = None
        self.url = None

    @property
    def monster_id(self):
        """Get the ID number of the monster."""
        return self._monster_id

    @monster_id.setter
    def monster_id(self, value):
        self._monster_id = value

    @property
    def name(self):
        """Get the name of the monster."""
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def members(self):
        """Get if the monster is members only, or not."""
        return self._members

    @members.setter
    def members(self, value):
        self._members = value

    @property
    def release_date(self):
        """Get the release date of the monster."""
        return self._release_date

    @release_date.setter
    def release_date(self, value):
        self._release_date = value

    @property
    def combat_level(self):
        """Get the combat level of the monster."""
        return self._combat_level

    @combat_level.setter
    def combat_level(self, value):
        self._combat_level = value

    @property
    def examine(self):
        """Get the examine text of the monster."""
        return self._examine

    @examine.setter
    def examine(self, value):
        self._examine = value

    @property
    def hit_points(self):
        """Get the hit points of the monster."""
        return self._hit_points

    @hit_points.setter
    def hit_points(self, value):
        self._hit_points = value

    @property
    def max_hit(self):
        """Get the max hit of the monster."""
        return self._max_hit

    @max_hit.setter
    def max_hit(self, value):
        self._max_hit = value

    @property
    def aggressive(self):
        """Get if the monster is aggressive, or not."""
        return self._aggressive

    @aggressive.setter
    def aggressive(self, value):
        self._aggressive = value

    @property
    def poison(self):
        """Get if the monster poisons, or not."""
        return self._poison

    @poison.setter
    def poison(self, value):
        self._poison = value

    @property
    def weakness(self):
        """Get a list of weaknesses of the monster."""
        return self._weakness

    @weakness.setter
    def weakness(self, value):
        self._weakness = value

    @property
    def attack_type(self):
        """Get the attack type of the monster."""
        return self._attack_type

    @attack_type.setter
    def attack_type(self, value):
        self._attack_type = value

    @property
    def attack_style(self):
        """Get the attack style of the monster."""
        return self._attack_style

    @attack_style.setter
    def attack_style(self, value):
        self._attack_style = value

    @property
    def url(self):
        """Get the OSRS Wiki URL of the monster."""
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    def load_monster_definition_from_file(self, monster_data: Dict):
        """Load a Monster object from an existing JSON file.

        :param monster_data: A dictionary loaded from a JSON file.
        """
        for prop in vars(self):
            prop = prop[1:]
            setattr(self, prop, monster_data[prop])

        # Initialize an empty MonsterStats object
        self.monster_stats: object = MonsterStats()

        # Populate monster stats
        self.monster_stats.load_monster_stats_from_file(monster_data["stats"])

    def construct_json(self) -> Dict:
        """Construct dictionary/JSON for exporting or printing.

        :return json_out: All class attributes stored in a dictionary.
        """
        json_out: Dict = OrderedDict()
        for prop in vars(self):
            if prop.startswith("_"):
                prop = prop[1:]
                json_out[prop] = getattr(self, prop)

        json_out["stats"] = self.monster_stats.construct_json()

        return json_out

    def export_json(self, pretty: bool, export_path: str):
        """Output monster to JSON file.

        :param pretty: Toggles pretty (indented) JSON output.
        :param export_path: The folder location to save the JSON output to.
        """
        json_out = self.construct_json()
        out_file_name = str(self.id) + ".json"
        out_file_path = os.path.join(export_path, out_file_name)
        with open(out_file_path, "w", newline="\n") as out_file:
            if pretty:
                json.dump(json_out, out_file, indent=4)
            else:
                json.dump(json_out, out_file)
