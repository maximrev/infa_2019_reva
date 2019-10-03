from graph import *

windowSize(950, 500)
canvasSize(950, 500)
tex='NOT AT ALL!'
def lox(tex):
    button('P Y T H O N  i s  R E A L L Y  A M A Z I N G !', 6, 15, font = ("Arial", 24, "bold"), background="#00ff00", justify = CENTER, width = 49, height = 0, command = lambda: knop(tex+'!'))

def knop(tex):
    bt = button(tex, 0, 0, font = ("Arial", 77, "bold"), height = 4, width = 15, command = lambda: hide_me(bt,tex))

def hide_me(event, tex):
    event.place_forget()
    lox(tex)

#заливка
penColor(0, 0, 0)
brushColor(0, 0, 0)
rectangle(0, 0, 1000, 500)

#руки
penColor(255, 233, 210)
brushColor(255, 233, 210)
polygon([(30, 80), (130, 370), (150, 370), (50, 80)])
polygon([(470, 80), (370, 370), (350, 370), (450, 80)])

#кисти
penColor(255, 233, 210)
brushColor(255, 233, 210)
circle(45, 80, 25)
circle(455, 80, 25)

#зелёный прямоугольник
penColor(0, 0, 0)
brushColor(0, 255, 0)
rectangle(10, 20, 490, 80)

#тело
penColor("green")
brushColor("green")
circle(250, 480, 150)

#уберёмизлишки
penColor(0, 0, 0)
brushColor(0, 0, 0)
rectangle(0, 460, 500, 500)

#голова
penColor(255, 233, 210)
brushColor(255, 233, 210)
circle(250, 250, 120)

#белкиглаз
penColor(0, 0, 0)
brushColor(154, 240, 255)
circle(215, 225, 25)
circle(285, 225, 25)

#зрачки
penColor(0, 0, 0)
brushColor(0, 0, 0)
circle(215, 230, 7)
circle(285, 230, 7)

#нос
penColor(0, 0, 0)
brushColor("#8d4100")
polygon([(250, 270), (240, 254), (260, 254)])

#рот
penColor(0, 0, 0)
brushColor("#ff1a1a")
polygon([(250, 320), (190, 280), (310, 280)])

#рукава
penColor(0, 0, 0)
brushColor("green")
polygon([(150, 400), (110, 390), (105, 350), (150, 325), (175, 355)])
polygon([(350, 400), (390, 390), (395, 350), (350, 325), (325, 355)])

#волосы
penColor(0, 0, 0)
brushColor("yellow")
polygon([(145, 192), (165, 165), (132, 157)])
polygon([(160, 171), (182, 151), (152, 136)])
polygon([(176, 156), (200, 141), (174, 121)])
polygon([(193, 144), (224, 132), (195, 110)])
polygon([(218, 134), (252, 130), (230, 101)])
polygon([(500-145, 192), (500-165, 165), (500-132, 157)])
polygon([(500-160, 171), (500-182, 151), (500-152, 136)])
polygon([(500-176, 156), (500-200, 141), (500-174, 121)])
polygon([(500-193, 144), (500-224, 132), (500-195, 110)])
polygon([(500-218, 134), (500-252, 130), (500-230, 101)])


#------------------------------------------2-й


#руки
penColor(255, 233, 210)
brushColor(255, 233, 210)
polygon([(30+450, 80), (130+450, 370), (150+450, 370), (50+450, 80)])
polygon([(470+450, 80), (370+450, 370), (350+450, 370), (450+450, 80)])

#кисти
penColor(255, 233, 210)
brushColor(255, 233, 210)
circle(45+450, 80, 25)
circle(455+450, 80, 25)

#зелёный прямоугольник
penColor(0, 0, 0)
brushColor(0, 255, 0)
rectangle(10+450, 20, 490+450, 80)

#тело
penColor("#cd5700")
brushColor("#cd5700")
circle(250+450, 480, 150)

#уберёмизлишки
penColor(0, 0, 0)
brushColor(0, 0, 0)
rectangle(0+450, 460, 500+450, 500)

#голова
penColor(255, 233, 210)
brushColor(255, 233, 210)
circle(250+450, 250, 120)

#белкиглаз
penColor(0, 0, 0)
brushColor(114, 190, 255)
circle(215+450, 225, 25)
circle(285+450, 225, 25)

#зрачки
penColor(0, 0, 0)
brushColor(0, 0, 0)
circle(215+450, 230, 7)
circle(285+450, 230, 7)

#нос
penColor(0, 0, 0)
brushColor("#8d4100")
polygon([(250+450, 270), (240+450, 254), (260+450, 254)])

#рот
penColor(0, 0, 0)
brushColor("#ff1a1a")
polygon([(250+450, 320), (190+450, 280), (310+450, 280)])

#рукава
penColor(0, 0, 0)
brushColor("#cd5700")
polygon([(150+450, 400), (110+450, 390), (105+450, 350), (150+450, 325), (175+450, 355)])
polygon([(350+450, 400), (390+450, 390), (395+450, 350), (350+450, 325), (325+450, 355)])

#волосы
penColor(0, 0, 0)
brushColor(255, 0, 255)
polygon([(145+450, 192), (165+450, 165), (132+450, 157)])
polygon([(160+450, 171), (182+450, 151), (152+450, 136)])
polygon([(176+450, 156), (200+450, 141), (174+450, 121)])
polygon([(193+450, 144), (224+450, 132), (195+450, 110)])
polygon([(218+450, 134), (252+450, 130), (230+450, 101)])
polygon([(500-145+450, 192), (500-165+450, 165), (500-132+450, 157)])
polygon([(500-160+450, 171), (500-182+450, 151), (500-152+450, 136)])
polygon([(500-176+450, 156), (500-200+450, 141), (500-174+450, 121)])
polygon([(500-193+450, 144), (500-224+450, 132), (500-195+450, 110)])
polygon([(500-218+450, 134), (500-252+450, 130), (500-230+450, 101)])

#надпись
button('P Y T H O N  i s  R E A L L Y  A M A Z I N G !', 6, 15, font = ("Arial", 24, "bold"), background="#00ff00", justify = CENTER, width = 49, height = 0, command =lambda: knop(tex))

run()
