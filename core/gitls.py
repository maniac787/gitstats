import logging
from typing import List

from core import process

GIT_LS_FILES = "git -C '{}' ls-files"


def git_ls_files(repo_path: str) -> List[str]:
    GIT_LS_FILES_PATH = GIT_LS_FILES.format(repo_path)
    logging.info("executing %s", GIT_LS_FILES_PATH)
    return process.execute(GIT_LS_FILES_PATH).split("\n")[0:-1]
