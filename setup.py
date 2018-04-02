from setuptools import setup

setup (
    name='lang_translation',
    version='1.0',
    packages=[ 'translator', 'translator.task', 'translator.model', 'translator.unittest' ],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
    url='https://github.com/mantoshkumar1/lang_translation',
    license='MIT License',
    author='Mantosh Kumar',
    author_email='mantoshkumar1@gmail.com',
    description='Language Translator'
)
