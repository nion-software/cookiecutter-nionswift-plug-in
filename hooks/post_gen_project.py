# Remove the files Finder leaves behind. Generating from a local directory copies them along with the template, since
# they sit beside the template files, and they have no place in a new project.

import pathlib

for path in pathlib.Path.cwd().rglob(".DS_Store"):
    path.unlink()
