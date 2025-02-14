import sys
from awsglue.utils import getResolvedOptions

args = getResolvedOptions(sys.argv, [
    "name",
    "arg2",
])

print(f"Hello, {args['name']}!")