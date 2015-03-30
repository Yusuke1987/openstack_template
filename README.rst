OpenStack Template README
=====================

Introduction
--------
This template has been made based on Openstack Nova

   https://github.com/openstack/nova

Template used when you want to create a python application.

There are following such advantage by using the template

* Building of eventlet based WSGI server
* Paste (routes) based WSGI filter / dispatcher
* JSON serialization
* OpenStack-compliant logging
* OpenStack reading and writing of WSGI / App setting of compliance
* OpenStack compliant DB access
* OpenStack request object mapping of compliance
* OpenStack compliant internationalization mechanism
* OpenStack compliant RPC mechanism
* OpenStack compliant package build mechanism
* OpenStack compliance of UT mechanism

Quickstart
--------
Install sample APP::

  $ python setup.py install

Copy configuration::

  $ cp -rp etc/openapp /etc/
  
Start sample APP::

  $ openapp

API Examples using Curl::

  $ curl -H "X-Auth-Token:test-token"  http://127.0.0.1:8773/template
  Sample API Test Return OK

Running the tests
--------
Run the unit tests by doing::

  $ ./run_tests.sh
