import shutil
import subprocess  # nosec
import sys
from pathlib import Path


def compile_gettext_translations(config):
    """Compile gettext translations."""
    sys.stdout.write("\33[1m* Compiling gettext translations...\33[0m\n")

    msgfmt = shutil.which("msgfmt")

    if msgfmt is None:
        msg = "msgfmt not found, please install gettext or check your PATH."
        raise OSError(msg)

    # working directory is the source tree
    for file in Path().rglob(f"{config.module}/**/*.po"):
        file = Path(file)
        cmd = [msgfmt, "-c", "-o", file.parent / f"{file.stem}.mo", file]
        subprocess.check_output(cmd)  # noqa: S603
