import Tkinter

class runningGUI(Tkinter.Tk):
	def __init__(self, parent):
		Tkinter.Tk.__init__(self, parent)
		self.parent = parent
		self.initialize()

	def initialize(self):
		self.grid()

		#time entry: h:m:s
		self.hourVar = Tkinter.IntVar()
		self.hourEntry = Tkinter.Entry(self, textvariable=self.hourVar)
		self.hourEntry.grid(column=0, row=2, sticky='EW')
		self.hourVar.set(0)

		self.minVar = Tkinter.IntVar()
		self.minEntry = Tkinter.Entry(self, textvariable=self.minVar)
		self.minEntry.grid(column=1, row=2, sticky='EW')
		self.minVar.set(00)

		self.secVar = Tkinter.DoubleVar()
		self.secEntry = Tkinter.Entry(self, textvariable=self.secVar)
		self.secEntry.grid(column=2, row=2, sticky='EW')
		self.secVar.set(00)

		timeButton = Tkinter.Button(self, text=u"Calculate Time", command=self.onTimeClick)
		timeButton.grid(column=3, row=2)

		#pace entry
		self.paceMinVar = Tkinter.IntVar()
		self.paceMinEntry = Tkinter.Entry(self, textvariable=self.paceMinVar)
		self.paceMinEntry.grid(column=0, row=0, columnspan=1, sticky='EW')
		self.paceMinVar.set(0)

		self.paceSecVar = Tkinter.DoubleVar()
		self.paceSecEntry = Tkinter.Entry(self, textvariable=self.paceSecVar)
		self.paceSecEntry.grid(column=1, row=0, columnspan=2, sticky='EW')
		self.paceSecVar.set(0)

		paceButton = Tkinter.Button(self, text=u"Calculate Pace", command=self.onPaceClick)
		paceButton.grid(column=3, row=0)

		#distance entry
		self.distance = Tkinter.DoubleVar()
		self.distEntry = Tkinter.Entry(self, textvariable=self.distance)
		self.distEntry.grid(column=0, row=1, columnspan=3, sticky='EW')
		self.distance.set(0.0)

		distButton = Tkinter.Button(self, text=u"Calculate Distance", command=self.onDistClick)
		distButton.grid(column=3, row=1)

		#workout interval calculator button
		workoutButton = Tkinter.Button(self, text=u"Generate Interval Splits", command=self.onWClick)
		workoutButton.grid(column=1, row=4)



		#label = Tkinter.Label(self, anchor="w",fg="white",bg="blue")
        #label.grid(column=0,row=1,columnspan=2,sticky='EW')

        #self.grid_columnconfigure(0,weight=1)
	def timeToSeconds(self):
		hours = self.hourVar.get()
		minutes = self.minVar.get()
		seconds = self.secVar.get()
		return (3600*hours + 60*minutes + seconds)

	def paceToSeconds(self):
		pm = self.paceMinVar.get()
		ps = self.paceSecVar.get()
		return (60*pm + ps)

	def secondsToPace(self, fSeconds):
		seconds = fSeconds % 60
		minutes = ((fSeconds - seconds) / 60) % 60
		return (int(minutes), seconds)

	def secondsToTime(self, fSeconds):
		seconds = fSeconds % 60
		minutes = ((fSeconds - seconds) / 60) % 60
		hours = (fSeconds - minutes*60) / 3600
		return (int(hours), int(minutes), seconds)

	def onPaceClick(self):
		d = self.distance.get()
		if d != 0:
			seconds = self.timeToSeconds()
			sPace = seconds/d
			m, s = self.secondsToPace(sPace)
			self.paceMinVar.set(m)
			self.paceSecVar.set(s)
		else:
			pass

	def onTimeClick(self):
		d = self.distance.get()
		ps = self.paceToSeconds()
		h, m, s = self.secondsToTime(d*ps)
		self.hourVar.set(h)
		self.minVar.set(m)
		self.secVar.set(s)



	def onDistClick(self):
		ps = self.paceToSeconds()
		fSec = self.timeToSeconds()
		d = fSec/ps
		self.distance.set(d)


	def onWClick(self):
		ps = self.paceToSeconds()
		m_meter = 1/1609.34
		pace_meter = ps * m_meter
		intervals = [200, 400, 600, 800, 1000, 1200, 1600]
		interval_seconds = [d*pace_meter for d in intervals]
		interval_output = [self.secondsToPace(s) for s in interval_seconds]
		print interval_output


if __name__ == "__main__":
	app = runningGUI(None)
	app.title('Running Application')
	app.mainloop()
