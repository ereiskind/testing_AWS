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

print(f"Initial `logging.root.manager.__dict__`:\n{logging.root.manager.__dict__}")
log1 = logging.getLogger("log1")
print(f"`log1`: {log1}\n{log1.__dict__}")
print(f"`logging.root.manager.__dict__` after 'log1' creation:\n{logging.root.manager.__dict__}")
configure_logging()
print(f"`logging.root.manager.__dict__` after function call:\n{logging.root.manager.__dict__}")
log2 = logging.getLogger("log2")
print(f"`log2`: {log2}\n{log2.__dict__}")
print(f"`logging.root.manager.__dict__` after 'log2' creation:\n{logging.root.manager.__dict__}")

args = getResolvedOptions(sys.argv, ["name"])

if __name__ == '__main__':
    statement = f", {args['name']}!"
    print("Hello" + statement)
    log.debug("This a debug statement")
    log.info("This an info statement")
    log.warning("This a warning statement")
    log.error("This an error statement")
    log.critical("This a critical statement")
    print("Goodbye" + statement)