/**
 * AksharaFlow Studio — Multi-Script 60–144fps HTML5 Canvas Arcade Engine
 * Automatically adapts to English or any of the 13 Indian InScript Languages!
 */

const GAME_WORD_POOL_EN = [
  "focus", "rhythm", "speed", "laser", "orbit", "planet", "galaxy", "system",
  "memory", "reflex", "matrix", "stream", "shield", "vector", "signal", "breeze",
  "energy", "spark", "future", "motion", "steady", "active", "global", "cipher",
  "record;", "ready.", "check,", "power!", "wait?", "100%", "2026", "450",
  "clear;", "exact.", "fast,", "score:", "alpha;", "omega.", "turbo!", "calm,"
];

const RACER_SENTENCES_EN = [
  "Speed emerges naturally from smooth, relaxed accuracy; keep your eyes ahead!",
  "The quick brown fox jumps over 12 lazy dogs; pack my box with 5 dozen jugs.",
  "Every finger knows its home key: A, S, D, F on the left; J, K, L, ; on the right!",
  "Focus on rhythm first, then watch your velocity climb past 50 words per minute."
];

let GAME_ENGINE = {
  selectedGame: "bubbles",
  running: false,
  animFrame: null,
  canvas: null,
  ctx: null,
  logicalWidth: 960,
  logicalHeight: 430,

  score: 0,
  combo: 0,
  lives: 5,
  totalKeystrokes: 0,
  errorKeystrokes: 0,
  startTimeMs: 0,
  lastFrameMs: 0,
  spawnTimerSec: 0,
  nextEntityId: 1,
  lockedEntityId: null,
  keyStats: {},

  entities: [],
  particles: [],
  lasers: [],
  clouds: [],

  racerText: "",
  racerCharIdx: 0,
  aiCars: [],
};

window.addEventListener("DOMContentLoaded", () => {
  const canvas = document.getElementById("typingGameCanvas");
  if (canvas) {
    GAME_ENGINE.canvas = canvas;
    GAME_ENGINE.ctx = canvas.getContext("2d");
    syncCanvasResolution();
    initBackgroundClouds();
    drawIdleGameBanner();
  }
  window.addEventListener("resize", () => {
    syncCanvasResolution();
    if (!GAME_ENGINE.running) drawIdleGameBanner();
  });
  window.addEventListener("keydown", handleCanvasGameKeyDown);
});

function syncCanvasResolution() {
  const c = GAME_ENGINE.canvas;
  if (!c || !c.parentElement) return;
  const rect = c.parentElement.getBoundingClientRect();
  const w = Math.max(640, Math.floor(rect.width || 960));
  const h = Math.max(360, Math.floor(rect.height || 430));
  const dpr = window.devicePixelRatio || 1;

  c.width = w * dpr;
  c.height = h * dpr;
  GAME_ENGINE.logicalWidth = w;
  GAME_ENGINE.logicalHeight = h;

  if (GAME_ENGINE.ctx) {
    GAME_ENGINE.ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }
}

function initBackgroundClouds() {
  GAME_ENGINE.clouds = [
    { x: 120, y: 75, r: 34, speed: 12 },
    { x: 420, y: 115, r: 42, speed: 9 },
    { x: 760, y: 65, r: 30, speed: 15 },
  ];
}

function selectCanvasGame(gameType) {
  stopCanvasGame();
  GAME_ENGINE.selectedGame = gameType;
  document.querySelectorAll(".arcade-card").forEach((c) => c.classList.remove("active"));
  const card = document.getElementById(`gcard-${gameType}`);
  if (card) card.classList.add("active");

  const titles = {
    bubbles: "🫧 Bubble Pop Reflex",
    rain: "☄️ Meteor Laser Defense",
    racer: "🏎️ Nitro Type Sprint",
  };
  document.getElementById("activeGameTitle").textContent = titles[gameType] || "Arcade Game";
  syncCanvasResolution();
  drawIdleGameBanner();
}

function changeGamePool() {
  const sel = document.getElementById("gamePoolSelect");
  if (sel) sel.blur();
  if (!GAME_ENGINE.running) drawIdleGameBanner();
}

function drawIdleGameBanner() {
  const ctx = GAME_ENGINE.ctx;
  const w = GAME_ENGINE.logicalWidth;
  const h = GAME_ENGINE.logicalHeight;
  if (!ctx) return;

  ctx.clearRect(0, 0, w, h);

  if (GAME_ENGINE.selectedGame === "bubbles") {
    const grad = ctx.createLinearGradient(0, 0, 0, h);
    grad.addColorStop(0, "#e0f2fe");
    grad.addColorStop(1, "#fef3c7");
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, w, h);
  } else if (GAME_ENGINE.selectedGame === "rain") {
    const grad = ctx.createLinearGradient(0, 0, 0, h);
    grad.addColorStop(0, "#0f172a");
    grad.addColorStop(1, "#1e293b");
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, w, h);
  } else {
    const grad = ctx.createLinearGradient(0, 0, 0, h);
    grad.addColorStop(0, "#ecfdf5");
    grad.addColorStop(1, "#fef3c7");
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, w, h);
  }

