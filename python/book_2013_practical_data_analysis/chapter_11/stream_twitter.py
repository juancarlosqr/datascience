# -*- coding: utf-8 -*-
'''
Created on Sun Oct 7 13:21:35 2018

@author: jc
'''

from twython import TwythonStreamer
import read_twitter as tw

class MyStreamer(TwythonStreamer):

    count_stream = 0
    max_stream = 20

    def on_success(self, data):
        if 'text' in data:
            self.count_stream += 1
            print(f"@{data['user']['screen_name']}: {data['text']}\n")
            if self.count_stream == self.max_stream:
                self.disconnect()

    def on_error(self, status_code, data):
        print(status_code)
        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        # self.disconnect()

if __name__ == '__main__':
    config_twitter = tw.get_config('twitter')
    stream = MyStreamer(
        config_twitter['consumer_key'],
        config_twitter['consumer_secret'],
        config_twitter['access_token'],
        config_twitter['access_secret']
    )
    stream.statuses.filter(track='china')