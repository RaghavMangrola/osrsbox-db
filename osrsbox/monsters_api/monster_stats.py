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

from collections import OrderedDict
from typing import Dict


class MonsterStats:
    """This class defines the object structure and stats for an OSRS monster."""
    def __init__(self):
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

    def load_monster_stats_from_file(self, monster_data: Dict):
        """Load a MonsterDefinition object from an existing JSON file.

        param :obj:`dict` monster_data: A dictionary loaded from a JSON file.
        """
        for prop in vars(self):
            prop = prop[1:]
            setattr(self, prop, monster_data[prop])

    def construct_json(self) -> Dict:
        """Construct dictionary/JSON for exporting or printing.

        :return json_out: All class attributes stored in a dictionary
        """
        json_out: Dict = OrderedDict()
        for prop in vars(self):
            if prop.startswith("_"):
                prop = prop[1:]
                json_out[prop] = getattr(self, prop)

        return json_out
