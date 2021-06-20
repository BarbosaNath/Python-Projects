from enum import IntEnum


class Note(IntEnum):
    C  = 0
    CS = 1
    D  = 2
    DS = 3
    E  = 4
    F  = 5
    FS = 6
    G  = 7
    GS = 8
    A  = 9
    AS = 10
    B  = 11





class Notes:
    def __init__(self, note, radius = 15):
        self.note       = note
        self.radius     = radius
        self.is_enabled = False


        nName = lambda: Note(self.note).name
        self.note_name  = lambda: nName()[0]    if len(nName()) == 1 else nName()[0] + '#'
        self.note_name_ = lambda: nName()[0]+' 'if len(nName()) == 1 else nName()[0] + '#'



    def update(self):
        self.note = 11 if self.note<0 else 0 if self.note>11 else self.note

class Fret(object):
    def __init__(self, notes = [
                Notes(Note.G),
                Notes(Note.C),
                Notes(Note.E), 
                Notes(Note.A)]):
        self.notes = notes

    def half_step_up(self):
        half_toned = []
        for i in range(len(self.notes)): 
            half_toned.append(Notes(self.notes[i].note + 1))
            half_toned[i].update()
        return half_toned

    def half_step_down(self):
        half_toned = []
        for i in range(len(self.notes)): 
            half_toned.append(Note(self.notes[i].note + 1))
            half_toned[i].update()
        return half_toned
        


class Fret_board(object):
    def __init__(self, open_strs = Fret([
                Notes(Note.G),
                Notes(Note.C),
                Notes(Note.E), 
                Notes(Note.A)]),
                fret_num = 12):
        self.fret_num  = fret_num

        self.frets = []
        temp = open_strs
        for i in range(fret_num+1):
            self.frets.append( temp )
            temp = Fret( temp.half_step_up() )

    def print(self):
        for y in range(len(self.frets)): 
            for x in range(len(self.frets[y].notes)):
                print ('|' + self.frets[y].notes[x].note_name_(),end='')
            print('|')