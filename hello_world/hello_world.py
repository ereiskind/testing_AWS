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

log = logging.getLogger(__name__)

args = getResolvedOptions(sys.argv, ["name"])

log.info("Start logging")
print(f"Hello, {args['name']}!")
log.info("End logging")