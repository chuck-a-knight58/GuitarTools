class Triad {
  static get NOTES() {
    return ["C", "C#", "Db", "D", "D#", "Eb", "E", "F", "F#", "Gb", "G", "G#", "Ab", "A", "A#", "Bb", "B"];
  }

  static get CHORD_MODIFICATIONS() {
    return [
      "maj",
      "min",
      "sus2",
      "sus4",
      "aug",
      "dim",
      "major6",
      "major7",
      "dom7",
      "min7",
      "min7Flat5",
      "dim7",
      "maj9",
      "dom9",
      "dom11",
      "dom13",
      "majAdd9",
    ];
  }

  constructor(root, steps) {
    // Create the steps array using the step notation WWHWWWH
    this._steps = [];
    this._steps.push(0);
    for (let i = 0; i < 6; i++) {
      if (steps.charAt(i).toUpperCase() == "W") {
        this._steps.push(2);
      } else if (steps.charAt(i).toUpperCase() == "H") {
        this._steps.push(1);
      } else {
        console.log(`Unknown character in step array ${steps} (only W and H are allowed)`);
        return;
      }
    }

    var r = this.create_notes(root);
    this._notes = r[0];
    this._scale = r[1];
  }

  create_notes(root) {
    var notes = [
      ["C"],
      ["C#", "Db"],
      ["D"],
      ["D#", "Eb"],
      ["E"],
      ["F"],
      ["F#", "Gb"],
      ["G"],
      ["G#", "Ab"],
      ["A"],
      ["A#", "Bb"],
      ["B"],
    ];

    // Find the root note of the scale in the notes array and fold the array
    var index = -1;
    for (let i = 0; i < notes.length; i++) {
      if (notes[i].includes(root)) {
        index = i;
        break;
      }
    }
    if (index < 0) {
      console.log(`Failed to find root note ${root} in notes ${notes}`);
      return;
    }
    notes = notes.slice(index).concat(notes.slice(0, index));

    // Use the steps to walk through correctly spell the scale
    var letters_used = [];
    var scale = [];
    var offset = 0;

    // First is always spelled with the root
    letters_used.push(root[0]);
    notes[offset] = root;
    scale.push(root);

    // Now spell the rest of the scale
    for (let i = 1; i < this._steps.length; i++) {
      offset = offset + this._steps[i];
      var note = this.spell_note(letters_used, notes[offset]);
      letters_used.push(note[0]);
      notes[offset] = note;
      scale.push(note);
    }

    // Fix spelling of remaining notes
    for (let i = 0; i < notes.length; i++) {
      if (Array.isArray(notes[i])) {
        notes[i] = notes[i][0];
      }
    }

    // Correct any spelling errors in the scale
    // https://www.themusicalear.com/sharps-or-flats-how-to-spell-notes-correctly/

    return [notes, scale];
  }

  spell_note(letters_used, note) {
    var n;
    for (n of note) {
      var l = n[0];
      if (!letters_used.includes(l)) {
        letters_used.push(l);
        return n;
      }
    }

    console.log(`No valid choices for note spelling in notes ${note}`);
    return "";
  }

  flat(note) {
    var index = this._notes.findIndex((scale) => scale === note);
    if (index == 0) {
      index = this._notes.length - 1;
    } else {
      index = index - 1;
    }
    return this._notes[index];
  }

  sharp(note) {
    var index = this._notes.findIndex((scale) => scale === note);
    if (index == this._notes.length - 1) {
      index = 0;
    } else {
      index = index + 1;
    }
    return this._notes[index];
  }

  get scale() {
    return this._scale;
  }

  get steps() {
    return this._steps;
  }

  get notes() {
    return this._notes;
  }

  get root() {
    return this._scale[0];
  }

  get first() {
    return this._scale[0];
  }

  get second() {
    return this._scale[1];
  }

  get third() {
    return this._scale[2];
  }

  get fourth() {
    return this._scale[3];
  }

  get fifth() {
    return this._scale[4];
  }

  get sixth() {
    return this._scale[5];
  }

  get seventh() {
    return this._scale[6];
  }

  get nineth() {
    return this._scale[8 - 7];
  }

  get eleventh() {
    return this._scale[10 - 7];
  }

  get thirteenth() {
    return this._scale[12 - 7];
  }

  get maj() {
    return [this.first, this.third, this.fifth];
  }

  get min() {
    return [this.first, this.flat(this.third), this.fifth];
  }

  get sus2() {
    return [this.first, this.second, this.fifth];
  }

  get sus4() {
    return [this.first, this.fourth, this.fifth];
  }

  get aug() {
    return [this.first, this.third, this.sharp(this.fifth)];
  }

  get dim() {
    return [this.first, this.flat(this.third), this.flat(this.fifth)];
  }

  get major6() {
    return [this.first, this.third, this.fifth, this.sixth];
  }

  get major7() {
    return [this.first, this.third, this.fifth, this.seventh];
  }

  get dom7() {
    return [this.first, this.third, this.fifth, this.flat(this.seventh)];
  }

  get min7() {
    return [this.first, this.flat(this.third), this.fifth, this.flat(this.seventh)];
  }

  get min7Flat5() {
    return [this.first, this.flat(this.third), this.flat(this.fifth), this.flat(this.seventh)];
  }

  get dim7() {
    return [this.first, this.flat(this.third), this.flat(this.fifth), this.flat(this.flat(this.seventh))];
  }

  get maj9() {
    return [this.first, this.third, this.fifth, this.seventh, this.nineth];
  }

  get dom9() {
    return [this.first, this.third, this.fifth, this.flat(this.seventh), this.nineth];
  }

  get dom11() {
    return [this.first, this.third, this.fifth, this.flat(this.seventh), this.nineth, this.eleventh];
  }

  get dom13() {
    return [this.first, this.third, this.fifth, this.flat(this.seventh), this.nineth, this.eleventh, this.thirteenth];
  }

  get majAdd9() {
    return [this.first, this.third, this.fifth, this.nineth];
  }
}
