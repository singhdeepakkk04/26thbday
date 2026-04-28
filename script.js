/* ============================================================
   BIRTHDAY WEBSITE — script.js
   26th Birthday Edition
============================================================ */

// ─── Typed name effect ───────────────────────────────────────
const nameEl = document.getElementById('nameReveal');
const nameText = '✨ Happy Birthday ✨';
let ni = 0;
function typeName() {
  if (ni <= nameText.length) {
    nameEl.textContent = nameText.slice(0, ni);
    ni++;
    setTimeout(typeName, 80);
  }
}
setTimeout(typeName, 1200);

// ─── Falling petals (canvas) ─────────────────────────────────
const canvas = document.getElementById('petals');
const ctx    = canvas.getContext('2d');

function resizeCanvas() {
  canvas.width  = window.innerWidth;
  canvas.height = window.innerHeight;
}
resizeCanvas();
window.addEventListener('resize', resizeCanvas);

const PETAL_EMOJIS = ['🌸', '🌺', '🌹', '💮', '🌷', '✿'];
const petals = [];

function createPetal() {
  return {
    x:     Math.random() * canvas.width,
    y:     -30,
    size:  Math.random() * 18 + 10,
    speed: Math.random() * 1.5 + 0.5,
    drift: (Math.random() - 0.5) * 1.2,
    rot:   Math.random() * 360,
    rotSpeed: (Math.random() - 0.5) * 3,
    emoji: PETAL_EMOJIS[Math.floor(Math.random() * PETAL_EMOJIS.length)],
    opacity: Math.random() * 0.5 + 0.4,
  };
}

// Spawn petals gradually
setInterval(() => {
  if (petals.length < 40) petals.push(createPetal());
}, 300);

function animatePetals() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  for (let i = petals.length - 1; i >= 0; i--) {
    const p = petals[i];
    ctx.save();
    ctx.globalAlpha = p.opacity;
    ctx.translate(p.x, p.y);
    ctx.rotate((p.rot * Math.PI) / 180);
    ctx.font = `${p.size}px serif`;
    ctx.fillText(p.emoji, -p.size / 2, p.size / 2);
    ctx.restore();

    p.y   += p.speed;
    p.x   += p.drift;
    p.rot += p.rotSpeed;

    if (p.y > canvas.height + 40) {
      petals.splice(i, 1);
    }
  }
  requestAnimationFrame(animatePetals);
}
animatePetals();

// ─── Candles ─────────────────────────────────────────────────
const candlesRow = document.getElementById('candlesRow');
const NUM_CANDLES = 6;
let candlesLit = true;

for (let i = 0; i < NUM_CANDLES; i++) {
  const div = document.createElement('div');
  div.className = 'candle';
  div.innerHTML = `
    <div class="candle-flame" id="flame-${i}"></div>
    <div class="candle-body"></div>
  `;
  candlesRow.appendChild(div);
}

const blowBtn  = document.getElementById('blowBtn');
const wishText = document.getElementById('wishMessage');

blowBtn.addEventListener('click', () => {
  if (!candlesLit) {
    // Relight
    for (let i = 0; i < NUM_CANDLES; i++) {
      const flame = document.getElementById(`flame-${i}`);
      flame.style.opacity = '1';
    }
    candlesLit = true;
    blowBtn.textContent = '🎂 Blow the candles!';
    wishText.textContent = '';
    wishText.classList.remove('show');
    return;
  }

  // Blow out one by one
  for (let i = 0; i < NUM_CANDLES; i++) {
    setTimeout(() => {
      const flame = document.getElementById(`flame-${i}`);
      flame.style.opacity = '0';
      if (i === NUM_CANDLES - 1) {
        setTimeout(() => {
          wishText.textContent = '🌟 Your wish has been sent to the universe! 🌟';
          wishText.classList.add('show');
          blowBtn.textContent = '🕯️ Relight candles';
          candlesLit = false;
          launchConfetti(document.getElementById('confettiContainer'));
        }, 400);
      }
    }, i * 180);
  }
});

