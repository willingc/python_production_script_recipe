from setuptools import setup

requirements = [
    'pytest-cov==1.8.1',
    'tox==1.9.2',
]

setup(
    name='python_production_script_recipe',
    version='0.1',
    author='Adam Burns',
    author_email='adam@yourteamneedsadam.com',
    description='Recipe of best practices for Python scripts in production.',
    install_requires=requirements,
)
