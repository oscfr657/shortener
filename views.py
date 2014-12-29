from django.shortcuts import render
from django.shortcuts import redirect

from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

import re
from random import randint

from urlparse import urlparse
from posixpath import dirname, basename

from .forms import UrlForm
from .models import ShortUrl


def index(request):

    if request.method == 'POST':

        form = UrlForm(request.POST)

        if form.is_valid():
            url = form.cleaned_data['url']
            parsed_url = urlparse(url)

            net = parsed_url.netloc
            site = re.split('\W+', net)
            site.reverse()
            domain = site.pop()
            if domain.lower() == 'www':
                domain = site.pop()
            words = [domain]

            path = dirname(parsed_url.path)
            words += re.split('\W+', path)

            file = basename(parsed_url.path)
            file_name = re.split('\W+', file)
            file_name.reverse()
            words.append(file_name.pop())

            words.reverse()
            for word in words:
                if word != '':
                    try:
                        short_url = ShortUrl.objects.get(word=word)
                        if short_url.url is None or short_url.url == '':
                            short_url.url = url
                            short_url.save()

                            form = UrlForm()
                            urls = ShortUrl.objects.exclude(url__isnull=True).exclude(url__exact='')
                            return render(request, 'index.html', {'form': form, 'urls': urls})
                    except ObjectDoesNotExist:
                        #print('word: {0}'.format(word))
                        pass
                    except IntegrityError:
                        #print('word: {0}'.format(word))
                        pass

            # If we are here there was no matching or free word in the db.
            urls = ShortUrl.objects.filter(url__isnull=True)
            if urls.exists():
                rand = randint(0, urls.count())
                short_url = urls[rand]
                short_url.url = url
                short_url.save()
            else:
                urls = ShortUrl.objects.order_by('changed_at_date_time')[0]
                short_url = urls[0]
                short_url.url = url
                short_url.save()

    form = UrlForm()
    urls = ShortUrl.objects.exclude(url__isnull=True).exclude(url__exact='')
    return render(request, 'index.html', {'form': form, 'urls': urls})


def shorturl(request, word):

    try:
        short_url = ShortUrl.objects.get(word=word)
    except ObjectDoesNotExist as e:
        return redirect('/')

    return redirect(short_url.url)