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

Continue below at :ref:`setup.configuration`.

RPM
~~~

#. ADD REPO DETAILS

#. ADD PACKAGE DETAILS

#. Once completed, a web server should be running on port 80.

Continue below at :ref:`setup.configuration`.


.. _setup.configuration:

Configuration
-------------

Now that the software is installed, there are a few extra configuration steps needed to get Boundless Exchange running.

.. note:: If using the VM install, log in to the console and perform these steps.

#. Update your IP address to your system::

     geoshape-config updateip <IP_ADDRESS>

   Making sure to replace ``<IP_ADDRESS>`` with the IP address of your system.

#. Update the GeoServer catalog of layers to include the IP address::

     geoshape-config updatelayers

#. Rebuild the index::

     geoshape-config rebuild_index

#. Restart the service::

     service geoshape restart
