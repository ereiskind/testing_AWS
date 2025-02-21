import sys
import logging
from awsglue.utils import getResolvedOptions
import subprocess

freeze = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
print(freeze)

def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format= "[%(asctime)s] %(name)s::%(lineno)d - %(message)s",  # "[timestamp] module name::line number - error message"
        datefmt="%Y-%m-%d %H:%M:%S",
        encoding="utf-8",
    )
    print("`configure_logging()` ran")

log = logging.getLogger(__name__)
print(f"`log` and `log.__dict__` before function:\n{log}\n{log.__dict__}")
configure_logging()
print(f"`log` and `log.__dict__` after function:\n{log}\n{log.__dict__}")

args = getResolvedOptions(sys.argv, ["name"])

print(f"Hello, {args['name']}!")
log.debug("This a debug statement")
log.info("This an info statement")
log.warning("This a warning statement")
log.error("This an error statement")
log.critical("This a critical statement")
print(f"Goodbye, {args['name']}!")