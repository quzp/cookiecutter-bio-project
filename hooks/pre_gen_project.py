"""Validate user input before the project is generated."""
import re
import sys

SLUG = "{{ cookiecutter.project_slug }}"
EMAIL = "{{ cookiecutter.author_email }}"

if not re.match(r"^[a-z][a-z0-9_\-]+$", SLUG):
    sys.stderr.write(
        "\nERROR: invalid project_slug: '%s'\n"
        "  Use lowercase letters, digits, underscores and hyphens only,\n"
        "  starting with a letter. Example: retinal_organoid_ezh2_screen\n" % SLUG
    )
    sys.exit(1)

if EMAIL and "@" not in EMAIL:
    sys.stderr.write("\nERROR: author_email does not look like an address: '%s'\n" % EMAIL)
    sys.exit(1)
