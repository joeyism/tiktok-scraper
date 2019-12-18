
TikTok Scraper
==============

Installation
------------

To install with pip, run

.. code-block:: bash

   pip3 install tiktok-scraper

Simple Usage
------------

To use it with default settings, the latest version of Chrome is required. After which, you can run

.. code-block:: bash

   tiktok-scraper <USERNAME>

which downloads locally to a folder with the same name as the username

API
---

.. code-block::

   usage: tiktok-scraper [-h] [--driver DRIVER] [--driver-type DRIVER_TYPE]
                         [--show-browser] [--delay DELAY] [--location LOCATION]
                         username
   positional arguments:
     username              The TikTok username

   optional arguments:
     -h, --help            show this help message and exit
     --driver DRIVER       Driver location
     --driver-type DRIVER_TYPE
                           Type of driver (i.e. Chrome)
     --show-browser        Shows browser while scraping. Useful for debugging
     --delay DELAY         Number of seconds to delay between video downloading
     --location LOCATION   Location to store the files

OPTIONS
^^^^^^^

.. code-block::

   --driver        Location of the driver (i.e. ./chromedriver). If not specified, it checks in `$PATH` first, and if it's not in there, a chromedriver is downloaded locally

   --driver-type   Type of driver (i.e. Chrome, Firefox)

   --show-browser  If set, the scraping is done with showing the browser. This is useful for debugging why sometime scraping may fail

   --delay         The number of seconds to delay between video downloading. This may be important if there's a rate limit

   --location      Location of where the videos are downloaded. If not specified, location is the same as the username
