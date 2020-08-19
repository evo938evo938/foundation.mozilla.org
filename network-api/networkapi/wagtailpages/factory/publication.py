from wagtail.core.models import Collection
from networkapi.wagtailpages.pagemodels.publications.publication import PublicationPage
from wagtail_factories import PageFactory, ImageFactory
from networkapi.utility.faker.helpers import (
    get_homepage,
    reseed
)
from factory import (
    Faker,
    SubFactory,
    django,
    DjangoModelFactory,

)

# UGLY COPYPASTE FROM latest
# https://github.com/mvantellingen/wagtail-factories/blob/master/src/wagtail_factories/factories.py

from wagtail_factories.factories import MP_NodeFactory

from wagtail.documents import get_document_model


class CollectionFactory(MP_NodeFactory):
    name = Faker('text', max_nb_chars=60)

    class Meta:
        model = Collection


class CollectionMemberFactory(DjangoModelFactory):
    collection = SubFactory(CollectionFactory, parent=None)


class DocumentFactory(CollectionMemberFactory):
    class Meta:
        model = get_document_model()
    title = Faker('text', max_nb_chars=255)
    file = django.FileField(filename=Faker('file_name', category="text"), file_extension="pdf")


class PublicationPageFactory(PageFactory):
    title = Faker('text', max_nb_chars=255)
    subtitle = Faker('text', max_nb_chars=255)
    secondary_subtitle = Faker('text', max_nb_chars=255)
    publication_date = Faker('date_object')
    hero_image = SubFactory(ImageFactory)
    publication_file = DocumentFactory()

    class Meta:
        model = PublicationPage


def generate(seed):
    """
    makes a batch of 3 publication pages
    eventually I'd like to add a post_generation hooks that gives each of these pages an arbitrary number of chapters
    and chapters an arbitrary number of articles
    """
    reseed(seed)
    home_page = get_homepage()

    PublicationPageFactory.create_batch(parent=home_page, size=3)
