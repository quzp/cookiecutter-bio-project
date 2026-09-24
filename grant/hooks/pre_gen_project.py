"""Validate user input before the grant project is generated."""
import re
import sys

SLUG = "{{ cookiecutter.project_slug }}"
DEADLINE = "{{ cookiecutter.deadline }}"

if not re.match(r"^[a-z][a-z0-9_\-]+$", SLUG):
    sys.stderr.write(
        "\nERROR: invalid project_slug: '%s'\n"
        "  Use lowercase letters, digits, underscores and hyphens only,\n"
        "  starting with a letter. Example: cone_chromatin_r01\n" % SLUG
    )
    sys.exit(1)

if DEADLINE != "YYYY-MM-DD" and not re.match(r"^\d{4}-\d{2}-\d{2}$", DEADLINE):
    sys.stderr.write("\nERROR: deadline must be YYYY-MM-DD, got '%s'\n" % DEADLINE)
    sys.exit(1)
