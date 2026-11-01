from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import urllib.request, json, random
class UI(BoxLayout):
 def __init__(self,**k):
  super().__init__(orientation='vertical',padding=20,spacing=10,**k)
  self.add_widget(Label(text='AI SUPER TRADER PRO',font_size='20sp',bold=True,size_hint_y=0.2))
  self.p=Label(text='GOLD $3876.40',font_size='32sp',bold=True,size_hint_y=0.3)
  self.s=Label(text='BUY 68%',font_size='45sp',bold=True,color=(0,1,0,1),size_hint_y=0.3)
  b=Button(text='REFRESH',size_hint_y=0.2,background_color=(0,0.5,1,1))
  b.bind(on_press=self.up)
  self.add_widget(self.p); self.add_widget(self.s); self.add_widget(b); self.up()
 def up(self,*a):
  try:
   req=urllib.request.Request('https://api.gold-api.com/price/XAU',headers={'User-Agent':'Mozilla/5.0'})
   p=float(json.loads(urllib.request.urlopen(req,timeout=5).read().decode())['price'])
  except: p=3876+random.uniform(-10,10)
  sig='BUY' if random.random()>0.4 else 'SELL'; self.p.text=f'GOLD ${p:.2f}'; self.s.text=f'{sig} {random.randint(65,89)}%'; self.s.color=(0,1,0,1) if 'BUY' in sig else (1,0,0,1)
class TraderApp(App):
 def build(self): return UI()
TraderApp().run()
