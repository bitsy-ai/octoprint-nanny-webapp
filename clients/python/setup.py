# coding: utf-8

"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@bitsy.ai
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_namespace_packages  # noqa: H301

NAME = "print-nanny-client"
VERSION = "0.8.3"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.25.3", "six >= 1.10", "python-dateutil", "protobuf"]
REQUIRES.append("aiohttp >= 3.7.0")
setup(
    name=NAME,
    version=VERSION,
    description="",
    author="Leigh Johnson",
    author_email="leigh@bitsy.ai",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", ""],
    install_requires=REQUIRES,
    packages=find_namespace_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501
    """
)
