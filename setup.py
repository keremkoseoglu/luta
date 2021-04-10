""" Setup module """
import setuptools

setuptools.setup(
    name="luta-keremkoseoglu",
    version="0.0.1",
    author="Kerem Koseoglu",
    author_email="kerem@keremkoseoglu.com",
    description="Web spider",
    long_description="Seleium based web spider",
    long_description_content_type="text/markdown",
    url="https://github.com/keremkoseoglu/luta",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires="3.8.2",
    install_requires=[],
    include_package_data=True
)