// ─── 26 Reasons ──────────────────────────────────────────────
const reasons = [
  "Your smile can genuinely brighten the darkest room.",
  "You never give up, even when things get impossibly hard.",
  "The way you care for the people you love is extraordinary.",
  "You have a sense of humor that catches people off guard.",
  "You're braver than you give yourself credit for.",
  "Your taste in music is actually impeccable.",
  "You notice the small things others miss.",
  "You've grown so much and you don't even see it.",
  "Your honesty, even when it's uncomfortable, is a gift.",
  "You make ordinary moments feel special.",
  "You have a quiet strength that's impossible to ignore.",
  "You're not afraid to feel things deeply — that's rare.",
  "Your ambition is inspiring, even from a distance.",
  "You know how to make people feel seen.",
  "You've survived every hard day so far. 100% success rate.",
  "Your eyes tell stories your words never could.",
  "You're the kind of person people remember.",
  "You hold yourself to a high standard — and you meet it.",
  "You're fiercely loyal to the people who matter to you.",
  "You have a way of making people feel at home.",
  "You're more beautiful than you believe on your worst days.",
  "You've turned pain into wisdom more than once.",
  "Your presence in a room changes the energy.",
  "You dream big and that's never something to apologize for.",
  "You deserve every good thing coming your way.",
  "The world is genuinely better because you're in it.",
];

const grid = document.getElementById('reasonsGrid');
reasons.forEach((r, i) => {
  const card = document.createElement('div');
  card.className = 'reason-card';
  card.innerHTML = `<span class="reason-num">${String(i + 1).padStart(2, '0')}</span><span class="reason-text">${r}</span>`;
  grid.appendChild(card);
});

// ─── Intersection Observer for scroll animations ──────────────
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.12 });

document.querySelectorAll('.reason-card, .memory-card').forEach(el => observer.observe(el));

// ─── Confetti burst ───────────────────────────────────────────
function launchConfetti(container) {
  const colors = ['#f7a8c4', '#e8729a', '#d4a843', '#f5d98b', '#c0395e', '#fff', '#ffd6e8'];
  for (let i = 0; i < 80; i++) {
    const piece = document.createElement('div');
    const size  = Math.random() * 10 + 5;
    piece.style.cssText = `
      position: absolute;
      width: ${size}px;
      height: ${size}px;
      background: ${colors[Math.floor(Math.random() * colors.length)]};
      border-radius: ${Math.random() > 0.5 ? '50%' : '2px'};
      left: ${Math.random() * 100}%;
      top: ${Math.random() * 40}%;
      animation: confettiFall ${Math.random() * 2 + 1.5}s ease forwards;
      animation-delay: ${Math.random() * 0.5}s;
      opacity: 0.9;
    `;
    container.appendChild(piece);
    setTimeout(() => piece.remove(), 4000);
  }
}

// ─── Celebrate button ─────────────────────────────────────────
const celebrateBtn  = document.getElementById('celebrateBtn');
const confettiBurst = document.getElementById('confettiContainer');

celebrateBtn.addEventListener('click', () => {
  launchConfetti(confettiBurst);
  celebrateBtn.textContent = '🎊 Again!';
  // Burst petals
  for (let i = 0; i < 15; i++) {
    petals.push(createPetal());
  }
});

// ─── Music (Web Audio API — gentle ambient tone) ──────────────
const musicBtn = document.getElementById('musicToggle');
let audioCtx   = null;
let musicNodes = [];
let musicPlaying = false;

function startMusic() {
  if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();

  // Simple gentle chord: C major arpeggio
  const notes = [261.63, 329.63, 392.00, 523.25]; // C4 E4 G4 C5
  musicNodes = notes.map((freq, i) => {
    const osc  = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.type = 'sine';
    osc.frequency.value = freq;
    gain.gain.value = 0;
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.start();

    // Gentle fade in with stagger
    gain.gain.setTargetAtTime(0.04, audioCtx.currentTime + i * 0.3, 0.5);
    return { osc, gain };
  });
  musicPlaying = true;
  musicBtn.classList.add('playing');
  musicBtn.title = 'Pause music';
}

