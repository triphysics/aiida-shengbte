# -*- coding: utf-8 -*-
# pylint: disable=wrong-import-position,wildcard-import
"""Module for the command line interface."""
import click
import click_completion

from aiida.cmdline.params import options, types

# Activate the completion of parameter types provided by the click_completion package
click_completion.init()


@click.group(
    "aiida-shengbte",
    context_settings={"help_option_names": ["-h", "--help"]},
)
@options.PROFILE(type=types.ProfileParamType(load_profile=True))
def cmd_root(profile):  # pylint: disable=unused-argument
    """CLI for the `aiida-shengbte` plugin."""


# from .calculations import cmd_calculation
# from .workflows import cmd_workflow
from .test import cmd_test