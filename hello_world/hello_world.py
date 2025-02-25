import sys
import logging
from awsglue.utils import getResolvedOptions
import subprocess

freeze = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
print(freeze)

def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(name)s::%(lineno)d - %(message)s",  # "[timestamp] module name::line number - error message"
        datefmt="%Y-%m-%d %H:%M:%S",
        encoding="utf-8",
    )

name_log = logging.getLogger(__name__)
print(f"`name_log` before `basicConfig`: {name_log}")
logging.basicConfig(level=logging.DEBUG)
print(f"`name_log` before `basicConfig`: {name_log}")

args = getResolvedOptions(sys.argv, ["name"])

if __name__ == '__main__':
    statement = f", {args['name']}!"
    print("Hello" + statement)
    name_log.debug("This a debug statement")
    name_log.info("This an info statement")
    name_log.warning("This a warning statement")
    name_log.error("This an error statement")
    name_log.critical("This a critical statement")
    print("Goodbye" + statement)