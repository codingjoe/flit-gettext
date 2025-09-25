import os
import subprocess  # nosec
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent


def test_build_sdist(package):
    """Test that build_wheel() compiles gettext translations."""
    # Create a dummy .po file
    po = package / "package/locale/en/LC_MESSAGES/django.po"
    po.parent.mkdir(parents=True)
    po.write_text(
        r"""
        msgid ""
        msgstr ""
        "POT-Creation-Date: 2022-11-11 11:11+0100\n"
        "PO-Revision-Date: 2022-11-11 11:11+0100\n"
        "Language-Team: \n"
        "Language: en\n"
        "MIME-Version: 1.0\n"
        "Content-Type: text/plain; charset=UTF-8\n"
        "Content-Transfer-Encoding: 8bit\n"
        """
    )

    output = subprocess.check_output(  # noqa: S603
        [sys.executable, "-m", "build", "--sdist"],
        cwd=package,
        env={**os.environ, "PYTHONPATH": f".:{ROOT}"},
    )

    # Check that the gettext compilation was logged
    assert b"* Compiling gettext translations..." not in output


def test_build_wheel(package):
    """Test that build_wheel() compiles gettext translations."""
    # Create a dummy .po file
    po = package / "package/locale/en/LC_MESSAGES/django.po"
    po.parent.mkdir(parents=True)
    po.write_text(
        r"""
        msgid ""
        msgstr ""
        "POT-Creation-Date: 2022-11-11 11:11+0100\n"
        "PO-Revision-Date: 2022-11-11 11:11+0100\n"
        "Language-Team: \n"
        "Language: en\n"
        "MIME-Version: 1.0\n"
        "Content-Type: text/plain; charset=UTF-8\n"
        "Content-Transfer-Encoding: 8bit\n"
        """
    )

    output = subprocess.check_output(  # noqa: S603
        [sys.executable, "-m", "build", "--wheel"],
        cwd=package,
        env={**os.environ, "PYTHONPATH": f".:{ROOT}"},
    )

    # Check that the gettext compilation was logged
    assert b"* Compiling gettext translations..." in output


def test_editable_editable(package):
    """Test that build_editable() compiles gettext translations."""
    # Create a dummy .po file
    po = package / "package/locale/en/LC_MESSAGES/django.po"
    po.parent.mkdir(parents=True)
    po.write_text(
        r"""
        msgid ""
        msgstr ""
        "POT-Creation-Date: 2022-11-11 11:11+0100\n"
        "PO-Revision-Date: 2022-11-11 11:11+0100\n"
        "Language-Team: \n"
        "Language: en\n"
        "MIME-Version: 1.0\n"
        "Content-Type: text/plain; charset=UTF-8\n"
        "Content-Transfer-Encoding: 8bit\n"
        """
    )

    packages_dir = package / "packages"
    packages_dir.mkdir(parents=True)

    output = subprocess.check_output(  # noqa: S603
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "--target",
            str(packages_dir),
            "-v",
            "-e",
            ".",
        ],
        cwd=package,
        env={
            **os.environ,
            "PYTHONPATH": f".:{ROOT}",
            "_PYPROJECT_HOOKS_BACKEND_PATH": str(ROOT),
        },
        stderr=subprocess.STDOUT,
    )

    # Check that the gettext compilation was logged
    assert b"* Compiling gettext translations..." in output
