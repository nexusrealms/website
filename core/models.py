from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

class Home(Page):
    parent_page_types = []

    def get_template(self,request):
        return 'home/index.html'

class Announcements(Page):
    parent_page_types = []
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]

    def get_template(self, request):
        return 'home/announcements.html'

class Announcement(Page):
    parent_page_types = ['core.Announcements']
    date = models.DateField("Post Date")
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('body', classname="full"),
    ]

    def get_template(self, request):
        return 'home/page.html'

class Policies(Page):
    parent_page_types = []
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]

    def get_template(self, request):
        return 'home/page.html'

class Terms(Page):
    parent_page_types = []
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]

    def get_template(self, request):
        return 'home/page.html'

