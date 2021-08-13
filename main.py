# Tim tutorial start episode 1
#    https://www.youtube.com/watch?v=_fx7FQ3SP0U
#
from ponglogger import PongLogger, MyLoggerBase
from server import Server
import argparse
from logging import INFO
import auxiliary_module

logger = PongLogger()
logger.log(INFO, "This is the shell logger, not much to see here")


# class A(MyLoggerBase):
#     pass
#
#
# a = A()
# a.log(INFO, "£AAA")
#
# logger.info('creating an instance of auxiliary_module.Auxiliary')
# a = auxiliary_module.Auxiliary()
# logger.info('created an instance of auxiliary_module.Auxiliary')
# logger.info('calling auxiliary_module.Auxiliary.do_something')
# a.do_something()
# logger.info('finished auxiliary_module.Auxiliary.do_something')
# logger.info('calling auxiliary_module.some_function()')
# auxiliary_module.some_function()
# logger.info('done with auxiliary_module.some_function()')


def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage="%(prog)s --server for server mode",
        description="Pong client."
    )
    parser.add_argument(
        "-v", "--version", action="version",
        version=f"{parser.prog} version 1.0.0"
    )
    parser.add_argument(
        "-s", "--server", action="store_true"
    )
    return parser


parser = init_argparse()
args = parser.parse_args()


if args.server:
    logger.info("Starting a server")
    s = Server()
    s.run()
else:
    logger.info("Starting a client")
    from client import Client

    cl = Client()
    cl.run_game()
