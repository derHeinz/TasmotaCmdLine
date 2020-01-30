#!/usr/bin/python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen, Request
from urllib.parse import quote
import json

class TasmotaPowerPlug(object):
    
    def __init__(self, address):
        self._address = address
        
    def _send_cmd(self, cmd_str):
        url = "http://" + self._address + "/cm?cmnd=" + quote(cmd_str)
        header = {"Content-Type":"application/json"}
        req = Request(url, None, header)
        response = urlopen(req)
        return json.load(response)
        
    def on(self):
        self._send_cmd("Power On")
        return True
        
    def off(self):
        self._send_cmd("Power Off")
        return True
    
    def get_power(self):
        res = self._send_cmd("Status 8")
        return res['StatusSNS']['ENERGY']['Power']
        
    def get_state(self):
        res = self._send_cmd("Power")
        state = res['POWER']
        if "OFF" == state:
            return False
        if "ON" == state:
            return True
    