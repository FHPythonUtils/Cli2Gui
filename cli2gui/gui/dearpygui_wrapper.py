from __future__ import annotations

from pathlib import Path
from typing import Any, Callable

import dearpygui.dearpygui as dpg

from cli2gui import types
from cli2gui.gui import helpers
from cli2gui.gui.abstract_gui import AbstractGUI

THISDIR = Path(__file__).resolve().parent


def hex_to_rgb(hex_code: str) -> tuple[int, int, int, int]:
	"""Convert a color hex code to a tuple of integers (r, g, b)."""
	hex_code = hex_code.lstrip("#")
	r = int(hex_code[0:2], 16)
	g = int(hex_code[2:4], 16)
	b = int(hex_code[4:6], 16)
	return (r, g, b, 255)


class DearPyGuiWrapper(AbstractGUI):
	"""Wrapper class for Dear PyGui."""

	def __init__(self, base24Theme: list[str]) -> None:
		self.base24Theme = base24Theme
		super().__init__()

	def _helpText(self, item: types.Item) -> None:
		dpg.add_text(
			helpers.stringSentencecase(f'\n- {item["dest"]}: {item["commands"]}'),
			color=hex_to_rgb(self.base24Theme[13]),
		)
		dpg.add_text(helpers.stringSentencecase(item["help"]))

	def _helpFlagWidget(self, item: types.Item) -> None:
		with dpg.group(horizontal=False):
			self._helpText(item)
			dpg.add_checkbox(tag=item["dest"], default_value=(item["default"] or False))

	def _helpTextWidget(self, item: types.Item) -> None:
		with dpg.group(horizontal=False):
			self._helpText(item)
			dpg.add_input_text(tag=item["dest"], default_value=(item["default"] or ""))

	def _helpCounterWidget(self, item: types.Item) -> None:
		with dpg.group(horizontal=False):
			self._helpText(item)
			dpg.add_input_float(
				tag=item["dest"],
				default_value=float(item["default"] or 0),
				min_value=-(2**16),
				max_value=2**16,
				step=1,
				step_fast=10,
			)

	def _helpFileWidget(self, item: types.Item) -> None:
		with dpg.group(horizontal=False):
			self._helpText(item)
			dpg.add_input_text(tag=item["dest"], default_value=(item["default"] or ""))

	def _helpDropdownWidget(self, item: types.Item) -> None:
		with dpg.group(horizontal=False):
			self._helpText(item)
			dpg.add_combo(tag=item["dest"], items=item["additional_properties"]["choices"])

	def addWidgetFromItem(self, item: types.Item) -> None:
		"""Select a widget based on the item type.

		:param types.Item item: the item
		"""
		functionMap = {
			types.ItemType.Bool: self._helpFlagWidget,
			types.ItemType.File: self._helpFileWidget,
			types.ItemType.Choice: self._helpDropdownWidget,
			types.ItemType.Int: self._helpCounterWidget,
			types.ItemType.Text: self._helpTextWidget,
		}
		if item["type"] in functionMap:
			return functionMap[item["type"]](item)
		return None

	def addItemsAndGroups(
		self,
		section: types.Group,
	) -> list[types.Item]:
		"""Items and groups and return a list of these so we can get values from the dpg widgets.

		:param types.Group section: section with a name to display and items
		:return list[types.Item]: flattened list of items
		"""
		dpg.add_text(
			f'=== {helpers.stringTitlecase(section["name"], " ")} ===',
			color=hex_to_rgb(self.base24Theme[14]),
		)

		items = []

		for item in section["arg_items"]:
			if item["type"] == types.ItemType.RadioGroup:
				rGroup = item["additional_properties"]["radio"]
				for rElement in rGroup:
					self.addWidgetFromItem(rElement)
					items.append(rElement)
			else:
				self.addWidgetFromItem(item)
				items.append(item)
		for group in section["groups"]:
			items.extend(self.addItemsAndGroups(group))

		return items

	def open_menu_item(self, sender: str, _app_data: None) -> None:
		"""Open a menu item.

		:param _type_ sender: file to open
		:param _type_ _app_data: [unused]
		"""
		f = Path(sender)
		if f.is_file():
			with dpg.window(label=f.name, width=825, height=400, horizontal_scrollbar=True):
				dpg.add_text(helpers.read_file(sender))
		else:
			with dpg.window(label="Error"):
				dpg.add_text(f"File {sender} Not Found :(")

	def main(
		self,
		buildSpec: types.FullBuildSpec,
		quit_callback: Callable[[], None],
		run_callback: Callable[[dict[str, Any]], None],
	) -> None:
		"""Run the gui (dpg) with a given buildSpec, quit_callback, and run_callback.

		- Theming + Configure dpg
		- Menu Prep
		- Create Window, set up Menu and Widgets
		- Then, start dpg

		:param types.FullBuildSpec buildSpec: Full cli parse/ build spec
		:param Callable[[], None] quit_callback: generic callable used to quit
		:param Callable[[dict[str, Any]], None] run_callback: generic callable used to run
		"""

		################
		# Theming + Configure dpg
		################

		dpg.create_context()
		with dpg.font_registry():
			default_font = dpg.add_font(f"{THISDIR}/FiraCode-Regular.ttf", 17)

		with dpg.theme() as global_theme, dpg.theme_component(dpg.mvAll):
			dpg.add_theme_color(
				dpg.mvThemeCol_WindowBg,
				hex_to_rgb(self.base24Theme[16]),
				category=dpg.mvThemeCat_Core,
			)
			dpg.add_theme_color(
				dpg.mvThemeCol_FrameBg,
				hex_to_rgb(self.base24Theme[17]),
				category=dpg.mvThemeCat_Core,
			)
			dpg.add_theme_color(
				dpg.mvThemeCol_PopupBg,
				hex_to_rgb(self.base24Theme[17]),
				category=dpg.mvThemeCat_Core,
			)
			dpg.add_theme_color(
				dpg.mvThemeCol_FrameBgActive,
				hex_to_rgb(self.base24Theme[17]),
				category=dpg.mvThemeCat_Core,
			)
			dpg.add_theme_color(
				dpg.mvThemeCol_FrameBgHovered,
				hex_to_rgb(self.base24Theme[17]),
				category=dpg.mvThemeCat_Core,
			)
			dpg.add_theme_color(
				dpg.mvThemeCol_Text,
				hex_to_rgb(self.base24Theme[6]),
				category=dpg.mvThemeCat_Core,
			)
			dpg.add_theme_color(
				dpg.mvThemeCol_MenuBarBg,
				hex_to_rgb(self.base24Theme[0]),
				category=dpg.mvThemeCat_Core,
			)
			dpg.add_theme_color(
				dpg.mvThemeCol_ScrollbarBg,
				hex_to_rgb(self.base24Theme[2]),
				category=dpg.mvThemeCat_Core,
			)
			dpg.add_theme_color(
				dpg.mvThemeCol_ScrollbarGrab,
				hex_to_rgb(self.base24Theme[17]),
				category=dpg.mvThemeCat_Core,
			)
			dpg.add_theme_color(
				dpg.mvThemeCol_Header,
				hex_to_rgb(self.base24Theme[0]),
				category=dpg.mvThemeCat_Core,
			)
			dpg.add_theme_color(
				dpg.mvThemeCol_HeaderHovered,
				hex_to_rgb(self.base24Theme[1]),
				category=dpg.mvThemeCat_Core,
			)
			dpg.add_theme_color(
				dpg.mvThemeCol_HeaderActive,
				hex_to_rgb(self.base24Theme[1]),
				category=dpg.mvThemeCat_Core,
			)
			dpg.add_theme_color(
				dpg.mvThemeCol_ScrollbarGrabActive,
				hex_to_rgb(self.base24Theme[1]),
				category=dpg.mvThemeCat_Core,
			)
			dpg.add_theme_color(
				dpg.mvThemeCol_ScrollbarGrabHovered,
				hex_to_rgb(self.base24Theme[1]),
				category=dpg.mvThemeCat_Core,
			)
			dpg.add_theme_color(
				dpg.mvThemeCol_Button,
				hex_to_rgb(self.base24Theme[1]),
				category=dpg.mvThemeCat_Core,
			)
			dpg.add_theme_color(
				dpg.mvThemeCol_ButtonHovered,
				hex_to_rgb(self.base24Theme[2]),
				category=dpg.mvThemeCat_Core,
			)
			dpg.add_theme_color(
				dpg.mvThemeCol_ButtonActive,
				hex_to_rgb(self.base24Theme[2]),
				category=dpg.mvThemeCat_Core,
			)
			dpg.add_theme_color(
				dpg.mvThemeCol_Border,
				hex_to_rgb(self.base24Theme[2]),
				category=dpg.mvThemeCat_Core,
			)
			dpg.add_theme_color(
				dpg.mvThemeCol_BorderShadow,
				hex_to_rgb(self.base24Theme[2]),
				category=dpg.mvThemeCat_Core,
			)
			dpg.add_theme_color(
				dpg.mvThemeCol_CheckMark,
				hex_to_rgb(self.base24Theme[14]),
				category=dpg.mvThemeCat_Core,
			)
			dpg.add_theme_color(
				dpg.mvThemeCol_TitleBg,
				hex_to_rgb(self.base24Theme[1]),
				category=dpg.mvThemeCat_Core,
			)
			dpg.add_theme_color(
				dpg.mvThemeCol_TitleBgActive,
				hex_to_rgb(self.base24Theme[14]),
				category=dpg.mvThemeCat_Core,
			)
			dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)
			dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 1, category=dpg.mvThemeCat_Core)

		dpg.bind_theme(global_theme)
		dpg.bind_font(default_font)

		################
		# Menu Prep
		################

		if len(buildSpec["menu"]) == 0:
			buildSpec["menu"] = {}

		elif isinstance(buildSpec["menu"], str):
			buildSpec["menu"] = {"File": buildSpec["menu"]}

		################
		# Create Window, set up Menu and Widgets
		################

		dpg.create_viewport(
			title=buildSpec["program_name"],
			width=875,
			height=min(max(400, 120 * buildSpec["max_args_shown"]), 1080),
		)

		with dpg.window(label="", tag="primary"):
			if len(buildSpec["menu"]) > 0:
				with dpg.menu_bar(), dpg.menu(label="Open"):
					for menu_item in buildSpec["menu"]:
						dpg.add_menu_item(
							label=menu_item,
							tag=buildSpec["menu"][menu_item],
							callback=self.open_menu_item,
						)
			# Program Description
			dpg.add_text(
				helpers.stringSentencecase(
					buildSpec["program_description"] or buildSpec["parser_description"]
				)
			)

			# Add widgets
			items = []
			for widget in buildSpec["widgets"]:
				items.extend(self.addItemsAndGroups(widget))

			# Define "Run" and "Exit" buttons
			def _run_callback() -> None:
				_items = [item for item in items if "dest" in item]
				myd = {item["dest"]: dpg.get_value(item["dest"]) for item in _items}
				run_callback(myd)

			def close_dpg() -> None:
				dpg.destroy_context()
				quit_callback()

			dpg.add_button(label="Run", callback=_run_callback)
			dpg.add_button(label="Exit", callback=close_dpg)

		################
		# Start dpg
		################

		dpg.setup_dearpygui()
		dpg.show_viewport()
		dpg.set_primary_window(window="primary", value=True)
		dpg.start_dearpygui()
		dpg.destroy_context()