function drawWrappedCenteredText(ctx, text, centerX, startY, maxWidth, lineHeight) {
  const words = String(text || "").split(" ");
  let line = "";
  let y = startY;
  for (let i = 0; i < words.length; i++) {
    const testLine = line ? `${line} ${words[i]}` : words[i];
    if (ctx.measureText(testLine).width > maxWidth && line) {
      ctx.fillText(line, centerX, y);
      line = words[i];
      y += lineHeight;
    } else {
      line = testLine;
    }
  }
  if (line) ctx.fillText(line, centerX, y);
  return y;
}

  const cardW = Math.min(w - 64, 580);
  const cardH = 205;
  const cx = (w - cardW) / 2;
  const cy = (h - cardH) / 2;
  const innerMaxW = cardW - 56;

  ctx.fillStyle = "rgba(255, 255, 255, 0.96)";
  ctx.strokeStyle = "#f59e0b";
  ctx.lineWidth = 3;
  ctx.beginPath();
  ctx.roundRect(cx, cy, cardW, cardH, 22);
  ctx.fill();
  ctx.stroke();

  const titles = {
    bubbles: "🫧 Bubble Pop Reflex",
    rain: "☄️ Meteor Laser Defense",
    racer: "🏎️ Nitro Type Sprint",
  };
  const descriptions = {
    bubbles: "Pop rising meadow bubbles in your active script! Golden bubbles train your weak keys.",
    rain: "Type falling words in your active script to lock your laser turret onto meteors.",
    racer: "Type full sentences smoothly to boost your roadster past 3 WPM-calibrated pace cars!",
  };

  ctx.fillStyle = "#0d9488";
  ctx.font = "800 24px 'Fredoka', 'Segoe UI', sans-serif";
  ctx.textAlign = "center";
  ctx.fillText(titles[GAME_ENGINE.selectedGame], w / 2, cy + 52, innerMaxW);

  ctx.fillStyle = "#524b46";
  ctx.font = "600 14.5px 'Plus Jakarta Sans', 'Segoe UI', sans-serif";
  drawWrappedCenteredText(ctx, descriptions[GAME_ENGINE.selectedGame], w / 2, cy + 92, innerMaxW, 22);

  ctx.fillStyle = "#d97706";
  ctx.font = "800 15px 'Plus Jakarta Sans', 'Segoe UI', sans-serif";
  ctx.fillText("Click '▶ Play Game' above or press Enter to start!", w / 2, cy + 162, innerMaxW);
}

function getWeakKeysPool() {
  if (
    typeof APP_STATE !== "undefined" &&
    APP_STATE.weaknessAnalysis &&
    APP_STATE.weaknessAnalysis.weak_keys &&
    APP_STATE.weaknessAnalysis.weak_keys.length > 0
  ) {
    return APP_STATE.weaknessAnalysis.weak_keys.map((w) => w.key);
  }
  if (typeof APP_STATE !== "undefined" && APP_STATE.activeLanguage !== "en" && APP_STATE.inscriptKeymap) {
    const km = APP_STATE.inscriptKeymap;
    return [km.KeyK?.main, km.KeyJ?.main, km.KeyE?.main, km.KeyF?.main].filter(Boolean);
  }
  return ["f", "j", "g", "h", ";", ".", ","];
}

function getPhysicalKeyHintForChar(ch) {
  if (!ch) return "";
  if (ch === " ") return "Space";
  if (ch === "\u200C") return "D+D";
  if (typeof APP_STATE === "undefined" || APP_STATE.activeLanguage === "en" || !APP_STATE.inscriptKeymap) {
    return ch.toUpperCase();
  }
  const km = APP_STATE.inscriptKeymap;
  for (const [code, pair] of Object.entries(km)) {
    const shortKey = code
      .replace(/^Key/, "")
      .replace(/^Digit/, "")
      .replace("Semicolon", ";")
      .replace("Quote", "'")
      .replace("Comma", ",")
      .replace("Period", ".")
      .replace("Slash", "/")
      .replace("BracketLeft", "[")
      .replace("BracketRight", "]")
      .replace("Minus", "-")
      .replace("Equal", "=")
      .replace("Backquote", "`");
    if (pair.main === ch) return shortKey;
    if (pair.shift === ch) return `⇧+${shortKey}`;
  }
  return ch;
}

function showGameKeyHints() {
  const cb = document.getElementById("gameKeyHintToggle");
  return cb ? cb.checked : true;
}

