.. _setup:

Setting up Boundless Exchange
=============================

This section will show how to install and configure Boundless Exchange.

.. _setup.installation:

Installation
------------

There are two ways to install Boundless Exchange: through a virtual machine (VM) or through RPM packages for Red Hat / CentOS.

Virtual Machine
~~~~~~~~~~~~~~~

The virtual machine is in the OVA exchange format, which is compatible with all major virtualization software such as VMware or VirtualBox.

#. Use the Import utility of your program to import this virtual machine into your catalog.

#. Adjust the Network settings of your VM to allow for bridged networking. This will allow your host to connect to the web server that exists on the VM.

#. Launch the VM. You can log in with the following credentials:

   * User name: ``root``
   * Password:  ``boundless123``

#. Test your network connection by typing in the IP address of the VM in your host's browser. You should see the login screen for Boundless Exchange.

   .. note:: You can use the ``ifconfig`` command on the terminal of the VM to determine the IP address.

Continue below at :ref:`setup.configuration`.

RPM
~~~

Boundless Exchange requires either Red Hat Enterprise Linux (RHEL) 6 or CentOS 6.

#. In a terminal, create a new file ``/etc/yum.repos.d/exchange-centos6.repo`` and populate it with the following content::

      [exchange-centos6]
      name=Boundless Exchange for RHEL6/Centos6
      baseurl=http://USERNAME:PASSWORD@exchange-rpm.boundlessgeo.com/exchange/centos6
      enabled=1
      gpgcheck=0

   Make sure to replace ``USERNAME`` and ``PASSWORD`` with the credentials supplied to you by Boundless.

#. Save and close the file.

#. Create a new file ``/etc/yum.repos.d/pgdg95.repo`` and populate it with the following content::

      [pgdg95]
      name=PostgreSQL 9.5 $releasever - $basearch
      baseurl=https://download.postgresql.org/pub/repos/yum/9.5/redhat/rhel-$releasever-$basearch
      enabled=1
      gpgcheck=1
      gpgkey=https://yum.boundlessps.com/RPM-GPG-KEY-PGDG-95

#. Save and close the file.

#. Create a new file ``/etc/yum.repos.d/rabbitmq-server.repo`` and populate it with the following content::

      [rabbitmq-server]
      name=rabbitmq_rabbitmq-server
      baseurl=https://packagecloud.io/rabbitmq/rabbitmq-server/el/$releasever/$basearch
      enabled=1
      gpgcheck=0

#. Save and close the file.

#. Create a new file ``/etc/yum.repos.d/elasticsearch-17.repo`` and populate it with the following content::

      [elasticsearch-1.7]
      name=Elasticsearch repository for 1.7.x packages
      baseurl=https://packages.elastic.co/elasticsearch/1.7/centos
      enabled=1
      gpgcheck=1
      gpgkey=https://packages.elastic.co/GPG-KEY-elasticsearch

#. Save and close the file.

#. To install, run the following command:::

     sudo yum install geoshape

   This will install Boundless Exchange and required dependencies.

Once completed, a web server should be running on port 80. Continue below at :ref:`setup.configuration`.

.. _setup.configuration:

Configuration
-------------

Now that the software is installed, there are a few extra configuration steps needed to get Boundless Exchange running.

.. note:: If using the VM install, log in to the console and perform these steps.

#. Update your IP address to your system::

     geoshape-config updateip IP_ADDRESS

   Make sure to replace ``IP_ADDRESS`` with the IP address of your system.

#. Update the GeoServer catalog of layers to include the IP address::

     geoshape-config updatelayers

#. Rebuild the index::

     geoshape-config rebuild_index

#. Restart the service::

     service geoshape restart
