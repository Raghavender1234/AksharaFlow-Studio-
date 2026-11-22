/**
 * AksharaFlow Studio — Core Multi-Script Desktop Application & Adaptive Coach
 * Supports English (QWERTY) + 13 Indian Languages (InScript Standard)
 */

const SCRIPT_GLYPHS = {
  en: "A",
  hi: "अ",
  mr: "म",
  sa: "सं",
  bn: "অ",
  pa: "ੳ",
  gu: "અ",
  or: "ଅ",
  ta: "அ",
  te: "అ",
  kn: "ಅ",
  ml: "അ",
  as: "অ",
  ur: "ع",
};

const QUICK_WELCOME_GUIDES = {
  hi: {
    title: "हिन्दी (InScript) कीबोर्ड कैसे चालू करें:",
    steps: [
      "अपने कंप्यूटर पर 'Windows + Space' दबाकर 'Hindi InScript' चुनें।",
      "या चिंता न करें — हमारा 'Auto-InScript स्मार्ट मोड' आपके अंग्रेजी कीबोर्ड से भी सीधे हिन्दी टाइप करेगा!"
    ]
  },
  mr: {
    title: "मराठी (InScript) कीबोर्ड कसा सुरू करावा:",
    steps: [
      "संगणकावर 'Windows + Space' दाबून 'Marathi InScript' निवडा.",
      "किंवा काळजी करू नका — आमचा 'Auto-InScript' मोड तुमच्या इंग्रजी कीबोर्डवरूनही थेट मराठी टाइप करेल!"
    ]
  },
  sa: {
    title: "संस्कृतम् (InScript) टङ्कनफलकं कथं प्रारभेत:",
    steps: [
      "संगणके 'Windows + Space' नुत्वा 'Sanskrit / Devanagari InScript' चिनुत।",
      "अथवा 'Auto-InScript' सुविधया साक्षात् संस्कृत-टङ्कनं कुरुत!"
    ]
  },
  bn: {
    title: "বাংলা (InScript) কীবোর্ড কীভাবে চালু করবেন:",
    steps: [
      "কম্পিউটারে 'Windows + Space' চেপে 'Bengali InScript' নির্বাচন করুন।",
      "অথবা আমাদের 'Auto-InScript' মোডের মাধ্যমে সরাসরি বাংলা টাইপ শুরু করুন!"
    ]
  },
  pa: {
    title: "ਪੰਜਾਬੀ (InScript) ਕੀਬੋਰਡ ਕਿਵੇਂ ਚਾਲੂ ਕਰੀਏ:",
    steps: [
      "ਆਪਣੇ ਕੰਪਿਊਟਰ 'ਤੇ 'Windows + Space' ਦਬਾ ਕੇ 'Punjabi InScript' ਚੁਣੋ।",
      "ਜਾਂ ਸਾਡੇ ਬਿਲਟ-ਇਨ 'Auto-InScript' ਮੋਡ ਨਾਲ ਸਿੱਧਾ ਪੰਜਾਬੀ ਟਾਈਪ ਕਰੋ!"
    ]
  },
  gu: {
    title: "ગુજરાતી (InScript) કીબોર્ડ કેવી રીતે ચાલુ કરવું:",
    steps: [
      "તમારા કમ્પ્યુટર પર 'Windows + Space' દબાવીને 'Gujarati InScript' પસંદ કરો.",
      "અથવા અમારા 'Auto-InScript' મોડથી સીધું જ ગુજરાતી ટાઇપિંગ શરૂ કરો!"
    ]
  },
  or: {
    title: "ଓଡ଼ିଆ (InScript) କିବୋର୍ଡ୍ କିପରି ଚାଲୁ କରିବେ:",
    steps: [
      "କମ୍ପ୍ୟୁଟରରେ 'Windows + Space' ଦବାଇ 'Odia InScript' ବାଛନ୍ତୁ।",
      "କିମ୍ବା ଆମର 'Auto-InScript' ମୋଡ୍ ସାହାଯ୍ୟରେ ସିଧାସଳଖ ଓଡ଼ିଆ ଟାଇপ୍ କରନ୍ତୁ!"
    ]
  },
  ta: {
    title: "தமிழ் (InScript) விசைப்பலகையை இயக்குவது எப்படி:",
    steps: [
      "கணினியில் 'Windows + Space' அழுத்தி 'Tamil InScript' என்பதைத் தேர்ந்தெடுக்கவும்.",
      "அல்லது எமது 'Auto-InScript' வசதி மூலம் நேரடியாகத் தமிழில் தட்டச்சு செய்யத் தொடங்குங்கள்!"
    ]
  },
  te: {
    title: "తెలుగు (InScript) కీబోర్డును ఎలా ప్రారంభించాలి:",
    steps: [
      "కంప్యూటర్‌లో 'Windows + Space' నొక్కి 'Telugu InScript' ఎంచుకోండి.",
      "లేదా మా 'Auto-InScript' సదుపాయంతో నేరుగా తెలుగులో టైప్ చేయడం ప్రారంభించండి!"
    ]
  },
  kn: {
    title: "ಕನ್ನಡ (InScript) ಕೀಬೋರ್ಡ್ ಆನ್ ಮಾಡುವುದು ಹೇಗೆ:",
    steps: [
      "ಕಂಪ್ಯೂಟರ್‌ನಲ್ಲಿ 'Windows + Space' ಒತ್ತಿ 'Kannada InScript' ಆಯ್ಕೆಮಾಡಿ.",
      "ಅಥವಾ ನಮ್ಮ 'Auto-InScript' ಸ್ಮಾರ್ಟ್ ಮೋಡ್ ಮೂಲಕ ನೇರವಾಗಿ ಕನ್ನಡದಲ್ಲಿ ಟೈಪ್ ಮಾಡಿ!"
    ]
  },
  ml: {
    title: "മലയാളം (InScript) കീബോർഡ് എങ്ങനെ ഓണാക്കാം:",
    steps: [
      "കമ്പ്യൂട്ടറിൽ 'Windows + Space' അമർത്തി 'Malayalam InScript' തിരഞ്ഞെടുക്കുക.",
      "അല്ലെങ്കിൽ ഞങ്ങളുടെ 'Auto-InScript' മോഡ് വഴി നേരിട്ട് മലയാളം ടൈപ്പ് ചെയ്യാം!"
    ]
  },
  as: {
    title: "অসমীয়া (InScript) কীবোৰ্ড কেনেকৈ অন কৰিব:",
    steps: [
      "কম্পিউটাৰত 'Windows + Space' টিপি 'Assamese InScript' বাছনি কৰক।",
      "অথবা আমাৰ 'Auto-InScript' মোডৰ জৰিয়তে পোনে পোনে অসমীয়া টাইপ কৰক!"
    ]
  },
  ur: {
    title: "اردو کی بورڈ کیسے آن کریں:",
    steps: [
      "اپنے کمپیوٹر پر 'Windows + Space' دبا کر 'Urdu' کی بورڈ منتخب کریں۔",
      "یا ہمارے بلٹ ان 'Auto-Mapper' موڈ کے ذریعے براہِ راست اردو ٹائپنگ شروع کریں!"
    ]
  }
};

let APP_STATE = {
  user: null,
  activeLanguage: "en",
  selectedWelcomeLang: "en",
  autoInscriptEnabled: true,

  units: [],
  allLessons: [],
  progressMap: {},
  recentSessions: [],
  telemetry: [],
  weaknessAnalysis: null,
  recommendedRemedial: null,
  speedPassages: [],
  fingerMap: {},
  fingerLabels: {},
  languages: [],
  inscriptKeymap: null,
  inscriptSetupGuide: null,
  nativeVocab: null,
  activeTab: "course",

  // Active Practice Session State
  currentDrill: null,
  charIndex: 0,
  streakCombo: 0,
  errorIndices: new Set(),
  totalTypedChars: 0,
  totalErrorChars: 0,
  startTimeMs: null,
  lastKeystrokeMs: null,
  timerInterval: null,
  isCompleted: false,
  keyStats: {},

  speedTestDurationSec: 60,
  selectedPassageId: "st_en_1",
};