function generateSpawnToken() {
  const poolMode = document.getElementById("gamePoolSelect")?.value || "gunintalu";
  const weakKeys = getWeakKeysPool();
  const isBoss = Math.random() < 0.22 && weakKeys.length > 0;
  const isIndian = typeof APP_STATE !== "undefined" && APP_STATE.activeLanguage !== "en" && APP_STATE.inscriptKeymap;

  if (isIndian) {
    const km = APP_STATE.inscriptKeymap;
    const vocab = APP_STATE.nativeVocab || {};
    const homeCons = [
      km.KeyH?.main, km.KeyJ?.main, km.KeyK?.main, km.KeyL?.main, km.Semicolon?.main, km.Quote?.main
    ].filter(Boolean);
    const allSimpleCons = [
      ...homeCons,
      km.KeyY?.main, km.KeyU?.main, km.KeyI?.main, km.KeyO?.main, km.KeyP?.main,
      km.KeyC?.main, km.KeyV?.main, km.KeyB?.main, km.KeyN?.main, km.KeyM?.main
    ].filter(Boolean);
    const easyMatras = [
      km.KeyE?.main, km.KeyF?.main, km.KeyR?.main, km.KeyG?.main, km.KeyT?.main, km.KeyS?.main, km.KeyA?.main
    ].filter(Boolean);

    if (poolMode === "simple_cons") {
      const ch = allSimpleCons[Math.floor(Math.random() * allSimpleCons.length)];
      return { text: ch || "क", isBoss: false };
    }
    if (poolMode === "gunintalu") {
      const c = allSimpleCons[Math.floor(Math.random() * allSimpleCons.length)] || "क";
      const m = easyMatras[Math.floor(Math.random() * easyMatras.length)] || "";
      return { text: `${c}${m}`, isBoss };
    }
    if (poolMode === "homerow") {
      const c = homeCons[Math.floor(Math.random() * homeCons.length)] || "क";
      const hm = [km.KeyF?.main, km.KeyG?.main, km.KeyS?.main, km.KeyA?.main, ""].filter((x) => x !== undefined);
      const m = hm[Math.floor(Math.random() * hm.length)] || "";
      return { text: `${c}${m}`, isBoss: false };
    }
    if (poolMode === "weak") {
      const w = weakKeys[Math.floor(Math.random() * weakKeys.length)] || homeCons[0];
      return { text: w, isBoss: true };
    }
    const wordList = [
      ...(vocab.home_words || []),
      ...(vocab.top_words || []),
      ...(vocab.bottom_words || []),
    ];
    if (wordList.length > 0) {
      const w = wordList[Math.floor(Math.random() * wordList.length)];
      return { text: w, isBoss };
    }
  }

  // English mode
  if (poolMode === "simple_cons") {
    const ch = String.fromCharCode(97 + Math.floor(Math.random() * 26));
    return { text: ch, isBoss: false };
  }
  if (poolMode === "gunintalu") {
    const shortEn = ["as", "at", "be", "do", "go", "in", "is", "it", "me", "no", "of", "on", "or", "so", "to", "up", "we", "and", "for", "the", "fun", "run", "sky", "joy", "sun"];
    return { text: shortEn[Math.floor(Math.random() * shortEn.length)], isBoss };
  }
  if (poolMode === "homerow") {
    const hr = ["as", "df", "jk", "sad", "lad", "ask", "all", "fall", "glad", "half", "dash"];
    return { text: hr[Math.floor(Math.random() * hr.length)], isBoss: false };
  }
  if (poolMode === "weak") {
    const base = [...weakKeys, "a", "s", "d", "f", "j", "k", "l", ";", "e", "i", "r", "u"];
    const ch = base[Math.floor(Math.random() * base.length)];
    return { text: ch, isBoss: weakKeys.includes(ch) };
  }

  const activeFirstChars = new Set(GAME_ENGINE.entities.map((e) => e.text[0]));
  const pool = GAME_WORD_POOL_EN;
  const candidates = pool.filter((w) => !activeFirstChars.has(w[0]));
  const chosenPool = candidates.length > 0 ? candidates : pool;
  const word = chosenPool[Math.floor(Math.random() * chosenPool.length)];
  return { text: word, isBoss };
}

function startSelectedCanvasGame() {
  stopCanvasGame();
  if (document.activeElement && document.activeElement !== document.body) {
    document.activeElement.blur();
  }
  syncCanvasResolution();
  const c = GAME_ENGINE.canvas;
  if (!c) return;
  c.focus();

  const now = performance.now();
  GAME_ENGINE.running = true;
  GAME_ENGINE.score = 0;
  GAME_ENGINE.combo = 0;
  GAME_ENGINE.lives = 5;
  GAME_ENGINE.totalKeystrokes = 0;
  GAME_ENGINE.errorKeystrokes = 0;
  GAME_ENGINE.startTimeMs = now;
  GAME_ENGINE.lastFrameMs = now;
  GAME_ENGINE.spawnTimerSec = 99;
  GAME_ENGINE.nextEntityId = 1;
  GAME_ENGINE.lockedEntityId = null;
  GAME_ENGINE.keyStats = {};
  GAME_ENGINE.entities = [];
  GAME_ENGINE.particles = [];
  GAME_ENGINE.lasers = [];

  if (GAME_ENGINE.selectedGame === "racer") {
    const isIndian = typeof APP_STATE !== "undefined" && APP_STATE.activeLanguage !== "en" && APP_STATE.nativeVocab;
    if (isIndian && APP_STATE.nativeVocab.paragraphs && APP_STATE.nativeVocab.paragraphs.length > 0) {
      GAME_ENGINE.racerText = APP_STATE.nativeVocab.paragraphs[0];
    } else {
      const shuffled = [...RACER_SENTENCES_EN].sort(() => Math.random() - 0.5);
      GAME_ENGINE.racerText = shuffled.join(" ");
    }
    GAME_ENGINE.racerCharIdx = 0;

    const diff = document.getElementById("gameDifficultySelect")?.value || "normal";
    const mult = diff === "easy" ? 0.7 : diff === "hard" ? 1.3 : 1.0;
    GAME_ENGINE.aiCars = [
      { name: "Cruiser (22 WPM)", color: "#10b981", wpm: Math.round(22 * mult), charsTyped: 0 },
      { name: "Sprinter (34 WPM)", color: "#f59e0b", wpm: Math.round(34 * mult), charsTyped: 0 },
      { name: "Pro Roadster (46 WPM)", color: "#f43f5e", wpm: Math.round(46 * mult), charsTyped: 0 },
    ];
  }

  updateGameHudUI();
  GAME_ENGINE.animFrame = requestAnimationFrame(gameLoop);
}

function stopCanvasGame() {
  if (GAME_ENGINE.animFrame) {
    cancelAnimationFrame(GAME_ENGINE.animFrame);
    GAME_ENGINE.animFrame = null;
  }
  GAME_ENGINE.running = false;
  GAME_ENGINE.lockedEntityId = null;
}

function getLockedEntity() {
  if (GAME_ENGINE.lockedEntityId === null) return null;
  const found = GAME_ENGINE.entities.find((e) => e.id === GAME_ENGINE.lockedEntityId);
  if (!found) {
    GAME_ENGINE.lockedEntityId = null;
    return null;
  }
  return found;
}

