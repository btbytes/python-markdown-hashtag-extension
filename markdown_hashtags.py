from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
import re

__author__ = "kongaloosh"


class HashtagExtension(Extension):

    def __init__(self, *args, **kwargs):
        super(HashtagExtension, self).__init__(*args, **kwargs)

    def extendMarkdown(self, md):
        md.registerExtension(self)
        md.preprocessors.register(
            HashtagPreprocessor(md),
            "hashtag",
            24)


class HashtagPreprocessor(Preprocessor):
    HASHTAG_RE = re.compile(
            r"""(?:(?<=\s)|^)#(\w*[A-Za-z_]+\w*)"""
    )

    def __init__(self, md):
        super(HashtagPreprocessor, self).__init__(md)

    def run(self, lines):
        HASHTAG_WRAP = '''<a href="/tags.html#{0}"> #{0}</a>'''
        text = "\n".join(lines)
        while True:
            hashtag = ''
            m = self.HASHTAG_RE.search(text)
            if m:                                    # if there is a match
                hashtag += HASHTAG_WRAP.format(m.group()[1:])
                placeholder = self.markdown.htmlStash.store(hashtag, safe=True)
                text = '%s %s %s' % (text[:m.start()], placeholder, text[m.end():])
            else:
                break
        return text.split('\n')


def makeExtension(*args, **kwargs):
    return HashtagExtension(*args, **kwargs)

