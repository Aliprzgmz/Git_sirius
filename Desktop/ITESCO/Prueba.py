import wx
 
#frame
class windows (wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'Calculadora Básica en Python, Programacion Avanzada',size=(420,420))
       
        #presentacion
        a=wx.MessageDialog(None,'hola mundo! \n Soy una Calculadora \n mi creador es Ali Perez Gomez','Ingenieria Electronica',style=wx.OK)
        b=a.ShowModal()
       
        #barra de menu
        status=self.CreateStatusBar()
        menu=wx.MenuBar()
        creditos=wx.Menu()
        contactos=wx.Menu()
        salir=wx.Menu()
 
        creditos.Append(wx.ID_ABOUT,'Creditos', 'Agradecimientos por Colaboracion')
        wx.EVT_MENU(self,wx.ID_ABOUT, self.creditos)
 
        contactos.Append(wx.ID_ADD, 'Contactar a Ali Perez Gomez', '¿Nesecitas Ayuda?')
        wx.EVT_MENU(self,wx.ID_ADD, self.contactar)
 
        contactos.Append(wx.ID_APPLY, 'Paginas con contenido acerca de Python', 'Ali Perez Gomez')
        wx.EVT_MENU(self,wx.ID_APPLY, self.paginas)
 
        salir.Append(wx.ID_EXIT,"Salir", "Vuelve pronto al sistema de Electronica")
        wx.EVT_MENU(self,wx.ID_EXIT, self.salir)
       
        menu.Append(creditos,'Creditos')
        menu.Append(contactos, 'Contactos')
        menu.Append(salir, 'Salir')
       
        self.SetMenuBar(menu)
 
        #botones
        suma = wx.Button(self, label = '+', pos = (100 - 60 - 15, 230), size = (60,25))
        suma.Bind(wx.EVT_BUTTON,self.suma)
        
        resta = wx.Button(self, label = '-', pos = (200 - 60 - 15, 230), size = (60,25))
        resta.Bind(wx.EVT_BUTTON,self.resta)
        
        multiplica = wx.Button(self, label = '*', pos = (300 - 60 - 15, 230), size = (60,25))
        multiplica.Bind(wx.EVT_BUTTON,self.multiplica)
        
        divide = wx.Button(self, label = '/', pos = (400 - 60 - 15, 230), size = (60,25))
        divide.Bind(wx.EVT_BUTTON,self.divide)
        
        limpia= wx.Button(self, label='Limpiar', pos=(250 - 60 - 15, 280),size=(60,25))
        limpia.Bind(wx.EVT_BUTTON,self.erradicador)
 
        #text box
        self.valor1 = wx.TextCtrl(self, pos = (10, 30), size = (400 - 120 - 15 - 10, 25), style=wx.TE_PROCESS_ENTER,value='Ingrese el Primer Valor')
        self.valor2 = wx.TextCtrl(self,  pos = (10, 100), size = (400 - 120 - 15 - 10, 25), style=wx.TE_PROCESS_ENTER,value='Ingrese el Segundo Valor')
        self.resultado = wx.TextCtrl(self,  pos = (10, 170), size = (400 - 120 - 15 - 10, 25),style=wx.TE_PROCESS_ENTER)
 
        #labels
        label1 = wx.StaticText(self,label='Valor 1', size = (400 - 120 - 15 - 10, 25),pos = (10, 8))
        label2 = wx.StaticText(self,label='Valor 2',size = (400 - 120 - 15 - 10, 25),pos = (10, 78))
        label3 = wx.StaticText(self,label='Resultado',size = (400 - 120 - 15 - 10, 25),pos = (10, 148))
        label4 = wx.StaticText(self,label='Electronica Avanzada',size = (300 - 120 - 15 - 10, 25),pos = (10, 298))
 
 
       
        self.Show(True)
       
    #Eventos
   
 
    def creditos(self,event):#creditos
                     salir=wx.MessageDialog(None, 'desarrollado por Ali Perez Gomez \n Colaborador 1: \n Colaborador 2:', 'Creditos',  style=wx.OK)
                     salir.ShowModal()
                     
 
    def salir(self,event):#Salir
                     salir=wx.MessageDialog(None, 'Saludos :,(','Salir', style=wx.OK)
                     salir.ShowModal()
                     self.Close(True)
 
    def contactar(self,event):#contactar a Ali Perez Gomez
                     salir=wx.MessageDialog(None,  'aperezg@itesco.edumx \n ,Contactar a Ali Perez Gomez' , style=wx.OK)
                     salir.ShowModal()
                     
 
    def paginas(self,event):#paginas python
                     salir=wx.MessageDialog(None, 'www.itesco.edu.mx \n Python.org \n wxpython.org','Paginas de Python', style=wx.OK)
                     salir.ShowModal()
               
 
    def suma(self,event):#Suma
        self.resultado.SetLabel(str(int (self.valor1.GetValue())+ int (self.valor2.GetValue())))
        resultado=wx.MessageDialog(None, 'su resultado es '+str(int (self.valor1.GetValue())+ int (self.valor2.GetValue())),'Resultado',style=wx.OK)
        resultado.ShowModal()
 
 
    def resta(self,event):#Resta
        self.resultado.SetLabel(str(int (self.valor1.GetValue())- int (self.valor2.GetValue())))
        resultado=wx.MessageDialog(None, 'su resultado es '+str(int (self.valor1.GetValue())- int (self.valor2.GetValue())),'Resultado',style=wx.OK)
        resultado.ShowModal()
 
    def multiplica(self,event):#Multiplica
        self.resultado.SetLabel(str(int (self.valor1.GetValue())* int (self.valor2.GetValue())))
        resultado=wx.MessageDialog(None, 'su resultado es '+ str(int (self.valor1.GetValue())* int (self.valor2.GetValue())),'Resultado',style=wx.OK)
        resultado.ShowModal()
 
    def divide(self,event):#Divide
        self.resultado.SetLabel(str(int (self.valor1.GetValue())/ int (self.valor2.GetValue())))
        resultado=wx.MessageDialog(None, 'su resultado es '+str(int (self.valor1.GetValue())/ int (self.valor2.GetValue())),'Resultado',style=wx.OK)
        resultado.ShowModal()
 
    def erradicador (self,event):#el limpiador XD
        self.valor1.SetLabel('Por Favor Ingrese el Primer Valor')
        self.valor2.SetLabel('Por Favor Ingrese el Segundo Valor')
        self.resultado.SetLabel('')
        erradicador=wx.MessageDialog(None,'Sector Clear \nReady to Continue', 'Erradicador',wx.OK)
        erradicador.ShowModal()
 
app = wx.App()
a=window()
app.MainLoop()