function updateGameHudUI() {
  document.getElementById("gameScore").textContent = GAME_ENGINE.score;
  document.getElementById("gameCombo").textContent = `${GAME_ENGINE.combo}x`;
  const elapsedMin = Math.max(0.04, (performance.now() - GAME_ENGINE.startTimeMs) / 60000);
  const netWpm = Math.max(
    0,
    Math.round(((GAME_ENGINE.totalKeystrokes - GAME_ENGINE.errorKeystrokes) / 5) / elapsedMin)
  );
  document.getElementById("gameWpm").textContent = `${netWpm} WPM`;
  document.getElementById("gameLives").textContent =
    "❤️".repeat(Math.max(0, GAME_ENGINE.lives)) || "0";

  const bufEl = document.getElementById("gameTypedBuffer");
  if (GAME_ENGINE.selectedGame === "racer") {
    const nextCh = GAME_ENGINE.racerText[GAME_ENGINE.racerCharIdx] || "";
    const hint = getPhysicalKeyHintForChar(nextCh);
    if (nextCh === " ") {
      bufEl.textContent = "Next: [Space]";
    } else if (typeof APP_STATE !== "undefined" && APP_STATE.activeLanguage !== "en") {
      bufEl.textContent = `Next: '${nextCh}' • Key [${hint}]`;
    } else {
      bufEl.textContent = `Next: '${nextCh}'`;
    }
  } else {
    const locked = getLockedEntity();
    if (locked) {
      const nextCh = locked.text[locked.typedCount] || "";
      const hint = getPhysicalKeyHintForChar(nextCh);
      bufEl.textContent = `Locked: ${locked.text} (${locked.typedCount}/${locked.text.length}) • Key [${hint}]`;
    } else {
      bufEl.textContent = "Type any target...";
    }
  }
}

function spawnParticles(x, y, color, count = 16) {
  for (let i = 0; i < count; i++) {
    const angle = Math.random() * Math.PI * 2;
    const spd = 60 + Math.random() * 170;
    GAME_ENGINE.particles.push({
      x,
      y,
      vx: Math.cos(angle) * spd,
      vy: Math.sin(angle) * spd,
      radius: 2.5 + Math.random() * 3.5,
      color,
      alpha: 1.0,
    });
  }
}

function gameLoop(timestamp) {
  if (!GAME_ENGINE.running) return;

  const rawDt = (timestamp - GAME_ENGINE.lastFrameMs) / 1000;
  const dt = Math.max(0.001, Math.min(0.05, rawDt));
  GAME_ENGINE.lastFrameMs = timestamp;

  const w = GAME_ENGINE.logicalWidth;
  const h = GAME_ENGINE.logicalHeight;
  const ctx = GAME_ENGINE.ctx;
  const diff = document.getElementById("gameDifficultySelect")?.value || "easy";
  const speedMult = diff === "easy" ? 0.55 : diff === "hard" ? 1.28 : 0.9;

  ctx.clearRect(0, 0, w, h);

  if (GAME_ENGINE.selectedGame === "bubbles") {
    updateAndDrawBubbles(ctx, w, h, dt, speedMult);
  } else if (GAME_ENGINE.selectedGame === "rain") {
    updateAndDrawMeteorRain(ctx, w, h, dt, speedMult);
  } else if (GAME_ENGINE.selectedGame === "racer") {
    updateAndDrawRacer(ctx, w, h, dt);
  }

  for (let i = GAME_ENGINE.particles.length - 1; i >= 0; i--) {
    const p = GAME_ENGINE.particles[i];
    p.x += p.vx * dt;
    p.y += p.vy * dt;
    p.alpha -= 1.8 * dt;
    if (p.alpha <= 0) {
      GAME_ENGINE.particles.splice(i, 1);
      continue;
    }
    ctx.save();
    ctx.globalAlpha = Math.max(0, p.alpha);
    ctx.fillStyle = p.color;
    ctx.beginPath();
    ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();
  }

  updateGameHudUI();

  if (GAME_ENGINE.lives <= 0) {
    finishCanvasGameSession("Session Complete — Out of Hearts!");
    return;
  }

  if (GAME_ENGINE.running) {
    GAME_ENGINE.animFrame = requestAnimationFrame(gameLoop);
  }
}

