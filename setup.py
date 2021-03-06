import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zpy-flask-msc",
    version="0.0.1",
    author="Noé Cruz | linkedin.com/in/zurckz/",
    author_email="zurckz.services@gmail.com",
    description="Helper layer for apis development with Python and Flask",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NoeCruzMW",
    packages=setuptools.find_packages(),
    install_requires=[
        "pycryptodome",
        "pycryptodomex",
        "Flask",
        "flask-rest-api",
        "Flask-RESTful",
        "marshmallow",
        "python-dotenv",
        "flask_cors",
        "cx-Oracle",
        "marshmallow_objects"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)