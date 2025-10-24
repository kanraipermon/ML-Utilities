from setuptools import setup, find_packages

setup(
    name="ml-utils",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "ml_utils=ml_utils.cli:main",
        ]
    },
    install_requires=[
        "pandas>=1.5.0",
        "numpy>=1.23.0",
        "scikit-learn>=1.2.0"
    ]
)
