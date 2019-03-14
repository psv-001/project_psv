from setuptools import setup, find_packages
setup(
    name='project_psv',
    description='',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'Flask==0.12.2',
        'Flask_restful==0.3.6',
        'Flask_script==2.0.6',
        'Flask_cors',
        'flask_compress',
        'flask_migrate==2.1.1',
        'marshmallow==2.14.0',
        'flask_marshmallow==0.8.0',
        'marshmallow-sqlalchemy',
        'flask_sqlalchemy==2.3.2',
        'sqlalchemy-filters',
        'Werkzeug',
        'gunicorn',
        'requests',
        'pytz',
        'psycopg2'
    ]
)

