import wx
import webbrowser

class MyApp(wx.App):
    def __init__(self):
        super().__init__(clearSigInt=True)
        
        # init frame
        self.InitFrame()
    
    def InitFrame(self):
        frame = MyFrame(parent=None, title="Boton de la APP", pos = (100, 100))
        frame.Show()


class MyFrame(wx.Frame):
    # Cambio en el Codigo 2
    # subclass of wx.Window; Frame is a top level window
    # A frame is a window whose size and position can (usually) be changed by the user.
    # Usually represents the first/main window a user will see
    def __init__(self, parent, title, pos):
        super().__init__(parent=parent, title=title, pos=pos)
        self.OnInit()
    
    def OnInit(self):
        panel = MyPanel(parent=self)


class MyPanel(wx.Panel):
    # A panel is a window on which controls are placed. (e.g. buttons and text boxes)
    # wx.Panel class is usually put inside a wxFrame object. This class is also inherited from wxWindow class.
    def __init__(self,parent):
        super().__init__(parent=parent)
        
        # add a hello message to the panel
        welcomeText = wx.StaticText(self, label="Documentacion wxPython, click para seguir el link!", pos=(20,20))

        # add a button to bring up the dialog box
        button = wx.Button(parent=self, label='Click Aqui!', pos = (20, 120))
        button.Bind(wx.EVT_BUTTON, self.onSubmit) # bind action to button


    def onSubmit(self, event):
        # stuff for the submit button to do
        webbrowser.open('https://wxpython.org/Phoenix/docs/html/index.html')
        

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()