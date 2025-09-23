import os
import subprocess  # nosec
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent


def test_build_sdist(package_scm):
    """Test that build_wheel() compiles gettext translations."""
    # Create a dummy .po file
    po = package_scm / "package/locale/en/LC_MESSAGES/django.po"
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

    output = subprocess.check_output(
        ["python", "-m", "build", "--sdist"],
        cwd=package_scm,
        env={**os.environ, "PYTHONPATH": f".:{ROOT}"},
    )

    # Check that the gettext compilation was logged
    assert b"* Compiling gettext translations..." not in output


def test_build_wheel(package_scm):
    """Test that build_wheel() compiles gettext translations."""
    # Create a dummy .po file
    po = package_scm / "package/locale/en/LC_MESSAGES/django.po"
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

    output = subprocess.check_output(
        [sys.executable, "-m", "build", "--wheel"],
        cwd=package_scm,
        env={**os.environ, "PYTHONPATH": f".:{ROOT}"},
    )

    # Check that the gettext compilation was logged
    assert b"* Compiling gettext translations..." in output


def test_editable_editable(package_scm):
    """Test that build_editable() compiles gettext translations."""
    # Create a dummy .po file
    po = package_scm / "package/locale/en/LC_MESSAGES/django.po"
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

    packages_dir = package_scm / "packages"
    packages_dir.mkdir(parents=True)

    output = subprocess.check_output(
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
        cwd=package_scm,
        env={
            **os.environ,
            "PYTHONPATH": f".:{ROOT}",
            "_PYPROJECT_HOOKS_BACKEND_PATH": str(ROOT),
        },
        stderr=subprocess.STDOUT,
    )

    # Check that the gettext compilation was logged
    assert b"* Compiling gettext translations..." in output
