import os
import logging


def str2bool(v):
    if v is None:
        return v
    return v.lower() in ('yes', 'true', 't', '1')


PROD = str2bool(os.getenv("PROD", "false"))


