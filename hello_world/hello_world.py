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
    print(f"`logging.root.manager.__dict__` at end of function:\n{logging.root.manager.__dict__}")

name_log = logging.getLogger(__name__)
configure_logging()
print(f"`logging.root.manager.__dict__` after function call:\n{logging.root.manager.__dict__}")
log2 = logging.getLogger("log2")
print(f"`log2`: {log2}\n{log2.__dict__}")
print(f"`logging.root.manager.__dict__` after 'log2' creation:\n{logging.root.manager.__dict__}")

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