import mediacloud, datetime
import configparser
import matplotlib.pyplot as plt
import numpy as np
import logging

# sources for all logging stuff: http://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/
# AND https://docs.python.org/3/howto/logging.html
logging.basicConfig(filename="logs.txt", level=logging.INFO)
logger = logging.getLogger(__name__)

## source for "test-driven" style: https://github.com/rahulbot/Programming-Style-Examples/blob/master/test-driven.py)
class MediaCloud:

    def get_api_key(self):
        logger.info('Getting API key from config file...')
        config = configparser.ConfigParser()
        try:
            config.read('../config.ini')
            self.api_key = config['MEDIACLOUD']['api_key']
        except (SystemExit, KeyboardInterrupt):
            raise
        except Exception:
            logger.error('Failed to read file', exc_info=True)

    def make_mc_connection(self):
        self.mc_connection = mediacloud.api.MediaCloud(self.api_key)
        if self.mc_connection is None:
            logger.error('Cannot make connection.')
        # return self.mc_connection

    # request is call to Media Cloud API
    # 1st arg is tuple of search term strings
    # 2nd argument is date tuple (Y, M, D)
    # 3rd argument is date tuple (Y, M, D)
    def handle_request(self, search_tuple, start_date, end_date):
        self.get_api_key()
        self.make_mc_connection()
        logger.info('Handling request...')
        logger.info('Search term(s): %s', search_tuple)
        logger.info('Start date: %s', start_date)
        logger.info('End date: %s', end_date)
        result = self.mc_connection.sentenceCount(str(search_tuple), solr_filter=[self.mc_connection.publish_date_query(datetime.date(start_date[0], start_date[1], start_date[2]), datetime.date(end_date[0], end_date[1], end_date[2])) ])
        logger.info('Return result: %s', result)
        return result

## Make MediaCloud object
media_cloud = MediaCloud()

## Beginner HW: 2016 election research question
trump_res = media_cloud.handle_request(('Trump'), (2016, 9, 1), (2016, 9, 30))
clinton_res = media_cloud.handle_request(('Clinton'), (2016, 9, 1), (2016, 9, 30))
print(trump_res['count']) #1917105
print(clinton_res['count']) #1267285
# "Did US Mainstream Media sources talk about Trump or Clinton more in September 2016?" --> Trump

## Intermediate HW: abortion research question
res_2015 = media_cloud.handle_request(('abortion'), (2015, 1, 1), (2015, 12, 31))
res_2016 = media_cloud.handle_request(('abortion'), (2016, 1, 1), (2016, 12, 31))
print(res_2015['count']) #607293
print(res_2016['count']) #833234
# "Was abortion talked about more in 2015 or 2016?" --> 2016

objects = ('Trump', 'Clinton')
y_pos = np.arange(len(objects))
plt.bar(y_pos, [trump_res['count'], clinton_res['count']], align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('# of Times Mentioned')
plt.title('Word Frequency of US Mainstream Media in September 2016')
plt.show()
