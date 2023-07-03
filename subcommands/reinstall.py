# -*- coding: utf-8 -*-

from argparse import ArgumentParser, Namespace
from pathlib import Path
import subprocess

from flow.commands import create
from flow.config import get_config
from flow.utils import success, error, info


def __exec(_: ArgumentParser, args: Namespace) -> int:
    config = get_config()
    install_dir = config.get("flow_install_dir")

    if install_dir is None:
        error("No install directory found in config file")
        return 1

    install_path = Path(install_dir)
    if not install_path.exists():
        error("Install directory does not exist")
        return 1

    setup_path = install_path / "setup.py"
    if not setup_path.exists():
        error("setup.py not found in install directory")
        return 1

    info("Reinstalling flow from local dev env")
    process = subprocess.run(["python3", "setup.py", "install", "--user"], cwd=install_path)
    if process.returncode != 0:
        error("Failed to reinstall flow from local dev env")
        return process.returncode

    success("Successfully reinstalled flow from local dev env")
    return 0


create("reinstall", "reinstalls flow from local dev env", lambda _: None, __exec)
