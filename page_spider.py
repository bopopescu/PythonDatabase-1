import os
import argparse
import mysql.connector

def main(database: str, url_list_file: str):
    print("open database: {}".format(database))
    print("web page will be scanned: {}".format(url_list_file))
    print("waiting for result")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-db", "--database", help = "SQLite File Name")