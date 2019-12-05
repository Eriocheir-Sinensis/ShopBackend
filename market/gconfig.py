bind                = '127.0.0.1:8000'
workers             = 2
accesslog           = '-'
access_log_format   = '"%({X-Forwarded-For}i)s" %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(L)s'
errorlog            = '-'
worker_class        = 'gevent'
proc_name           = 'api'
graceful_timeout    = 30
limit_request_field_size = 0