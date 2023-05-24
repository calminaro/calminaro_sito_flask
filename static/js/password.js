var caratteri = ["A", "B", "C", "1", "2", "3", "%", "&"];
var tmp_n = window.prompt("Di quanti caratteri deve essere la password? (inserisci un numero!)");
var n = parseInt(tmp_n);
var pw = "";
for (i=0; i<n; i++) {
    var charId = Math.floor(Math.random() * caratteri.length);
    pw = pw + caratteri[charId];
}
alert(pw);
