#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO https://github.com/abhirooptalasila/AutoSub/issues/60 -> gui version

import os
import re
import sys
import wave
#from . import logger
import argparse

#import numpy as np
#from tqdm import tqdm

#from cli2gui import Cli2Gui
from . import Cli2Gui # demo

#from .utils import *
#from .writeToFile import write_to_file
#from .audioProcessing import extract_audio
#from .segmentAudio import remove_silent_segments

#_logger = logger.setup_applevel_logger(__name__)

# Line count for SRT file
#line_count = 1

def run(args):
    print("this is the run function")
    print(args)

def main():
    # run the CLI version
    global line_count

    supported_output_formats = ["srt", "vtt", "txt"]
    supported_engines = ["stt", "ds"]

    parser = argparse.ArgumentParser(description="AutoSub")
    #parser = gooey.GooeyParser(description="AutoSub")
    main_args = parser.add_argument_group(
        #"Main",
        "Main Options",
    )
    main_args.add_argument(
        "--file",
        type=argparse.FileType("r"),
        required=False,
        help="Input video file"
    )
    main_args.add_argument(
        "--format",
        choices=supported_output_formats,
        nargs="+",
        help="Subtitles Output formats",
        default=supported_output_formats[0]
    )
    main_args.add_argument(
        "--engine",
        type=argparse._MutuallyExclusiveGroup,
        choices=supported_engines,
        #nargs="?", # TODO what is nargs
        default=supported_engines[0],
        help=f"Engine for speech recognition: STT or DeepSpeech. Default is {supported_engines[0]}"
    )
    # TODO output directory
    extra_args = parser.add_argument_group(
        #"Extra",
        "Extra Options",
    )
    extra_args.add_argument(
        "--dry-run",
        #type=argparse._StoreTrueAction,
        dest="dry_run",
        action="store_true",
        help=(
            "Don't run, only verify options. Also useful to populate " +
            "cuda/tensorflow cache before running multiple times"
        )
    )
    extra_args.add_argument(
        "--split-duration",
        dest="split_duration",
        type=float,
        default=5,
        help="Split sentences longer than X seconds into multiple subtitle frames"
    )
    extra_args.add_argument(
        "--model",
        type=argparse.FileType("r"),
        required=False,
        help="Optional *.pbmm model file"
    )
    extra_args.add_argument(
        "--scorer",
        type=argparse.FileType("r"),
        required=False,
        help="Optional *.scorer file"
    )

    args = parser.parse_args()

    run(args)


cli2gui_decorate = Cli2Gui(
    run_function=run,
    auto_enable=True,
    #gui="pysimplegui", # default
    #gui="pysimpleguiqt",
    program_name="AutoSub",
    program_description="Generate subtitles for videos with offline speech recognition",
)


# The gui function can be used as a GUI entrypoint
# Example: python -m mymodule:main.gui
gui = cli2gui_decorate(main)

if __name__ == "__main__":
    # TODO detect if run from terminal
    # os.environ["TERM"] etc
    if len(sys.argv) > 1:
        main()
    else:
        gui()
