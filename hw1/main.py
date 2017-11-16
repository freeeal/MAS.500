import mediacloud, datetime
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
mc_api_key = config['MEDIACLOUD']['api_key']

mc = mediacloud.api.MediaCloud(mc_api_key)
trump_res = mc.sentenceCount('(Trump)', solr_filter=[mc.publish_date_query(datetime.date(2016, 9, 1), datetime.date(2016, 9, 30)) ])
clinton_res = mc.sentenceCount('(Clinton)', solr_filter=[mc.publish_date_query(datetime.date(2016, 9, 1), datetime.date(2016, 9, 30)) ])
print(trump_res['count']) #1917105
print(clinton_res['count']) #1267285
# "Did US Mainstream Media sources talk about Trump or Clinton more in September 2016?" --> Trump
