from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = "hardhat"
copyright = "2026, Gene Dan"
author = "Gene Dan"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
