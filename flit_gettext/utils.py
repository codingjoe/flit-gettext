import subprocess  # nosec
from pathlib import Path


def compile_gettext_translations(config):
    """Compile gettext translations."""
    print("\33[1m* Compiling gettext translations...\33[0m")
    # working directory is the source tree
    for file in Path().rglob(f"{config.module}/**/*.po"):
        file = Path(file)
        cmd = ["msgfmt", "-c", "-o", file.parent / f"{file.stem}.mo", file]
        subprocess.check_output(cmd)  # nosec
