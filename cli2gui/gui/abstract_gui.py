from __future__ import annotations

from abc import ABC, abstractmethod

from cli2gui import types


class AbstractGUI(ABC):
	"""Abstract base class for GUI wrappers."""

	def __init__(self) -> None:
		pass

	@abstractmethod
	def main(
		self, buildSpec: types.FullBuildSpec, menu: list[str], quit_callback, run_callback
	) -> None:
		"""Abstract method for the main function."""
		raise NotImplementedError
