#!/usr/bin/env python3
import argparse
import os
import sys
import datetime
import boto
from boto.s3.key import Key


"""
Get most recent backup file

This program provides a command line utility
for obtaining the most recent backup file in
an S3 bucket. This is used to automate and
script restoration of charlesreid1.com 
docker pod from S3 backups.

Usage:
------

        usage: get_most_recent_backup.py [-h] [--prefix PREFIX] [--suffix SUFFIX]
                                     [--printall] [--print] [--download] [--force]
                                     [--download-to DOWNLOAD_TO]
                                     bucket
    
    positional arguments:
      bucket                The name of the AWS S3 bucket to use
    
    optional arguments:
      -h, --help            show this help message and exit
      --prefix PREFIX       Prefix (path to backups) in bucket
      --suffix SUFFIX       Suffix (file extension of backups) in bucket
      --printall            Print a list of *all* matching backup files, sorted by
                            date last modified
      --print               Print a list of *all* matching backup files, sorted by
                            date last modified
      --download            Download the most recent backup file
      --force               Force download the most recent backup file, even if
                            target file already exists on disk
      --download-to DOWNLOAD_TO
                            Location to download the file to (/tmp by default)

Example:
--------

    # Just print the most recent backup file:
    ./get_most_recent_backup.py charlesreid1-wiki-backup --print

    # Download the most recent backup file to a temporary dir
    mkdir /tmp/mybackups/
    ./get_most_recent_backup.py charlesreid1-wiki-backup --download --download-to=/tmp/mybackups

"""


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("bucket", help="The name of the AWS S3 bucket to use")

    parser.add_argument("--prefix",   default="",    help="Prefix (path to backups) in bucket")
    parser.add_argument("--suffix",   default=".gz", help="Suffix (file extension of backups) in bucket")

    # Processed in order of precedence:
    parser.add_argument("--printall", action='store_true', help="Print a list of *all* matching backup files, sorted by date last modified")
    parser.add_argument("--print",    action='store_true', help="Print a list of *all* matching backup files, sorted by date last modified")
    parser.add_argument("--download", action='store_true', help="Download the most recent backup file")

    # Both required for --download
    parser.add_argument("--force",       action='store_true', help="Force download the most recent backup file, even if target file already exists on disk")
    parser.add_argument("--download-to", default="/tmp", help="Location to download the file to (/tmp by default)")

    args = parser.parse_args()
    get_youngest_file(args)


def get_youngest_file(args):
    """
    Get the youngest file from a given S3 bucket,
    and perform the actions specified by the user's
    input flags.
    """

    bucket_name = args.bucket

    # Detect bucket region
    conn = boto.connect_s3()
    bucket = conn.get_bucket(bucket_name)
    bucket_location = bucket.get_location()
    if bucket_location:
        conn = boto.s3.connect_to_region(bucket_location)
        bucket = conn.get_bucket(bucket_name)

    # Get list of files
    bucket_list  = bucket.list(prefix=args.prefix)
    
    # Extract backup files and their modified date
    list_files = []
    for obj in bucket_list:
        if obj.name.endswith(args.suffix):
            date = obj.last_modified
            name = obj.name
            #if obj.name[0:2]=='./':
            #    name = obj.name[2:]
            #else:
            #    name = obj.name
            list_files.append((name,date))

    # Sort by modified date
    list_files.sort(key = lambda x: x[1], reverse=True)

    if args.printall:
        # Fancy print formatting
        print("%-30s %-30s"%("Date Modified","Backup File"))
        print("".join(["-"*30," ","-"*30]))
        for lf in list_files:
            print("%-30s %-30s"%(lf[1],lf[0]))

    elif args.print:
        # list_files[0] is a tuple: 
        # (name, timestamp) of youngest file
        print(list_files[0][0])

    elif args.download:
        most_recent_file_name = list_files[0][0]
        download_target = os.path.join(args.download_to, os.path.basename(most_recent_file_name))

        if os.path.isfile(download_target) and not args.force:
            print("Skipping download of file %s, already exists"%(target_file))
        else:
            key = Key(bucket, most_recent_file_name)
            key.get_contents_to_filename(download_target)


if __name__=="__main__":

    main()

