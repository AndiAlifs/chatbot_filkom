
    const msgerForm = get(".msger-inputarea");
    const msgerInput = get(".msger-input");
    const msgerChat = get(".msger-chat");

    const BOT_IMG = "static/halofilkom.png";
    const PERSON_IMG = "static/mahastudent.png";
    const BOT_NAME = "HaloFILKOM";
    const PERSON_NAME = "You";

    msgerForm.addEventListener("submit", event => {
      event.preventDefault();

      const msgText = msgerInput.value;
      if (!msgText) return;

      appendMessage(PERSON_NAME, PERSON_IMG, "right", msgText);
      msgerInput.value = "";
      botResponse(msgText);
    });

    function appendMessage(name, img, side, text) {
      //   Simple solution for small apps
      const msgHTML = `
            <div class="msg ${side}-msg">
              <div class="msg-img" style="background-image: url(${img})"></div>

              <div class="msg-bubble">
                <div class="msg-info">
                  <div class="msg-info-name">${name}</div>
                  <div class="msg-info-time">${formatDate(new Date())}</div>
                </div>

                <div class="msg-text">${text}</div>
              </div>
            </div>
            `;
      msgerChat.insertAdjacentHTML("beforeend", msgHTML);
      msgerChat.scrollTop += 500;
    }

    function botResponse(rawText) {

      // Bot Response
      $.get("/get", { msg: rawText }).done(function (data) {
        console.log(rawText);
        console.log(data);
        const msgText = data;

        // text2speech
        // responsiveVoice.speak(msgText, "Indonesian Female");
        
        appendMessage(BOT_NAME, BOT_IMG, "left", msgText);
        if (msgText != "Terima kasih telah menggunakan layanan HaloFILKOM Bot, jika ada hal hal yang ingin ditanyakan lebih lanjut jangan ragu menghubungi saya lagi. Have a good day.") {
          appendMessage(BOT_NAME, BOT_IMG, "left", "Apakah ada pertanyaan yang ingin anda tanyakan atau sudah cukup?");
        } else{
          appendMessage(BOT_NAME, BOT_IMG, "left","Jika berkenan silahkan mengisi form berikut sebagai bentuk evaluasi dari penelitian dan pengembangan kami. Terima kasih 😊🙏");
          appendMessage(BOT_NAME, BOT_IMG, "left","Evaluasi Efisiensi dan Efektivitas : <a href='http://s.ub.ac.id/evalfilkombot1' target='_blank'>Form Evaluasi Bot 1</a> <br> Evaluasi Satisfaction : <a href='http://s.ub.ac.id/evalfilkombot2' target='_blank'>Form Evaluasi Bot 2</a>");
        }
      });

    }


    // Utils
    function get(selector, root = document) {
      return root.querySelector(selector);
    }

    function formatDate(date) {
      const h = "0" + date.getHours();
      const m = "0" + date.getMinutes();

      return `${h.slice(-2)}:${m.slice(-2)}`;
    }


