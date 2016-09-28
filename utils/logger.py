import logging


def get_logger(app):
	app.logger.addHandler(logging.FileHandler('app.log'))
	app.logger.setLevel(logging.INFO)
	return app.logger
