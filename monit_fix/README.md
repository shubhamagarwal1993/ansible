# Adding monit to ansible scripts
This is an effort to add monit to monitor system details, and alert user when the systems are not performing as expected.

Will store some notes here, and eventually move it to monit's folder in ansible when complete

install using `sudo apt-get install monit`
go to /etc/monit -> all config stored here

writing a custom python file to monitor
create file in conf.d called offline and put following inside it
```
check process offline with pidfile /var/run/offline.pid
  group www
  group nginx
  start program = "/etc/init.d/offline start"
  stop program = "/etc/init.d/offline stop"
  if 5 restarts with 5 cycles then timeout
```

check permission of monitrc. This is the main file that runs all processes in it
`stat -c "%a %n" monitrc`. This should be 700. If not then change it using `sudo chmod 700 monitrc`


