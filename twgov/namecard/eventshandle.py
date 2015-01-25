from five import grok
from zope.lifecycleevent.interfaces import IObjectAddedEvent, IObjectCreatedEvent
from Products.PluggableAuthService.interfaces.events import IPrincipalCreatedEvent, IUserLoggedInEvent
from plone import api
import logging
logger = logging.getLogger('twgov.namecard.eventshandle')

from twgov.namecard.namecard import INameCard



@grok.subscribe(IUserLoggedInEvent)
def createdUser(event):
    id = event.object.getId()
    roles = api.user.get_roles(username=id)
    if ('NameCard Creator' in roles) or ('NameCard Owner' in roles):
        return
    api.user.grant_roles(username=id,
                         roles=['NameCard Creator']
    )
    return



@grok.subscribe(INameCard, IObjectAddedEvent)
def addedNameCard(object, event):
    newId = object.owner_info()['id'].encode('utf-8')
    api.content.rename(object, new_id=newId)
    api.user.grant_roles(username=event.object.getId(),
                         roles=['NameCard Owner']
    )
    api.user.revoke_roles(username=event.object.getId(),
                         roles=['NameCard Creator']
    )
    return
