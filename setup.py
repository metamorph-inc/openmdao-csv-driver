from setuptools import setup

kwargs = {'author': 'Kevin Smyth',
          'author_email': 'ksmyth@metamorphsoftware.com',
          'classifiers': ['Intended Audience :: Science/Research',
                          'Topic :: Scientific/Engineering'],
          'description': 'OpenMDAO Driver for CSV files',
          'download_url': '',
          'include_package_data': True,
          'install_requires': ['OpenMDAO==1.7.4'],
          'keywords': ['OpenMDAO'],
          'license': 'MIT',
          'maintainer': 'Kevin Smyth',
          'maintainer_email': 'ksmyth@metamorphsoftware.com',
          'name': 'openmdao_csv_driver',
          'packages': ['openmdao_csv_driver'],
          'url': 'https://github.com/metamorph-inc/openmdao-csv-driver',
          'version': '0.1',
          'zip_safe': False}

setup(**kwargs)
