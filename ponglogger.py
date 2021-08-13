import logging
import datetime as dt

# todo: mixin base class loggers
# https://stackoverflow.com/questions/29069655/python-logging-with-a-common-logger-class-mixin-and-class-inheritance


class PongLogger():
    class MyFormatter(logging.Formatter):
        converter = dt.datetime.fromtimestamp

        def formatTime(self, record, datefmt=None):
            ct = self.converter(record.created)
            if datefmt:
                s = ct.strftime(datefmt)
            else:
                t = ct.strftime("%Y-%m-%d %H:%M:%S")
                s = "%s,%03d" % (t, record.msecs)
            return s

    def __init__(self, log_name="main", file_name=None):
        if not log_name:
            log_name = '.'.join([i.__name__ for i in self.__class__.mro()[-3::-1]])
        # create logger with 'spam_application'
        logger = logging.getLogger(log_name)
        logger.setLevel(logging.DEBUG)
        logging.StrFormatStyle
        # create file handler which logs even debug messages
        if not file_name:
            file_name = 'pong'
        fh = logging.FileHandler(f"{file_name}.log")
        fh.setLevel(logging.DEBUG)
        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        # create formatter and add it to the handlers
        formatter = PongLogger.MyFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                           datefmt="%d %H:%M:%S.%f")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # add the handlers to the logger
        logger.addHandler(fh)
        logger.addHandler(ch)
        self.logger = logger

    def log(self,  level, *args, **kwargs):
        self.logger.log(level, *args, *kwargs)

    def info(self, *args, **kwargs):
        self.logger.info(*args, *kwargs)

    def debug(self, *args, **kwargs):
        self.logger.debug(*args, *kwargs)

    def error(self, *args, **kwargs):
        self.logger.error(*args, *kwargs)


class MyLoggerBase(PongLogger):

    def __init__(self, name=None, file_name=None):
        super(MyLoggerBase, self).__init__(name, file_name)

