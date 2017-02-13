from pyknon.genmidi import Midi
from pyknon.music import NoteSeq
from pyknon.music import Note, Rest




duration = 1

def generateSound (inputS)
    #--------Construction of Note----------------

    note_sequence = []

    #Takes inputS and maps it to a semitone.
    #0-3 -> Eb 2nd Octave , 252-255 -> F# 7th Octave

    scaled_value = int(inputS / 4) #Scales value from 0-63
    note_value = (scaled_value + 27) % 12
    octave = int((scaled_value + 27 - note_value) / 12)
    note = Note(note_value, octave, duration)
    note_sequence.append(note) #Adds them to the note sequence

    sound = NoteSeq(note_sequence)



    #-------Creating MIDI file -------------

    m2 = Midi(2, tempo=60, channel=[0,9], instrument= [3,3])
    #See https://www.midi.org/specifications/item/gm-level-1-sound-set for instrument codes
    m2.seq_notes(sound, track=0, channel=0)
    m2.write("output.mid")