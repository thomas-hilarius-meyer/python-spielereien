import random
import sys

import numpy as np
from argparse import ArgumentParser

try:
    import matplotlib.pyplot as plt
except ImportError:
    print('Matplotlib not installed - plotting not available')

class Krankheitsstatus():
    GESUND = 0
    KRANK = 1
    SCHWERKRANK = 2
    IMMUN = 3
    TOT = 4

class CoronaSimulation(object):

    def __init__(self, bevoelkerungszahl, inkubationszeit, ansteckung_nach_inkubation, ansteckungsfaktor,
                 komplikationsquote, mortalitaetsfaktor, krankheitsdauer, immunisierung, verbose):



        # einstellungen speichern
        self.bevoelkerungszahl = bevoelkerungszahl
        self.inkubationszeit = inkubationszeit
        self.ansteckung_nach_inkubation = ansteckung_nach_inkubation
        self.ansteckungsfaktor = ansteckungsfaktor
        self.komplikationsquote = komplikationsquote
        self.mortalitaetsfaktor = mortalitaetsfaktor
        self.krankheitsdauer = krankheitsdauer
        self.immunisierung = immunisierung
        self.verbose = verbose

        # relevante felder initialisieren
        self.tag = 0
        # TODO: man koennte status und krankentage auch in einer matrix zusammenfassen
        self.status = np.zeros(bevoelkerungszahl)
        self.status[:] = Krankheitsstatus.GESUND
        self.krankentag = np.zeros(bevoelkerungszahl)

        # Erste Infektion auslösen:
        self.infizierte_history = 1
        self.schwerkranke_history = 0
        self.setze_krank([0])
        # self.status[0] = Krankheitsstatus.KRANK
        # self.krankentag[0] = 1

        # statistiken initialisieren
        self.statistiken = {
            'geheilte': [],
            'infizierte': [],
            'tote': []
        }

    @property
    def infizierte(self):
        return np.sum(
            np.logical_or(
                self.status == Krankheitsstatus.KRANK,
                self.status == Krankheitsstatus.SCHWERKRANK
            ))

    def setze_krank(self, idx):
        assert all(self.status[idx] == Krankheitsstatus.GESUND)
        self.status[idx] = Krankheitsstatus.KRANK
        self.krankentag[idx] = 1

    @property
    def schwerkranke(self):
        return np.sum(self.status == Krankheitsstatus.SCHWERKRANK)

    @property
    def tote(self):
        return np.sum(self.status == Krankheitsstatus.TOT)

    @property
    def geheilte(self):
        # TODO: Funktioniert nur solange immunitaet an ist
        return np.sum(self.status == Krankheitsstatus.IMMUN)

    def _step_kranke_zu_schwerkrank(self):
        """
        fuehrt den Schritt aus der aus kranken schwerkranke macht
        """
        # komplikations step
        komplikationsentscheidungen = np.random.randint(
            0, self.komplikationsquote, size=self.bevoelkerungszahl
        )
        komplikationsentscheidungen = np.logical_and(
            self.status == Krankheitsstatus.KRANK,
            komplikationsentscheidungen == 1
        )
        self.status[komplikationsentscheidungen] = Krankheitsstatus.SCHWERKRANK
        self.schwerkranke_history += np.sum(komplikationsentscheidungen)
        if self.verbose:
            print('Patienten {} haben einen schweren Verlauf'.format(np.where(komplikationsentscheidungen)))

    def _step_kranke_sterben(self):
        sterbeentscheidungen = np.random.randint(
            0, self.mortalitaetsfaktor, size=self.bevoelkerungszahl
        )
        # nur kranke oder schwerkranke koennen versterben (eigtl nur schwerkrank)
        sterbeentscheidungen = np.logical_and(
            np.logical_or(
                self.status == Krankheitsstatus.KRANK,
                self.status == Krankheitsstatus.SCHWERKRANK
            ),
            sterbeentscheidungen == 1
        )
        self.status[sterbeentscheidungen] = Krankheitsstatus.TOT
        if self.verbose:
            print('Patienten {} sind verstorben'.format(np.where(sterbeentscheidungen)))

    def _step_menschen_werden_gesund(self):
        # handle the healing
        ind_krankheit_vorbei = self.krankentag > self.krankheitsdauer

        self.status[ind_krankheit_vorbei] = Krankheitsstatus.IMMUN if self.immunisierung else \
            Krankheitsstatus.GESUND
        self.krankentag[ind_krankheit_vorbei] = 0

    def step(self):
        """
        Fuehre einen Schritt der Simulation aus
        """
        self.tag = self.tag + 1

        # filtere alle kranken und schwerkranken und aktualisiere die krankehitstage
        ist_krank = np.logical_or(self.status == Krankheitsstatus.KRANK, self.status == Krankheitsstatus.SCHWERKRANK)
        self.krankentag[ist_krank] += 1

        # wenn keine menschen krank sind kann niemand erkrankne
        if np.sum(ist_krank) == 0:
            return

        # TODO: das wirkt noch etwas kompliziert
        # alle kranken koennen anstecken
        ansteckungsentscheidungen_fuer_kranke = np.random.randint(
            low=0, high=int (self.inkubationszeit / self.ansteckungsfaktor ),
            size=np.sum(ist_krank)
        )
        ind_ansteckungsentscheidungen_fuer_kranke = np.where(ansteckungsentscheidungen_fuer_kranke == 1)
        if self.ansteckung_nach_inkubation == False:
            # Pruefe ob diese bereits ansteckend sind
            krankheitstage_fuer_ansteckende = self.krankentag[ind_ansteckungsentscheidungen_fuer_kranke]
            krankheitstage_unter_inkubationszeit = np.where(krankheitstage_fuer_ansteckende < self.inkubationszeit)
            ansteckungsentscheidungen_fuer_kranke[krankheitstage_unter_inkubationszeit] = 0

        positive_ansteckungen = np.sum(ansteckungsentscheidungen_fuer_kranke == 1)
        ansteckungsziele = np.random.randint(
            low=0, high=self.bevoelkerungszahl, size=(positive_ansteckungen)
        )
        # Sicherstellen, dass die ansteckungsziele einzigartig sind
        ansteckungsziele = np.unique(ansteckungsziele)
        # nur gesunde personen koennen erkranken
        _status = self.status[ansteckungsziele]
        ansteckungsziele = ansteckungsziele[_status == Krankheitsstatus.GESUND]

        # zuweisen
        self.infizierte_history += ansteckungsziele.shape[0]
        self.setze_krank(ansteckungsziele)
        # self.status[ansteckungsziele] = Krankheitsstatus.KRANK
        # self.krankentag[ansteckungsziele] = 1

        self._step_kranke_zu_schwerkrank()

        self._step_kranke_sterben()

        self._step_menschen_werden_gesund()

    def print_summary(self):
        self.statistiken['geheilte'].append(self.geheilte)
        self.statistiken['infizierte'].append(self.infizierte_history)
        self.statistiken['tote'].append(self.tote)

        print(f'Tag {self.tag: >4}: - akut Inf.: {self.infizierte: >7} Summe: {self.infizierte_history: >7} '
              f'- akut Intensivpat.: {self.schwerkranke: >7} Summe: {self.schwerkranke_history: >7} - '
              f'Geheilte: {self.geheilte: >7} - Tote: {self.tote: >7}'.format(self=self))
        # print ("Tag", self.tag, ": - akut Inf.: ", self.infizierte, "Summe:", self.infizierte_history, " - akut Intensivpat.: ", self.schwerkranke, "Summe:", self.schwerkranke_history, " - Geheilte:", self.geheilte, " - Tote:", self.tote)

