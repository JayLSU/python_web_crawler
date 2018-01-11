# This is a web crawler to dig Wikipedia!

The web crawler is written in python and is a case study project in [Udacity Introduction to Python Programming](https://www.udacity.com/course/introduction-to-python--ud1110)

The crawler starts with a random Wikipedia page and always dig the first link in the main content! The stop conditions are:
	
* 	Arrive at the Wikipedia page for Philosophy.
* 	Arrive a page without any link.
* 	Arrive a page that has been searched for the current run. (That is in a cycle search. a -> b -> c -> a)
* 	Search more than 25 links.

## Enjoy crawling!