// Offline Web Audio Synthesizer
const SoundFX = {
  ctx: null,
  enabled: true,

  init() {
    if (!this.ctx) {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (AudioCtx) this.ctx = new AudioCtx();
    }
    if (this.ctx && this.ctx.state === "suspended") {
      this.ctx.resume();
    }
  },

  playClick() {
    if (!this.enabled) return;
    try {
      this.init();
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = "triangle";
      osc.frequency.setValueAtTime(560, this.ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(175, this.ctx.currentTime + 0.026);
      gain.gain.setValueAtTime(0.11, this.ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.026);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start();
      osc.stop(this.ctx.currentTime + 0.028);
    } catch (e) {}
  },

  playError() {
    if (!this.enabled) return;
    try {
      this.init();
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = "sine";
      osc.frequency.setValueAtTime(210, this.ctx.currentTime);
      osc.frequency.setValueAtTime(160, this.ctx.currentTime + 0.045);
      gain.gain.setValueAtTime(0.14, this.ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.004, this.ctx.currentTime + 0.1);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start();
      osc.stop(this.ctx.currentTime + 0.11);
    } catch (e) {}
  },

  playFanfare() {
    if (!this.enabled) return;
    try {
      this.init();
      const notes = [523.25, 659.25, 783.99, 1046.5];
      notes.forEach((freq, i) => {
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = "sine";
        const t = this.ctx.currentTime + i * 0.085;
        osc.frequency.setValueAtTime(freq, t);
        gain.gain.setValueAtTime(0.13, t);
        gain.gain.exponentialRampToValueAtTime(0.001, t + 0.24);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(t);
        osc.stop(t + 0.25);
      });
    } catch (e) {}
  }
};

// Base Physical ANSI QWERTY Keyboard Layout
const KEYBOARD_ROWS = [
  [
    { main: "`", shift: "~", code: "Backquote", finger: "L_PINKY" },
    { main: "1", shift: "!", code: "Digit1", finger: "L_PINKY" },
    { main: "2", shift: "@", code: "Digit2", finger: "L_RING" },
    { main: "3", shift: "#", code: "Digit3", finger: "L_MIDDLE" },
    { main: "4", shift: "$", code: "Digit4", finger: "L_INDEX" },
    { main: "5", shift: "%", code: "Digit5", finger: "L_INDEX" },
    { main: "6", shift: "^", code: "Digit6", finger: "R_INDEX" },
    { main: "7", shift: "&", code: "Digit7", finger: "R_INDEX" },
    { main: "8", shift: "*", code: "Digit8", finger: "R_MIDDLE" },
    { main: "9", shift: "(", code: "Digit9", finger: "R_RING" },
    { main: "0", shift: ")", code: "Digit0", finger: "R_PINKY" },
    { main: "-", shift: "_", code: "Minus", finger: "R_PINKY" },
    { main: "=", shift: "+", code: "Equal", finger: "R_PINKY" },
    { main: "Bksp", shift: "", code: "Backspace", finger: "R_PINKY", width: "w-18", special: true },
  ],
  [
    { main: "Tab", shift: "", code: "Tab", finger: "L_PINKY", width: "w-15", special: true },
    { main: "q", shift: "Q", code: "KeyQ", finger: "L_PINKY" },
    { main: "w", shift: "W", code: "KeyW", finger: "L_RING" },
    { main: "e", shift: "E", code: "KeyE", finger: "L_MIDDLE" },
    { main: "r", shift: "R", code: "KeyR", finger: "L_INDEX" },
    { main: "t", shift: "T", code: "KeyT", finger: "L_INDEX" },
    { main: "y", shift: "Y", code: "KeyY", finger: "R_INDEX" },
    { main: "u", shift: "U", code: "KeyU", finger: "R_INDEX" },
    { main: "i", shift: "I", code: "KeyI", finger: "R_MIDDLE" },
    { main: "o", shift: "O", code: "KeyO", finger: "R_RING" },
    { main: "p", shift: "P", code: "KeyP", finger: "R_PINKY" },
    { main: "[", shift: "{", code: "BracketLeft", finger: "R_PINKY" },
    { main: "]", shift: "}", code: "BracketRight", finger: "R_PINKY" },
    { main: "\\", shift: "|", code: "Backslash", finger: "R_PINKY", width: "w-15" },
  ],
  [
    { main: "Caps", shift: "", code: "CapsLock", finger: "L_PINKY", width: "w-18", special: true },
    { main: "a", shift: "A", code: "KeyA", finger: "L_PINKY" },
    { main: "s", shift: "S", code: "KeyS", finger: "L_RING" },
    { main: "d", shift: "D", code: "KeyD", finger: "L_MIDDLE" },
    { main: "f", shift: "F", code: "KeyF", finger: "L_INDEX", bump: true },
    { main: "g", shift: "G", code: "KeyG", finger: "L_INDEX" },
    { main: "h", shift: "H", code: "KeyH", finger: "R_INDEX" },
    { main: "j", shift: "J", code: "KeyJ", finger: "R_INDEX", bump: true },
    { main: "k", shift: "K", code: "KeyK", finger: "R_MIDDLE" },
    { main: "l", shift: "L", code: "KeyL", finger: "R_RING" },
    { main: ";", shift: ":", code: "Semicolon", finger: "R_PINKY" },
    { main: "'", shift: "\"", code: "Quote", finger: "R_PINKY" },
    { main: "Enter", shift: "", code: "Enter", finger: "R_PINKY", width: "w-18", special: true },
  ],
  [
    { main: "Shift", shift: "", code: "ShiftLeft", finger: "L_PINKY", width: "w-22", special: true },
    { main: "z", shift: "Z", code: "KeyZ", finger: "L_PINKY" },
    { main: "x", shift: "X", code: "KeyX", finger: "L_RING" },
    { main: "c", shift: "C", code: "KeyC", finger: "L_MIDDLE" },
    { main: "v", shift: "V", code: "KeyV", finger: "L_INDEX" },
    { main: "b", shift: "B", code: "KeyB", finger: "L_INDEX" },
    { main: "n", shift: "N", code: "KeyN", finger: "R_INDEX" },
    { main: "m", shift: "M", code: "KeyM", finger: "R_INDEX" },
    { main: ",", shift: "<", code: "Comma", finger: "R_MIDDLE" },
    { main: ".", shift: ">", code: "Period", finger: "R_RING" },
    { main: "/", shift: "?", code: "Slash", finger: "R_PINKY" },
    { main: "Shift", shift: "", code: "ShiftRight", finger: "R_PINKY", width: "w-22", special: true },
  ],
  [
    { main: "Spacebar", shift: "", char: " ", code: "Space", finger: "THUMB", width: "w-space", special: true }
  ]
];

window.addEventListener("DOMContentLoaded", async () => {
  // Keep standalone desktop .exe alive while the window is open
  const sendHeartbeat = () => {
    fetch("/api/heartbeat", { method: "GET", cache: "no-store" }).catch(() => {});
  };
  sendHeartbeat();
  setInterval(sendHeartbeat, 3000);

  await fetchSavedUsersList();
  buildVirtualKeyboardDOM();
  window.addEventListener("keydown", handleGlobalKeyDown);
});

function escapeHtml(str) {
  return String(str || "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function toggleStudioTheme(isDark) {
  document.documentElement.setAttribute("data-theme", isDark ? "dark" : "sunlit");
  if (APP_STATE.user) {
    updatePreference("dark_theme", isDark);
  }
  if (typeof drawIdleGameBanner === "function" && typeof GAME_ENGINE !== "undefined" && !GAME_ENGINE.running) {
    drawIdleGameBanner();
  }
}

function toggleAutoInscriptMode(enabled) {
  APP_STATE.autoInscriptEnabled = enabled;
  const t1 = document.getElementById("toggleAutoInscript");
  const t2 = document.getElementById("modalAutoInscriptToggle");
  if (t1) t1.checked = enabled;
  if (t2) t2.checked = enabled;
  if (APP_STATE.user) {
    updatePreference("auto_inscript", enabled);
  }
}

// ============================================================================
// BUILD DUAL-LEGEND 3D MECHANICAL KEYBOARD (ENGLISH + 13 INDIAN INSCRIPT)
// ============================================================================
function buildVirtualKeyboardDOM() {
  const container = document.getElementById("virtualKeyboard");
  if (!container) return;
  container.innerHTML = "";

  const isIndian = APP_STATE.activeLanguage !== "en" && APP_STATE.inscriptKeymap;
  const km = APP_STATE.inscriptKeymap || {};

  // Update Left/Right Hand role captions for InScript
  const lRole = document.getElementById("leftHandRoleTag");
  const rRole = document.getElementById("rightHandRoleTag");
  if (lRole && rRole) {
    if (isIndian && APP_STATE.activeLanguage !== "ur") {
      lRole.textContent = "Matras & Vowels";
      rRole.textContent = "Consonants";
    } else {
      lRole.textContent = "";
      rRole.textContent = "";
    }
  }

  KEYBOARD_ROWS.forEach((row) => {
    const rowDiv = document.createElement("div");
    rowDiv.className = "kb-row";
    row.forEach((k) => {
      const keyEl = document.createElement("div");
      const classes = ["kb-key", `f-${k.finger}`];
      if (k.width) classes.push(k.width);
      if (k.bump) classes.push("home-bump");
      keyEl.className = classes.join(" ");
      keyEl.dataset.code = k.code;
      keyEl.dataset.qwerty = k.main.toUpperCase();

      if (k.special) {
        keyEl.dataset.main = k.char || k.main;
        keyEl.dataset.shift = "";
        keyEl.innerHTML = `<span class="main-lbl">${escapeHtml(k.main)}</span>`;
      } else if (isIndian && km[k.code]) {
        const mapped = km[k.code];
        keyEl.dataset.main = mapped.main || "";
        keyEl.dataset.shift = mapped.shift || "";
        keyEl.innerHTML = `
          <span class="qwerty-corner">${escapeHtml(k.main.toUpperCase())}</span>
          <span class="shift-lbl">${escapeHtml(mapped.shift || "")}</span>
          <span class="main-lbl">${escapeHtml(mapped.main || "")}</span>
        `;
      } else {
        keyEl.dataset.main = k.main;
        keyEl.dataset.shift = k.shift || "";
        if (k.shift && k.main.toLowerCase() !== k.shift.toLowerCase()) {
          keyEl.innerHTML = `<span class="shift-lbl">${escapeHtml(k.shift)}</span><span class="main-lbl">${escapeHtml(k.main)}</span>`;
        } else {
          keyEl.innerHTML = `<span class="main-lbl">${escapeHtml(k.main.toUpperCase())}</span>`;
        }
      }
      rowDiv.appendChild(keyEl);
    });
    container.appendChild(rowDiv);
  });
}

// ============================================================================
// WELCOME MODAL: NAME + 14-LANGUAGE SELECTOR GRID
// ============================================================================
async function fetchSavedUsersList() {
  try {
    const res = await fetch("/api/users");
    const json = await res.json();
    if (json.ok) {
      APP_STATE.languages = json.languages || [];
      renderWelcomeLanguageGrid();
      renderSavedUsersModalList(json.users || []);
    }
  } catch (e) {
    console.error("Failed to fetch users:", e);
  }
}

function renderWelcomeLanguageGrid() {
  const grid = document.getElementById("welcomeLangGrid");
  if (!grid) return;
  const langs = APP_STATE.languages || [];

  grid.innerHTML = langs
    .map((l) => {
      const isSel = l.code === APP_STATE.selectedWelcomeLang;
      const glyph = SCRIPT_GLYPHS[l.code] || l.native_name.slice(0, 1);
      return `
        <div class="wlang-tile ${isSel ? "selected" : ""}" onclick="selectWelcomeLanguage('${l.code}')">
          <div class="wlang-glyph">${escapeHtml(glyph)}</div>
          <div class="wlang-meta">
            <strong>${escapeHtml(l.native_name)}</strong>
            <span>${escapeHtml(l.name)}</span>
          </div>
        </div>
      `;
    })
    .join("");

  updateWelcomeInscriptPreview();
}

function selectWelcomeLanguage(langCode) {
  APP_STATE.selectedWelcomeLang = langCode;
  renderWelcomeLanguageGrid();
}

function updateWelcomeInscriptPreview() {
  const code = APP_STATE.selectedWelcomeLang;
  const langObj = (APP_STATE.languages || []).find((l) => l.code === code);
  const btnText = document.getElementById("btnLaunchText");
  if (btnText && langObj) {
    btnText.textContent = `Start My Typing Journey in ${langObj.native_name} (${langObj.name})`;
  }

  const previewBox = document.getElementById("welcomeInscriptPreview");
  if (!previewBox) return;

  if (code === "en" || !QUICK_WELCOME_GUIDES[code]) {
    previewBox.classList.add("hidden");
  } else {
    const g = QUICK_WELCOME_GUIDES[code];
    document.getElementById("wipNativeTitle").textContent = g.title;
    document.getElementById("wipNativeSteps").innerHTML = g.steps
      .map((s) => `<li>${escapeHtml(s)}</li>`)
      .join("");
    previewBox.classList.remove("hidden");
  }
}

function renderSavedUsersModalList(users) {
  const countEl = document.getElementById("savedUsersCount");
  const listEl = document.getElementById("savedUsersList");
  countEl.textContent = `${users.length} learner${users.length === 1 ? "" : "s"}`;

  if (users.length === 0) {
    listEl.innerHTML = `<div class="sub-copy small" style="padding:20px;text-align:center;">No saved learners on this computer yet. Enter your name and pick a script on the left!</div>`;
    return;
  }

  listEl.innerHTML = users
    .map((u) => {
      const initials = u.name.trim().slice(0, 2).toUpperCase();
      const completed = u.completed_lessons || 0;
      const wpm = Math.round(u.peak_wpm || 0);
      const langObj = (APP_STATE.languages || []).find((l) => l.code === u.current_language) || { native_name: "English" };
      return `
        <div class="saved-user-item" onclick="loginByName('${escapeHtml(u.name.replace(/'/g, "\\'"))}', '${escapeHtml(u.current_language || "en")}')">
          <div class="su-left">
            <div class="su-avatar" style="background:${u.avatar_color || "#e11d48"}">${escapeHtml(initials)}</div>
            <div class="su-info">
              <strong>${escapeHtml(u.name)} <span class="badge-pill" style="margin-left:4px;">${escapeHtml(langObj.native_name)}</span></strong>
              <span>${completed} steps done • Best ${wpm} WPM • 🔥 ${u.streak_days || 1}d</span>
            </div>
          </div>
          <button class="btn-del-user" title="Remove Profile" onclick="deleteUserProfile(event, ${u.id})">✕</button>
        </div>
      `;
    })
    .join("");
}

async function handleUserLogin(e) {
  e.preventDefault();
  const input = document.getElementById("userNameInput");
  const name = input.value.trim();
  if (!name) return;
  await loginByName(name, APP_STATE.selectedWelcomeLang);
}

async function loginByName(name, languageCode) {
  try {
    const res = await fetch("/api/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        name,
        language: languageCode || APP_STATE.selectedWelcomeLang || "en",
      }),
    });
    const json = await res.json();
    if (!json.ok) {
      alert(json.error || "Could not load user profile.");
      return;
    }

    APP_STATE.currentDrill = null;
    applyDashboardPayload(json.data);
    document.getElementById("userModal").classList.add("hidden");

    // If user selected an Indian language, show the friendly native InScript Guide Modal!
    if (APP_STATE.activeLanguage !== "en" && APP_STATE.inscriptSetupGuide) {
      openInscriptGuideModal();
    }
  } catch (err) {
    console.error("Login error:", err);
  }
}

