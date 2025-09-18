#!/usr/local/bin/python
#
# (c) Copyright 2013, 2014, University of Manchester
#
# HydraPlatform is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# HydraPlatform is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with HydraPlatform.  If not, see <http://www.gnu.org/licenses/>
#
import sys
import os
import click
from hydra_server import initialize

import pywrparser


global DEFAULT_PORT
DEFAULT_PORT = os.getenv('HYDRA_SERVER_PORT')
if DEFAULT_PORT is not None:
    DEFAULT_PORT = hb.config.get('hydra_server', 'port', 8080)


@click.command()
@click.option('-p', '--port', default=DEFAULT_PORT, help='Hydra Server Port Number')
def run(port):

    application, api_server = initialize(None)
    api_server.run_server(port=port)

#To kill this process, use this command:
#ps -ef | grep 'server.py' | grep 'python' | awk '{print $2}' | xargs kill
if __name__ == '__main__':
    run()
