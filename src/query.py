import logging
import os
import sys
import argparse
from sds.SdsQuery import query_rag

from sds.SdsReader import loadDocumentsInDir
from sds.SdsSpitter import addToChromadb, splitDocuments


def main():
    """ Extract a specified file
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text
    query_rag(query_text)
    text = query_rag(query_text=query_text)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
