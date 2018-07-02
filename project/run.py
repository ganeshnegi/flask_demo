import os
import redis, time

from wsgi import app

cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
	retries = 5
	while True:
		try:
			return cache.incr('hits')
		except redis.exceptions.ConnectionError as e:
			if retries == 0:
				raise e
				retries -= 1
				time.sleep(0.5)

@app.route('/hello')
@app.route('/')
def index():
	return 'hello'

@app.route('/count')
def index1():
	count = get_hit_count()
	return 'you visited {} times'.format(count)

if __name__ == '__main__':
    app.run()
