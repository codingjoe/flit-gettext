from flit_core import buildapi
from flit_core.buildapi import *  # noqa: F403

from flit_gettext.utils import compile_gettext_translations


def build_wheel(
    wheel_directory, config_settings=None, metadata_directory=None
):  # pragma: no cover
    info = buildapi.read_flit_config(buildapi.pyproj_toml)
    compile_gettext_translations(info)
    return buildapi.build_wheel(wheel_directory, config_settings, metadata_directory)


def build_editable(
    wheel_directory, config_settings=None, metadata_directory=None
):  # pragma: no cover
    info = buildapi.read_flit_config(buildapi.pyproj_toml)
    compile_gettext_translations(info)
    return buildapi.build_editable(wheel_directory, config_settings, metadata_directory)
