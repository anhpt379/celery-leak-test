#! coding: utf-8
# pylint: disable-msg=W0311
import gc
import celery
from celery.decorators import task

def objects_count():
  gc.collect()
  return len(gc.get_objects())

def write_down(celery_version, count, objects_in_memory):
  filename = celery_version + '.txt'
  open(filename, 'a').write("%s\t%s\n" % (count, objects_in_memory))
  print '%s\t\t%s' % (count, objects_in_memory)
  return True

@task
def foobar():
  return True

if __name__ == "__main__":
  print "Celery version: ", celery.__version__
  print "messages_sent\tobjects_in_memory"
  
  count = 0  
  write_down(celery.__version__, count, objects_count())
  
  while True:
    foobar.delay()
    count += 1 
    if count % 100 == 0:
      write_down(celery.__version__, count, objects_count())