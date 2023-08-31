import argparse
import sys
from pathlib import Path

THISDIR = Path(__file__).resolve().parent
sys.path.insert(0, str(THISDIR.parent.parent))
from cli2gui import Cli2Gui


def run(args):
	print(args.arg)


def main():
	parser = argparse.ArgumentParser(description="this is an example parser")
	parser.add_argument("--arg", type=str, default="foo", help="keyword arg")
	parser.add_argument("--bool", action="store_true", default=True, help="boolean arg")
	args = parser.parse_args()
	run(args)


decorator_function = Cli2Gui(
	run_function=run,
	auto_enable=True,
)

gui = decorator_function(main)

if __name__ == "__main__":
	gui()