function updateAndDrawBubbles(ctx, w, h, dt, speedMult) {
  const grad = ctx.createLinearGradient(0, 0, 0, h);
  grad.addColorStop(0, "#e0f2fe");
  grad.addColorStop(0.85, "#f0fdf4");
  grad.addColorStop(1, "#dcfce7");
  ctx.fillStyle = grad;
  ctx.fillRect(0, 0, w, h);

  ctx.fillStyle = "rgba(255, 255, 255, 0.72)";
  GAME_ENGINE.clouds.forEach((cl) => {
    cl.x += cl.speed * dt;
    if (cl.x - cl.r * 2 > w) cl.x = -cl.r * 2;
    ctx.beginPath();
    ctx.arc(cl.x, cl.y, cl.r, 0, Math.PI * 2);
    ctx.arc(cl.x + cl.r * 0.75, cl.y + 4, cl.r * 0.8, 0, Math.PI * 2);
    ctx.arc(cl.x - cl.r * 0.75, cl.y + 6, cl.r * 0.75, 0, Math.PI * 2);
    ctx.fill();
  });

  GAME_ENGINE.spawnTimerSec += dt;
  const spawnInterval = 1.48 / speedMult;
  if (GAME_ENGINE.spawnTimerSec >= spawnInterval && GAME_ENGINE.entities.length < 10) {
    GAME_ENGINE.spawnTimerSec = 0;
    const tok = generateSpawnToken();
    const radius = Math.max(34, 24 + tok.text.length * 6.5);
    const x = radius + 30 + Math.random() * (w - (radius + 30) * 2);
    const palette = ["#0d9488", "#0284c7", "#7c3aed", "#059669", "#ea580c"];
    GAME_ENGINE.entities.push({
      id: GAME_ENGINE.nextEntityId++,
      text: tok.text,
      typedCount: 0,
      isBoss: tok.isBoss,
      x,
      y: h + radius,
      vy: (52 + Math.random() * 32) * speedMult,
      wobblePhase: Math.random() * Math.PI * 2,
      radius,
      color: tok.isBoss ? "#d97706" : palette[Math.floor(Math.random() * palette.length)],
    });
  }

  for (let i = GAME_ENGINE.entities.length - 1; i >= 0; i--) {
    const b = GAME_ENGINE.entities[i];
    b.y -= b.vy * dt;
    b.wobblePhase += 2.2 * dt;
    const drawX = b.x + Math.sin(b.wobblePhase) * 10;

    if (b.y + b.radius < 0) {
      if (GAME_ENGINE.lockedEntityId === b.id) {
        GAME_ENGINE.lockedEntityId = null;
      }
      GAME_ENGINE.entities.splice(i, 1);
      GAME_ENGINE.lives--;
      GAME_ENGINE.combo = 0;
      SoundFX.playError();
      continue;
    }

    const isLocked = GAME_ENGINE.lockedEntityId === b.id;

    ctx.save();
    ctx.beginPath();
    ctx.arc(drawX, b.y, b.radius, 0, Math.PI * 2);
    ctx.fillStyle = isLocked ? "rgba(254, 243, 199, 0.96)" : "rgba(255, 255, 255, 0.9)";
    ctx.fill();
    ctx.lineWidth = isLocked ? 3.5 : b.isBoss ? 3 : 2.2;
    ctx.strokeStyle = isLocked ? "#d97706" : b.color;
    ctx.stroke();

    ctx.beginPath();
    ctx.arc(drawX - b.radius * 0.35, b.y - b.radius * 0.35, b.radius * 0.16, 0, Math.PI * 2);
    ctx.fillStyle = "rgba(255, 255, 255, 0.9)";
    ctx.fill();

    const isIndian = typeof APP_STATE !== "undefined" && APP_STATE.activeLanguage !== "en";
    const showHints = showGameKeyHints();

    ctx.font = "bold 20px 'Plus Jakarta Sans', 'Nirmala UI', Consolas, sans-serif";
    ctx.textBaseline = "middle";

    if (isIndian) {
      // Render unbroken Indic syllable/word (zero dotted circles!)
      ctx.textAlign = "center";
      ctx.fillStyle = isLocked ? "#0f766e" : "#1c1917";
      ctx.fillText(b.text, drawX, b.y - (showHints ? 6 : 0));

      // Progress dots for multi-keystroke syllables
      if (b.text.length > 1) {
        const dotGap = 8;
        const startDotX = drawX - ((b.text.length - 1) * dotGap) / 2;
        for (let d = 0; d < b.text.length; d++) {
          ctx.beginPath();
          ctx.arc(startDotX + d * dotGap, b.y + 11, 2.8, 0, Math.PI * 2);
          ctx.fillStyle = d < b.typedCount ? "#059669" : "#cbd5e1";
          ctx.fill();
        }
      }

      // Live Physical Key Hint Badge inside/bottom of bubble
      if (showHints) {
        const nextCh = b.text[b.typedCount] || "";
        const hint = getPhysicalKeyHintForChar(nextCh);
        if (hint) {
          ctx.font = "800 11px Consolas, sans-serif";
          ctx.textAlign = "center";
          ctx.fillStyle = isLocked ? "#b45309" : "#0d9488";
          ctx.fillText(`[${hint}]`, drawX, b.y + b.radius - 10);
        }
      }
    } else {
      const doneStr = b.text.slice(0, b.typedCount);
      const remStr = b.text.slice(b.typedCount);
      const totalW = ctx.measureText(b.text).width;
      let startX = drawX - totalW / 2;

      ctx.textAlign = "left";
      if (doneStr) {
        ctx.fillStyle = "#059669";
        ctx.fillText(doneStr, startX, b.y);
        startX += ctx.measureText(doneStr).width;
      }
      ctx.fillStyle = "#1c1917";
      ctx.fillText(remStr, startX, b.y);
    }

    if (b.isBoss) {
      ctx.font = "800 10px 'Plus Jakarta Sans', sans-serif";
      ctx.textAlign = "center";
      ctx.fillStyle = "#d97706";
      ctx.fillText("WEAK KEY BONUS", drawX, b.y - b.radius - 9);
    }
    ctx.restore();
  }
}

