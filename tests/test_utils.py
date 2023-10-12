import subprocess

import pytest

import flit_gettext.utils


def test_compile_gettext_translations(capsys, package):
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

    flit_gettext.utils.compile_gettext_translations(
        type("LoadedConfig", (), {"module": "package"})()
    )

    assert (package / "package/locale/en/LC_MESSAGES/django.mo").exists()
    captured = capsys.readouterr()
    assert captured.out == "\x1b[1m* Compiling gettext translations...\x1b[0m\n"
    assert captured.err == ""


def test_compile_gettext_translations__invalid(capsys, package):
    po = package / "package/locale/en/LC_MESSAGES/django.po"
    po.parent.mkdir(parents=True)
    po.write_text(
        r"""
        msgid ""
        msgstr ""
        """
    )

    with pytest.raises(subprocess.CalledProcessError):
        flit_gettext.utils.compile_gettext_translations(
            type("LoadedConfig", (), {"module": "package"})()
        )
