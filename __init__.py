# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.


bl_info = {
    'name': 'SIMPLE TABS',
    'author': 'bonjorno7, Chipp Walters, MasterXeon1001, Updated for Blender 4.0+ by gh0stck',
    'description': 'Organize the Blender sidebar (Community Update)',
    'blender': (4, 0, 0),
    'version': (2, 0, 0),
    'location': 'View3D',
    'category': '3D View',
}


from . import addon


def register():
    addon.register()


def unregister():
    addon.unregister()
