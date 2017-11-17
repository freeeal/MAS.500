import mediacloud, datetime
import configparser
import matplotlib.pyplot as plt
import numpy as np
import logging

# sources for all logging stuff: http://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/
# AND https://docs.python.org/3/howto/logging.html
logging.basicConfig(filename="logs.txt", level=logging.INFO)
logger = logging.getLogger(__name__)

def get_api_key():
    logger.info('Getting API key from config file...')
    config = configparser.ConfigParser()
    try:
        config.read('../config.ini')
        return config['MEDIACLOUD']['api_key']
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        logger.error('Failed to read file', exc_info=True)

def make_mc_connection(api_key):
    mc_connection = mediacloud.api.MediaCloud(mc_api_key)
    if mc_connection is None:
        logger.error('Cannot make connection.')
    return mc_connection

mc_api_key = get_api_key()
mc = make_mc_connection(mc_api_key)

# request is call to Media Cloud API
# 1st arg is tuple of search term strings
# 2nd argument is date tuple (Y, M, D)
# 3rd argument is date tuple (Y, M, D)
def handle_request(search_tuple, start_date, end_date):
    logger.info('Handling request...')
    logger.info('Search term(s): %s', search_tuple)
    logger.info('Start date: %s', start_date)
    logger.info('End date: %s', end_date)
    result = mc.sentenceCount(str(search_tuple), solr_filter=[mc.publish_date_query(datetime.date(start_date[0], start_date[1], start_date[2]), datetime.date(end_date[0], end_date[1], end_date[2])) ])
    logger.info('Return result: %s', result)
    return result

## Beginner HW: 2016 election research question
# trump_res = mc.sentenceCount('(Trump)', solr_filter=[mc.publish_date_query(datetime.date(2016, 9, 1), datetime.date(2016, 9, 30)) ])
# clinton_res = mc.sentenceCount('(Clinton)', solr_filter=[mc.publish_date_query(datetime.date(2016, 9, 1), datetime.date(2016, 9, 30)) ])
trump_res = handle_request(('Trump'), (2016, 9, 1), (2016, 9, 30))
clinton_res = handle_request(('Clinton'), (2016, 9, 1), (2016, 9, 30))
print(trump_res['count']) #1917105
print(clinton_res['count']) #1267285
# "Did US Mainstream Media sources talk about Trump or Clinton more in September 2016?" --> Trump

## Intermediate HW: abortion research question
res_2015 = mc.sentenceCount('(abortion)', solr_filter=[mc.publish_date_query(datetime.date(2015, 1, 1), datetime.date(2015, 12, 31)) ])
res_2016 = mc.sentenceCount('(abortion)', solr_filter=[mc.publish_date_query(datetime.date(2016, 1, 1), datetime.date(2016, 12, 31)) ])
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
