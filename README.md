# Install Cookiecutter

Install cookiecutter into your Python environment. Version 2.2 or later is required, since the questions use prompt
text.

[CookieCutter project on GitHub](https://github.com/cookiecutter/cookiecutter)

# Run Cookiecutter to Generate a Nion Swift package

```
cookiecutter gh:nion-software/cookiecutter-nionswift-plug-in
```

Cookiecutter will ask a number of questions to configure your package.

| Question | Meaning |
| --- | --- |
| `title` | The plug-in title, used as the menu name in Nion Swift and as the readme heading. |
| `author` | Your name, recorded as the package author. |
| `github_organization` | The GitHub organization or user which owns the repository. |
| `github_username` | The GitHub username of the package maintainer. |
| `repo_name` | The repository directory name, which is also the distribution name on PyPI. |
| `org_name` | The top level Python package name, usually your organization. Must be a valid Python name. |
| `lib_name` | The Python package name for your library. Must be a valid Python name. |
| `release_date` | The date of your initial release, or `unreleased` until you make one. |

The answers are checked before anything is generated, so an unusable package or distribution name is reported instead
of producing a project which cannot be imported or built.

The library is generated in `<org_name>/<lib_name>` and the user interface in `nionswift_plugin/<lib_name>_ui`.

# Install New Package into Your Python Environment

Ensure your Nion Swift environment is [configured](https://github.com/nion-software/nionswift/wiki/Developer-Installation) and running.

The following command installs a developer version.

```
python -m pip install --no-deps --editable <name-of-your-package>
```

The following command installs an end user version.

```
python -m pip install <name-of-your-package>
```

# Launch Swift

```
nionswift
```

# Check Your Package

The generated package is configured so the same commands run locally and in continuous integration.

```
python -m pip install -r test-requirements.txt
python -m pytest
mypy
```

# Publish Your Package

The generated workflow builds on each push and pull request against the `main` branch, and publishes to PyPI when you
push a tag. Publishing uses a trusted publisher, so there is no API token to create or store. Set it up once, before
pushing your first tag.

1. Create an environment named `release` in the repository settings on GitHub.
2. Add a trusted publisher on PyPI for the project, naming the owner, the repository, the workflow file
   `python-package.yml`, and the `release` environment. For a project which has never been published, add it as a
   pending publisher instead.
