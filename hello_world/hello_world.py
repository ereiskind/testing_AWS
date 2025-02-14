import sys
from awsglue.utils import getResolvedOptions

args = getResolvedOptions(sys.argv, [
    "arg1",
    "arg2",
])

print("Hello, world!")