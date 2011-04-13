#! coding: utf-8
# pylint: disable-msg=W0311
import gc
import celery
from celery.decorators import task

def objects_count():
  gc.set_debug(gc.DEBUG_SAVEALL)
  gc.collect()
  return len(gc.get_objects())

def write_down(celery_version, count, objects_in_memory):
  filename = celery_version + '.txt'
  open(filename, 'a').write("%s\t%s\n" % (count, objects_in_memory))
  return True
  

@task
def foobar():
  return True

if __name__ == "__main__":
  print "Celery version: ", celery.__version__
  
  count = 0
  objects_in_memory = objects_count()
  
  print "At the beginning: %s objects in memory" % objects_in_memory
  write_down(celery.__version__, count, objects_in_memory)
  
  while True:
    foobar.delay()
    count += 1
    if count % 100 == 0:
      objects_in_memory = objects_count()
      print "After %s messages sent: %s objects in memory" % (count, objects_in_memory)
      write_down(celery.__version__, count, objects_in_memory)