from modules import cbpi
from modules.core.props import Property, StepProperty
from modules.core.hardware import ActorBase

@cbpi.actor
class ActorGroup(ActorBase):

	actor01 = StepProperty.Actor("Actor 1")
	actor02 = StepProperty.Actor("Actor 2")
	actor03 = StepProperty.Actor("Actor 3")
	actor04 = StepProperty.Actor("Actor 4")
	actor05 = StepProperty.Actor("Actor 5")
	actor06 = StepProperty.Actor("Actor 6")
	actor07 = StepProperty.Actor("Actor 7")
	actor08 = StepProperty.Actor("Actor 8")

	actors = []

	def init(self):
		#self.actors.clear()
	
		if self.actor01 is not None:
			self.actors.append(self.actor01)
		if self.actor02 is not None:
			self.actors.append(self.actor02)
		if self.actor03 is not None:
			self.actors.append(self.actor03)
		if self.actor04 is not None:
			self.actors.append(self.actor04)
		if self.actor05 is not None:
			self.actors.append(self.actor05)
		if self.actor06 is not None:
			self.actors.append(self.actor06)
		if self.actor07 is not None:
			self.actors.append(self.actor07)
		if self.actor08 is not None:
			self.actors.append(self.actor08)

	def set_power(self, power):		
		for actor in self.actors:
			self.api.actor_power(actor, power=power)
			
	def on(self, power=None):
		for actor in self.actors:
			self.api.switch_actor_on(actor, power=power)

	def off(self):
		for actor in self.actors:
			self.api.switch_actor_off(actor)
