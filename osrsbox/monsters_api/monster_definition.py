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


class MonsterDefinition:
    """This class defines the object structure and properties for an OSRS monster.

    The MonsterDefinition class is the object that retains all properties and stats
    for one specific monster. Every monster has the properties defined in this class,
    as well as the stats.
    """

    def __init__(self):
        self.id = None
        self.name = None
        self.wiki_name = None
        self.members = None
        self.release_date = None
        self.combat_level = None
        self.hit_points = None
        self.max_hit = None
        self.attack_type = None
        self.attack_speed = None
        self.aggressive = None
        self.poisonous = None
        self.immune_poison = None
        self.immune_venom = None
        self.weakness = None
        self.slayer_level = None
        self.slayer_xp = None
        self.examine = None
        self.url = None
        self.attack_level = None
        self.strength_level = None
        self.defence_level = None
        self.magic_level = None
        self.ranged_level = None
        self.attack_stab = None
        self.attack_slash = None
        self.attack_crush = None
        self.attack_magic = None
        self.attack_ranged = None
        self.defence_stab = None
        self.defence_slash = None
        self.defence_crush = None
        self.defence_magic = None
        self.defence_ranged = None
        self.attack_accuracy = None
        self.melee_strength = None
        self.ranged_strength = None
        self.magic_damage = None

    @property
    def id(self):
        """Get the ID number of the monster."""
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        """Get the name of the monster."""
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def wiki_name(self):
        """Get the OSRS wiki name of the monster."""
        return self._wiki_name

    @wiki_name.setter
    def wiki_name(self, value):
        self._wiki_name = value

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
    def attack_type(self):
        """Get the attack type of the monster."""
        return self._attack_type

    @attack_type.setter
    def attack_type(self, value):
        self._attack_type = value

    @property
    def attack_speed(self):
        """Get the attack speed of the monster."""
        return self._attack_speed

    @attack_speed.setter
    def attack_speed(self, value):
        self._attack_speed = value

    @property
    def aggressive(self):
        """Get if the monster is aggressive, or not."""
        return self._aggressive

    @aggressive.setter
    def aggressive(self, value):
        self._aggressive = value

    @property
    def poisonous(self):
        """Get if the monster poisons, or not."""
        return self._poisonous

    @poisonous.setter
    def poisonous(self, value):
        self._poisonous = value

    @property
    def immune_poison(self):
        """Get if the monster is immune to poison, or not."""
        return self._immune_poison

    @immune_poison.setter
    def immune_poison(self, value):
        self._immune_poison = value

    @property
    def immune_venom(self):
        """Get if the monster is immune to venon, or not."""
        return self._immune_venom

    @immune_venom.setter
    def immune_venom(self, value):
        self._immune_venom = value

    @property
    def weakness(self):
        """Get a list of weaknesses of the monster."""
        return self._weakness

    @weakness.setter
    def weakness(self, value):
        self._weakness = value

    @property
    def slayer_level(self):
        """Get the slayer level of the monster."""
        return self._slayer_level

    @slayer_level.setter
    def slayer_level(self, value):
        self._slayer_level = value

    @property
    def slayer_xp(self):
        """Get the slayer xp of the monster."""
        return self._slayer_xp

    @slayer_xp.setter
    def slayer_xp(self, value):
        self._slayer_xp = value

    @property
    def examine(self):
        """Get the examine text of the monster."""
        return self._examine

    @examine.setter
    def examine(self, value):
        self._examine = value

    @property
    def url(self):
        """Get the OSRS Wiki URL of the monster."""
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    @property
    def attack_level(self):
        """Get the attack level of the monster."""
        return self._attack_level

    @attack_level.setter
    def attack_level(self, value):
        self._attack_level = value

    @property
    def strength_level(self):
        """Get the strength level of the monster."""
        return self._strength_level

    @strength_level.setter
    def strength_level(self, value):
        self._strength_level = value

    @property
    def defence_level(self):
        """Get the defence level of the monster."""
        return self._defence_level

    @defence_level.setter
    def defence_level(self, value):
        self._defence_level = value

    @property
    def magic_level(self):
        """Get the magic level of the monster."""
        return self._magic_level

    @magic_level.setter
    def magic_level(self, value):
        self._magic_level = value

    @property
    def ranged_level(self):
        """Get the ranged level of the monster."""
        return self._ranged_level

    @ranged_level.setter
    def ranged_level(self, value):
        self._ranged_level = value

    @property
    def attack_stab(self):
        """Get the stab attack bonus of the monster."""
        return self._attack_stab

    @attack_stab.setter
    def attack_stab(self, value):
        self._attack_stab = value

    @property
    def attack_slash(self):
        """Get the slash attack bonus of the monster."""
        return self._attack_slash

    @attack_slash.setter
    def attack_slash(self, value):
        self._attack_slash = value

    @property
    def attack_crush(self):
        """Get the crush attack bonus of the monster."""
        return self._attack_crush

    @attack_crush.setter
    def attack_crush(self, value):
        self._attack_crush = value

    @property
    def attack_magic(self):
        """Get the magic attack bonus of the monster."""
        return self._attack_magic

    @attack_magic.setter
    def attack_magic(self, value):
        self._attack_magic = value

    @property
    def attack_ranged(self):
        """Get the ranged attack bonus of the monster."""
        return self._attack_ranged

    @attack_ranged.setter
    def attack_ranged(self, value):
        self._attack_ranged = value

    @property
    def defence_stab(self):
        """Get the stab defence bonus of the monster."""
        return self._defence_stab

    @defence_stab.setter
    def defence_stab(self, value):
        self._defence_stab = value

    @property
    def defence_slash(self):
        """Get the slash defence bonus of the monster."""
        return self._defence_slash

    @defence_slash.setter
    def defence_slash(self, value):
        self._defence_slash = value

    @property
    def defence_crush(self):
        """Get the crush defence bonus of the monster."""
        return self._defence_crush

    @defence_crush.setter
    def defence_crush(self, value):
        self._defence_crush = value

    @property
    def defence_magic(self):
        """Get the magic defence bonus of the monster."""
        return self._defence_magic

    @defence_magic.setter
    def defence_magic(self, value):
        self._defence_magic = value

    @property
    def defence_ranged(self):
        """Get the ranged defence bonus of the monster."""
        return self._defence_ranged

    @defence_ranged.setter
    def defence_ranged(self, value):
        self._defence_ranged = value

    @property
    def attack_accuracy(self):
        """Get the attack accuracy bonus of the monster."""
        return self._attack_accuracy

    @attack_accuracy.setter
    def attack_accuracy(self, value):
        self._attack_accuracy = value

    @property
    def melee_strength(self):
        """Get the melee strength bonus of the monster."""
        return self._melee_strength

    @melee_strength.setter
    def melee_strength(self, value):
        self._melee_strength = value

    @property
    def ranged_strength(self):
        """Get the ranged strength bonus of the monster."""
        return self._ranged_strength

    @ranged_strength.setter
    def ranged_strength(self, value):
        self._ranged_strength = value

    @property
    def magic_damage(self):
        """Get the magic damage bonus of the monster."""
        return self._magic_damage

    @magic_damage.setter
    def magic_damage(self, value):
        self._magic_damage = value

    def load_monster_definition_from_file(self, monster_data: Dict):
        """Load a Monster object from an existing JSON file.

        :param monster_data: A dictionary loaded from a JSON file.
        """
        for prop in vars(self):
            prop = prop[1:]
            setattr(self, prop, monster_data[prop])

    def construct_json(self) -> Dict:
        """Construct dictionary/JSON for exporting or printing.

        :return json_out: All class attributes stored in a dictionary.
        """
        json_out: Dict = OrderedDict()
        for prop in vars(self):
            if prop.startswith("_"):
                prop = prop[1:]
                json_out[prop] = getattr(self, prop)

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
