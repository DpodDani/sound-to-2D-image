from pyknon.genmidi import Midi
from pyknon.music import NoteSeq
from pyknon.music import Note, Rest
import math

#Input Vector, currently set to test.
inputV = [23, 44, 46, 156, 54, 1 , 0 , 55, 34, 223, 34, 45, 22, 54, 23, 11]


dimension = math.log(len(inputV), 2) #Equals N, where the length of inputV is 2^N
duration = 1/dimension #Scales the note duration accordingly.

#--------Construction of Note Sequence----------------

note_sequence = [Rest(2)] #Create two bars of rest at the start.

for value in inputV:
    #Takes values from inputV and maps them to semitones.
    #0-3 -> Eb 2nd Octave , 252-255 -> F# 7th Octave

    scaled_value = int(value / 4) #Scales value from 0-63
    note_value = (scaled_value + 27) % 12
    octave = int((scaled_value + 27 - note_value) / 12)
    note = Note(note_value, octave, duration)
    note_sequence.append(note) #Adds them to the note sequence

melody = NoteSeq(note_sequence)


#--------Backing Drumbeat Construction --------------------

b = Note(11, 2)
hh = Note(6, 3)

drumBeat = NoteSeq([b, hh, hh, hh, b, hh, hh, hh, b, hh, hh, hh, b, hh, hh, hh, b, hh, hh, hh, b, hh, hh, hh])

#-------Creating MIDI file -------------

m2 = Midi(2, tempo=60, channel=[0,9], instrument= [3,3])
#See https://www.midi.org/specifications/item/gm-level-1-sound-set for instrument codes
m2.seq_notes(drumBeat, track=0, channel=9) #Channel 9 = Percussion
m2.seq_notes(melody, track=1, channel=0)
m2.write("output.mid")
