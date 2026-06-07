import pretty_midi
import numpy as np
import matplotlib.pyplot as plt
import librosa.display
import IPython.display

pm = pretty_midi.PrettyMIDI(initial_tempo=130)
print(pm.instruments)

inst = pretty_midi.Instrument(program=1, is_drum=False)
pm.instruments.append(inst)

velocity = 100
for pitch, start, end in zip([60, 62, 64], [0.2, 0.6, 1.0], [1.1, 1.7, 2.3]):
    inst.notes.append(pretty_midi.Note(velocity, pitch, start, end))


pm.write('out.mid')