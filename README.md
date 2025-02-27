# Install Cookiecutter

Install cookiecutter into your Python environment.

[CookieCutter project on GitHub](https://github.com/cookiecutter/cookiecutter)

# Run Cookiecutter to Generate a Nion Swift package

```
cookiecutter gh:nion-software/cookiecutter-nionswift-plug-in
```

Cookiecutter will ask a number of questions to configure your package.

The 'repo_name' will be the name of the directory for the new package.

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
