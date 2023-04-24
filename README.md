# python-markdown-hashtag-extension

A python markdown extension to find hashtags and turn them into html links.

Example:

    #python

will be converted to

    <a href="/tags.html#python">#python</a>

## Installation

    pip install git+https://github.com/btbytes/python-markdown-hashtag-extension#egg=MarkdownHashtags

## Usage

    import markdown
    from markdown_hashtags import HashtagExtension

    md = markdown.Markdown(
            extensions=[HashtagExtension, ...]
