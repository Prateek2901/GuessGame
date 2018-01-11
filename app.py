import wx
from random import randint
import os
class MyApp(wx.App):
	def OnInit(self):
		self.frame = MyFrame(None, title="Guess Game")
		self.SetTopWindow(self.frame)
		self.frame.Show()
		return True
class MyFrame(wx.Frame):
	turns = 0
	def __init__(self, parent, id=wx.ID_ANY, title="Guess Game", 
				 pos=wx.DefaultPosition, size=wx.DefaultSize,
				 style=wx.DEFAULT_FRAME_STYLE,
				 name="MyFrame"):
		super(MyFrame, self).__init__(parent, id, title,pos, size, style, name)
		# Attributes

		self.compRandom = self.randomNumber()
		self.draw()

	def draw(self):
		self.panel = wx.Panel(self)
		vbox = wx.BoxSizer(wx.VERTICAL) 
		hbox1 = wx.BoxSizer(wx.HORIZONTAL) 

		l1 = wx.StaticText(self.panel, -1, "Enter the Guessed Number",pos=(130, 100))
		hbox1.Add(l1, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
		self.t1 = wx.TextCtrl(self.panel,pos=(160, 150))
		hbox1.Add(self.t1,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
		self.t1.Bind(wx.EVT_TEXT,self.OnKeyTyped) 
		vbox.Add(hbox1)

		path = os.path.abspath("./guess.png")
		icon = wx.Icon(path, wx.BITMAP_TYPE_PNG)
		self.SetIcon(icon)
		#self.panel.SetBackgroundColour(wx.BLACK)
		self.btn = wx.Button(self.panel,-1,"click Me",pos=(160, 300)) 
		#button3.SetBackgroundColour("Red")
		vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
		self.btn.Bind(wx.EVT_BUTTON,self.OnClicked) 
		self.Bind(wx.EVT_CLOSE,self.OnClose)
		self.Centre() 
		self.Show() 
		#self.Fit()
	def OnKeyTyped(self, event): 
		string = event.GetString()
		if len(string) > 0:
			self.nos = int(string)
		else:
			self.nos = 0
		print("Input be %d"%self.nos)
	def OnClicked(self, event): 
		btn = event.GetEventObject().GetLabel() 
		#print(self.nos)
		self.game(self.nos,self.compRandom)
	def OnClose(self,evt):
		  print ("CLOSE!!!")
		  self.Destroy()
	
	def randomNumber(self):
		from random import randint
		num = randint(1, 100)
		print("Debug Log %d"%num)
		return num
		
	def game(self,user,comp):
		title = ""
		txt = ""
		if comp < user:
			title = "Incorrect"
			txt = "Sorry!! Lower Your Guess"
			self.turns+=1
			print(txt)
			
		elif comp > user:
			title = "Incorrect"
			txt = "Sorry!! Higher Your Guess"
			self.turns+=1
			print(txt)
			
		else:
			title = "Correct"
			txt = "Eureka you did it in %d!!!!"%self.turns
			print(txt)
			
		
		wx.MessageBox(message=txt,caption=title,style=wx.OK | wx.ICON_INFORMATION)
if __name__ == "__main__":
	app = MyApp(False)
	app.MainLoop()