function updateAndDrawMeteorRain(ctx, w, h, dt, speedMult) {
  const grad = ctx.createLinearGradient(0, 0, 0, h);
  grad.addColorStop(0, "#0f172a");
  grad.addColorStop(1, "#1e293b");
  ctx.fillStyle = grad;
  ctx.fillRect(0, 0, w, h);

  ctx.strokeStyle = "rgba(20, 184, 166, 0.45)";
  ctx.lineWidth = 3;
  ctx.beginPath();
  ctx.moveTo(0, h - 22);
  ctx.lineTo(w, h - 22);
  ctx.stroke();

  GAME_ENGINE.spawnTimerSec += dt;
  const spawnInterval = 1.68 / speedMult;
  if (GAME_ENGINE.spawnTimerSec >= spawnInterval && GAME_ENGINE.entities.length < 9) {
    GAME_ENGINE.spawnTimerSec = 0;
    const tok = generateSpawnToken();
    const x = 85 + Math.random() * (w - 170);
    GAME_ENGINE.entities.push({
      id: GAME_ENGINE.nextEntityId++,
      text: tok.text,
      typedCount: 0,
      isBoss: tok.isBoss,
      x,
      y: -15,
      vx: (w / 2 - x) * 0.08,
      vy: (40 + Math.random() * 24) * speedMult,
      color: tok.isBoss ? "#f43f5e" : "#f59e0b",
    });
  }

  const turretX = w / 2;
  const turretY = h - 20;
  for (let i = GAME_ENGINE.lasers.length - 1; i >= 0; i--) {
    const l = GAME_ENGINE.lasers[i];
    l.alpha -= 4.5 * dt;
    if (l.alpha <= 0) {
      GAME_ENGINE.lasers.splice(i, 1);
      continue;
    }
    ctx.save();
    ctx.globalAlpha = Math.max(0, l.alpha);
    ctx.strokeStyle = "#2dd4bf";
    ctx.lineWidth = 3.5;
    ctx.beginPath();
    ctx.moveTo(turretX, turretY - 10);
    ctx.lineTo(l.tx, l.ty);
    ctx.stroke();
    ctx.restore();
  }

  ctx.fillStyle = "#14b8a6";
  ctx.beginPath();
  ctx.arc(turretX, turretY, 22, Math.PI, 0);
  ctx.fill();

  for (let i = GAME_ENGINE.entities.length - 1; i >= 0; i--) {
    const m = GAME_ENGINE.entities[i];
    m.x += m.vx * dt;
    m.y += m.vy * dt;

    if (m.y >= h - 28) {
      if (GAME_ENGINE.lockedEntityId === m.id) {
        GAME_ENGINE.lockedEntityId = null;
      }
      GAME_ENGINE.entities.splice(i, 1);
      GAME_ENGINE.lives--;
      GAME_ENGINE.combo = 0;
      SoundFX.playError();
      spawnParticles(m.x, h - 24, "#f43f5e", 20);
      continue;
    }

    const isLocked = GAME_ENGINE.lockedEntityId === m.id;

    ctx.save();
    ctx.beginPath();
    ctx.arc(m.x, m.y, 14, 0, Math.PI * 2);
    ctx.fillStyle = isLocked ? "#2dd4bf" : m.color;
    ctx.fill();

    if (isLocked) {
      ctx.strokeStyle = "#2dd4bf";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.arc(m.x, m.y, 21, 0, Math.PI * 2);
      ctx.stroke();
    }

    const isIndian = typeof APP_STATE !== "undefined" && APP_STATE.activeLanguage !== "en";
    const showHints = showGameKeyHints();

    ctx.font = "bold 16.5px 'Plus Jakarta Sans', 'Nirmala UI', Consolas, sans-serif";
    const nextCh = m.text[m.typedCount] || "";
    const hintText = isIndian && showHints ? ` [${getPhysicalKeyHintForChar(nextCh)}]` : "";
    const fullLabel = `${m.text}${hintText}`;
    const textW = ctx.measureText(fullLabel).width;
    const pillW = Math.max(60, textW + 22);
    const pillX = m.x - pillW / 2;
    const pillY = m.y + 18;

    ctx.fillStyle = isLocked ? "#0f172a" : "rgba(15, 23, 42, 0.92)";
    ctx.strokeStyle = isLocked ? "#2dd4bf" : "#475569";
    ctx.lineWidth = isLocked ? 2 : 1.2;
    ctx.beginPath();
    ctx.roundRect(pillX, pillY, pillW, 29, 7);
    ctx.fill();
    ctx.stroke();

    ctx.textBaseline = "middle";
    if (isIndian) {
      ctx.textAlign = "center";
      ctx.fillStyle = isLocked ? "#2dd4bf" : "#f8fafc";
      ctx.fillText(fullLabel, m.x, pillY + 14.5);
    } else {
      const doneStr = m.text.slice(0, m.typedCount);
      const remStr = m.text.slice(m.typedCount);
      let cursorX = m.x - textW / 2;
      ctx.textAlign = "left";
      if (doneStr) {
        ctx.fillStyle = "#2dd4bf";
        ctx.fillText(doneStr, cursorX, pillY + 14.5);
        cursorX += ctx.measureText(doneStr).width;
      }
      ctx.fillStyle = "#f8fafc";
      ctx.fillText(remStr, cursorX, pillY + 14.5);
    }
    ctx.restore();
  }
}

