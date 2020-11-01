from mido import MidiFile, MidiTrack, Message

mid = MidiFile()
track = MidiTrack()

mid.tracks.append(track)

track.append(Message('program_change', program=12, time=0))
track.append(Message('note_on', note=64, velocity=64, time=320))
track.append(Message('note_off', note=64, velocity=127, time=320))

mid.save('usemido.mid')