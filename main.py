from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, BooleanProperty
from models import Pizza
from kivy.uix.behaviors import CoverBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from http_client import HttpClient
from storage_manager import StorageManager


class MainWidget(FloatLayout):
    recycleview = ObjectProperty(None)
    msg_erreur = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        HttpClient().get_pizzas(self.on_server_data, self.on_server_error, self.on_server_failure)
 
    def on_parent(self, widget, parent):
        self.recycleview.data = StorageManager().load_data("pizzas_saved")
    
    def on_server_data(self, result):
        self.recycleview.data = result
        StorageManager().save_data("pizzas_saved", self.recycleview.data)

    def on_server_error(self, error):
        self.msg_erreur = f"erreur: {error}"

    def on_server_failure(self, result):
        self.msg_erreur = f"erreur: {result}"
      
class PizzaWidget(BoxLayout):
    nom = StringProperty()
    ingredients = StringProperty()
    prix = NumericProperty()
    vegetarienne = BooleanProperty()
    
with open("pizza_kv.kv", encoding = "utf8") as f:
    Builder.load_string(f.read())

class PizzaApp(App):
    def build(self):
        return MainWidget()

PizzaApp().run()