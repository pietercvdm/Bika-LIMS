from AccessControl import ClassSecurityInfo
from Products.CMFCore import permissions
from Products.Five.browser import BrowserView
from plone.app.content.browser.interfaces import IFolderContentsView
from plone.app.folder.folder import ATFolder
from Products.bika.browser.bika_folder_contents import BikaFolderContentsView
from zope.interface.declarations import implements

class DepartmentsView(BikaFolderContentsView):
    implements(IFolderContentsView)
    contentFilter = {'portal_type': 'Department'}
    content_add_buttons = ['Department']
    batch = True
    b_size = 100
    full_objects = False
    columns = {
               'DepartmentDescription': {'title': 'DepartmentDescription', 'icon':'department.png'},
               'Manager': {'title': 'Manager'},
              }
    wflist_states = [
                    {'title': 'All', 'id':'all',
                     'columns': ['DepartmentDescription', 'Manager'],
                     'buttons':[BikaFolderContentsView.default_buttons['delete']]},
                    ]

    def folderitems(self):
        items = BikaFolderContentsView.folderitems(self)
        for x in range(len(items)):
            obj = items[x]['obj'].getObject()
            items[x]['DepartmentDescription'] = obj.DepartmentDescription()
            items[x]['Manager'] = obj.ManagerName()
            items[x]['links'] = {'DepartmentDescription': items[x]['url']}

        return items