async function switchActiveLanguage(newLangCode) {
  if (!APP_STATE.user || !newLangCode) return;
  stopActiveTimer();
  if (typeof stopCanvasGame === "function") stopCanvasGame();

  const res = await fetch("/api/settings", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      user_id: APP_STATE.user.id,
      current_language: newLangCode,
    }),
  });
  const json = await res.json();
  if (json.ok && json.data) {
    APP_STATE.currentDrill = null;
    applyDashboardPayload(json.data);
    if (newLangCode !== "en" && APP_STATE.inscriptSetupGuide) {
      openInscriptGuideModal();
    }
  }
}

function openInscriptGuideModal() {
  const guide = APP_STATE.inscriptSetupGuide;
  if (!guide) {
    alert("Standard English QWERTY layout is active. No special InScript setup needed!");
    return;
  }
  const langObj = (APP_STATE.languages || []).find((l) => l.code === APP_STATE.activeLanguage);
  document.getElementById("imGlyphBadge").textContent =
    SCRIPT_GLYPHS[APP_STATE.activeLanguage] || "अ";
  document.getElementById("imModalNativeTitle").textContent = guide.native_title;
  document.getElementById("imModalSubTitle").textContent = langObj
    ? `${langObj.native_name} (${langObj.name}) — Government of India Standard InScript Layout`
    : "InScript Keyboard Setup";

  document.getElementById("imNativeStepsList").innerHTML = (guide.native_steps || [])
    .map((s) => `<li>${escapeHtml(s)}</li>`)
    .join("");
  document.getElementById("imEnglishStepsList").innerHTML = (guide.en_steps || [])
    .map((s) => `<li>${escapeHtml(s)}</li>`)
    .join("");

  document.getElementById("inscriptGuideModal").classList.remove("hidden");
}

function closeInscriptGuideModal() {
  document.getElementById("inscriptGuideModal").classList.add("hidden");
  if (APP_STATE.activeTab === "practice") {
    focusTypingArena();
  }
}

async function deleteUserProfile(e, userId) {
  e.stopPropagation();
  if (!confirm("Remove this learner's saved progress from this computer?")) return;
  const res = await fetch("/api/delete_user", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ user_id: userId }),
  });
  const json = await res.json();
  if (json.ok) {
    renderSavedUsersModalList(json.users || []);
  }
}

function openUserSwitcher() {
  stopActiveTimer();
  if (typeof stopCanvasGame === "function") stopCanvasGame();
  fetchSavedUsersList();
  document.getElementById("userModal").classList.remove("hidden");
  document.getElementById("userNameInput").focus();
}

