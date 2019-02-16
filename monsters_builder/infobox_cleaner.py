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

import datetime

import dateparser


def clean_release_date(value: str) -> str:
    """A helper method to convert the release date entry from an OSRS Wiki infobox.

    The returned value will be a specifically formatted string: dd Month YYYY.
    For example, 25 June 2017 or 01 November 2014.

    :param value: The extracted raw wiki text.
    :return release_date: A cleaned release date of an item.
    """
    release_date = value
    release_date = release_date.strip()
    release_date = release_date.replace("[", "")
    release_date = release_date.replace("]", "")

    try:
        release_date = datetime.datetime.strptime(release_date, "%d %B %Y")
        return release_date.strftime("%d %B %Y")
    except ValueError:
        pass

    try:
        release_date = dateparser.parse(release_date)
        release_date = release_date.strftime("%d %B %Y")
    except (ValueError, TypeError):
        return None

    return release_date


def clean_examine(value: str) -> str:
    """A helper method to convert the examine text entry from an OSRS Wiki infobox.

    :param value: The extracted raw wiki text.
    :return tradeable: A cleaned tradeable property of an item.
    """
    examine = str(value)
    examine = examine.strip()

    examine = examine.replace("[", "")
    examine = examine.replace("]", "")

    return examine


def clean_boolean(value: str) -> bool:
    """A helper method to convert a boolean entry from an OSRS Wiki infobox.

    :param value: The extracted raw wiki text.
    :return tradeable: A cleaned tradeable property of an item.
    """
    value = str(value)
    value = value.strip()

    value = value.replace("[", "")
    value = value.replace("]", "")

    if value in ["True", "true", True, "Yes", "yes"]:
        value = True
    elif value in ["False", "false", False, "No", "no"]:
        value = False
    else:
        value = False

    return value


def clean_integer(value: str) -> int:
    """A helper method to convert a integer entry from an OSRS Wiki infobox.

    :param value: The extracted raw wiki text.
    :return tradeable: A cleaned property of an item.
    """
    value = str(value)
    value = value.strip()

    value = value.replace("[", "")
    value = value.replace("]", "")

    try:
        value = int(value)
    except ValueError:
        value = None

    return value


def clean_attack_style(value: str) -> str:
    """A helper method to convert the examine text entry from an OSRS Wiki infobox.

    :param value: The extracted raw wiki text.
    :return value: A cleaned value property of an item.
    """
    value = str(value)
    value = value.strip()

    value = value.replace("[", "")
    value = value.replace("]", "")

    return value
