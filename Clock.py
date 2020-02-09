from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.lang.builder import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button

from threading import Thread

import time
import winsound
    
alarms = []

class clockFace(Screen):

	def on_enter(self):
		Clock.schedule_interval(self.showTime, 1)
		Clock.schedule_interval(self.checkAlarm, 1)

	def showTime(self, sec):
		self.time.text = time.strftime("%H:%M:%S")
		

	def setAlarm(self):
		alarms.append(self.hour.text+":"+self.minute.text+":"+self.second.text);
		self.add_widget(Label(text= "Alarm Added", pos_hint= {'center_x': 0.8, 'center_y': 0.9}))


	def checkAlarm(self, sec):
		if alarms:
			for alarm in alarms:
				if alarm == time.strftime("%H:%M:%S") :
					alarms.remove(alarm)
					winsound.Beep(2500, 3000)

	def stopAlarm(self):
		winsound.PlaySound(None, winsound.SND_PURGE)


class ClockApp(App):

	def build(self):
		sm = ScreenManager()
		sm.add_widget(clockFace(name="clockFace"))
		return sm



ClockApp().run()
