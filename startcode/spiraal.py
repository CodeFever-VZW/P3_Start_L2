import turtle

# beginwaarden instellen
afstand = 1
aantal_stappen = 500

# turtle-object aanmaken
turtle = turtle.Turtle()

# snelheid instellen
turtle.speed(10)

# patroon tekenen
for _ in range(aantal_stappen):
    turtle.forward(afstand)    # beweeg vooruit
    turtle.left(120)           # draai naar links (driehoekhoek)
    turtle.left(1)             # kleine extra draai
    afstand += 1               # afstand vergroten bij elke stap

turtle.screen.mainloop()  # in plaats van turtle.done(), omdat turtle overschreven is
