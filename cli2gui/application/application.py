"""Application here uses PySimpleGUI.
"""

from __future__ import annotations

import logging
import sys
from typing import Any

from cli2gui import types
from cli2gui.application.application2args import argFormat
from cli2gui.gui import helpers
from cli2gui.gui.dearpygui_wrapper import DearPyGuiWrapper
from cli2gui.gui.pysimplegui_wrapper import PySimpleGUIWrapper


def run(buildSpec: types.FullBuildSpec) -> None:
	"""Establish the main entry point.

	Args:
	----
		buildSpec (types.FullBuildSpec): args that customise the application such as the theme
		or the function to run

	"""

	# Set the theme
	theme = helpers.get_base24_theme(buildSpec["theme"], buildSpec["darkTheme"])

	gui_wrapper = {
		"dearpygui": DearPyGuiWrapper,
		"pysimplegui": PySimpleGUIWrapper,
	}.get(buildSpec["gui"], DearPyGuiWrapper)

	if "pysimplegui" in buildSpec["gui"]:
		gui = gui_wrapper(theme, buildSpec["gui"])
	else:
		gui = gui_wrapper(theme)

	def quit_callback() -> None:
		sys.exit(0)

	def run_callback(values: dict[str, Any]) -> None:
		args = argFormat(values, buildSpec["parser"])
		if not buildSpec["run_function"]:
			return args
		buildSpec["run_function"](args)
		return None

	try:
		gui.main(buildSpec=buildSpec, quit_callback=quit_callback, run_callback=run_callback)

	except KeyboardInterrupt:
		logging.error("Application Exited Early!")  # noqa: TRY400
