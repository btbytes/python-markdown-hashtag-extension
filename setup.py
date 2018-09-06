from distutils.core import setup

setup(
    name="MarkdownHashtags",
    version=0.1,
    packages=['markdown_hashtags'],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
    install_requires=open('requirements.txt').read().split('\n'),
)
