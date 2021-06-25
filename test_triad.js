var Triad = require('./triad.js');

function createChords(root) {
    var t = new Triad(root);
    console.log(`Scale = ${t.scale}`);
    console.log(`\t${t.root}          \t= ${t.maj}`);
    console.log(`\t${t.root}m         \t= ${t.min}`);
    console.log(`\t${t.root}sus2      \t= ${t.sus2}`);
    console.log(`\t${t.root}sus4      \t= ${t.sus4}`);
    console.log(`\t${t.root}aug       \t= ${t.aug}`);
    console.log(`\t${t.root}dim       \t= ${t.dim}`);
    console.log(`\t${t.root}6         \t= ${t.major6}`);
    console.log(`\t${t.root}7         \t= ${t.major7}`);
    console.log(`\t${t.root}dom7      \t= ${t.dom7}`);
    console.log(`\t${t.root}m7        \t= ${t.min7}`);
    console.log(`\t${t.root}m7Flat5   \t= ${t.min7Flat5}`);
    console.log(`\t${t.root}dim7      \t= ${t.dim7}`);
    console.log(`\t${t.root}9         \t= ${t.maj9}`);
    console.log(`\t${t.root}dom9      \t= ${t.dom9}`);
    console.log(`\t${t.root}dom11     \t= ${t.dom11}`);
    console.log(`\t${t.root}dom13     \t= ${t.dom13}`);
    console.log(`\t${t.root}add9      \t= ${t.majAdd9}`);
}

for (let i = 0; i < Triad.NOTES.length; i++) {
    createChords(Triad.NOTES[i]);
}
