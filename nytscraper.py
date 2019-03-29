import argparse
import os
import json
import csv
from nytcomments.nytcomments import get_dataset , get_comments, get_replies

def main(args):



    ARTICLE_API_KEY = args.key
    query = args.query
    dates = args.date

    articles_df, comments_df = get_comments(ARTICLE_API_KEY, save=True, query=query, page_lower=0, page_upper=2, begin_date=dates, sort='oldest')

    print ("Done")


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--key')
    parser.add_argument('-q' ,'--query')
    parser.add_argument('-d', '--date')
    args = parser.parse_args()
    main(args)