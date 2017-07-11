from modules import cbpi
from modules.core.props import Property
from modules.core.hardware import ActorBase
from modules.core.hardware import SensorPassive

@cbpi.actor
class ActorGroup(ActorBase):

	actordesc = "Select an actor to be controlled by this group."
	actor01 = Property.Actor("Actor 1", description=actordesc)
	actor02 = Property.Actor("Actor 2", description=actordesc)
	actor03 = Property.Actor("Actor 3", description=actordesc)
	actor04 = Property.Actor("Actor 4", description=actordesc)
	actor05 = Property.Actor("Actor 5", description=actordesc)
	actor06 = Property.Actor("Actor 6", description=actordesc)
	actor07 = Property.Actor("Actor 7", description=actordesc)
	actor08 = Property.Actor("Actor 8", description=actordesc)

	def init(self):
		self.actors = []

		if isinstance(self.actor01, unicode) and self.actor01:
			self.actors.append(int(self.actor01))
		if isinstance(self.actor02, unicode) and self.actor02:
			self.actors.append(int(self.actor02))			
		if isinstance(self.actor03, unicode) and self.actor03:
			self.actors.append(int(self.actor03))
		if isinstance(self.actor04, unicode) and self.actor04:
			self.actors.append(int(self.actor04))
		if isinstance(self.actor05, unicode) and self.actor05:
			self.actors.append(int(self.actor05))			
		if isinstance(self.actor06, unicode) and self.actor06:
			self.actors.append(int(self.actor06))
		if isinstance(self.actor07, unicode) and self.actor07:
			self.actors.append(int(self.actor07))
		if isinstance(self.actor08, unicode) and self.actor08:
			self.actors.append(int(self.actor08))
			
	def set_power(self, power):
		for actor in self.actors:
			self.api.actor_power(actor, power=power)

	def on(self, power=None):
		for actor in self.actors:
			self.api.switch_actor_on(actor, power=power)

	def off(self):
		for actor in self.actors:
			self.api.switch_actor_off(actor)
			
@cbpi.sensor
class SensorGroup(SensorPassive):

	sensordesc = "Select a sensor to be averaged with the other sensors in this group."
	sensor01 = Property.Sensor("Sensor 1", description=sensordesc)
	sensor02 = Property.Sensor("Sensor 2", description=sensordesc)
	sensor03 = Property.Sensor("Sensor 3", description=sensordesc)
	sensor04 = Property.Sensor("Sensor 4", description=sensordesc)
	sensor05 = Property.Sensor("Sensor 5", description=sensordesc)
	sensor06 = Property.Sensor("Sensor 6", description=sensordesc)
	sensor07 = Property.Sensor("Sensor 7", description=sensordesc)
	sensor08 = Property.Sensor("Sensor 8", description=sensordesc)
	
	def init(self):
		self.sensors = []

		if isinstance(self.sensor01, unicode) and self.sensor01:
			self.sensors.append(int(self.sensor01))
		if isinstance(self.sensor02, unicode) and self.sensor02:
			self.sensors.append(int(self.sensor02))			
		if isinstance(self.sensor03, unicode) and self.sensor03:
			self.sensors.append(int(self.sensor03))
		if isinstance(self.sensor04, unicode) and self.sensor04:
			self.sensors.append(int(self.sensor04))
		if isinstance(self.sensor05, unicode) and self.sensor05:
			self.sensors.append(int(self.sensor05))			
		if isinstance(self.sensor06, unicode) and self.sensor06:
			self.sensors.append(int(self.sensor06))
		if isinstance(self.sensor07, unicode) and self.sensor07:
			self.sensors.append(int(self.sensor07))
		if isinstance(self.sensor08, unicode) and self.sensor08:
			self.sensors.append(int(self.sensor08))
			
	def stop(self):
		pass
		
	def read(self):
		tempsum = float(0)
		for sensor in self.sensors:
			tempsum += float(cbpi.cache.get("sensors")[sensor].instance.last_value)
		self.data_received(round(tempsum / len(self.sensors), 2))
		
	def get_unit(self):
		if len(self.sensors) > 0:
			return cbpi.cache.get("sensors")[self.sensors[0]].instance.get_unit()
		else:
			return super(SensorBase, self).get_unit()
