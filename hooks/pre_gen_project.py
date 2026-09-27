# Validate the answers before generating anything. An invalid package name produces a project which cannot be imported
# and an invalid repository name produces one which cannot be built, in both cases long after the mistake was made.

import keyword
import re
import sys
import typing

PACKAGE_NAME_PATTERN = re.compile(r"^[a-z_][a-z0-9_]*$")
DISTRIBUTION_NAME_PATTERN = re.compile(r"^[a-zA-Z0-9]([a-zA-Z0-9._-]*[a-zA-Z0-9])?$")


def fail(message: str) -> typing.NoReturn:
    """Report the invalid answer and stop the project from being generated."""
    print(f"Error: {message}")
    sys.exit(1)


def check_package_name(label: str, package_name: str) -> None:
    """Check that the package name can be used as a Python package directory and import."""
    if not PACKAGE_NAME_PATTERN.match(package_name):
        fail(f"{label} {package_name!r} must be lowercase letters, digits, and underscores, and cannot start with a digit.")
    if keyword.iskeyword(package_name):
        fail(f"{label} {package_name!r} is a Python keyword and cannot be used as a package name.")


check_package_name("org_name", "{{cookiecutter.org_name}}")
check_package_name("lib_name", "{{cookiecutter.lib_name}}")

if not DISTRIBUTION_NAME_PATTERN.match("{{cookiecutter.repo_name}}"):
    fail("repo_name '{{cookiecutter.repo_name}}' must start and end with a letter or digit and otherwise contain only letters, digits, '-', '_', and '.'.")