// ============================================================================
// APPLY DASHBOARD PAYLOAD & RENDER ALL STUDIO TABS
// ============================================================================
function applyDashboardPayload(data) {
  if (!data) return;
  APP_STATE.user = data.user;
  APP_STATE.activeLanguage = data.active_language || data.user.current_language || "en";
  APP_STATE.units = data.units || [];
  APP_STATE.allLessons = data.all_lessons || [];
  APP_STATE.progressMap = data.progress_map || {};
  APP_STATE.recentSessions = data.recent_sessions || [];
  APP_STATE.telemetry = data.telemetry || [];
  APP_STATE.weaknessAnalysis = data.weakness_analysis || {};
  APP_STATE.recommendedRemedial = data.recommended_remedial || null;
  APP_STATE.speedPassages = data.speed_passages || [];
  APP_STATE.fingerMap = data.finger_map || {};
  APP_STATE.fingerLabels = data.finger_labels || {};
  APP_STATE.languages = data.languages || [];
  APP_STATE.inscriptKeymap = data.inscript_keymap || null;
  APP_STATE.inscriptSetupGuide = data.inscript_setup_guide || null;
  APP_STATE.nativeVocab = data.native_vocab || null;

  // Preferences
  const settings = APP_STATE.user.settings || {};
  SoundFX.enabled = settings.sound !== false;
  document.getElementById("toggleSound").checked = SoundFX.enabled;
  const showKb = settings.show_keyboard !== false;
  document.getElementById("toggleKeyboard").checked = showKb;
  document.getElementById("visualKeyboardSection").classList.toggle("hidden", !showKb);

  APP_STATE.autoInscriptEnabled = settings.auto_inscript !== false;
  const autoToggle = document.getElementById("toggleAutoInscript");
  if (autoToggle) autoToggle.checked = APP_STATE.autoInscriptEnabled;

  const isDark = settings.dark_theme === true;
  const darkToggle = document.getElementById("toggleDarkTheme");
  if (darkToggle) darkToggle.checked = isDark;
  document.documentElement.setAttribute("data-theme", isDark ? "dark" : "sunlit");

  // Rebuild 3D Keyboard with active script legends!
  buildVirtualKeyboardDOM();

  // Populate Sidebar Script Dropdown
  const langSelect = document.getElementById("sidebarLangSelect");
  if (langSelect) {
    langSelect.innerHTML = APP_STATE.languages
      .map(
        (l) =>
          `<option value="${l.code}" ${l.code === APP_STATE.activeLanguage ? "selected" : ""}>${escapeHtml(l.native_name)} (${escapeHtml(l.name)})</option>`
      )
      .join("");
  }

  const isIndian = APP_STATE.activeLanguage !== "en";
  document.getElementById("btnCourseInscriptHelp")?.classList.toggle("hidden", !isIndian);
  document.getElementById("btnDeskInscriptGuide")?.classList.toggle("hidden", !isIndian);

  const activeLangObj = APP_STATE.languages.find((l) => l.code === APP_STATE.activeLanguage) || {
    name: "English",
    native_name: "English",
    layout: "QWERTY",
    greeting: "Welcome! Ready to flow?",
  };

  document.querySelector(".logo-emblem").textContent =
    SCRIPT_GLYPHS[APP_STATE.activeLanguage] || "अ";
  document.getElementById("courseLanguageBadge").textContent =
    `${activeLangObj.native_name} • ${activeLangObj.name.toUpperCase()} (${activeLangObj.layout})`;
  document.getElementById("kaviSidebarSpeech").textContent =
    activeLangObj.greeting || "Keep your shoulders relaxed and let your fingers flow!";

  // Update Sidebar User Card
  const u = APP_STATE.user;
  const avatarEl = document.getElementById("sidebarAvatar");
  avatarEl.textContent = u.name.trim().slice(0, 2).toUpperCase();
  avatarEl.style.background = u.avatar_color || "#e11d48";
  document.getElementById("sidebarUserName").textContent = u.name;
  document.getElementById("sidebarStreak").textContent = `🔥 ${u.streak_days || 1}d`;

  let completedCount = 0;
  let peakWpm = 0;
  let accSum = 0;
  let accCount = 0;
  Object.values(APP_STATE.progressMap).forEach((lp) => {
    if (lp.completed) completedCount++;
    if (lp.best_net_wpm > peakWpm) peakWpm = lp.best_net_wpm;
    if (lp.best_accuracy > 0) {
      accSum += lp.best_accuracy;
      accCount++;
    }
  });
  const totalLessons = APP_STATE.allLessons.length || 24;
  const avgAcc = accCount > 0 ? (accSum / accCount).toFixed(1) : "100.0";
  const mins = Math.max(1, Math.round((u.total_practice_sec || 0) / 60));

  document.getElementById("sidebarUserProgress").textContent = `${completedCount}/${totalLessons} steps • ${Math.round(peakWpm)} WPM`;
  document.getElementById("navCourseBadge").textContent = `${completedCount}/${totalLessons}`;

  document.getElementById("courseCompletedCount").textContent = `${completedCount} / ${totalLessons}`;
  document.getElementById("coursePeakWpm").textContent = `${Math.round(peakWpm)} WPM`;
  document.getElementById("courseAvgAcc").textContent = `${avgAcc}%`;
  document.getElementById("courseTotalTime").textContent = `${u.total_practice_sec ? mins : 0} mins`;

  const weakKeys = (APP_STATE.weaknessAnalysis.weak_keys || []).slice(0, 4);
  document.getElementById("courseWeakKeysQuick").textContent =
    weakKeys.length > 0 ? weakKeys.map((w) => w.key).join("  ") : "All clear! ✨";
  document.getElementById("navWeakBadge").textContent =
    weakKeys.length > 0 ? `${weakKeys.length} keys` : "Clear";

  renderCourseUnits();
  renderSmartTutorTab();
  renderSpeedTestPassages();
  renderStatsAndLanguagesTab();

  // Load current lesson into Typing Desk
  if (!APP_STATE.currentDrill) {
    const targetLessonId = u.current_lesson_id || `${APP_STATE.activeLanguage}_u1_l1`;
    const lessonObj =
      APP_STATE.allLessons.find((l) => l.id === targetLessonId) || APP_STATE.allLessons[0];
    if (lessonObj) {
      loadDrillIntoStudio(
        {
          id: lessonObj.id,
          title: lessonObj.title,
          mode: "lesson",
          text: lessonObj.text,
          tip: lessonObj.tip,
          next_lesson_id: getNextLessonId(lessonObj.id),
        },
        false
      );
    }
  }
}

function getNextLessonId(lessonId) {
  const idx = APP_STATE.allLessons.findIndex((l) => l.id === lessonId);
  if (idx >= 0 && idx + 1 < APP_STATE.allLessons.length) {
    return APP_STATE.allLessons[idx + 1].id;
  }
  return null;
}

function renderCourseUnits() {
  const container = document.getElementById("unitsContainer");
  if (!container) return;
  const currentLessonId = APP_STATE.user
    ? APP_STATE.user.current_lesson_id
    : `${APP_STATE.activeLanguage}_u1_l1`;

  container.innerHTML = APP_STATE.units
    .map((unit, uIdx) => {
      const themeClass = `unit-theme-${uIdx % 6}`;
      const lessonsHtml = unit.lessons
        .map((lesson) => {
          const prog = APP_STATE.progressMap[lesson.id];
          const isCompleted = prog && prog.completed;
          const isCurrent = lesson.id === currentLessonId;
          const stars = prog ? prog.stars : 0;
          const starStr = stars > 0 ? "⭐".repeat(stars) + "☆".repeat(3 - stars) : "☆☆☆";
          const statsStr = prog
            ? `Best: ${Math.round(prog.best_net_wpm)} WPM • ${prog.best_accuracy}%`
            : `Goal: ${lesson.target_wpm} WPM`;
          const keysPreview =
            lesson.new_keys && lesson.new_keys.length > 0
              ? `<span class="lc-keys-badge">Keys: ${escapeHtml(lesson.new_keys.slice(0, 5).join(" "))}</span>`
              : `<span class="lc-keys-badge">${escapeHtml(lesson.type.replace("_", " "))}</span>`;

          return `
            <div class="lesson-card ${isCompleted ? "completed" : ""} ${isCurrent ? "current-target" : ""}"
                 onclick="startLessonById('${lesson.id}')">
              <div class="lc-top">
                <div class="lc-title">${escapeHtml(lesson.title)}</div>
                <div class="lc-stars">${starStr}</div>
              </div>
              <div class="lc-bottom">
                ${keysPreview}
                <span>${statsStr}</span>
              </div>
            </div>
          `;
        })
        .join("");

      return `
        <div class="unit-card ${themeClass}">
          <div class="unit-banner">
            <div>
              <h3>${escapeHtml(unit.title)}</h3>
              <p>${escapeHtml(unit.subtitle)}</p>
            </div>
          </div>
          <div class="lessons-grid">${lessonsHtml}</div>
        </div>
      `;
    })
    .join("");
}

// ============================================================================
// NAVIGATION & PREFERENCES
// ============================================================================
function setSidebarCollapsed(collapsed) {
  const frame = document.getElementById("appFrame");
  const floatBtn = document.getElementById("floatingSidebarToggle");
  if (!frame) return;
  frame.classList.toggle("sidebar-collapsed", collapsed);
  if (floatBtn) {
    // On Practice tab, the integrated ☰ button in the desk header handles toggling cleanly
    const showFloat = collapsed && APP_STATE.activeTab !== "practice";
    floatBtn.classList.toggle("hidden", !showFloat);
  }
  if (APP_STATE.activeTab === "games" && typeof syncCanvasResolution === "function") {
    setTimeout(() => {
      syncCanvasResolution();
      if (!GAME_ENGINE.running) drawIdleGameBanner();
    }, 260);
  }
}

function toggleSidebarPanel() {
  const frame = document.getElementById("appFrame");
  if (!frame) return;
  const isCurrentlyCollapsed = frame.classList.contains("sidebar-collapsed");
  setSidebarCollapsed(!isCurrentlyCollapsed);
}

function switchTab(tabName) {
  APP_STATE.activeTab = tabName;
  document.querySelectorAll(".cnav-btn").forEach((btn) => {
    btn.classList.toggle("active", btn.dataset.tab === tabName);
  });
  document.querySelectorAll(".tab-pane").forEach((pane) => {
    pane.classList.toggle("active", pane.id === `tab-${tabName}`);
  });

  // Update floating sidebar button visibility for the active tab
  const frame = document.getElementById("appFrame");
  const floatBtn = document.getElementById("floatingSidebarToggle");
  if (frame && floatBtn) {
    const collapsed = frame.classList.contains("sidebar-collapsed");
    floatBtn.classList.toggle("hidden", !(collapsed && tabName !== "practice"));
  }

  if (tabName !== "games" && typeof stopCanvasGame === "function") {
    stopCanvasGame();
  }
  if (tabName === "games" && typeof syncCanvasResolution === "function") {
    setTimeout(() => {
      syncCanvasResolution();
      if (!GAME_ENGINE.running) drawIdleGameBanner();
    }, 30);
  }
  if (tabName === "practice") {
    setTimeout(() => focusTypingArena(), 60);
  }
}

async function updatePreference(key, val) {
  if (key === "sound") {
    SoundFX.enabled = val;
  } else if (key === "show_keyboard") {
    document.getElementById("visualKeyboardSection").classList.toggle("hidden", !val);
  }
  if (!APP_STATE.user) return;
  await fetch("/api/settings", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      user_id: APP_STATE.user.id,
      settings: { [key]: val },
    }),
  });
}

// ============================================================================
// ARTISAN TYPING DESK (PRACTICE STUDIO ENGINE + AUTO-INSCRIPT MAPPER)
// ============================================================================
function startLessonById(lessonId) {
  const lessonObj = APP_STATE.allLessons.find((l) => l.id === lessonId);
  if (!lessonObj) return;
  loadDrillIntoStudio(
    {
      id: lessonObj.id,
      title: lessonObj.title,
      mode: "lesson",
      text: lessonObj.text,
      tip: lessonObj.tip,
      next_lesson_id: getNextLessonId(lessonObj.id),
    },
    true
  );
}

function resumeCurrentLesson() {
  const curId =
    (APP_STATE.user && APP_STATE.user.current_lesson_id) ||
    `${APP_STATE.activeLanguage}_u1_l1`;
  startLessonById(curId);
}

