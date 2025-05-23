import bpy
from .. import props
from .. import utils


def update_exclude_tabs(self=None, context=None):
    if not self:
        self = bpy.context.preferences.addons[utils.addon.module()].preferences

    exclude: str = self.exclude_tabs
    default: str = self.bl_rna.properties['exclude_tabs'].default

    exclude = [tab.strip() for tab in exclude.split(',')]
    default = [tab.strip() for tab in default.split(',')]

    combined = sorted(set(exclude + default))
    self['exclude_tabs'] = ', '.join(tab for tab in combined if tab)


class AddonPrefs(bpy.types.AddonPreferences):
    bl_idname = utils.addon.module()


    popover_width: bpy.props.FloatProperty(
        name='Popover Width',
        description='Width of the 3D view popover in UI units',
        default=16,
        min=8,
        max=32,
        step=1,
        precision=2,
    )


    startup_delay: bpy.props.FloatProperty(
        name='Startup Delay',
        description='How many seconds to wait after blender startup before panels',
        default=5,
        min=1,
        max=20,
        step=1,
        precision=2,
    )


    exclude_tabs: bpy.props.StringProperty(
        name='Exclude Tabs',
        description='A comma separated list of tabs that SIMPLE TABS should ignore',
        default='Item, Tool',
        update=update_exclude_tabs,
    )


    show_sidebar: bpy.props.BoolProperty(
        name='Show Sidebar',
        description='Open the sidebar when the refresh or update buttons are pressed',
        default=False,
    )


    tab_items: bpy.props.CollectionProperty(type=props.tab.TabProps)
    tab_index: bpy.props.IntProperty(name='', description='Ignore the sentence above')


    def draw(self, context: bpy.types.Context):
        layout = self.layout
        column = layout.column()

        split = column.split(factor=0.5)
        split.label(text='Popover Width')
        split.prop(self, 'popover_width', text='')

        split = column.split(factor=0.5)
        split.label(text='Startup Delay')
        split.prop(self, 'startup_delay', text='')

        split = column.split(factor=0.5)
        split.label(text='Exclude Tabs')
        split.prop(self, 'exclude_tabs', text='')

        split = column.split(factor=0.5)
        split.label(text='Show Sidebar')
        split.prop(self, 'show_sidebar', text='')

        column.separator()

        split = column.split(factor=0.5)
        split.operator('simpletabs.export_settings')
        split.operator('simpletabs.import_settings')