function stopMusic() {
  musicNodes.forEach(({ gain }) => {
    gain.gain.setTargetAtTime(0, audioCtx.currentTime, 0.3);
  });
  setTimeout(() => {
    musicNodes.forEach(({ osc }) => { try { osc.stop(); } catch(e){} });
    musicNodes = [];
  }, 800);
  musicPlaying = false;
  musicBtn.classList.remove('playing');
  musicBtn.title = 'Play music';
}

musicBtn.addEventListener('click', () => {
  if (musicPlaying) {
    stopMusic();
  } else {
    startMusic();
  }
});

// ─── Staggered reason card reveal ────────────────────────────
// Add transition delays to reason cards
document.querySelectorAll('.reason-card').forEach((card, i) => {
  card.style.transitionDelay = `${(i % 6) * 0.07}s`;
});


// ─── Photo Gallery Dynamic Load ──────────────────────────────
const galleryPhotos = [
  'images/0189f8b6-e8c2-426a-80d6-2ebadad5730c.JPG',
  'images/21844c1f-8249-474a-aff2-ed28e1006ace.JPG',
  'images/4cc15f9b-30f8-4dac-acaf-a9e24ad1d752.JPG',
  'images/IMG_0780.PNG',
  'images/IMG_1869.PNG',
  'images/IMG_1954.PNG',
  'images/IMG_3287.PNG',
  'images/IMG_2024.PNG',
  'images/IMG_1960.PNG',
  'images/IMG_1775.PNG'
];

const galleryContainer = document.getElementById('photoGallery');
if (galleryContainer) {
  galleryPhotos.forEach((src, i) => {
    const imgWrapper = document.createElement('div');
    imgWrapper.className = 'gallery-item fade-in-up';
    imgWrapper.style.setProperty('--delay', `${(i % 4) * 0.15}s`);
    
    const img = document.createElement('img');
    img.src = src;
    img.loading = 'lazy';
    img.alt = 'Memory';
    
    imgWrapper.appendChild(img);
    galleryContainer.appendChild(imgWrapper);
    observer.observe(imgWrapper);
  });
}

// ─── Carousel Controls ─────────────────────────────────────────
const carousel = document.getElementById('memoriesCarousel');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');

if (carousel && prevBtn && nextBtn) {
  prevBtn.addEventListener('click', () => {
    carousel.scrollBy({ left: -350, behavior: 'smooth' });
  });
  nextBtn.addEventListener('click', () => {
    carousel.scrollBy({ left: 350, behavior: 'smooth' });
  });
}

// ─── Music Update (Softer Music Box Tone) ──────────────────────
// Replace startMusic with a more emotional progression
function startMusic() {
  if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
  
  // A gentle, emotional chord progression arpeggio
  // Notes: Fmaj9 -> Cmaj9 -> G6 -> Am11
  const sequence = [
    349.23, 440.00, 523.25, 659.25, // F A C E
    261.63, 329.63, 392.00, 587.33, // C E G D
    392.00, 493.88, 587.33, 659.25, // G B D E
    440.00, 523.25, 659.25, 783.99  // A C E G
  ];
  
  let noteIndex = 0;
  
  function playNote() {
    if (!musicPlaying) return;
    const freq = sequence[noteIndex % sequence.length];
    noteIndex++;
    
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    
    osc.type = 'sine'; // soft sine
    osc.frequency.value = freq;
    
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    
    // Attack / Decay
    gain.gain.setValueAtTime(0, audioCtx.currentTime);
    gain.gain.linearRampToValueAtTime(0.08, audioCtx.currentTime + 0.1);
    gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 1.5);
    
    osc.start(audioCtx.currentTime);
    osc.stop(audioCtx.currentTime + 1.6);
    
    musicNodes.push({ osc, gain });
    
    // Clean up old nodes
    if (musicNodes.length > 20) {
      musicNodes.shift();
    }
    
    setTimeout(playNote, 400); // 400ms per note
  }
  
  musicPlaying = true;
  musicBtn.classList.add('playing');
  musicBtn.title = 'Pause music';
  playNote();
}
