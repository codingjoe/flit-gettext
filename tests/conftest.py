import contextlib
import os
import shutil
import tempfile
from pathlib import Path

import pytest

PACKAGE_DIR = Path(__file__).parent.parent
BACKEND_DIR = PACKAGE_DIR / "flit_gettext"


def copy_backend(temp_dir):
    """
    Copy the in-tree build backend into the package directory.

    ``backend-path`` must point to a directory inside the project.
    """
    shutil.copytree(BACKEND_DIR, temp_dir / BACKEND_DIR.name)


@pytest.fixture
def package():
    with tempfile.TemporaryDirectory() as tmpdirname:
        temp_dir = Path(tmpdirname)
        copy_backend(temp_dir)
        pyproject_toml = temp_dir / "pyproject.toml"
        pyproject_toml.write_text(
            "[project]\n"
            'name = "package"\n'
            'version = "0.1.0"\n'
            'description = "A package"\n'
            "[build-system]\n"
            'requires = ["flit_core >=3.0.0,<4"]\n'
            'build-backend = "flit_gettext.core"\n'
            'backend-path = ["."]\n'
        )
        (temp_dir / "package").mkdir(parents=True)
        (temp_dir / "package" / "__init__.py").touch()

        with chdir(temp_dir):
            yield temp_dir


@pytest.fixture
def package_scm():
    with tempfile.TemporaryDirectory() as tmpdirname:
        temp_dir = Path(tmpdirname)
        copy_backend(temp_dir)
        pyproject_toml = temp_dir / "pyproject.toml"
        pyproject_toml.write_text(
            "[project]\n"
            'name = "package"\n'
            'description = "A package"\n'
            'dynamic = ["version"]\n'
            "[build-system]\n"
            'requires = ["flit_core >=3.0.0,<4", "flit_scm"]\n'
            'build-backend = "flit_gettext.scm"\n'
            'backend-path = ["."]\n'
            "[tool.setuptools_scm]\n"
            'write_to = "package/_version.py"\n'
            'fallback_version = "0.1.0"\n'
        )
        (temp_dir / "package").mkdir(parents=True)
        (temp_dir / "package" / "__init__.py").touch()
        (temp_dir / "package" / "_version.py").write_text('version = "0.1.0"\n')

        with chdir(temp_dir):
            yield temp_dir


@contextlib.contextmanager
def chdir(path):
    """Context manager to temporarily change the working directory."""
    cwd = Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(cwd)
