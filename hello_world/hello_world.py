import sys
import logging
from awsglue.utils import getResolvedOptions

def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format= "[%(asctime)s] %(name)s::%(lineno)d - %(message)s",  # "[timestamp] module name::line number - error message"
        datefmt="%Y-%m-%d %H:%M:%S",
        encoding="utf-8",
    )

print(f"`logging` before (type {type(logging)}): {logging}")
configure_logging()
print(f"`logging` after (type {type(logging)}): {logging}")
log = logging.getLogger(__name__)
print(f"`log` (type {type(log)}): {log}")

args = getResolvedOptions(sys.argv, ["name"])

log.info("Start logging")
print(f"Hello, {args['name']}!")

try:
    df = pandas.DataFrame(
        [
            [1, 10, "a"],
            [2, 20, "b"],
            [3, 30, "c"],
        ],
        columns=["one", "two", "three"],
    )
    print(df)
except Exception as e1:
    print(f"`pandas.DataFrame()` without import caused exception {e1}")
    try:
        import pandas
        df = pandas.DataFrame(
            [
                [1, 10, "a"],
                [2, 20, "b"],
                [3, 30, "c"],
            ],
            columns=["one", "two", "three"],
        )
        print(df)
    except Exception as e2:
        print(f"`pandas.DataFrame()` with import caused exception {e2}")

log.info("End logging")