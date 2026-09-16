"""生成前校验输入。"""
import re
import sys

SLUG = "{{ cookiecutter.project_slug }}"
EMAIL = "{{ cookiecutter.author_email }}"

if not re.match(r"^[a-z][a-z0-9_\-]+$", SLUG):
    sys.stderr.write(
        "\nERROR: project_slug 不合法: '%s'\n"
        "  只能使用小写字母、数字、下划线、连字符，且以字母开头。\n"
        "  例如: retinal_organoid_ezh2_screen\n" % SLUG
    )
    sys.exit(1)

if EMAIL and "@" not in EMAIL:
    sys.stderr.write("\nERROR: author_email 看起来不是邮箱: '%s'\n" % EMAIL)
    sys.exit(1)
