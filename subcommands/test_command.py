# -*- coding: utf-8 -*-

from argparse import ArgumentParser, Namespace
from flow.commands import create
from flow.utils import success


def __parser(parser: ArgumentParser) -> None:
    parser.add_argument("name", help="your name")


def __exec(_: ArgumentParser, args: Namespace) -> int:
    success(f"Hello, {args.name}!")
    return 0


create("hello", "your first subcommand", __parser, __exec)
