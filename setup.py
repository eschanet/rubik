from setuptools import setup

install_requires = set([])


extras_require = {}
extras_require["test"] = sorted(
    set(
        [
            "pytest",
            "pytest-cov>=2.6.1",
            "flake8",
            "flake8-bugbear",
            "flake8-import-order",
            "flake8-print",
            "mypy",
            "types-PyYAML",
            "types-tabulate",
            "typeguard~=2.10.0",
            "pydocstyle",
            "black",
            "ruff",
            "readme_renderer[md]",
        ]
    )
)

extras_require["develop"] = sorted(
    set(extras_require["test"] + ["bump2version", "pre-commit", "twine", "jupyter"])
)

extras_require["complete"] = sorted(set(sum(extras_require.values(), [])))

long_description = open("README.md").read()

setup(
    # install_requires=install_requires,
    extras_require=extras_require,
    use_scm_version=lambda: {"local_scheme": lambda version: ""},
    name="rubik",
    version="0.0.1",
    license="MIT",
    author="Eric Schanet",
    author_email="eric.schanet@gmail.com",
    url="https://github.com/eschanet/rubik",
    packages=["rubik"],
    package_data={"": ["LICENSE"]},
    package_dir={"rubik": "rubik"},
    include_package_data=True,
    description="A basic, pure-Python Rubik's cube solver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.11",
    ],
)
