# -*- coding: utf-8 -*-

from ..base.dead_downloader import DeadDownloader


class TurbouploadCom(DeadDownloader):
    __name__ = "TurbouploadCom"
    __type__ = "downloader"
    __version__ = "0.08"
    __status__ = "stable"

    __pattern__ = r"http://(?:www\.)?turboupload\.com/(\w+)"
    __config__ = []  # TODO: Remove in 0.6.x

    __description__ = """Turboupload.com downloader plugin"""
    __license__ = "GPLv3"
    __authors__ = [("zoidberg", "zoidberg@mujmail.cz")]