function updateAndDrawRacer(ctx, w, h, dt) {
  const totalChars = Math.max(1, GAME_ENGINE.racerText.length);
  const playerProgress = Math.min(1, GAME_ENGINE.racerCharIdx / totalChars);

  ctx.fillStyle = "#dcfce7";
  ctx.fillRect(0, 0, w, h);

  const bannerX = 24;
  const bannerY = 14;
  const bannerW = w - 48;
  const bannerH = 82;

  ctx.fillStyle = "#ffffff";
  ctx.strokeStyle = "#0d9488";
  ctx.lineWidth = 2.5;
  ctx.beginPath();
  ctx.roundRect(bannerX, bannerY, bannerW, bannerH, 14);
  ctx.fill();
  ctx.stroke();

  const winStart = Math.max(0, GAME_ENGINE.racerCharIdx - 14);
  const winSlice = GAME_ENGINE.racerText.slice(winStart, winStart + 46);
  const activeOffset = GAME_ENGINE.racerCharIdx - winStart;

  ctx.font = "bold 20px 'Plus Jakarta Sans', 'Nirmala UI', Consolas, sans-serif";
  ctx.textAlign = "left";
  ctx.textBaseline = "middle";

  const typedPart = winSlice.slice(0, activeOffset);
  const currentChar = winSlice.slice(activeOffset, activeOffset + 1);
  const remainPart = winSlice.slice(activeOffset + 1);

  let xCursor = bannerX + 24;
  const textY = bannerY + 41;

  if (typedPart) {
    ctx.fillStyle = "#059669";
    ctx.fillText(typedPart, xCursor, textY);
    xCursor += ctx.measureText(typedPart).width;
  }

  const charW = Math.max(14, ctx.measureText(currentChar || " ").width);
  ctx.fillStyle = "#fef3c7";
  ctx.strokeStyle = "#d97706";
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.roundRect(xCursor - 1, textY - 16, charW + 4, 32, 5);
  ctx.fill();
  ctx.stroke();

  ctx.fillStyle = "#b45309";
  ctx.fillText(currentChar === " " ? "␣" : currentChar, xCursor + 1, textY);
  xCursor += charW + 3;

  ctx.fillStyle = "#44403c";
  ctx.fillText(remainPart, xCursor, textY);

  GAME_ENGINE.aiCars.forEach((ai) => {
    const charsPerSec = (ai.wpm * 5) / 60;
    ai.charsTyped = Math.min(totalChars, ai.charsTyped + charsPerSec * dt);
  });

  const racers = [
    { id: "player", name: "YOU (Player Roadster)", color: "#0d9488", progress: playerProgress, isPlayer: true },
    ...GAME_ENGINE.aiCars.map((ai, i) => ({
      id: `ai_${i}`,
      name: ai.name,
      color: ai.color,
      progress: Math.min(1, ai.charsTyped / totalChars),
      isPlayer: false,
    })),
  ];

  const sortedIds = [...racers].sort((a, b) => b.progress - a.progress).map((r) => r.id);
  const rankLabels = ["1st", "2nd", "3rd", "4th"];

  const trackTop = 110;
  const laneH = (h - trackTop - 14) / 4;

  racers.forEach((r, idx) => {
    const y = trackTop + idx * laneH;
    ctx.fillStyle = idx % 2 === 0 ? "#334155" : "#3e4c63";
    ctx.fillRect(24, y, w - 48, laneH - 6);

    ctx.strokeStyle = "rgba(255,255,255,0.22)";
    ctx.setLineDash([18, 14]);
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(36, y + (laneH - 6) / 2);
    ctx.lineTo(w - 80, y + (laneH - 6) / 2);
    ctx.stroke();
    ctx.setLineDash([]);

    ctx.fillStyle = "#f8fafc";
    ctx.fillRect(w - 72, y, 10, laneH - 6);

    const rankIdx = sortedIds.indexOf(r.id);
    ctx.fillStyle = "#e2e8f0";
    ctx.font = "700 12.5px 'Plus Jakarta Sans', sans-serif";
    ctx.fillText(`${rankLabels[rankIdx]} • ${r.name}`, 38, y + 16);

    const startX = 42;
    const finishX = w - 145;
    const carX = startX + r.progress * (finishX - startX);
    const carY = y + (laneH - 6) / 2 - 6;

    ctx.fillStyle = "#0f172a";
    ctx.fillRect(carX + 8, carY - 3, 13, 4);
    ctx.fillRect(carX + 45, carY - 3, 13, 4);
    ctx.fillRect(carX + 8, carY + 27, 13, 4);
    ctx.fillRect(carX + 45, carY + 27, 13, 4);

    ctx.fillStyle = r.color;
    ctx.beginPath();
    ctx.roundRect(carX, carY, 66, 28, 9);
    ctx.fill();

    ctx.fillStyle = "#e0f2fe";
    ctx.beginPath();
    ctx.roundRect(carX + 34, carY + 4, 18, 20, 4);
    ctx.fill();

    if (r.isPlayer && GAME_ENGINE.combo >= 3) {
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath();
      ctx.moveTo(carX, carY + 7);
      ctx.lineTo(carX - 16 - Math.random() * 10, carY + 14);
      ctx.lineTo(carX, carY + 21);
      ctx.fill();
    }
  });

  if (playerProgress >= 1) {
    const playerRank = sortedIds.indexOf("player") + 1;
    const suffix = playerRank === 1 ? "st" : playerRank === 2 ? "nd" : playerRank === 3 ? "rd" : "th";
    finishCanvasGameSession(`🏁 Checkered Flag! You Finished ${playerRank}${suffix}!`);
  }
}

function handleCanvasGameKeyDown(e) {
  if (typeof APP_STATE === "undefined" || APP_STATE.activeTab !== "games") return;
  if (!document.getElementById("userModal").classList.contains("hidden")) return;
  if (!document.getElementById("inscriptGuideModal").classList.contains("hidden")) return;
  if (!document.getElementById("resultModal").classList.contains("hidden")) return;

  if (!GAME_ENGINE.running) {
    if (e.key === "Enter") {
      e.preventDefault();
      startSelectedCanvasGame();
    }
    return;
  }

  if (["Shift", "Control", "Alt", "Meta", "CapsLock", "Tab"].includes(e.key)) return;

  if (e.key === "Backspace" || e.key === "Escape") {
    e.preventDefault();
    const locked = getLockedEntity();
    if (locked) {
      locked.typedCount = 0;
      GAME_ENGINE.lockedEntityId = null;
    }
    updateGameHudUI();
    return;
  }

  if (e.key.length !== 1) return;
  e.preventDefault();

  GAME_ENGINE.totalKeystrokes++;

  if (GAME_ENGINE.selectedGame === "racer") {
    const expected = GAME_ENGINE.racerText[GAME_ENGINE.racerCharIdx];
    const ch = typeof resolveEffectiveTypedChar === "function" ? resolveEffectiveTypedChar(e, expected) : e.key;
    recordGameKeyTelemetry(expected, ch);
    if (ch === expected) {
      SoundFX.playClick();
      GAME_ENGINE.racerCharIdx++;
      GAME_ENGINE.combo++;
      GAME_ENGINE.score += 10 + Math.min(25, GAME_ENGINE.combo);
    } else {
      SoundFX.playError();
      GAME_ENGINE.errorKeystrokes++;
      GAME_ENGINE.combo = 0;
    }
    updateGameHudUI();
    return;
  }

  let target = getLockedEntity();
  // Determine candidate character via Native or Auto-InScript
  const ch =
    typeof resolveEffectiveTypedChar === "function"
      ? resolveEffectiveTypedChar(e, target ? target.text[target.typedCount] : "")
      : e.key;

  if (!target) {
    const matches = GAME_ENGINE.entities.filter((ent) => ent.text[0] === ch);
    if (matches.length > 0) {
      if (GAME_ENGINE.selectedGame === "bubbles") {
        matches.sort((a, b) => a.y - b.y);
      } else {
        matches.sort((a, b) => b.y - a.y);
      }
      target = matches[0];
      GAME_ENGINE.lockedEntityId = target.id;
    }
  }

  if (target) {
    const expectedChar = target.text[target.typedCount];
    recordGameKeyTelemetry(expectedChar, ch);

    if (ch === expectedChar) {
      SoundFX.playClick();
      target.typedCount++;

      if (GAME_ENGINE.selectedGame === "rain") {
        GAME_ENGINE.lasers.push({ tx: target.x, ty: target.y, alpha: 1.0 });
        spawnParticles(target.x, target.y, "#2dd4bf", 5);
      }

      if (target.typedCount >= target.text.length) {
        const bonus = target.isBoss ? 50 : 25;
        GAME_ENGINE.combo++;
        GAME_ENGINE.score += bonus + GAME_ENGINE.combo * 5;
        spawnParticles(target.x, target.y, target.color || "#0d9488", 18);

        const idx = GAME_ENGINE.entities.findIndex((ent) => ent.id === target.id);
        if (idx !== -1) GAME_ENGINE.entities.splice(idx, 1);
        GAME_ENGINE.lockedEntityId = null;

        if (GAME_ENGINE.score >= 700) {
          finishCanvasGameSession("🏆 Stage Complete — Phenomenal Reflexes!");
        }
      }
    } else {
      SoundFX.playError();
      GAME_ENGINE.errorKeystrokes++;
      GAME_ENGINE.combo = 0;
    }
  } else {
    SoundFX.playError();
    GAME_ENGINE.errorKeystrokes++;
    GAME_ENGINE.combo = 0;
    if (GAME_ENGINE.entities.length > 0) {
      recordGameKeyTelemetry(GAME_ENGINE.entities[0].text[0], ch);
    }
  }

  updateGameHudUI();
}

