import { createApp } from 'https://unpkg.com/petite-vue?module'

createApp({
$delimiters: ['[[', ']]'],
genera_redirect() {
    window.location.href = 'https://wa.me/39'+document.getElementById('numero').value+'?'+encodeURI(document.getElementById('testo_messaggio').value);
}
}).mount()
