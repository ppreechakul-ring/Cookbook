from WindowsWifi import getWirelessNetworkBssList
from WindowsWifi import getWirelessInterfaces
from WindowsWifi import disconnect, getWirelessAvailableNetworkList

"""
    connection_params should be a dict with this structure:
    { "connectionMode": "valid connection mode string",
      "profile": ("profile name string" | "profile xml" | None)*,
      "ssid": "ssid string",
      "bssidList": [ "desired bssid string", ... ],
      "bssType": valid bss type int,
      "flags": valid flag dword in 0x00000000 format }
    * Currently, only the name string is supported here.
"""

iface = getWirelessInterfaces()
# disconnect(iface[0])
net = getWirelessAvailableNetworkList(iface[0])
for n in net:
    print n
