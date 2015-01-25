from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope import schema
from plone.directives import form
from zope.component import adapts
from zope.interface import alsoProvides, implements

from plone.app.content.interfaces import INameFromTitle
from Products.CMFPlone.utils import safe_unicode
from plone import api

from twgov.namecard import MessageFactory as _


class ISetIdFromUserIdBehavior(model.Schema):
    """
       Marker/Form interface for SetIdFromUserIdBehavior
    """

    # -*- Your Zope schema definitions here ... -*-


alsoProvides(ISetIdFromUserIdBehavior, IFormFieldProvider)

def context_property(name):
    def getter(self):
        return getattr(self.context, name)
    def setter(self, value):
        setattr(self.context, name, value)
    def deleter(self):
        delattr(self.context, name)
    return property(getter, setter, deleter)


class SetIdFromUserIdBehavior(object):
    """
       Adapter for SetIdFromUserIdBehavior
    """
    implements(INameFromTitle)
    adapts(ISetIdFromUserIdBehavior)

    def __new__(cls, context):
        instance = super(SetIdFromUserIdBehavior, cls).__new__(cls)
        newId = safe_unicode(api.user.get_current().id)
        instance.title = newId
        import pdb;pdb.set_trace()
        return instance


    def __init__(self, context):
        self.context = context


    # -*- Your behavior property setters & getters here ... -*-
