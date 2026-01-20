from pathlib import Path

from setuptools import find_packages, setup

README = (Path(__file__).parent / "README.md").read_text(encoding="utf-8")

setup(
    name="netbox-gateways",
    version="0.9.2",
    description="Manage simple prefix default gateways",
    long_description=README,
    long_description_content_type="text/markdown",
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
