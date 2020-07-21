try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


config = {
    'description': 'A Land-Use information Application',
    'author': 'Ifedayo Ijabadeniyi, Oluwapelumi',
    'url': 'https://github.com/Adeniyii/landUse',
    'download url': 'https://github.com/Adeniyii/landUse',
    'author email': 'ifedayoadeniyi@gmail.com',
    'version': '0.1',
    'install_requires': ['flask', 'python-dotenv'],
    'packages': ['landuse'],
    'scripts': ['python file to be installed'],
    'name': 'landuse'
}

setup(**config)
