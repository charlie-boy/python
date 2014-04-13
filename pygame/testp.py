class App:
	def on_init(self):
		self.x = [10, 20, 30]

	def on_execute(self):
		self.on_init()
		y = [0,0,0]
		y[0] = self.x[0]
		print self.x[0]
		print y[0]
		y[4] = 5



theApp = App()
theApp.on_execute()
