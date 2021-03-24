import setuptools

with open('requirements.txt') as req_file:
    requirements = req_file.read().splitlines()

setuptools.setup(
    name='ml_flask_restx',
    version='0.0.1',
    author_email='b.tseytlin@lambda-it.ru',
    packages=['ml_flask_restx'],
    install_requires=requirements,
    python_requires=">=3.7"
)
