#! /usr/bin/python3
# -*- coding: utf-8 -*-

import logging

from src.gitlab_http_logger import GitlabHTTPHandler

h = GitlabHTTPHandler(
    webhook_url="<your webhook url>",
    auth_key="<your auth key>",
    title="Example App 1"
)
h.setLevel(logging.WARNING)
logging.getLogger().addHandler(h)

logging.warning("Test warning!")
