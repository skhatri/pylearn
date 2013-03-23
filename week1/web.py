import urllib

website = urllib.urlopen('https://raw.github.com/skhatri/pylearn/master/week1/exercise.py')
exercise = website.read()

print "Exercise"
print exercise
