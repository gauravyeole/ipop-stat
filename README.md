IPOP Stats
==========

**Warning:** *This is under heavy development, and is not ready for use.*

*Gathers anonymous usage statistics of IPOP users.*

We need these statistics to justify our funding in grant proposals. They're
opt-in only, and the only information we collect is:

-   Your IP address
-   A randomly generated UUID
-   Client version number
-   The number of connections your node makes
-   If STUN or TURN is being used
-   The name of the controller (groupvpn or socialvpn)
-   Statistics about average connection lifetime

We'll never publish full database dumps, but we will publish general statistical
information from our database.

API Documentation
-----------------

The API still needs to be finalized and documented. For now, read the source to
see how the API works.

We follow the [JSend specification] for successes and failures.

[JSend specification]: http://labs.omniti.com/labs/jsend



Coding Style
------------

We follow [PEP 8] with a few exceptions:

-   Lines are 80 characters long (not 79). This includes docstrings and
    comments.
-   Explicit line continuation is often preferred over implicit, when it saves
    us from deeply nesting parenthesis

[PEP 8]: http://www.python.org/dev/peps/pep-0008/

Abuse
-----

It's possible for someone to write a client that abuses the API, spamming it
with artificially inflated statistics. We record IPs so we could perform some
analysis later to filter out these results, but heavily NATed environments could
complicate this.

Generally, we assume nobody will spam us with API calls, as there's no
motivation for an attacker to do so.

Upon setting up a production system, we should use some sort of rate-limiting,
to avoid being DoSed. The configuration file allows limiting based on UUID,
IPv4, and IPv6 addresses. This can be paired with [nginx's rate limiting
module][nginx limit req].

*Please don't be evil!*

Running server (without installing as an debian package)
--------------
```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list
sudo apt-get update
sudo apt-get install -y mongodb-org
python -m pip install pymongo
sudo apt-get install git python-pip python-flask pymongo python-yaml
git clone https://github.com/ipop-project/ipop-stats.git
cd ipop-stats/ipopstat-0.15/DEBIAN
sudo bash preinst
sudo passwd ipop
Enter new UNIX password: ipop
Retype new UNIX password: ipop
passwd: password updated successfully
sudo service mongod start
su ipop
Password:ipop
cd ../usr/share/ipop-stat
./run.py
```

now you can access this server through webbrowser. 

http://ip_address:8080/api

controller reports status info 

http://ip_address:8080/api/submit

database location:
/var/lib/mongodb/

you can query database using Mongo shell as:
$ mongo
> use usage_report
> db.user.find()          // to get the data in database
> db.user.count()         // to get number of documents in collection


Note for next time
------------------------------------------------
I need to stop the ipop-stat before update. 
Add the command in preinst or something like "service ipop-stat stop"

Issues
------------------------------------------------
For some reason, "service ipop-stat start/stop" does not work. 




[nginx limit req]: http://nginx.org/en/docs/http/ngx_http_limit_req_module.html
