import sys
import unittest
import pprint

NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

CHORDS = ["maj", "min", "sus2", "sus4", "aug", "dim", "major6", "major7", "dom7", "min7", "min7Flat5", "dim7", "maj9", "dom9", "dom11", "dom13", "majAdd9"]

STEPS = [0, 2, 2, 1, 2, 2, 2]

class Triad:

    def __init__(self, root):
        self._steps = STEPS
        self._notes = NOTES

        # Find the root note of the scale in the notes array and fold the array
        index = self._notes.index(root)
        if (index < 0):
            print("Failed to find root note ${0} in notes ${1}".format(root, NOTES))
            return
        self._notes.extend(self._notes)
        self._notes = self._notes[slice(index, index + len(NOTES))]

        # Use the steps to walk through and construct the scale
        self._scale = []
        offset = 0
        for s in self._steps:
            offset = offset + s
            self._scale.append(self._notes[offset])

    def flat(self, note):
        index = self._notes.index(note)
        if index == 0:
            index = len(self._notes)-1
        else:
            index = index - 1
        return self._notes[index]

    def sharp(self, note):
        index = self._notes.index(note)
        if index == len(self._notes)-1:
            index = 0
        else:
            index = index + 1
        return self._notes[index]

    def scale(self):
        return self._scale

    def steps(self):
        return self._steps

    def notes(self):
        return self._notes

    def root(self):
        return self._scale[0]
    
    def first(self):
        return self._scale[0]

    def second(self):
        return self._scale[1]

    def third(self):
        return self._scale[2]

    def fourth(self):
        return self._scale[3]

    def fifth(self):
        return self._scale[4]

    def sixth(self):
        return self._scale[5]

    def seventh(self):
        return self._scale[6]

    def nineth(self):
        return self._scale[8-7]

    def eleventh(self):
        return self._scale[10-7]

    def thirteenth(self):
        return self._scale[12-7]

    def maj(self):
        return [ self.first(), self.third(), self.fifth()]

    def min(self):
        return [ self.first(), self.flat(self.third()), self.fifth()]

    def sus2(self):
        return [ self.first(), self.second(), self.fifth()]

    def sus4(self):
        return [ self.first(), self.fourth(), self.fifth()]

    def aug(self):
        return [ self.first(), self.third(), self.sharp(self.fifth())]

    def dim(self):
        return [ self.first(), self.flat(self.third()), self.flat(self.fifth())]

    def major6(self):
        return [ self.first(), self.third(), self.fifth(), self.sixth()]

    def major7(self):
        return [ self.first(), self.third(), self.fifth(), self.seventh()]

    def dom7(self):
        return [ self.first(), self.third(), self.fifth(), self.flat(self.seventh())]

    def min7(self):
        return [ self.first(), self.flat(self.third()), self.fifth(), self.flat(self.seventh())]

    def min7Flat5(self):
        return [ self.first(), self.flat(self.third()), self.flat(self.fifth()), self.flat(self.seventh())]

    def dim7(self):
        return [ self.first(), self.flat(self.third()), self.flat(self.fifth()), self.flat(self.flat(self.seventh()))]

    def maj9(self):
        return [ self.first(), self.third(), self.fifth(), self.seventh(), self.nineth()]

    def dom9(self):
        return [ self.first(), self.third(), self.fifth(), self.flat(self.seventh()), self.nineth()]

    def dom11(self):
        return [ self.first(), self.third(), self.fifth(), self.flat(self.seventh()), self.nineth(), self.eleventh()]

    def dom13(self):
        return [ self.first(), self.third(), self.fifth(), self.flat(self.seventh()), self.nineth(), self.eleventh(), self.thirteenth()]

    def majAdd9(self):
        return [ self.first(), self.third(), self.fifth(), self.nineth()]


class TestTriadMethods(unittest.TestCase):

    def test_triad(self):
        t = Triad('C')
        self.assertTrue(t)

    def test_flat(self):
        t = Triad('C')
        self.assertTrue(t.flat('C') == 'B')

    def test_sharp(self):
        t = Triad('C')
        self.assertTrue(t.sharp('C') == 'C#')

    def test_scale(self):
        t = Triad('C')
        self.assertTrue(t.scale() == ['C', 'D', 'E', 'F', 'G', 'A', 'B'])

    def test_steps(self):
        t = Triad('C')
        self.assertTrue(t.steps() == STEPS)

    def test_notes(self):
        t = Triad('C')
        self.assertTrue(t.notes() == NOTES)

    def test_root(self):
        t = Triad('C')
        self.assertTrue(t.root() == 'C')
    
    def test_first(self):
        pass

    def test_second(self):
        pass

    def test_third(self):
        pass

    def test_fourth(self):
        pass

    def test_fifth(self):
        pass

    def test_sixth(self):
        pass

    def test_seventh(self):
        pass

    def test_nineth(self):
        pass

    def test_eleventh(self):
        pass

    def test_thirteenth(self):
        pass

    def test_maj(self):
        t = Triad('C')
        self.assertTrue(t.maj() == ['C', 'E', 'G'])

    def test_min(self):
        pass

    def test_sus2(self):
        pass

    def test_sus4(self):
        pass

    def test_aug(self):
        pass

    def test_dim(self):
        pass

    def test_major6(self):
        pass

    def test_major7(self):
        pass

    def test_dom7(self):
        pass

    def test_min7(self):
        pass

    def test_min7Flat5(self):
        pass

    def test_dim7(self):
        pass

    def test_maj9(self):
        pass

    def test_dom9(self):
        pass

    def test_dom11(self):
        pass

    def test_dom13(self):
        pass

    def test_majAdd9(self):
        pass

def printList(l):
    if l[0] == '=':
        sys.stdout.write('|')
        for item in l:
            sys.stdout.write(item)
            sys.stdout.write('|')
        sys.stdout.write("\n")
    elif l[0] == '-':
        sys.stdout.write('|')
        for item in l:
            sys.stdout.write(item)
            sys.stdout.write('|')
        sys.stdout.write("\n")
    else:
        sys.stdout.write('|')
        for item in l:
            sys.stdout.write(item)
            sys.stdout.write('|')
        sys.stdout.write("\n")

def advanceTuning(tuning):
    for i in range(0, len(tuning)):
        note = tuning[i]
        index = NOTES.index(note)
        if index == len(NOTES)-1:
            index = 0
        else:
            index = index + 1
        tuning[i] = NOTES[index]
    return tuning

def displayChord(tuning, chord):
    strings = [' ' for string in tuning]
    for i in range(0, len(tuning)):
        if tuning[i] in chord:
            strings[i] = '0'
    printList(strings)
    strings = ['=' for string in tuning]
    printList(strings)
    for fret in range(1, 15):
        tuning = advanceTuning(tuning)
        strings = [' ' for string in tuning]
        #printList(strings)
        for i in range(0, len(tuning)):
            if tuning[i] in chord:
                strings[i] = '0'
        printList(strings)
        strings = ['-' for string in tuning]
        printList(strings)

if __name__ == '__main__':
    #unittest.main()
    for note in NOTES:
        t = Triad(note)
        print("root = {0}".format(t.root()))
        for chord in CHORDS:
            notes = getattr(t, chord)()
            print("{0}{1} = {2}".format(t.root(), chord, notes))
            displayChord(['E', 'A', 'D', 'G', 'B' , 'E'], notes)
            print("\n")