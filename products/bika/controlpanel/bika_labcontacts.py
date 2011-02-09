from AccessControl import ClassSecurityInfo
from Products.CMFCore import permissions
from Products.Five.browser import BrowserView
from plone.app.content.browser.interfaces import IFolderContentsView
from plone.app.folder.folder import ATFolder
from Products.bika.browser.bika_folder_contents import BikaFolderContentsView
from zope.interface.declarations import implements

class LabContactsView(BikaFolderContentsView):
    implements(IFolderContentsView)
    contentFilter = {'portal_type': 'LabContact'}
    content_add_buttons = ['LabContact']
    batch = True
    b_size = 100
    full_objects = False
    columns = {
               'title': {'title': 'Title', 'icon':'contact.png'},
               'BusinessPhone': {'title': 'BusinessPhone'},
               'MobilePhone': {'title': 'MobilePhone'},
               'EmailAddress': {'title': 'EmailAddress'},
              }
    wflist_states = [
                    {'title': 'All', 'id':'all',
                     'columns': ['title', 'BusinessPhone', 'MobilePhone', 'EmailAddress'],
                     'buttons':[BikaFolderContentsView.default_buttons['delete']]},
                    ]

    def folderitems(self):
        items = BikaFolderContentsView.folderitems(self)
        for x in range(len(items)):
            obj = items[x]['obj'].getObject()
            items[x]['BusinessPhone'] = obj.BusinessPhone()
            items[x]['MobilePhone'] = obj.MobilePhone()
            items[x]['EmailAddress'] = obj.EmailAddress()
            items[x]['links'] = {'title': items[x]['url']}

        return items
