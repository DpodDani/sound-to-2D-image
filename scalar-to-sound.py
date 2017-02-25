from pyknon.genmidi import Midi
from pyknon.music import NoteSeq
from pyknon.music import Note, Rest




duration = 1
def generateSound (colour):
    #--------Construction of Note----------------

    note_sequence = []

        #Takes colour and maps it to a note in the C Maj Chord.

    if (colour == "black"):
        note = Note("C4", duration)
    elif (colour == "red"):
        note = Note("D4", duration)
    elif (colour == "yellow"):
        note = Note("E4", duration)
    elif (colour == "green"):
        note = Note("F4", duration)
    elif (colour == "cyan"):
        note = Note("G4", duration)
    elif (colour == "blue"):
        note = Note("A4", duration)
    elif (colour == "magenta"):
        note = Note("B4", duration)
    elif (colour == "white"):
        note = Note("C5", duration)

    note
    note_sequence.append(note) #Adds them to the note sequence

    sound = NoteSeq(note_sequence)



        #-------Creating MIDI file -------------

    m2 = Midi(2, tempo=60, channel=[0,9], instrument= [3,3])
        #See https://www.midi.org/specifications/item/gm-level-1-sound-set for instrument codes
    m2.seq_notes(sound, track=0, channel=0)
    m2.write("output.mid")
