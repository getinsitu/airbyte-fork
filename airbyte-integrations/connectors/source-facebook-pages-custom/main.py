#
# Copyright (c) 2024 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_facebook_pages_custom import SourceFacebookPagesCustom

if __name__ == "__main__":
    source = SourceFacebookPagesCustom()
    launch(source, sys.argv[1:])
