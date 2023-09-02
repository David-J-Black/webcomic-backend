import multiprocessing

# Always do 2 * the amount of cpu cores you have? From what i've maybe heard...
workers = multiprocessing.cpu_count() * 2
umask = 0o007
reload = True

#logging
accesslog = '-'
errorlog = '-'