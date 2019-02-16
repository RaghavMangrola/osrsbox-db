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

import logging
import mwparserfromhell

from osrsbox.monsters_api.monster_definition import MonsterDefinition
from monsters_builder import infobox_cleaner


class BuildMonster:
    def __init__(self, monster_name, json_data, version_number):
        # Input monster name
        self.monster_name = monster_name
        # Input JSON file (wiki text)
        self.json_data = json_data
        # Set infobox version number
        self.version_number = version_number

        # For this monster, initialize the required objects
        self.monsterDefinition = MonsterDefinition()

        # Setup logging
        logging.basicConfig(filename="builder.log",
                            filemode='a',
                            level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)

        # If a page does not have a wiki page, it may be given a status number

    def find_monster_unique_name(self):
        # Extract the infobox for the monster, return in not available
        has_infobox = self.extract_infobox()
        if not has_infobox:
            return []

        versions = list()  # wiki_name, version_name, version_number, wiki_text

        # Try determine the versions in the infobox monster
        try:
            self.template.get("version1").value
            # Now, try to determine how many versions are present
            i = 1
            while i <= 20:  # Guessing max version number is 20
                try:
                    test_version = "version" + str(i)
                    version_name = self.template.get(test_version).value.strip()
                    unique_name = f"{self.monster_name} - {version_name}"
                    versions.append({unique_name: [str(i), self.json_data]})
                except ValueError:
                    break
                i += 1
        except ValueError:
            pass

        # The infobox is not versioned, generate default content
        if not versions:
            versions.append({self.monster_name: ["", self.json_data]})

        return versions

    def find_monster_unique_ids(self):
        # Extract the infobox for the monster, return in not available
        has_infobox = self.extract_infobox()
        if not has_infobox:
            return []

        print(self.monster_name)
        ids = list()  # id, wiki_name, version_name, version_number, wiki_text

        versions = list()
        versions.append("")
        for version in range(1, 20):
            version = str(version)
            versions.append(version)

        for version in versions:
            try:
                version_name = "id" + version
                content = self.template.get(version_name).value.strip()
                print(version_name, content)
            except ValueError:
                pass

        return versions

    def populate(self):
        """The primary entry and monster object population function."""
        # Start section in logger
        self.logger.debug("============================================ START")
        self.logger.debug(f"monster_name: {self.monster_name}")
        # print(f"{self.monster_name}|{self.version_number}")

        # STAGE THREE: EXTRACT and PARSE INFOBOX
        self.logger.debug("STAGE THREE: Extracting the infobox...")

        # Extract the infobox for the item
        has_infobox = self.extract_infobox()

        if not has_infobox:
            print("Error infobox not found")
            return  # Just skip this monster

        self.parse_infobox()

        self.parse_stats()

        self.dump_monster()

    def extract_infobox(self):
        """Extract the primary properties and bonuses for the monster."""
        self.template = None

        wikicode = mwparserfromhell.parse(self.json_data)
        # Loop through templates in wikicode from wiki page
        # Then call Inforbox Item processing method
        templates = wikicode.filter_templates()
        for template in templates:
            template_name = template.name.strip()
            template_name = template_name.lower()
            if "infobox monster" in template_name:
                self.template = template

        # If no template_primary was found, return false
        if not self.template:
            self.logger.debug("extract_infobox: no infobox monster found")
            return False

        # If we got this far, return true
        return True

    def parse_infobox(self):
        """Parse an actual Infobox template."""
        template = self.template

        # Determine the release date
        id = self.extract_infobox_value(template, "id")
        if id:
            self.monsterDefinition.id = infobox_cleaner.clean_integer(id)
        else:
            self.monsterDefinition.id = None

        # Determine the release date
        name = self.extract_infobox_value(template, "name")
        if name:
            self.monsterDefinition.name = name
        else:
            self.monsterDefinition.name = None

        # Determine the release date
        release_date = self.extract_infobox_value(template, "release")
        if release_date:
            self.monsterDefinition.release_date = infobox_cleaner.clean_release_date(release_date)
        else:
            self.monsterDefinition.release_date = None

        # Determine the release date
        members = self.extract_infobox_value(template, "members")
        if members:
            self.monsterDefinition.members = infobox_cleaner.clean_boolean(members)
        else:
            self.monsterDefinition.members = None

        # Determine the release date
        combat_level = self.extract_infobox_value(template, "combat")
        if combat_level:
            self.monsterDefinition.combat_level = infobox_cleaner.clean_integer(combat_level)
        else:
            self.monsterDefinition.combat_level = None

        # Determine the release date
        hit_points = self.extract_infobox_value(template, "hitpoints")
        if hit_points:
            self.monsterDefinition.hit_points = infobox_cleaner.clean_integer(hit_points)
        else:
            self.monsterDefinition.hit_points = None

        # Determine the release date
        max_hit = self.extract_infobox_value(template, "max hit")
        if max_hit:
            self.monsterDefinition.max_hit = infobox_cleaner.clean_integer(max_hit)
        else:
            self.monsterDefinition.max_hit = None

        # Determine the release date
        aggressive = self.extract_infobox_value(template, "aggressive")
        if aggressive:
            self.monsterDefinition.aggressive = infobox_cleaner.clean_boolean(aggressive)
        else:
            self.monsterDefinition.aggressive = None

        # Determine the release date
        poisonous = self.extract_infobox_value(template, "poisonous")
        if poisonous:
            self.monsterDefinition.poisonous = infobox_cleaner.clean_boolean(poisonous)
        else:
            self.monsterDefinition.poisonous = None

        # Determine the release date
        attack_style = self.extract_infobox_value(template, "attack style")
        if attack_style:
            self.monsterDefinition.attack_style = infobox_cleaner.clean_attack_style(attack_style)
        else:
            self.monsterDefinition.attack_style = None

        # Determine the release date
        attack_speed = self.extract_infobox_value(template, "attack speed")
        if attack_speed:
            self.monsterDefinition.attack_speed = infobox_cleaner.clean_integer(attack_speed)
        else:
            self.monsterDefinition.attack_speed = None

        # Determine the release date
        examine = self.extract_infobox_value(template, "examine")
        if examine:
            self.monsterDefinition.examine = infobox_cleaner.clean_examine(examine)
        else:
            self.monsterDefinition.examine = None

        # | turael = Yes
        # | mazchna = Yes
        # | vannaka = Yes
        # | chaeldar = Yes
        # | nieve = Yes
        # | duradel = Yes
        # | konar = Yes
        # | krystilia = Yes
        # | immunepoison = Not immune
        # | immunevenom = Not Immune
        # | slaylvl = 85
        # | slayxp = 150

    def extract_infobox_value(self, template: mwparserfromhell.nodes.template.Template, key: str) -> str:
        """Helper method to extract a value from a template using a specified key.

        This helper method is a simple solution to repeatedly try to fetch a specific
        entry from a wiki text template (a mwparserfromhell template object).

        :param template: A mediawiki wiki text template.
        :param key: The key to query in the template.
        :return value: The extracted template value based on supplied key.
        """
        value = None
        try:
            first_key = f"{key}{self.version_number}"
            value = template.get(first_key).value
        except ValueError:
            pass

        if value:
            try:
                second_key = f"{key}"
                value = template.get(second_key).value
            except ValueError:
                pass

            value = value.strip()
            return value
        else:
            return None

    def parse_stats(self):
        """Parse an actual Infobox template."""
        stats = {"att": "attack_level",
                 "str": "strength_level",
                 "def": "defence_level",
                 "mage": "magic_level",
                 "range": "ranged_level",
                 "astab": "attack_stab",
                 "aslash": "attack_slash",
                 "acrush": "attack_crush",
                 "amagic": "attack_magic",
                 "arange": "attack_ranged",
                 "dstab": "defence_stab",
                 "dslash": "defence_slash",
                 "dcrush": "defence_crush",
                 "dmagic": "defence_magic",
                 "drange": "defence_ranged",
                 "strbns": "melee_strength",
                 "rngbns": "ranged_strength",
                 "attbns": "attack_accuracy",
                 "mbns": "magic_damage"}

        for key, value in stats.items():
            stats_value = self.extract_infobox_value(self.template, key)
            if stats_value:
                cleaned_value = infobox_cleaner.clean_integer(stats_value)
                setattr(self.monsterDefinition, value, cleaned_value)
            else:
                setattr(self.monsterDefinition, value, None)

            # to_p = getattr(self.monsterDefinition, value)
            # print(to_p)

    def dump_monster(self):
        json_data = self.monsterDefinition.construct_json()
        values = []

        for value in json_data.values():
            values.append(value)
        print(values)
