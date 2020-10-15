# #!/bin/sh -ex
# celery -A pdf_pro worker --loglevel=info  &
# celery -A pdf_pro beat --pidfile=  -l info -S django &
# tail -f  /dev/null