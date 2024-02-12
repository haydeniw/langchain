"""The definition of the NVIDIA Riva LangChain server."""

import logging

from fastapi import FastAPI
from langserve import add_routes

from .chain import chain

_LOGGER = logging.getLogger(__name__)

app = FastAPI(
    title="NVIDIA Riva",
    version="0.1.0",
    description="NVIDIA Riva with LangChain.",
)


add_routes(
    app,
    chain,
    path="/chain",
)