function recordGameKeyTelemetry(expectedChar, typedChar) {
  if (!expectedChar) return;
  if (!GAME_ENGINE.keyStats[expectedChar]) {
    GAME_ENGINE.keyStats[expectedChar] = {
      hits: 0,
      misses: 0,
      latencies: [200],
      confused_with: {},
    };
  }
  if (expectedChar === typedChar) {
    GAME_ENGINE.keyStats[expectedChar].hits++;
  } else {
    GAME_ENGINE.keyStats[expectedChar].misses++;
    const c = GAME_ENGINE.keyStats[expectedChar].confused_with;
    c[typedChar] = (c[typedChar] || 0) + 1;
  }
}

async function finishCanvasGameSession(bannerTitle) {
  stopCanvasGame();
  SoundFX.playFanfare();

  const elapsedSec = Math.max(1, (performance.now() - GAME_ENGINE.startTimeMs) / 1000);
  const mins = elapsedSec / 60;
  const total = Math.max(1, GAME_ENGINE.totalKeystrokes);
  const errs = GAME_ENGINE.errorKeystrokes;
  const grossWpm = (total / 5) / mins;
  const netWpm = Math.max(0, ((total - errs) / 5) / mins);
  const accuracy = Math.max(0, Math.min(100, ((total - errs) / total) * 100));

  const ctx = GAME_ENGINE.ctx;
  const w = GAME_ENGINE.logicalWidth;
  const h = GAME_ENGINE.logicalHeight;
  if (ctx) {
    ctx.fillStyle = "rgba(35, 31, 29, 0.72)";
    ctx.fillRect(0, 0, w, h);

    const cardW = Math.min(w - 64, 580);
    const cardH = 200;
    const cx = (w - cardW) / 2;
    const cy = (h - cardH) / 2;
    const innerMaxW = cardW - 52;

    ctx.fillStyle = "#ffffff";
    ctx.strokeStyle = "#f59e0b";
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.roundRect(cx, cy, cardW, cardH, 22);
    ctx.fill();
    ctx.stroke();

    ctx.fillStyle = "#0d9488";
    ctx.font = "800 23px 'Fredoka', 'Segoe UI', sans-serif";
    ctx.textAlign = "center";
    ctx.fillText(bannerTitle, w / 2, cy + 52, innerMaxW);

    ctx.fillStyle = "#231f1d";
    ctx.font = "700 17px 'Plus Jakarta Sans', sans-serif";
    ctx.fillText(
      `Score: ${GAME_ENGINE.score}  •  Speed: ${Math.round(netWpm)} WPM  •  Accuracy: ${accuracy.toFixed(1)}%`,
      w / 2,
      cy + 100,
      innerMaxW
    );

    ctx.fillStyle = "#d97706";
    ctx.font = "700 14.5px 'Plus Jakarta Sans', sans-serif";
    ctx.fillText("Press Enter or click '▶ Play Game' to play again!", w / 2, cy + 150, innerMaxW);
  }

  if (typeof APP_STATE !== "undefined" && APP_STATE.user) {
    try {
      const res = await fetch("/api/record_session", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          user_id: APP_STATE.user.id,
          language: APP_STATE.activeLanguage || "en",
          lesson_id: `game_${GAME_ENGINE.selectedGame}`,
          lesson_title: `Arcade Game: ${GAME_ENGINE.selectedGame.toUpperCase()}`,
          mode: `game_${GAME_ENGINE.selectedGame}`,
          gross_wpm: grossWpm,
          net_wpm: netWpm,
          accuracy,
          duration_sec: elapsedSec,
          total_chars: total,
          error_chars: errs,
          score: GAME_ENGINE.score,
          key_stats: GAME_ENGINE.keyStats,
        }),
      });
      const json = await res.json();
      if (json.ok) {
        applyDashboardPayload(json.data);
      }
    } catch (e) {
      console.error("Failed to save game telemetry:", e);
    }
  }
}
