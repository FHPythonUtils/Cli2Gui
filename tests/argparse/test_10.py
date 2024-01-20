import argparse
import sys
from pathlib import Path

THISDIR = Path(__file__).resolve().parent
sys.path.insert(0, str(THISDIR.parent.parent))
from cli2gui import Cli2Gui


def run(args: argparse.Namespace) -> None:
	print(args)


def main() -> None:
	parser = argparse.ArgumentParser(description="this is an example parser")
	subparsers = parser.add_subparsers(help="types of A")
	parser.add_argument(
		"-v",
	)

	a_parser = subparsers.add_parser("A")
	_b_parser = subparsers.add_parser("B")

	a_parser.add_argument("something", choices=["a1", "a2"])

	args = parser.parse_args()
	run(args)


decorator_function = Cli2Gui(
	run_function=run,
	auto_enable=True,
)

gui = decorator_function(main)

if __name__ == "__main__":
	gui()