if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument('--bevoelkerungszahl', type=int, default=1000000)
    parser.add_argument('--inkubationszeit', type=int, default=7)  # in Tagen
    parser.add_argument('--krankheitsdauer', type=int, default=28)  # in Tagen
    parser.add_argument('--ansteckung_nach_inkubation', action='store_true', default=False)  # in Tagen
    parser.add_argument('--ansteckungsfaktor', type=int, default=3)  # in Tagen
    parser.add_argument('--mortalitaetsfaktor', type=int, default=1000)   # "einer von 1000 stirbt..."
    parser.add_argument('--immunisierung', action='store_false', default=True) # bisschen verdreht
    parser.add_argument('--komplikationsquote', type=int, default=100)
    parser.add_argument('--simulationsdauer', type=int, default=365)
    parser.add_argument('--verbose', action='store_true', default=False)

    args = parser.parse_args()

    cs = CoronaSimulation(
        args.bevoelkerungszahl, args.inkubationszeit,
        ansteckung_nach_inkubation=args.ansteckung_nach_inkubation,
        ansteckungsfaktor=args.ansteckungsfaktor,
        komplikationsquote = args.komplikationsquote,
        mortalitaetsfaktor=args.mortalitaetsfaktor,
        krankheitsdauer=args.krankheitsdauer,
        immunisierung=args.immunisierung,
        verbose=args.verbose
    )

    fig = None
    if 'matplotlib' in sys.modules:
        fig = plt.figure(0)

    for tag in range(args.simulationsdauer):
        cs.step()
        cs.print_summary()

        if cs.infizierte == 0:
            print('Keine Infizierte mehr die Pandemie ist beendet')
            break

        if fig is not None:
            fig.clf()
            plt.plot(np.arange(len(cs.statistiken['infizierte'])), cs.statistiken['infizierte'])
            plt.xlabel('Tage')
            plt.ylabel('Infizierte')
            plt.draw()
            plt.pause(0.05)

