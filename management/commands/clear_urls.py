from django.core.management.base import BaseCommand

from urlshortener.models import ShortUrl


class Command(BaseCommand):
    help = 'Clear all urls.'

    def handle(self, *args, **options):

        short_urls = ShortUrl.objects.exclude(url__isnull=True).exclude(url__exact='')
        for url in short_urls:
            self.stdout.write('Url: "%s"' % url.url)
            url.url = None
            url.save()

        self.stdout.write('Success')