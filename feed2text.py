#!/usr/bin/env python
import os

from collections import Counter

import click
import feedparser

from html2text import html2text


@click.command()
@click.argument('url')
def fetch(url):
    response = feedparser.parse(url)
    if response.get('status') != 200:
        return click.echo("There was a problem fetching %s" % url)

    # We're going to save into a directory named after the feed
    # in our current directory in a 'feeds' directory
    feed_name = response.feed.title
    feed_directory = "%s/%s/%s" % (os.path.abspath(os.curdir), 'feeds', feed_name)
    if not os.path.exists(feed_directory):
        os.makedirs(feed_directory)

    # parse and save each feed item as [title].markdown
    saved = Counter()
    for entry in response.entries:
        title = entry.title
        content = html2text(entry.content[0].value)
        file_path = "%s/%s.mkd" % (feed_directory, title)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                click.echo('Saving "%s"...' % title)
                f.write(content.encode('utf8'))
                saved['entries'] += 1

    if saved['entries']:
        click.echo("Saved %s entries!" % saved['entries'])
    else:
        click.echo("Nothing new to read!")

@click.group()
def cli():
    pass

cli.add_command(fetch)

if __name__ == '__main__':
    cli()
