// check if web speech recognition
if (! 'webkitSpeechRecognition' in window) {
    alert('Web Speech API is not supported by this browser. Upgrade to Chrome version 25 or later.');
}

const SpeechRecognition = window.SpeechRecognition || webkitSpeechRecognition;
const SpeechGrammarList = window.SpeechGrammarList || webkitSpeechGrammarList;
const SpeechRecognitionEvent = window.SpeechRecognitionEvent || webkitSpeechRecognitionEvent;

const grammar = '#JSGF V1.0; grammar filkom; public <filkom> = filkom ;'

let recognition = new SpeechRecognition();
let speechRecognitionList = new SpeechGrammarList();
speechRecognitionList.addFromString(grammar, 1);
recognition.grammars = speechRecognitionList;
recognition.lang = 'id-ID';

recognition.continuous = true;
recognition.interimResults = false;
recognition.maxAlternatives = 1;

let standby = false;

recognition.start();
console.log('Ready to receive a command.');

recognition.onresult = (event) => {
    let last = event.results.length - 1;
    let text = event.results[last][0].transcript;
    console.log(text);

        if (standby){
            document.querySelector('#textInput').value = text;
            console.log("kirim ke server");
            document.querySelector(".msger-send-btn").click();
    }
    if (text.toLowerCase().includes('halo filkom') || text.toLowerCase().includes('halo film')){
        standby = true;
        appendMessage(BOT_NAME, BOT_IMG, "left","Fungsi Voice Command Diaktifkan ✅");
    } else if (text.toLowerCase().includes('makasih filkom')  || text.toLowerCase().includes('makasih film')) {
        standby = false;
        appendMessage(BOT_NAME, BOT_IMG, "left","Fungsi Voice Command Dinonaktifkan ❌");
    }

}

recognition.end = (event) => {
    recognition.start();
}
