import sys
import logging
from awsglue.utils import getResolvedOptions
import subprocess
from random import choice


def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(name)s::%(lineno)d - %(message)s",  # "[timestamp] module name::line number - error message"
        datefmt="%Y-%m-%d %H:%M:%S",
        encoding="utf-8",
        force=True,
    )

log = logging.getLogger(__name__)


#Section: Check Packages
freeze = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
log.info(f"The installed packages:\n{freeze}")


#Section: Check Input Ingest
args = getResolvedOptions(sys.argv, [
    "first_input",
    "second_input"
])

statement = f", {args['first_input']}!"
log.info("Hello" + statement)
for i in len(args['second_input']):
    log.warning(choice(args['second_input']))
log.info("Goodbye" + statement)