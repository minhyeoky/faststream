# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/Uvicorn_Helpers.ipynb.

# %% auto 0
__all__ = ['run_uvicorn']

# %% ../nbs/Uvicorn_Helpers.ipynb 1
from typing import *
from contextlib import contextmanager

import multiprocessing

from fastapi import FastAPI
from uvicorn import Config, Server

# %% ../nbs/Uvicorn_Helpers.ipynb 4
@contextmanager
def run_uvicorn(arg: Union[Config, FastAPI]) -> Generator[None, None, None]:
    if isinstance(arg, Config):
        config: Config = arg
    else:
        config = Config(app=arg)

    def run(config=config):
        server = Server(config=config)
        server.run()

    p = multiprocessing.Process(target=run)
    try:
        p.start()
        yield
    except Exception as e:
        print(f"Exception raised {e=}")
    finally:
        p.terminate()
        p.join()
        p.close()