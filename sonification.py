import pandas as pd
import matplotlib.pyplot as plt
from audiolazy import str2midi 
from midiutil import MIDIFile 
import pygame


def map_value(value, min_value, max_value, min_result, max_result):
        result = min_result + (value - min_value)/(max_value - min_value)*(max_result - min_result) + 0.2
        return result


class Sonification:
    def __init__(self, dataframe, class_name, y_axis, x_axis, graph = 'Line Graph'):
        self.dataframe = dataframe
        self.class_name = 'State'
        self.y_axis = y_axis
        self.x_axis = x_axis

    

    def make_sonifications(self):
        no_of_classes = self.dataframe[self.class_name].unique()

        for class_name in no_of_classes:
            y_axis = self.dataframe[self.dataframe[self.class_name] == class_name][self.y_axis].values
            x_axis = self.dataframe[self.dataframe[self.class_name] == class_name][self.x_axis].values

            n_impacts = len(x_axis)

            duration_beats = n_impacts
            bpm = 60 
            y_scale = 0.5 
            note_names = ['C1','C2','G2', 'C3','E3','G3','A3','B3', 'D4','E4','G4','A4','B4', 'D5','E5','G5','A5','B5','D6','E6','F#6','G6','A6']
            vel_min,vel_max = 35, 127 

            t_data = map_value(x_axis, min(x_axis), max(x_axis), duration_beats, 0)
            duration_sec = max(t_data)*60/bpm
            
            y_data = map_value(y_axis, min(y_axis), max(y_axis), 0, 1) 
            y_data = y_data**y_scale

            note_midis = [str2midi(n) for n in note_names] 
            n_notes = len(note_midis)
            
            midi_data = []
            vel_data = []
            for i in range(n_impacts):
                note_index = round(map_value(y_data[i], 0, 1, n_notes-1, 0)) 
                midi_data.append(note_midis[note_index])

                note_velocity = round(map_value(y_data[i], 0, 1, vel_min, vel_max)) 
                vel_data.append(note_velocity)

           
            my_midi_file = MIDIFile(1) 
            my_midi_file.addTempo(track=0, time=0, tempo=bpm)

            for i in range(n_impacts):
                my_midi_file.addNote(track=0, channel=0, pitch=midi_data[i], time=t_data[i] , duration=2, volume=vel_data[i])
            
            filename = class_name
            with open(filename + '.mid', "wb") as f:
                my_midi_file.writeFile(f)


    def play_plot(self, class_name):
        pygame.init()
        pygame.mixer.music.load(class_name + '.mid')
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.wait(1000)

