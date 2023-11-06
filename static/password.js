import { createApp } from 'https://unpkg.com/petite-vue?module'

createApp({
$delimiters: ['[[', ']]'],
password: "",
genera_password() {
    let pass = '';
    let str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' +
        'abcdefghijklmnopqrstuvwxyz0123456789@#$!?%';

    for (let i = 1; i <= parseInt(document.getElementById('numero').value); i++) {
        let char = Math.floor(Math.random()
            * str.length + 1);

        pass += str.charAt(char)
    }
    document.getElementById('numero').value
    this.password = pass
}
}).mount()
