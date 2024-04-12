# file tornado/simple_httpclient.py:622-682
# lines [622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 633, 634, 644, 645, 647, 648, 649, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 681, 682]
# branches ['627->628', '627->667', '644->647', '644->659', '649->655', '649->659', '667->668', '667->670']

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient, HTTPRequest
from tornado.httpclient import HTTPResponse
from unittest.mock import Mock
import urllib.parse
from tornado.testing import AsyncHTTPTestCase, gen_test
from tornado.web import Application, RequestHandler

class RedirectHandler(RequestHandler):
    def get(self):
        self.redirect("/new_location")

class MainHandler(RequestHandler):
    def get(self):
        self.write("Final destination")

class TestHTTPConnectionFinishRedirect(AsyncHTTPTestCase):
    def get_app(self):
        return Application([
            (r"/redirect", RedirectHandler),
            (r"/new_location", MainHandler),
        ])

    @gen_test
    async def test_http_connection_finish_redirect(self):
        client = SimpleAsyncHTTPClient()
        response = await client.fetch(
            self.get_url("/redirect"),
            method="GET",
            follow_redirects=True,
            max_redirects=1
        )
        assert response.code == 200
        assert response.effective_url.endswith("/new_location")
        client.close()
