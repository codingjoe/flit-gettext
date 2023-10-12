# Flit gettext

[![PyPi Version](https://img.shields.io/pypi/v/flit-gettext.svg)](https://pypi.python.org/pypi/flit-gettext/)
[![Test Coverage](https://codecov.io/gh/codingjoe/flit-gettext/branch/main/graph/badge.svg)](https://codecov.io/gh/codingjoe/flit-gettext)
[![GitHub License](https://img.shields.io/github/license/codingjoe/flit-gettext)](https://raw.githubusercontent.com/codingjoe/flit-gettext/main/LICENSE)

Compiling gettext i18n messages during project bundling.

_"Binary files should never be committed to a repository to promote transparency and security."_
That is why this project was created.

### Usage

Simple, just add `flit-gettext` to your `pyproject.toml`
build-system requirements and set the `build-backend`:

```toml
# pyproject.toml
[build-system]
requires = [
  "flit-gettext[scm]",  # [scm] is optional
  # …others, like wheel, etc.
]
# using flit-core as a base build-backend
build-backend = "flit_gettext.core"
# or using flit-scm as a base build-backend for git-based versioning
build-backend = "flit_gettext.scm"
# To use use flit-scm, you will need to include the optional dependency above.
```

_Please make sure, your build system has `gettext` installed._
If you ship wheels, those will include the compiled `.mo` files.

**That's it!**