function loadDrillIntoStudio(drillConfig, switchToPracticeTab = true) {
  stopActiveTimer();
  APP_STATE.currentDrill = drillConfig;
  APP_STATE.charIndex = 0;
  APP_STATE.streakCombo = 0;
  APP_STATE.errorIndices = new Set();
  APP_STATE.totalTypedChars = 0;
  APP_STATE.totalErrorChars = 0;
  APP_STATE.startTimeMs = null;
  APP_STATE.lastKeystrokeMs = null;
  APP_STATE.isCompleted = false;
  APP_STATE.keyStats = {};

  document.getElementById("studioModeBadge").textContent = (drillConfig.mode || "lesson").toUpperCase();
  document.getElementById("studioLessonTitle").textContent = drillConfig.title;
  document.getElementById("studioCoachTip").textContent =
    drillConfig.tip || "Keep your shoulders relaxed and eyes on the parchment scroll.";

  document.getElementById("liveNetWpm").textContent = "0";
  document.getElementById("liveAccuracy").textContent = "100%";
  document.getElementById("liveStreakCombo").textContent = "0🔥";
  document.getElementById("liveErrors").textContent = "0";
  document.getElementById("liveTimer").textContent = drillConfig.timeLimitSec
    ? formatSeconds(drillConfig.timeLimitSec)
    : "0:00";
  document.getElementById("drillProgressBar").style.width = "0%";

  renderTypingTextDOM();
  updateNextKeyAndFingerGuide();

  if (switchToPracticeTab) {
    switchTab("practice");
  }
}

function restartCurrentDrill() {
  if (!APP_STATE.currentDrill) return;
  document.getElementById("resultModal").classList.add("hidden");
  loadDrillIntoStudio(APP_STATE.currentDrill, true);
}

function focusTypingArena() {
  const box = document.getElementById("typingArenaBox");
  if (box) box.focus();
  document.getElementById("arenaFocusOverlay").classList.add("hidden");
}

// Halant / Virama across all 12 Indian Brahmic scripts
const INDIC_HALANT_RE = /[\u094D\u09CD\u0A4D\u0ACD\u0B4D\u0BCD\u0C4D\u0CCD\u0D4D]/;
// Combining marks (matras, anusvara, visarga, nukta, chandrabindu, Urdu diacritics)
const COMBINING_MARK_RE = /\p{M}/u;

/**
 * Segments text into unbroken Indic Akshara (orthographic syllable) clusters so
 * consonants + halants + conjuncts + matras NEVER split across <span> boundaries
 * and NEVER display broken dotted circles (◌).
 */
function segmentIntoAksharaClusters(text) {
  const clusters = [];
  if (!text) return clusters;

  if (APP_STATE.activeLanguage === "en") {
    for (let i = 0; i < text.length; i++) {
      clusters.push({ start: i, end: i + 1, text: text[i] });
    }
    return clusters;
  }

  let i = 0;
  while (i < text.length) {
    const start = i;
    i++;
    // Absorb any combining marks (matras, nukta, halant, anusvara, visarga)
    // AND if a halant/virama appears, also absorb the joined following consonant + its marks!
    while (i < text.length) {
      const prevCh = text[i - 1];
      const curCh = text[i];
      if (curCh === "\u200C") {
        // ZWNJ attaches to preceding halant and explicitly terminates the cluster!
        i++;
        break;
      } else if (curCh === "\u200D") {
        // ZWJ joins into current cluster
        i++;
      } else if (INDIC_HALANT_RE.test(prevCh) && curCh !== " " && !/[.,;:!?]/.test(curCh)) {
        // Conjunct consonant after halant (e.g. మ + ్ + మ -> మ్మ)
        i++;
      } else if (COMBINING_MARK_RE.test(curCh)) {
        // Vowel matra / anusvara / visarga / halant attached to current syllable
        i++;
      } else {
        break;
      }
    }
    clusters.push({ start, end: i, text: text.slice(start, i) });
  }
  return clusters;
}

function updateTypingTextHighlights() {
  const clusters = APP_STATE.clusters || [];
  let activeSpan = null;

  for (let idx = 0; idx < clusters.length; idx++) {
    const c = clusters[idx];
    const span = document.getElementById(`tcluster-${idx}`);
    if (!span) continue;

    if (c.end <= APP_STATE.charIndex) {
      // Completed cluster — check if any keystroke inside it had a slip
      let hadError = false;
      for (let pos = c.start; pos < c.end; pos++) {
        if (APP_STATE.errorIndices.has(pos)) {
          hadError = true;
          break;
        }
      }
      span.className = hadError ? "t-char wrong" : "t-char correct";
    } else if (c.start <= APP_STATE.charIndex && APP_STATE.charIndex < c.end) {
      span.className = "t-char current";
      activeSpan = span;
    } else {
      span.className = "t-char";
    }
  }

  if (activeSpan) {
    const box = document.getElementById("typingArenaBox");
    if (box && activeSpan.offsetTop - box.scrollTop > 100) {
      box.scrollTop = activeSpan.offsetTop - 48;
    }
  }
}

function renderTypingTextDOM() {
  const display = document.getElementById("typingTextDisplay");
  if (!display || !APP_STATE.currentDrill) return;
  const text = APP_STATE.currentDrill.text;
  APP_STATE.clusters = segmentIntoAksharaClusters(text);

  const html = APP_STATE.clusters.map((c, idx) => {
    const cls = idx === 0 ? "t-char current" : "t-char";
    const visible = c.text === " " ? " " : escapeHtml(c.text);
    return `<span class="${cls}" id="tcluster-${idx}">${visible}</span>`;
  });

  display.innerHTML = html.join("");
  const box = document.getElementById("typingArenaBox");
  if (box) box.scrollTop = 0;
}

/**
 * Resolves the character typed by the user, supporting BOTH:
 * 1. Native OS InScript Keyboard (where e.key is already the Indian character)
 * 2. Built-in Smart Auto-InScript Mapper (translates physical e.code + e.shiftKey when OS is in English)
 */
function resolveEffectiveTypedChar(e, expectedChar) {
  // Windows InScript ZWNJ (Zero-Width Non-Joiner):
  // Supports double-tap 'd' (KeyD right after halant) OR Ctrl+Shift+2 OR native \u200C
  if (expectedChar === "\u200C") {
    if (
      e.key === "\u200C" ||
      (e.code === "KeyD" && !e.shiftKey) ||
      (e.ctrlKey && e.shiftKey && e.code === "Digit2")
    ) {
      return "\u200C";
    }
  }
  // Windows InScript ZWJ (Zero-Width Joiner): Ctrl+Shift+1 or native \u200D
  if (expectedChar === "\u200D") {
    if (e.key === "\u200D" || (e.ctrlKey && e.shiftKey && e.code === "Digit1")) {
      return "\u200D";
    }
  }

  if (e.key === expectedChar) {
    return e.key;
  }
  if (
    APP_STATE.activeLanguage !== "en" &&
    APP_STATE.autoInscriptEnabled &&
    APP_STATE.inscriptKeymap &&
    APP_STATE.inscriptKeymap[e.code]
  ) {
    const mapping = APP_STATE.inscriptKeymap[e.code];
    const mappedChar = e.shiftKey ? mapping.shift : mapping.main;
    if (mappedChar) {
      return mappedChar;
    }
  }
  return e.key;
}

function spawnSparklePopup(text) {
  const layer = document.getElementById("floatingSparkleLayer");
  if (!layer) return;
  const sp = document.createElement("div");
  sp.className = "floating-spark";
  sp.style.left = `${30 + Math.random() * 60}%`;
  sp.style.top = "20px";
  sp.textContent = text;
  layer.appendChild(sp);
  setTimeout(() => sp.remove(), 750);
}

function handleGlobalKeyDown(e) {
  if (APP_STATE.activeTab !== "practice") return;
  if (!document.getElementById("userModal").classList.contains("hidden")) return;
  if (!document.getElementById("inscriptGuideModal").classList.contains("hidden")) return;
  if (!document.getElementById("resultModal").classList.contains("hidden")) return;
  if (!APP_STATE.currentDrill || APP_STATE.isCompleted) return;

  if (e.key === "Escape") {
    e.preventDefault();
    restartCurrentDrill();
    return;
  }

  if (["Shift", "Control", "Alt", "Meta", "CapsLock", "Tab"].includes(e.key)) {
    return;
  }

  const text = APP_STATE.currentDrill.text;

  if (e.key === "Backspace") {
    e.preventDefault();
    if (APP_STATE.charIndex > 0) {
      APP_STATE.charIndex--;
      updateTypingTextHighlights();
      updateNextKeyAndFingerGuide();
      updateLiveMetricsUI();
    }
    return;
  }

  if (e.key.length !== 1) return;
  e.preventDefault();

  const now = performance.now();
  if (!APP_STATE.startTimeMs) {
    APP_STATE.startTimeMs = now;
    APP_STATE.lastKeystrokeMs = now;
    startLiveSessionTimer();
    // Auto-collapse sidebar into Focus Mode when typing begins so both hands have full room!
    setSidebarCollapsed(true);
  }

  const latencyMs = Math.max(20, Math.min(2000, now - (APP_STATE.lastKeystrokeMs || now)));
  APP_STATE.lastKeystrokeMs = now;

  const expectedChar = text[APP_STATE.charIndex];
  const typedChar = resolveEffectiveTypedChar(e, expectedChar);

  if (!APP_STATE.keyStats[expectedChar]) {
    APP_STATE.keyStats[expectedChar] = {
      hits: 0,
      misses: 0,
      latencies: [],
      confused_with: {},
    };
  }

  APP_STATE.totalTypedChars++;

  if (typedChar === expectedChar) {
    SoundFX.playClick();
    APP_STATE.streakCombo++;
    APP_STATE.keyStats[expectedChar].hits++;
    APP_STATE.keyStats[expectedChar].latencies.push(Math.round(latencyMs));
    if (APP_STATE.streakCombo > 0 && APP_STATE.streakCombo % 12 === 0) {
      spawnSparklePopup(`✨ ${APP_STATE.streakCombo} Streak!`);
      document.getElementById("deskOwlEmoji").textContent = "🤩";
    }
  } else {
    SoundFX.playError();
    APP_STATE.streakCombo = 0;
    APP_STATE.totalErrorChars++;
    APP_STATE.errorIndices.add(APP_STATE.charIndex);
    APP_STATE.keyStats[expectedChar].misses++;
    const conf = APP_STATE.keyStats[expectedChar].confused_with;
    conf[typedChar] = (conf[typedChar] || 0) + 1;

    document.getElementById("deskOwlEmoji").textContent = "🦉";
    flashWrongKeyOnKeyboard(typedChar, e.code);
  }

  APP_STATE.charIndex++;
  updateTypingTextHighlights();

  const pct = Math.min(100, (APP_STATE.charIndex / text.length) * 100);
  document.getElementById("drillProgressBar").style.width = `${pct}%`;

  updateLiveMetricsUI();

  if (APP_STATE.charIndex >= text.length) {
    completeDrillSession();
  } else {
    updateNextKeyAndFingerGuide();
  }
}

