import logging
from logging.handlers import TimedRotatingFileHandler

class Logger():
    def __init__(self, logger_name='apiframework'):
        # 创建一个logger实例，如果参数为空则返回root logger
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        self.log_file_name = './testout/test.log'
        self.backup_count = 5

        # 日志输出级别
        self.console_output_level = 'DEBUG'
        self.file_output_level = 'DEBUG'

        # 日志输出格式
        self.formatter = logging.Formatter('%(asctime)s|%(levelname)8s|%(filename)10s:%(lineno)4s|%(message)s')

    def get_logger(self):
        '''在logger日志中添加日志句柄并返回，如果logger句柄已经存在，则直接返回'''
        if not self.logger.handlers:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)

            # 每天重新创建一个日志文件，最多保留backup_count份
            file_handler = TimedRotatingFileHandler( self.log_file_name,
                                                    when='D',
                                                    interval=1,
                                                    backupCount=self.backup_count,
                                                    delay=True,
                                                    encoding='utf-8'
                                                    )
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger


logger = Logger().get_logger()

if __name__ == '__main__':
    print(logger)