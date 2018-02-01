#!/usr/bin/env python

# Based on http://stackoverflow.com/questions/22390064/use-dbus-to-just-send-a-message-in-python

# Python DBUS Test Server
# runs until the Quit() method is called via DBUS

from gi.repository import GLib
from pydbus import SystemBus
from pydbus.generic import signal
import dbus
import dbus.service

loop = GLib.MainLoop()

# /etc/dbus-1/system.conf
#<policy context="default">
#	<allow own="com.ssangyong.AutomotiveProxy.LocationManager"/>
#   <allow send_destination="com.ssangyong.AutomotiveProxy.LocationManager"/>
#   <allow receive_sender="com.ssangyong.AutomotiveProxy.LocationManager"/>
#</policy>

class LocationService(object):
	"""
		<?xml version="1.0" encoding="UTF-8" ?>
		<node name="/com/ssangyong/AutomotiveProxy/LocationManager" xmlns:doc="http://www.freedesktop.org/dbus/1.0/doc.dtd">

		<interface name="com.ssangyong.AutomotiveProxy.LocationManager">

		<method name="Get">
		   <annotation name="org.freedesktop.DBus.GLib.Async" value=""/>
		   <arg name="request" type="s" direction="in"/>
		   <arg name="response" type="s" direction="out"/>
		</method>

		<method name="Set">
			<annotation name="org.freedesktop.DBus.GLib.Async" value=""/>
			<arg name="request" type="s" direction="in"/>
			<arg name="response" type="s" direction="out"/>
		</method>

		<method name="AddListener">
		   <annotation name="org.freedesktop.DBus.GLib.Async" value=""/>
		   <arg name="request" type="s" direction="in"/>
		   <arg name="response" type="s" direction="out"/>
		</method>

		<signal name="UpdateInfo">
			<arg type="s" name="info"/>
		</signal>

		</interface>
		</node>

	"""
	UpdateInfo = signal()
	def Get(self, s):
		print("com.ssangyong.AutomotiveProxy.LocationManager " + "Get : " + s)
		return "Location Manager - Get"
	def Set(self, s):
		print("com.ssangyong.AutomotiveProxy.LocationManager " + "Set : " + s)
		return "Location Manager - Set"

	def AddListener(self, s):
		print("com.ssangyong.AutomotiveProxy.LocationManager " + "AddListener : " + s)
		return "Location Manager - AddLister"

bus = SystemBus()
bus.publish("com.ssangyong.AutomotiveProxy.LocationManager", LocationService())
location = bus.get("com.ssangyong.AutomotiveProxy.LocationManager")
location.onUpdateInfo = LocationService.AddListener

loop.run()