function flashWrongKeyOnKeyboard(typedChar, keyCode) {
  document.querySelectorAll(".kb-key").forEach((el) => {
    if (
      el.dataset.code === keyCode ||
      el.dataset.main === typedChar ||
      el.dataset.shift === typedChar
    ) {
      el.classList.add("pressed-wrong");
      setTimeout(() => el.classList.remove("pressed-wrong"), 220);
    }
  });
}

function updateNextKeyAndFingerGuide() {
  if (!APP_STATE.currentDrill) return;
  const text = APP_STATE.currentDrill.text;
  const nextChar = text[APP_STATE.charIndex] || "";

  const badge = document.getElementById("nextKeyBadge");
  const physHint = document.getElementById("nextPhysicalKeyHint");
  const fingerBadge = document.getElementById("nextFingerBadge");

  if (nextChar === "\u200C") {
    badge.textContent = "ZWNJ";
  } else if (nextChar === "\u200D") {
    badge.textContent = "ZWJ";
  } else {
    badge.textContent = nextChar === " " ? "Space" : nextChar;
  }

  const fingerCode =
    nextChar === "\u200C" || nextChar === "\u200D"
      ? "L_MIDDLE"
      : APP_STATE.fingerMap[nextChar] || "R_INDEX";
  const fingerName = APP_STATE.fingerLabels[fingerCode] || fingerCode;
  fingerBadge.textContent = fingerName;

  document.querySelectorAll(".kb-key").forEach((el) => el.classList.remove("target-key"));
  document.querySelectorAll(".finger-node").forEach((el) => el.classList.remove("active-finger"));

  let requiresShift = false;
  let matchedQwertyKey = "";

  document.querySelectorAll(".kb-key").forEach((el) => {
    if (nextChar === " " && el.dataset.code === "Space") {
      el.classList.add("target-key");
      matchedQwertyKey = "Space";
    } else if (nextChar === "\u200C" && el.dataset.code === "KeyD") {
      el.classList.add("target-key");
      matchedQwertyKey = "D again (d+d Break)";
    } else if (el.dataset.main === nextChar && nextChar !== "") {
      el.classList.add("target-key");
      matchedQwertyKey = el.dataset.qwerty || "";
    } else if (el.dataset.shift === nextChar && nextChar !== "") {
      el.classList.add("target-key");
      requiresShift = true;
      matchedQwertyKey = `Shift + ${el.dataset.qwerty || ""}`;
    }
  });

  if (physHint) {
    if (APP_STATE.activeLanguage !== "en" && matchedQwertyKey && nextChar !== " ") {
      const activeCluster = (APP_STATE.clusters || []).find(
        (c) => c.start <= APP_STATE.charIndex && APP_STATE.charIndex < c.end
      );
      if (activeCluster && activeCluster.end - activeCluster.start > 1) {
        const stepNum = APP_STATE.charIndex - activeCluster.start + 1;
        const totalSteps = activeCluster.end - activeCluster.start;
        physHint.textContent = `${activeCluster.text} (${stepNum}/${totalSteps}) • [Key: ${matchedQwertyKey}]`;
      } else {
        physHint.textContent = `[Key: ${matchedQwertyKey}]`;
      }
    } else {
      physHint.textContent = "";
    }
  }

  if (requiresShift) {
    const isLeftHandKey = fingerCode.startsWith("L_");
    const shiftCode = isLeftHandKey ? "ShiftRight" : "ShiftLeft";
    const shiftFinger = isLeftHandKey ? "R_PINKY" : "L_PINKY";
    const shiftKeyEl = document.querySelector(`.kb-key[data-code="${shiftCode}"]`);
    if (shiftKeyEl) shiftKeyEl.classList.add("target-key");
    const shiftFingerEl = document.getElementById(`finger-${shiftFinger}`);
    if (shiftFingerEl) shiftFingerEl.classList.add("active-finger");
  }

  if (fingerCode === "THUMB") {
    document.getElementById("finger-L_THUMB")?.classList.add("active-finger");
    document.getElementById("finger-R_THUMB")?.classList.add("active-finger");
  } else {
    document.getElementById(`finger-${fingerCode}`)?.classList.add("active-finger");
  }
}

function startLiveSessionTimer() {
  stopActiveTimer();
  APP_STATE.timerInterval = setInterval(() => {
    if (!APP_STATE.startTimeMs || APP_STATE.isCompleted) return;
    const elapsedSec = (performance.now() - APP_STATE.startTimeMs) / 1000;
    const timeLimit = APP_STATE.currentDrill.timeLimitSec;

    if (timeLimit) {
      const remaining = Math.max(0, Math.ceil(timeLimit - elapsedSec));
      document.getElementById("liveTimer").textContent = formatSeconds(remaining);
      if (remaining <= 0) {
        completeDrillSession();
        return;
      }
    } else {
      document.getElementById("liveTimer").textContent = formatSeconds(Math.floor(elapsedSec));
    }
    updateLiveMetricsUI();
  }, 250);
}

function stopActiveTimer() {
  if (APP_STATE.timerInterval) {
    clearInterval(APP_STATE.timerInterval);
    APP_STATE.timerInterval = null;
  }
}

function formatSeconds(sec) {
  const m = Math.floor(sec / 60);
  const s = sec % 60;
  return `${m}:${s < 10 ? "0" : ""}${s}`;
}

function computeSessionMetrics() {
  const elapsedSec = APP_STATE.startTimeMs
    ? Math.max(1, (performance.now() - APP_STATE.startTimeMs) / 1000)
    : 1;
  const minutes = elapsedSec / 60;
  const totalTyped = APP_STATE.totalTypedChars;
  const errors = APP_STATE.totalErrorChars;
  const grossWpm = (totalTyped / 5) / minutes;
  const netChars = Math.max(0, totalTyped - errors);
  const netWpm = (netChars / 5) / minutes;
  const accuracy = totalTyped > 0 ? ((totalTyped - errors) / totalTyped) * 100 : 100;

  return {
    elapsedSec,
    grossWpm: Math.max(0, grossWpm),
    netWpm: Math.max(0, netWpm),
    accuracy: Math.max(0, Math.min(100, accuracy)),
  };
}

function updateLiveMetricsUI() {
  const m = computeSessionMetrics();
  document.getElementById("liveNetWpm").textContent = Math.round(m.netWpm);
  document.getElementById("liveAccuracy").textContent = `${m.accuracy.toFixed(1)}%`;
  document.getElementById("liveStreakCombo").textContent = `${APP_STATE.streakCombo}🔥`;
  document.getElementById("liveErrors").textContent = APP_STATE.totalErrorChars;
}

async function completeDrillSession() {
  if (APP_STATE.isCompleted) return;
  APP_STATE.isCompleted = true;
  stopActiveTimer();
  SoundFX.playFanfare();

  const m = computeSessionMetrics();
  const drill = APP_STATE.currentDrill;

  try {
    const res = await fetch("/api/record_session", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        user_id: APP_STATE.user.id,
        language: APP_STATE.activeLanguage,
        lesson_id: drill.id,
        lesson_title: drill.title,
        mode: drill.mode || "lesson",
        gross_wpm: m.grossWpm,
        net_wpm: m.netWpm,
        accuracy: m.accuracy,
        duration_sec: m.elapsedSec,
        total_chars: APP_STATE.totalTypedChars,
        error_chars: APP_STATE.totalErrorChars,
        score: Math.round(m.netWpm * m.accuracy),
        key_stats: APP_STATE.keyStats,
      }),
    });
    const json = await res.json();
    if (json.ok) {
      applyDashboardPayload(json.data);
      showResultModal(m, json.session_result);
    }
  } catch (err) {
    console.error("Failed to record session:", err);
  }
}

