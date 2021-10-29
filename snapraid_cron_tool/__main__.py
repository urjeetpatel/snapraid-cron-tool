import argparse
from snapraid_cron_tool.utils.config import Config


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--config",
        default="snapraid-cron-tool.conf",
        metavar="CONFIG",
        help="Configuration file (default: %(default)s)",
    )
    parser.add_argument("--no-scrub", action="store_false", dest="scrub", default=None, help="Do not scrub (overrides config)")
    parser.add_argument("--ignore-deletethreshold", action="store_true", help="Sync even if configured delete threshold is exceeded")
    args = parser.parse_args()
    Config.init_config(args.config)


if __name__ == "__main__":
    main()
