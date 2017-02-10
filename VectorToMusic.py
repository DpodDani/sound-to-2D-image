from pyknon.genmidi import Midi
from pyknon.music import NoteSeq
from pyknon.music import Note, Rest
import math

#Input Vector, currently set to test.


def generateMusic(inputV, inputTempo, scaleType):

    dimension = math.log(len(inputV), 2) #Equals N, where the length of inputV is 2^N
    duration = math.pow(len(inputV)/4, -1) #Scales the note duration accordingly.
    print(duration)
    #--------Construction of Note Sequence----------------

    note_sequence = [Rest(2)] #Create two bars of rest at the start.

    for value in inputV:

        #Note Value:
        #0-C, 1-C#, 2-D, 3-D#, 4-E, 5-F, 6-F#
        #7-G, 8-G#, 9-A, 10-A#, 11-B


        if(scaleType == 0):
            #----CHROMATIC----------
            #Takes values from inputV and maps them to semitones.
            #0-3 -> Eb 2nd Octave , 252-255 -> F# 7th Octave

            scaled_value = int(value / 4) #Scales value from 0-63
            note_value = (scaled_value + 27) % 12
            octave = int((scaled_value + 27 - note_value) / 12)
            note = Note(note_value, octave, duration)
            note_sequence.append(note)

        if(scaleType == 1):

            #----DIATONIC------------

            #Over 4 Octaves, 28 notes
            #0-9 -> 3C
            #10-18 -> 3D
            #37-46
            #82-90 -> 4E

            #127-136 -> 5C , 137-146 -> 5D

            diatonicValue = [0, 2, 4, 5, 7, 9, 11]
            scaled_value = int(value / 9.1) #Scales value from 0-27
            note_value = (scaled_value) % 7 #Takes 14 -> 0 ie Middle C
            octave = int(scaled_value / 7) + 3 #0-6 = 3, 7-13 = 4, 14-20 = 5, 21-27 = 6
            note = Note(diatonicValue[note_value], octave, duration)
            note_sequence.append(note)

        #------------------------

        #Adds them to the note sequence

    melody = NoteSeq(note_sequence)


    #--------Backing Drumbeat Construction --------------------

    b = Note(11, 2)
    hh = Note(6, 3)

    drumBeat = NoteSeq([b, hh, hh, hh, b, hh, hh, hh, b, hh, hh, hh, b, hh, hh, hh, b, hh, hh, hh, b, hh, hh, hh])

    #-------Creating MIDI file -------------

    m2 = Midi(number_tracks=2, tempo=inputTempo, channel=[0,9], instrument= [61,3])
    #See https://www.midi.org/specifications/item/gm-level-1-sound-set for instrument codes
    m2.seq_notes(drumBeat, track=0, channel=9) #Channel 9 = Percussion
    m2.seq_notes(melody, track=1, channel=0)

    m2.write("output.mid")
    print("Success")
