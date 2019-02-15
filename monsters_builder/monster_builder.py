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
from osrsbox.monsters_api.monster_definition import MonsterStats


class BuildMonster:
    def __init__(self, monster_name, json_data):
        # Input monster name
        self.monster_name = monster_name
        # Input JSON file (wiki text)
        self.json_data = json_data

        # For this monster, initialize the required objects
        self.monsterDefinition = MonsterDefinition()
        self.monsterDefinition.monster_stats = MonsterStats()

        # Setup logging
        logging.basicConfig(filename="builder.log",
                            filemode='a',
                            level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)

        # If a page does not have a wiki page, it may be given a status number

    def find_monster(self):
        # Extract the infobox for the monster
        print(self.monster_name)

        has_infobox = self.extract_infobox()

        if not has_infobox:
            return

        version_identifiers = ["version",
                               "name",
                               "monstername"]

        version_count = 0  # the number of versions available
        for version_identifier in version_identifiers:
            # Check if the infobox is versioned, and get a version count
            if version_count == 0:
                try:
                    self.template.get(version_identifier + "1").value
                    is_versioned = True
                    # Now, try to determine how many versions are present
                    i = 1
                    while i <= 20:  # Guessing max version number is 20
                        try:
                            self.template.get(version_identifier + str(i)).value
                            print(version_identifier + str(i))
                            version_count += 1
                        except ValueError:
                            break
                        i += 1
                except ValueError:
                    pass

        return is_versioned

    def populate(self):
        """The primary entry and monster object population function."""
        # Start section in logger
        self.logger.debug("============================================ START")
        self.logger.debug(f"monster_name: {self.monster_name}")
        print(f"monster_name: {self.monster_name}")

        # STAGE THREE: EXTRACT and PARSE INFOBOX
        self.logger.debug("STAGE THREE: Extracting the infobox...")

        # Extract the infobox for the item
        has_infobox = self.extract_infobox()

        if not has_infobox:
            print("Error infobox not found")
            return  # Just skip this monster

        self.parse_infobox()

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
        # Set defaults for versioned infoboxes
        is_versioned = False  # has multiple versions available
        self.current_version = None  # The version that matches the item
        version_count = 0  # the number of versions available

        # STAGE ONE: Determine if we have a versioned infobox, and the version count

        version_identifiers = ["version",
                               "name",
                               "monstername"]

        for version_identifier in version_identifiers:
            # Check if the infobox is versioned, and get a version count
            if version_count == 0:
                try:
                    template.get(version_identifier + "1").value
                    is_versioned = True
                    # Now, try to determine how many versions are present
                    i = 1
                    while i <= 20:  # Guessing max version number is 20
                        try:
                            template.get(version_identifier + "1").value
                            version_count += 1
                        except ValueError:
                            break
                        i += 1
                except ValueError:
                    pass

        # STAGE TWO: Match a versioned infobox to the item name

        if is_versioned:
            # Try determine
            for version_identifier in version_identifiers:
                try:
                    template.get(version_identifier + "1").value
                    i = 1
                    while i <= version_count:
                        versioned_name = version_identifier + str(i)
                        if self.monster_name == template.get(versioned_name).value.strip():
                            self.current_version = i
                        i += 1
                except ValueError:
                    pass

            self.logger.debug("NOTE: versioned infobox: %s" % self.current_version)

        if is_versioned and self.current_version is None:
            self.current_version = 1

        if is_versioned:
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< VERSIONED")
            print(version_count)
            print(self.current_version)

        # # WEIGHT: Determine the weight of an item ()
        # weight = None
        # if self.current_version is not None:
        #     key = "weight" + str(self.current_version)
        #     weight = self.extract_infobox_value(template, key)
        # if weight is None:
        #     weight = self.extract_infobox_value(template, "weight")
        # if weight is not None:
        #     self.itemDefinition.weight = infobox_cleaner.clean_weight(weight)
