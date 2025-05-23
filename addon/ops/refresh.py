import bpy
from .. import utils


class Refresh(bpy.types.Operator):
    bl_idname = 'simpletabs.refresh'
    bl_label = 'Refresh'
    bl_description = 'Refresh the list, so it is synchronized with the sidebar'
    bl_options = {'REGISTER', 'INTERNAL'}


    def execute(self, context: bpy.types.Context):
        utils.sidebar.show()

        prefs = utils.addon.prefs()
        names = utils.sidebar.tabs()

        for name in names:
            if name not in prefs.tab_items:
                tab = prefs.tab_items.add()
                tab.name = name
                tab.rename = name

        if prefs.tab_items:
            if prefs.tab_index not in range(len(prefs.tab_items)):
                prefs.tab_index = 0

        utils.addon.save_userpref()        
        self.report({'INFO'}, f'Found {len(prefs.tab_items)} tabs')
        return {'FINISHED'}
