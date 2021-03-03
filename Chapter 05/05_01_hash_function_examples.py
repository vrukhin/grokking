#!/usr/bin/python

voted = dict()

def check_voter(name):

	if voted.get(name):
		print("Kick them out")
	else:
		voted[name] = True
		print("Let them vote")


check_voter("Tom")
check_voter("Mike")
check_voter("Mike")


cache = dict()

def get_page(url):
	if cache.get(url):
		return cache[url]
	else:
		data = get_data_from_server(url)
		cache[url] = data
		return data
