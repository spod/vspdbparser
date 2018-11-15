#! /usr/bin/env python
from __future__ import print_function

# NEWS_URL="http://go.vsb.bc.ca/schools/tupper/dailybulletin/Pages/default.aspx"
TEST_NEWS="test/sample.html"

from vspdbparser import VSBDBParser

def main():
    """CLI Entrypoint."""
    test = open(TEST_NEWS, 'r+').read()
    parser = VSBDBParser()
    parser.feed(test)

if __name__ == "__main__":
    main()
