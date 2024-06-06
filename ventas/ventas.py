from kivy.app import App
from kivy.uix.boxlayout import BoxLayout



class VentasWindow(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def agregar_producto_codigo(self, codigo):
		print("se mando:", codigo)

	def agregar_producto_nombre(self, nombre):
		print("se mando; ", nombre)

	def pagar(self):
		print('pagar')

	def nueva_compra(self):
		print('nueva compra')


	def admin(self):
		print("admin presionado")

	def signout(self):
		print("sigonout presionado")

	def eliminar_producto(self):
		print("eliminar presionado")

	def modificar_producto(self):
		print("modificar_producto")




class VentasApp(App):
	def build(self):
		return VentasWindow()




if __name__ == '__main__':
	VentasApp().run()