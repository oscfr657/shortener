from django.core.management.base import BaseCommand

from django.conf import settings

from django.core.files import File

from django.db import IntegrityError

import re

from urlshortener.models import ShortUrl


class Command(BaseCommand):
    help = 'Import words from file'

    def add_arguments(self, parser):
        parser.add_argument('file', nargs='+', type=File)

    def handle(self, *args, **options):

        for test in args:
            self.stdout.write(test)
            file_dir = settings.BASE_DIR + '/' + test

        self.stdout.write(file_dir)

        file = open(file_dir)

        try:
            for line in file:
                word = re.sub(r'[^a-z0-9]', '', line.lower())
                try:
                    short_url = ShortUrl(word=word)
                    short_url.save()
                    self.stdout.write('Successfully saved word "%s"' % word)
                except IntegrityError:
                    self.stdout.write('The word "%s" already exists' % word)
        finally:
            file.close()

        self.stdout.write('Success')