function showResultModal(metrics, sessionResult) {
  const stars = sessionResult ? sessionResult.stars : 2;
  document.getElementById("resultStars").textContent =
    stars > 0 ? "⭐".repeat(stars) + "☆".repeat(3 - stars) : "🌱 Keep Flowing!";
  document.getElementById("resultTitle").textContent =
    stars > 0 ? "Fantastic Flow!" : "Almost There — Aim for 86%+ Precision";
  document.getElementById("resultSubtitle").textContent = APP_STATE.currentDrill.title;

  document.getElementById("resNetWpm").textContent = `${Math.round(metrics.netWpm)} WPM`;
  document.getElementById("resGrossWpm").textContent = `Raw: ${Math.round(metrics.grossWpm)} WPM`;
  document.getElementById("resAccuracy").textContent = `${metrics.accuracy.toFixed(1)}%`;
  document.getElementById("resErrors").textContent = `${APP_STATE.totalErrorChars} slips`;
  document.getElementById("resDuration").textContent = `${Math.round(metrics.elapsedSec)}s`;
  document.getElementById("resKeystrokes").textContent = `${APP_STATE.totalTypedChars} keys`;

  const missedKeys = Object.entries(APP_STATE.keyStats)
    .filter(([k, st]) => st.misses > 0 && k !== " ")
    .sort((a, b) => b[1].misses - a[1].misses);

  const diagTextEl = document.getElementById("resDiagnosticText");
  const chipsEl = document.getElementById("resWeakKeysChips");

  if (missedKeys.length > 0) {
    diagTextEl.textContent =
      "Coach Kavi spotted slight hesitation on these characters. Click 'Practice Weak Keys' to smooth them out:";
    chipsEl.innerHTML = missedKeys
      .slice(0, 6)
      .map(([k, st]) => `<span class="weak-chip">'${escapeHtml(k)}' (${st.misses} slip${st.misses > 1 ? "s" : ""})</span>`)
      .join("");
  } else {
    diagTextEl.textContent =
      "Spotless rhythm! Every single character in this step landed cleanly.";
    chipsEl.innerHTML = "";
  }

  document.getElementById("resultModal").classList.remove("hidden");
}

function closeResultModalAndRetry() {
  document.getElementById("resultModal").classList.add("hidden");
  restartCurrentDrill();
}

function startSmartRemedialFromModal() {
  document.getElementById("resultModal").classList.add("hidden");
  launchRecommendedRemedial();
}

function startNextLessonFromModal() {
  document.getElementById("resultModal").classList.add("hidden");
  const nextId =
    (APP_STATE.currentDrill && APP_STATE.currentDrill.next_lesson_id) ||
    (APP_STATE.user && APP_STATE.user.current_lesson_id) ||
    `${APP_STATE.activeLanguage}_u1_l1`;
  startLessonById(nextId);
}

// ============================================================================
// SMART MISTAKE COACH & DYNAMIC REMEDIAL GENERATOR
// ============================================================================
function renderSmartTutorTab() {
  const analysis = APP_STATE.weaknessAnalysis || {};
  document.getElementById("tutorCoachBanner").textContent =
    analysis.coach_summary || "Complete a lesson so Coach Kavi can map your finger reflexes!";

  const weakWrap = document.getElementById("weakKeysTableWrap");
  const weakKeys = analysis.weak_keys || [];
  if (weakKeys.length === 0) {
    weakWrap.innerHTML = `<div class="sub-copy small">No weak keys spotted yet in this script! Practice a lesson first.</div>`;
  } else {
    weakWrap.innerHTML = weakKeys
      .map(
        (w) => `
        <div class="weak-key-row">
          <div>
            <span class="wk-badge">${escapeHtml(w.key)}</span>
            <strong style="margin-left:10px;">${escapeHtml(w.finger_name)}</strong>
          </div>
          <div class="sub-copy small">
            Slip Rate: <strong style="color:var(--coral)">${w.error_rate}%</strong> (${w.misses}/${w.total}) • Pace: <strong>${w.avg_latency_ms}ms</strong>
          </div>
        </div>
      `
      )
      .join("");
  }

  const confWrap = document.getElementById("confusionPairsList");
  const pairs = analysis.confusion_pairs || [];
  if (pairs.length === 0) {
    confWrap.innerHTML = `<div class="sub-copy small">No key mix-ups recorded yet.</div>`;
  } else {
    confWrap.innerHTML = pairs
      .map(
        (p) => `
        <div class="weak-key-row" style="border-left-color:var(--coral);">
          <div>
            Aimed for <span class="wk-badge">${escapeHtml(p.expected)}</span> &rarr; Pressed <span class="wk-badge" style="color:var(--coral)">${escapeHtml(p.typed)}</span>
          </div>
          <div class="sub-copy small"><strong>${p.count}x</strong> (${escapeHtml(p.finger)})</div>
        </div>
      `
      )
      .join("");
  }

  const fingerWrap = document.getElementById("fingerBreakdownList");
  const fStats = Object.values(analysis.finger_stats || {});
  if (fStats.length === 0) {
    fingerWrap.innerHTML = `<div class="sub-copy small">Finger breakdown will appear after your first drill.</div>`;
  } else {
    fingerWrap.innerHTML = fStats
      .map(
        (f) => `
        <div class="weak-key-row" style="border-left-color:var(--peacock);">
          <strong>${escapeHtml(f.finger_name)}</strong>
          <div class="sub-copy small">Precision: <strong>${f.accuracy}%</strong> • Pace: <strong>${f.avg_latency_ms}ms</strong></div>
        </div>
      `
      )
      .join("");
  }
}

async function launchRecommendedRemedial() {
  if (!APP_STATE.user) return;
  const res = await fetch("/api/remedial_drill", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      user_id: APP_STATE.user.id,
      language: APP_STATE.activeLanguage,
    }),
  });
  const json = await res.json();
  if (json.ok && json.drill) {
    loadDrillIntoStudio(
      {
        id: json.drill.id,
        title: json.drill.title,
        mode: "remedial",
        text: json.drill.text,
        tip: json.drill.tip,
      },
      true
    );
  }
}

async function launchCustomKeyDrill() {
  const raw = document.getElementById("customFocusKeysInput").value.trim();
  if (!raw) return;
  const keys = raw.split(/[\s,]+/).filter(Boolean);
  const res = await fetch("/api/remedial_drill", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      user_id: APP_STATE.user.id,
      language: APP_STATE.activeLanguage,
      focus_keys: keys,
    }),
  });
  const json = await res.json();
  if (json.ok && json.drill) {
    loadDrillIntoStudio(
      {
        id: "remedial_custom_user",
        title: json.drill.title,
        mode: "remedial",
        text: json.drill.text,
        tip: json.drill.tip,
      },
      true
    );
  }
}

// ============================================================================
// TIMED SPEED ARENA & 14-LANGUAGE LIBRARY
// ============================================================================
function setSpeedTestDuration(seconds, btnEl) {
  APP_STATE.speedTestDurationSec = seconds;
  document.querySelectorAll("#stDurationGroup .dur-pill").forEach((b) => b.classList.remove("active"));
  if (btnEl) btnEl.classList.add("active");
}

function renderSpeedTestPassages() {
  const container = document.getElementById("speedPassagesList");
  if (!container) return;
  if (
    APP_STATE.speedPassages.length > 0 &&
    !APP_STATE.speedPassages.some((p) => p.id === APP_STATE.selectedPassageId)
  ) {
    APP_STATE.selectedPassageId = APP_STATE.speedPassages[0].id;
  }

  container.innerHTML = APP_STATE.speedPassages
    .map(
      (p) => `
      <div class="passage-card ${p.id === APP_STATE.selectedPassageId ? "active" : ""}"
           onclick="selectSpeedPassage('${p.id}')">
        <h4>${escapeHtml(p.title)} <span class="badge-pill">${escapeHtml(p.difficulty)}</span></h4>
        <p class="sub-copy small" style="margin-top:6px;">${escapeHtml(p.text.slice(0, 125))}...</p>
      </div>
    `
    )
    .join("");
}

function selectSpeedPassage(pid) {
  APP_STATE.selectedPassageId = pid;
  renderSpeedTestPassages();
}

function startTimedSpeedTest() {
  const passage =
    APP_STATE.speedPassages.find((p) => p.id === APP_STATE.selectedPassageId) ||
    APP_STATE.speedPassages[0];
  if (!passage) return;
  const mins = Math.round(APP_STATE.speedTestDurationSec / 60);
  const fullText =
    APP_STATE.speedTestDurationSec >= 180 ? `${passage.text} ${passage.text}` : passage.text;

  loadDrillIntoStudio(
    {
      id: passage.id,
      title: `${mins}-Minute Speed Benchmark: ${passage.title}`,
      mode: "speed_test",
      text: fullText,
      tip: `Relax your shoulders and type smoothly for ${mins} minute${mins > 1 ? "s" : ""}.`,
      timeLimitSec: APP_STATE.speedTestDurationSec,
    },
    true
  );
}

function renderStatsAndLanguagesTab() {
  const sWrap = document.getElementById("recentSessionsTable");
  if (sWrap) {
    if (!APP_STATE.recentSessions || APP_STATE.recentSessions.length === 0) {
      sWrap.innerHTML = `<div class="sub-copy small">No practice sessions logged in this script yet.</div>`;
    } else {
      sWrap.innerHTML = APP_STATE.recentSessions
        .map(
          (s) => `
          <div class="session-row">
            <div>
              <strong>${escapeHtml(s.lesson_title)}</strong>
              <div class="sub-copy small">${escapeHtml(s.mode.toUpperCase())} • ${escapeHtml(s.created_at.replace("T", " "))}</div>
            </div>
            <div style="text-align:right;">
              <strong style="color:var(--peacock)">${s.net_wpm} WPM</strong>
              <div class="sub-copy small">${s.accuracy}% • ${Math.round(s.duration_sec)}s</div>
            </div>
          </div>
        `
        )
        .join("");
    }
  }

  const lWrap = document.getElementById("languagesGrid");
  if (lWrap) {
    lWrap.innerHTML = (APP_STATE.languages || [])
      .map((lang) => {
        const isCurrent = lang.code === APP_STATE.activeLanguage;
        const glyph = SCRIPT_GLYPHS[lang.code] || lang.native_name.slice(0, 1);
        return `
        <div class="lang-card ${isCurrent ? "active-lang" : ""}" onclick="switchActiveLanguage('${lang.code}')">
          <div style="display:flex;align-items:center;gap:10px;">
            <div class="wlang-glyph">${escapeHtml(glyph)}</div>
            <div>
              <strong>${escapeHtml(lang.native_name)} (${escapeHtml(lang.name)})</strong>
              <div class="sub-copy small">${escapeHtml(lang.layout)}</div>
            </div>
          </div>
          <span class="badge-pill" style="${isCurrent ? "background:var(--peacock);color:#fff;border-color:transparent;" : ""}">
            ${isCurrent ? "✓ Active" : "Switch"}
          </span>
        </div>
      `;
      })
      .join("");
  }
  renderRecentCustomPassages();
}

