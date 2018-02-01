#!/usr/bin/env python

# Based on http://stackoverflow.com/questions/22390064/use-dbus-to-just-send-a-message-in-python

# Python DBUS Test Server
# runs until the Quit() method is called via DBUS

from gi.repository import GLib
from pydbus import SessionBus
from pydbus.generic import signal
import dbus
import dbus.service

loop = GLib.MainLoop()

# /etc/dbus-1/system.conf
#<policy context="default">
#    <allow own="com.ssangyong.AutomotiveProxy"/>
#    <allow send_destination="com.ssangyong.AutomotiveProxy"/>
#    <allow receive_sender="com.ssangyong.AutomotiveProxy"/>
#</policy>

class VrService(object):
	"""
	<?xml version="1.0" encoding="UTF-8" ?>
	<node xmlns:doc="http://www.freedesktop.org/dbus/1.0/doc.dtd">

	<interface name="com.ssangyong.AutomotiveProxy.VrManager">

	<method name="Set">
		<arg name="request" type="s" direction="in"/>
		<arg name="resp_result" type="b" direction="out"/>
	    <arg name="resp_data" type="s" direction="out"/>
	</method>
	<method name="AddListener">
		<arg name="request" type="s" direction="in"/>
		<arg name="resp_result" type="b" direction="out"/>
	    <arg name="resp_data" type="s" direction="out"/>
	</method>

	<signal name="UpdateInfo">
	    <arg type="s" name="info"/>
	</signal>

	</interface>
	</node>
	"""
	UpdateInfo = signal()
	def Get(self, s):
		print("com.ssangyong.AutomotiveProxy.VrManager " + "Get : " + s)
		return "Vr Manager - Get"
	def Set(self, s):
		print("com.ssangyong.AutomotiveProxy.VrManager " + "Set : " + s)
		return "Vr Manager - Set"

	def AddListener(self, s):
		print("com.ssangyong.AutomotiveProxy.VrManager " + "AddListener : " + s)
		self.UpdateInfo("{\"Cmd\":\"PTTEvent\",\"Data\":{\"Action\":\"VrStartEvent123\"}}")
		return (True, "{\"Data\":null,\"Result\":{\"Message\":\"Success\",\"Status\":true}}")

class LocationService(object):
	"""
	<?xml version="1.0" encoding="UTF-8" ?>
	<node xmlns:doc="http://www.freedesktop.org/dbus/1.0/doc.dtd">

	<interface name="com.ssangyong.AutomotiveProxy.LocationManager">
	<method name="Get">
		<arg name="request" type="s" direction="in"/>
		<arg name="resp_result" type="b" direction="out"/>
	    <arg name="resp_data" type="s" direction="out"/>
	</method>

	<method name="AddListener">
		<arg name="request" type="s" direction="in"/>
		<arg name="resp_result" type="b" direction="out"/>
	    <arg name="resp_data" type="s" direction="out"/>
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
		return (True, "{\"Data\":null,\"Result\":{\"Message\":\"Success\",\"Status\":true}}")
	def Set(self, s):
		print("com.ssangyong.AutomotiveProxy.LocationManager " + "Set : " + s)
		return "Location Manager - Set"

	def AddListener(self, s):
		print("com.ssangyong.AutomotiveProxy.LocationManager " + "AddListener : " + s)
		self.UpdateInfo("{\"Cmd\":\"PTTEvent\",\"Data\":{\"Action\":\"VrStartEvent123\"}}")
		return (True, "{\"Data\":null,\"Result\":{\"Message\":\"Success\",\"Status\":true}}")

bus = SessionBus()
bus.publish("com.ssangyong.AutomotiveProxy", VrService(),
	("VrManager", VrService()), ("LocationManager", LocationService()))

loop.run()
