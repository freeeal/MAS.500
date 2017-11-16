import mediacloud, datetime
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
mc_api_key = config['MEDIACLOUD']['api_key']
mc = mediacloud.api.MediaCloud(mc_api_key)

## Beginner HW: 2016 election research question
trump_res = mc.sentenceCount('(Trump)', solr_filter=[mc.publish_date_query(datetime.date(2016, 9, 1), datetime.date(2016, 9, 30)) ])
clinton_res = mc.sentenceCount('(Clinton)', solr_filter=[mc.publish_date_query(datetime.date(2016, 9, 1), datetime.date(2016, 9, 30)) ])
print(trump_res['count']) #1917105
print(clinton_res['count']) #1267285
# "Did US Mainstream Media sources talk about Trump or Clinton more in September 2016?" --> Trump

## Intermediate HW: abortion research question
res_2015 = mc.sentenceCount('(abortion)', solr_filter=[mc.publish_date_query(datetime.date(2015, 1, 1), datetime.date(2015, 12, 31)) ])
res_2016 = mc.sentenceCount('(abortion)', solr_filter=[mc.publish_date_query(datetime.date(2016, 1, 1), datetime.date(2016, 12, 31)) ])
print(res_2015['count']) #607293
print(res_2016['count']) #833234
# "Was abortion talked about more in 2015 or 2016?" --> 2016
