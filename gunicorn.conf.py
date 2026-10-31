bind = "0.0.0.0:8000"
threads = 4
accesslog = "-"
errorlog = "-"
access_log_format = (
    '%({x-real-ip}i)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
)
