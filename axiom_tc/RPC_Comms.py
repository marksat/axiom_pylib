# Copyright (c) 2024 TouchNetix
# 
# This file is part of [Project Name] and is released under the MIT License: 
# See the LICENSE file in the root directory of this project or http://opensource.org/licenses/MIT.

import rpyc

class RPC_Comms:
    def __init__(self, hostname, port):
        self._connection = rpyc.connect(hostname, port)
        pass

    def comms_init(self, axiom):
        self.__axiom = axiom

    def read_page(self, target_address, length):
        return self._connection.root.read_page(target_address, length)

    def write_page(self, target_address, length, payload):
        self._connection.root.write_page(target_address, length, payload)

    def close(self):
        self._connection.close()