// ============================================================================
// TAB 7: CUSTOM TEXT PRACTICE STUDIO (PASTE ANY PARAGRAPH — UP TO 1,500 WORDS!)
// ============================================================================
const MAX_CUSTOM_WORDS = 1500;
const CUSTOM_STORAGE_KEY = "aksharaflow_recent_custom_passages";

function cleanCustomPracticeText(raw) {
  let s = String(raw || "")
    .replace(/[\u201C\u201D]/g, '"')
    .replace(/[\u2018\u2019]/g, "'")
    .replace(/[\u2013\u2014]/g, "-")
    .replace(/\u00A0/g, " ")
    .replace(/[\r\n\t]+/g, " ")
    .replace(/\s{2,}/g, " ")
    .trim();

  if (!s) return { text: "", words: 0, trimmed: false };
  const wordArr = s.split(" ").filter(Boolean);
  let trimmed = false;
  if (wordArr.length > MAX_CUSTOM_WORDS) {
    s = wordArr.slice(0, MAX_CUSTOM_WORDS).join(" ");
    trimmed = true;
  }
  return { text: s, words: Math.min(wordArr.length, MAX_CUSTOM_WORDS), totalOriginalWords: wordArr.length, trimmed };
}

function detectScriptFromText(text) {
  if (!text) return APP_STATE.activeLanguage || "en";

  const counts = {
    te: 0, hi: 0, ta: 0, kn: 0, ml: 0, bn: 0, pa: 0, gu: 0, or: 0, ur: 0, en: 0
  };
  let hasAssameseMarkers = false;

  for (let i = 0; i < text.length; i++) {
    const cp = text.charCodeAt(i);
    if (cp >= 0x0C00 && cp <= 0x0C7F) counts.te++;
    else if (cp >= 0x0900 && cp <= 0x097F) counts.hi++;
    else if (cp >= 0x0B80 && cp <= 0x0BFF) counts.ta++;
    else if (cp >= 0x0C80 && cp <= 0x0CFF) counts.kn++;
    else if (cp >= 0x0D00 && cp <= 0x0D7F) counts.ml++;
    else if (cp >= 0x0980 && cp <= 0x09FF) {
      counts.bn++;
      if (cp === 0x09F0 || cp === 0x09F1) hasAssameseMarkers = true;
    }
    else if (cp >= 0x0A00 && cp <= 0x0A7F) counts.pa++;
    else if (cp >= 0x0A80 && cp <= 0x0AFF) counts.gu++;
    else if (cp >= 0x0B00 && cp <= 0x0B7F) counts.or++;
    else if (cp >= 0x0600 && cp <= 0x06FF) counts.ur++;
    else if ((cp >= 65 && cp <= 90) || (cp >= 97 && cp <= 122)) counts.en++;
  }

  let bestLang = "en";
  let bestCount = 0;
  for (const [lang, cnt] of Object.entries(counts)) {
    if (cnt > bestCount) {
      bestCount = cnt;
      bestLang = lang;
    }
  }

  if (bestLang === "bn" && (hasAssameseMarkers || APP_STATE.activeLanguage === "as")) {
    return "as";
  }
  if (bestLang === "hi" && (APP_STATE.activeLanguage === "mr" || APP_STATE.activeLanguage === "sa")) {
    return APP_STATE.activeLanguage;
  }
  return bestLang;
}

function inspectCustomPastedText() {
  const ta = document.getElementById("customPasteInput");
  if (!ta) return;
  const info = cleanCustomPracticeText(ta.value);
  const detectedCode = detectScriptFromText(info.text);
  const langObj = (APP_STATE.languages || []).find((l) => l.code === detectedCode);

  const wcBadge = document.getElementById("customWordCountBadge");
  const ccBadge = document.getElementById("customCharCountBadge");
  const scBadge = document.getElementById("customDetectedScriptBadge");

  if (wcBadge) {
    const orig = info.totalOriginalWords || 0;
    wcBadge.textContent = info.trimmed
      ? `${orig} words (will trim to ${MAX_CUSTOM_WORDS})`
      : `${orig} / ${MAX_CUSTOM_WORDS} words`;
    wcBadge.style.borderColor = info.trimmed ? "var(--coral)" : "var(--border-med)";
    wcBadge.style.color = info.trimmed ? "var(--coral)" : "var(--text-dark)";
  }
  if (ccBadge) {
    ccBadge.textContent = `${info.text.length} characters`;
  }
  if (scBadge) {
    scBadge.textContent = info.text
      ? `Detected Script: ${langObj ? `${langObj.native_name} (${langObj.name})` : detectedCode.toUpperCase()}`
      : "Script: Auto-Detect";
  }
}

async function pasteFromClipboardToCustom() {
  try {
    const clipText = await navigator.clipboard.readText();
    if (clipText) {
      const ta = document.getElementById("customPasteInput");
      if (ta) {
        ta.value = clipText;
        inspectCustomPastedText();
      }
    }
  } catch (e) {
    alert("Click inside the text box and press Ctrl + V to paste your paragraph!");
  }
}

function clearCustomPassageBox() {
  const ta = document.getElementById("customPasteInput");
  const ti = document.getElementById("customPassageTitle");
  if (ta) ta.value = "";
  if (ti) ti.value = "";
  inspectCustomPastedText();
}

function saveRecentCustomPassage(title, text, langCode) {
  try {
    const existing = JSON.parse(localStorage.getItem(CUSTOM_STORAGE_KEY) || "[]");
    const filtered = existing.filter((item) => item.text !== text);
    filtered.unshift({ title, text, langCode, savedAt: new Date().toLocaleDateString() });
    localStorage.setItem(CUSTOM_STORAGE_KEY, JSON.stringify(filtered.slice(0, 6)));
    renderRecentCustomPassages();
  } catch (e) {}
}

function renderRecentCustomPassages() {
  const container = document.getElementById("recentCustomPassagesList");
  if (!container) return;
  let list = [];
  try {
    list = JSON.parse(localStorage.getItem(CUSTOM_STORAGE_KEY) || "[]");
  } catch (e) {}

  if (list.length === 0) {
    container.innerHTML = `<div class="sub-copy small">No custom paragraphs saved yet. Paste any text above and click Practice!</div>`;
    return;
  }

  container.innerHTML = list
    .map((item, idx) => {
      const words = item.text.split(" ").filter(Boolean).length;
      const langObj = (APP_STATE.languages || []).find((l) => l.code === item.langCode);
      const badge = langObj ? langObj.native_name : (item.langCode || "en").toUpperCase();
      return `
        <div class="passage-card" onclick="loadSavedCustomPassage(${idx})">
          <h4>${escapeHtml(item.title)} <span class="badge-pill">${escapeHtml(badge)} • ${words}w</span></h4>
          <p class="sub-copy small" style="margin-top:6px;">${escapeHtml(item.text.slice(0, 110))}...</p>
        </div>
      `;
    })
    .join("");
}

function loadSavedCustomPassage(idx) {
  try {
    const list = JSON.parse(localStorage.getItem(CUSTOM_STORAGE_KEY) || "[]");
    const item = list[idx];
    if (!item) return;
    document.getElementById("customPassageTitle").value = item.title || "";
    document.getElementById("customPasteInput").value = item.text || "";
    inspectCustomPastedText();
  } catch (e) {}
}

async function startCustomPastedPractice() {
  const ta = document.getElementById("customPasteInput");
  const titleInput = document.getElementById("customPassageTitle");
  const timerSelect = document.getElementById("customTimerSelect");
  const autoSwitch = document.getElementById("customAutoSwitchScript")?.checked !== false;

  const info = cleanCustomPracticeText(ta ? ta.value : "");
  if (!info.text || info.text.length < 3) {
    alert("Please paste at least one word or sentence to practice!");
    return;
  }

  const detectedLang = detectScriptFromText(info.text);
  const title = (titleInput?.value || "").trim() || `Custom Practice (${info.words} words)`;
  const timeLimitSec = parseInt(timerSelect?.value || "0", 10) || 0;

  saveRecentCustomPassage(title, info.text, detectedLang);

  // If the pasted text is in a different language script, silently switch the 3D Keyboard & Finger Map!
  if (autoSwitch && APP_STATE.user && detectedLang !== APP_STATE.activeLanguage) {
    try {
      const res = await fetch("/api/settings", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          user_id: APP_STATE.user.id,
          current_language: detectedLang,
        }),
      });
      const json = await res.json();
      if (json.ok && json.data) {
        APP_STATE.currentDrill = null;
        applyDashboardPayload(json.data);
      }
    } catch (e) {}
  }

  loadDrillIntoStudio(
    {
      id: `custom_${Date.now()}`,
      title: `Custom: ${title}`,
      mode: "custom",
      text: info.text,
      tip: "Custom Practice Mode! Follow the glowing 3D keycaps and Left/Right Hand fingers for every single character.",
      timeLimitSec: timeLimitSec > 0 ? timeLimitSec : null,
    },
    true
  );
}
