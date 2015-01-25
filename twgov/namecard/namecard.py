from five import grok

from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Container
from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder


from twgov.namecard import MessageFactory as _


class INameCard(form.Schema, IImageScaleTraversable):
    """
    Name Card Content type
    """
    contactName = schema.TextLine(
        title=_(u'Contact Name'),
        description=_(u'Fill in, if your namecard is a company, or ignore this field.'),
        required=False,
    )

    webSite = schema.URI(
        title=_(u'webiste url'),
        description=_(u'website url, must include http://'),
        required=False,
    )

    address = schema.TextLine(
        title=_(u'Address'),
        description=_(u'Fill your contact address.'),
        required=True,
    )

    telNo = schema.TextLine(
        title=_(u'Tel'),
        description=_(u'Fill your Tel No., format: 02-23456789, or 039-345678'),
        required=True,
    )

    faxNo = schema.TextLine(
        title=_(u'FAX'),
        description=_(u'Fill your FAX No., format: 02-23456789, or 039-345678'),
        required=False,
    )

    cellNo = schema.TextLine(
        title=_(u'Cell NO'),
        description=_(u'Fill your Tel No., format: 0912-123456'),
        required=False,
    )

    email = schema.TextLine(
        title=_(u'email address'),
        description=_(u'Fill your contact email address, '),
        required=False,
    )

    serviceKeyword = schema.Text(
        title=_(u'Service Keyword'),
        description=_(u'Fill your Service Keyowrd, one line one keyword.'),
        required=True,
    )

    detail = schema.Text(
        title=_(u'Detail Description'),
        description=_(u'Detail Description, Fill in here.'),
        required=False,
    )

#    form.widget('image', klass='button orange small')
    image = NamedBlobImage(
        title=_(u'Your Image'),
        description=_(u'Upload your personal image or company logo.'),
        required=True,
    )

    banner = NamedBlobImage(
        title=_(u'Your Banner'),
        description=_(u'Upload your Banner image.'),
        required=True,
    )



class NameCard(Container):
    grok.implements(INameCard)


class SampleView(dexterity.DisplayForm):
    """ sample view class """

    grok.context(INameCard)
    grok.require('zope2.View')
    grok.name('view')
