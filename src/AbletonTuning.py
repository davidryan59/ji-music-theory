from typing import List


DEFAULT_OCT_NUM_SEPARATOR = "|"  # separates Ableton octave number from note name (inc. octave number) constructed here
DEFAULT_DIRECTORY = "data/output/ableton_tunings"
DEFAULT_FILENAME = "ableton_tuning"
DEFAULT_DESCRIPTION = "Ableton tuning file generated from Python script."
DEFAULT_SOURCE = None
DEFAULT_LINK = None


TEMPLATE_TEXT = """! <FILENAME>
!
<DESCRIPTION>
!
<NOTES_IN_SCALE>
!
<LIST_OF_FREQS_ON_NEWLINES>
!
! @ABL NOTE_NAMES <LIST_OF_DOUBLEQUOTED_NOTE_NAMES_SPACE_SEPARATED>"""


# This class creates an Ableton tuning file in .ascl format


# # Example:
# ascl = AbletonTuning(
#     freq_fractions=["1/1", "3/2", "2/1"],
#     note_names = ["C4", "G4", "C5"],
# )
# print(ascl)

def wrap_note_name(note_name, oct_num_in_note_name, separator=DEFAULT_OCT_NUM_SEPARATOR):
    res = f'"{note_name}{separator if oct_num_in_note_name else ""}"'
    return res


class AbletonTuning:

    def __init__(
            self,
            freq_fractions: List[str],
            note_names: List[str],
            oct_num_in_note_name: bool=False,
            oct_num_separator: str=DEFAULT_OCT_NUM_SEPARATOR,
            directory: str=DEFAULT_DIRECTORY,
            filename: str=DEFAULT_FILENAME,
            description: str=DEFAULT_DESCRIPTION,
            source: str=DEFAULT_SOURCE,
            link: str=DEFAULT_LINK,
            ref_pitch_oct: int=None,
            ref_pitch_note: int=0,
            ref_pitch_hz: float=None,
            note_range_min_oct: int=None,
            note_range_min_note: int=0,
        ):
        if len(freq_fractions) != len(note_names):
            raise Exception("freq_fractions, and note_names must be lists of the same length")
        
        note_names_wrapped = [wrap_note_name(x, oct_num_in_note_name) for x in note_names]

        self.text = f"{TEMPLATE_TEXT}"
        self.count_notes = len(freq_fractions) - 1
        self.freq_fractions = freq_fractions
        self.oct_num_in_note_name = oct_num_in_note_name
        self.oct_num_separator = oct_num_separator
        self.note_names = note_names_wrapped
        self.directory = directory
        self.filename = f"{filename}.ascl"
        self.description = description
        self.source = source
        self.link = link
        self.ref_pitch_oct = ref_pitch_oct
        self.ref_pitch_note = ref_pitch_note
        self.ref_pitch_hz = ref_pitch_hz
        self.note_range_min_oct = note_range_min_oct
        self.note_range_min_note = note_range_min_note


    def __repr__(self):
        self.text = f"{TEMPLATE_TEXT}"
        self.text = self.text.replace("<FILENAME>", self.filename)
        self.text = self.text.replace("<DESCRIPTION>", self.description)
        self.text = self.text.replace("<NOTES_IN_SCALE>", str(self.count_notes))
        self.text = self.text.replace("<LIST_OF_FREQS_ON_NEWLINES>", "\n".join(self.freq_fractions[1:]))
        self.text = self.text.replace("<LIST_OF_DOUBLEQUOTED_NOTE_NAMES_SPACE_SEPARATED>", " ".join(self.note_names[:-1]))
        
        if type(self.ref_pitch_oct) == int and type(self.ref_pitch_note) == int and type(self.ref_pitch_hz) in (int, float):
            self.text += f"\n! @ABL REFERENCE_PITCH {self.ref_pitch_oct} {self.ref_pitch_note} {self.ref_pitch_hz}"
        
        if type(self.note_range_min_oct) == int and type(self.note_range_min_note) == int:
            self.text += f"\n! @ABL NOTE_RANGE_BY_INDEX {self.note_range_min_oct} {self.note_range_min_note}"

        if self.source is not None:
            self.text += f"\n! @ABL SOURCE {self.source}"

        if self.link is not None:
            self.text += f"\n! @ABL LINK {self.link}"

        return self.text


    def savefile(self):
        # Open the file for writing
        with open(f"{self.directory}/{self.filename}", "w") as f:
            f.write(f"{self}")
