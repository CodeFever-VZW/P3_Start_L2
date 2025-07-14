import random
from kleurkiezer import Kleurkiezer


class Boom:
    def __init__(self, pen, hoek_min=10, hoek_max=30, takken_verhouding_min=0.62, takken_verhouding_max=0.85):
        self.pen = pen
        self.hoek_min = hoek_min
        self.hoek_max = hoek_max
        self.takken_verhouding_min = takken_verhouding_min
        self.takken_verhouding_max = takken_verhouding_max
        self.kleurkiezer = Kleurkiezer()

    def teken(self, lengte=50, orde=4, breedte=8, kleuren=['black'] + ['brown'] * 2):
        if orde >= 0:
            huidige_kleur = kleuren[0] if kleuren else self.kleurkiezer.willekeurige_kleur()
            volgende_kleuren = kleuren[1:]
            self.pen.down()
            self.pen.color(huidige_kleur)

            self.pen.width(breedte)
            self.pen.forward(lengte)

            volgende_orde = orde - 1

            takken_verhouding_rechts = random.uniform(self.takken_verhouding_min, self.takken_verhouding_min)
            volgende_lengte_rechts = takken_verhouding_rechts * lengte
            volgende_breedte_rechts = takken_verhouding_rechts * breedte

            hoek_rechts = random.uniform(self.hoek_min, self.hoek_max)

            # Teken de rechtse tak
            self.pen.right(hoek_rechts)
            self.teken(volgende_lengte_rechts, volgende_orde, volgende_breedte_rechts, volgende_kleuren)

            # Teken de linkse tak
            takken_verhouding_links = random.uniform(self.takken_verhouding_min, self.takken_verhouding_min)
            volgende_lengte_links = takken_verhouding_links * lengte
            volgende_breedte_links = takken_verhouding_links * breedte

            hoek_links = random.uniform(self.hoek_min, self.hoek_max)

            self.pen.left(hoek_rechts + hoek_links)
            self.teken(volgende_lengte_links, volgende_orde, volgende_breedte_links, volgende_kleuren)

            # Zet de pen in de startpositie
            self.pen.up()
            self.pen.right(hoek_links)
            self.pen.forward(-lengte)

        else:
            self.pen.turtlesize(orde * 1.62)
            self.pen.color(self.kleurkiezer.willekeurige_kleur())
            self.pen.stamp()