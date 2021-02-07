import webview
import threading
import time
import sys
import random
import os

def retrieveStyle():
    try:
        with open('css.txt') as my_new_file:
            css1 = my_new_file.read()
        return(css1)
    except:
        with open("css.txt", "w") as myfile:
                myfile.write("blue")
        css1 = "blue"
        return(css1)

css = retrieveStyle()

class Api:
    def findGame(self):
        window.load_url('https://krunker.io')

    def getStyle(self, value):
        with open("css.txt", "w") as myfile:
            myfile.write(value)
        global css
        css = retrieveStyle()
        window.load_url('https://krunker.io')


def intialize(window, css):
    grey_css = ".button { background-color: #414a6d !important; box-shadow: inset 0 -7px 0 0 #252a3d !important; } #termsInfo { background-color: rgba(0,0,0,0) } #voiceDisplay { display:none !important; } .redditSocial { display:none !important; } .downloadClient { display:none !important; } .discordSocial { display:none !important; } #aMerger { display: none !important } #mainLogo { width: 40%; height: auto; } #seasonLabel { display: none !important; } #ot-sdk-btn-floating { display: none !important; } #subLogoButtons { bottom: 50px !important; } #endAContainer { display: none !important; } #aContainer { display: none !important; } #newsHolder { display: none !important; } #streamContainer { display: none !important; } .menuItem { background-color: rgba(0,0,0,0) } #mLevelCont { background-color: #414a6d !important; }"
    pink_css = ".button { background-color: #fa50ae !important; box-shadow: inset 0 -7px 0 0 #b2397c !important; } #termsInfo { background-color: rgba(0,0,0,0) } #voiceDisplay { display:none !important; } .redditSocial { display:none !important; } .downloadClient { display:none !important; } .discordSocial { display:none !important; } #aMerger { display: none !important } #mainLogo { width: 40%; height: auto; } #seasonLabel { display: none !important; } #ot-sdk-btn-floating { display: none !important; } #subLogoButtons { bottom: 50px !important; } #endAContainer { display: none !important; } #aContainer { display: none !important; } #newsHolder { display: none !important; } #streamContainer { display: none !important; } .menuItem { background-color: rgba(0,0,0,0) } #mLevelCont { background-color: #fa50ae !important; }"
    purple_css = ".button { background-color: #b447ff !important; box-shadow: inset 0 -7px 0 0 #672992 !important; } #termsInfo { background-color: rgba(0,0,0,0) } #voiceDisplay { display:none !important; } .redditSocial { display:none !important } .downloadClient { display:none !important; } .discordSocial { display:none !important; } #aMerger { display: none !important } #mainLogo { width: 40%; height: auto; } #seasonLabel { display: none !important; } #ot-sdk-btn-floating { display: none !important; } #subLogoButtons { bottom: 50px !important; } #endAContainer { display: none !important; } #aContainer { display: none !important; } #newsHolder { display: none !important; } #streamContainer { display: none !important; } .menuItem { background-color: rgba(0,0,0,0) } #mLevelCont { background-color: #b447ff !important; }"
    red_css = ".button { background-color: #ff4747 !important; box-shadow: inset 0 -7px 0 0 #992b2b !important; } #termsInfo { background-color: rgba(0,0,0,0) } #voiceDisplay { display:none !important; } .redditSocial { display:none !important; } .downloadClient { display:none !important; } .discordSocial { display:none !important; } #aMerger { display: none !important } #mainLogo { width: 40%; height: auto; } #seasonLabel { display: none !important; } #ot-sdk-btn-floating { display: none !important; } #subLogoButtons { bottom: 50px !important; } #endAContainer { display: none !important; } #aContainer { display: none !important; } #newsHolder { display: none !important; } #streamContainer { display: none !important; } .menuItem { background-color: rgba(0,0,0,0) } #mLevelCont { background-color: #ff4747 !important; }"
    blue_css = ".button { background-color: #476aff !important; box-shadow: inset 0 -7px 0 0 #3047ab !important; } #termsInfo { background-color: rgba(0,0,0,0) } #voiceDisplay { display:none !important; } .redditSocial { display:none !important; } .downloadClient { display:none !important; } .discordSocial { display:none !important; } #aMerger { display: none !important } #mainLogo { width: 40%; height: auto; } #seasonLabel { display: none !important; } #ot-sdk-btn-floating { display: none !important; } #subLogoButtons { bottom: 50px !important; } #endAContainer { display: none !important; } #aContainer { display: none !important; } #newsHolder { display: none !important; } #streamContainer { display: none !important; } .menuItem { background-color: rgba(0,0,0,0) } #mLevelCont { background-color: #3047ab !important; }"

    window.show()

    window.evaluate_js(
        r"""

        document.getElementById('mainLogo').src = 'https://cdn.discordapp.com/attachments/748652979598655618/807746171883225128/title.png';
        document.getElementById('subLogoButtons').innerHTML += "<div class='button small buttonP' style='background-color: #9c9c9c !important; box-shadow: inset 0 -7px 0 0 #858585 !important;' onmouseenter='playTick()' onclick='findGame()' id='refreshGameBtn' >Find Game</div>";
        document.getElementById('headerRight').innerHTML += "<select id='cssdrop' onchange='setstyle()' class='inputGrey2'> <option value='blue'>Default</option> <option value='blue'>Blue CSS</option> <option value='grey'>Grey CSS</option> <option value='pink'>Pink CSS</option> <option value='purple'>Purple CSS</option> <option value='red'>Red CSS</option></select>"
        function findGame() {
            pywebview.api.findGame();
        }

        var terms = document.getElementById('termsInfo').children;
        for (var y = 0; y < terms.length-1; y++) {
            terms[y].remove();
        }

        var sep = document.querySelectorAll('.verticalSeparatorInline');
        for (var z = 0; z < sep.length; z++) {
            sep[z].remove();
        }

        function setstyle() {
            var value = document.getElementById("cssdrop").value;
            pywebview.api.getStyle(value);
        }

        document.getElementById('editorBtnM').remove();

        // Return user agent
        'User agent:\n' + navigator.userAgent;
        """
    )

    if (css == "blue"):
        css = blue_css
    elif (css == "red"):
        css = red_css
    elif (css == "pink"):
        css = pink_css
    elif (css == "grey"):
        css = grey_css
    elif (css == "purple"):
        css = purple_css
    elif (css == ""):
        css = blue_css

    window.load_css(css)


def on_loaded():
    global init

    if (init == "false"):
        intialize(window, css)

    init = "false"


api = Api()
window = webview.create_window('Chroma Client v1.2', 'https://krunker.io', resizable=True, width=1600, height=900, js_api=api)
init = "true"
window.loaded += on_loaded
#webview.start(intialize, window)


#startup

def closeWindow(launcher):
    window.hide()
    time.sleep(4)
    launcher.destroy()
    intialize(window, css)

launcher = webview.create_window('Chroma Client Launcher', 'https://kzapas.github.io/Extras/index.html', frameless=True, width=900, height=600, background_color='#333333', on_top=True)
webview.start(closeWindow, launcher)