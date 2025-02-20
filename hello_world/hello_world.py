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
    print(f"A random number between 1 and 100: {random.randint(1, 100)}")
except Exception as e:
    print(f"`random.randint()` caused exception {e}")

log.info("End logging")