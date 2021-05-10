import setuptools

name = 'travel assistant'
version = '1.0'

setuptools.setup(
    author='x73495, Moreez317, senzaw',
    command_options={
            'build_sphinx': {
                'project': ('setup.py', name),
                'version': ('setup.py', version),
            }
        },
    description='Помощник для путешествий между Россией и Германией',
    name=name,
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires='>=3.7',
    url='https://github.com/x73495/travel-assistant',
    version=version
)
