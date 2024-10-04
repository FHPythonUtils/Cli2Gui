import asyncio
from threading import Thread

from cli2gui import Cli2Gui

THREAD: Thread = None
import argparse
from pathlib import Path


def main():
	parser = argparse.ArgumentParser(description="Web scraper with aria2c output")
	parser.add_argument(
		"urls_file",
		help="Input file containing URLs",
		type=argparse.FileType("r", encoding="utf-8"),
	)
	parser.add_argument(
		"aria2c_file",
		help="Output file for aria2c download links",
		type=Path,
	)
	parser.add_argument("--timeout", type=int, default=5000, help="Timeout per page (ms)")
	parser.add_argument("--max-workers", type=int, default=2, help="Maximum number of workers")
	parser.add_argument(
		"--save-trace",
		action="store_true",
		help="Save trace files (for debugging only)",
	)
	parser.add_argument(
		"--skip-edge",
		action="store_true",
		help="Don't use Edge",
	)
	args = parser.parse_args()
	blocking_run(args)


def blocking_run(args):
	asyncio.run(run(args))


async def run(args):
	print(args.timeout)


def wrapper(args):
	global THREAD

	if THREAD is not None and THREAD.is_alive():
		print("Task already running")
		return


decorator_function = Cli2Gui(
	run_function=wrapper,
	auto_enable=True,
	program_name="Test program #18",
)


gui = decorator_function(main)

if __name__ == "__main__":
	gui()
