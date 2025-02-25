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
#TEST:print(f"`logging.root.manager.loggerDict['name_log']`: {logging.root.manager.loggerDict['name_log']}\n{logging.root.manager.loggerDict['name_log'].__dict__}")
print(f"`logging.root.manager.loggerDict` after `name_log`: {logging.root.manager.loggerDict}")
configure_logging()
test1_log = logging.getLogger("test1_log")
print(f"`test1_log`: {test1_log}\n{test1_log.__dict__}")
print(f"`logging.root.manager.loggerDict` after `test1_log`: {logging.root.manager.loggerDict}")
#TEST:print(f"`logging.root.manager.loggerDict['test1_log']`: {logging.root.manager.loggerDict['test1_log']}\n{logging.root.manager.loggerDict['test1_log'].__dict__}")
logging.basicConfig(level=logging.DEBUG)
test2_log = logging.getLogger("test2_log")
print(f"`test2_log`: {test2_log}\n{test2_log.__dict__}")
print(f"`logging.root.manager.loggerDict` after `test2_log`: {logging.root.manager.loggerDict}")
#TEST:print(f"`logging.root.manager.loggerDict['test2_log']`: {logging.root.manager.loggerDict['test2_log']}\n{logging.root.manager.loggerDict['test2_log'].__dict__}")

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