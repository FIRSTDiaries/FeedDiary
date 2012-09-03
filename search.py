from twython import Twython

search_list = ['OMGrobots', 'FRC', 'FIRST Robotics', 'Dean Kamen']
# For the sake of testing, added more search terms

for tweet_keyword in search_list:
    
    twitter = Twython()
    search_results = twitter.search(q=tweet_keyword, rpp="100")
    
    for tweet in search_results["results"]:
        print "Tweet from @%s Date: %s" % (tweet['from_user'].encode('utf-8'),tweet['created_at'])
        print tweet['text'].encode('utf-8'),"\n"