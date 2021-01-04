'''Classes for Django & Wagtailcms Models

This module specifically contains classes for Django and Wagtailcms models.
Some classes act as wagtail page models allowing for new page configurations.
'''

from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

class Home(Page): # pylint: disable=too-many-ancestors

    '''Wagtailcms page model for the homepage (index).'''

    parent_page_types = []

    template = 'home/index.html'

class Announcements(Page): # pylint: disable=too-many-ancestors

    '''Wagtailcms page model for the announcements page.'''

    parent_page_types = []
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]

    template = 'home/announcements.html'

class Announcement(Page): # pylint: disable=too-many-ancestors

    '''Wagtailcms page model for individual announcement pages.'''

    parent_page_types = ['core.Announcements']
    date = models.DateField("Post Date")
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('body', classname="full"),
    ]

    template = 'home/page.html'

class Policies(Page): # pylint: disable=too-many-ancestors

    '''Wagtailcms page model for the policies page.'''

    parent_page_types = []
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]

    template = 'home/page.html'

class Terms(Page): # pylint: disable=too-many-ancestors

    '''Wagtailcms page model for the terms & conditions page.'''

    parent_page_types = []
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]

    template = 'home/page.html'
