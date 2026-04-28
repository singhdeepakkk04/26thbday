/* ============================================================
   BIRTHDAY WEBSITE — script.js
   26th Birthday Edition - Premium Ethereal Theme
============================================================ */

// ─── Scroll Progress & Reveal ────────────────────────────────
const progressBar = document.getElementById('progressBar');
const revealElements = document.querySelectorAll('.reveal-up');

window.addEventListener('scroll', () => {
  // Progress Bar
  const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
  const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  const scrolled = (winScroll / height) * 100;
  progressBar.style.width = scrolled + '%';
});

const observerOptions = { threshold: 0.1, rootMargin: '0px 0px -50px 0px' };
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, observerOptions);

revealElements.forEach(el => observer.observe(el));

// ─── Falling Particles (Ambient) ─────────────────────────────
const canvas = document.getElementById('particles');
const ctx = canvas.getContext('2d');
let particlesArray = [];

function resizeCanvas() {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
}
window.addEventListener('resize', resizeCanvas);
resizeCanvas();

class Particle {
  constructor() {
    this.x = Math.random() * canvas.width;
    this.y = Math.random() * canvas.height;
    this.size = Math.random() * 2 + 0.5;
    this.speedY = Math.random() * 0.5 + 0.1;
    this.speedX = (Math.random() - 0.5) * 0.5;
    this.opacity = Math.random() * 0.5 + 0.1;
  }
  update() {
    this.y -= this.speedY; // float upwards
    this.x += this.speedX;
    if (this.y < 0) {
      this.y = canvas.height;
      this.x = Math.random() * canvas.width;
    }
  }
  draw() {
    ctx.fillStyle = `rgba(212, 168, 67, ${this.opacity})`; // Gold particles
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
    ctx.fill();
  }
}

function initParticles() {
  particlesArray = [];
  for (let i = 0; i < 100; i++) {
    particlesArray.push(new Particle());
  }
}

function animateParticles() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  for (let i = 0; i < particlesArray.length; i++) {
    particlesArray[i].update();
    particlesArray[i].draw();
  }
  requestAnimationFrame(animateParticles);
}
initParticles();
animateParticles();

// ─── Massive Parallax Gallery ────────────────────────────────
const parallaxContainer = document.getElementById('parallaxContainer');
const imagesFolder = 'images/';
// Array of a rich selection of images from the directory
const allImages = [
  "0189f8b6-e8c2-426a-80d6-2ebadad5730c.JPG",
  "08a17a9c-5b56-4020-bdd1-91a900808f08.JPG",
  "21844c1f-8249-474a-aff2-ed28e1006ace.JPG",
  "274aa410-92af-4b5e-86ca-297ac790cb9e.JPG",
  "2ce97c33-71bd-4bfc-ac77-f754c75f78aa.JPG",
  "399d8af8-f766-4b6f-b82d-54fb90b6a71c.JPG",
  "413d4bcf-103f-43cf-bdcb-f280f144db78.JPG",
  "436bd4a9-7eed-43a1-8e6f-cf742794d62c.JPG",
  "4a77b92d-951a-4eb2-b593-b6aac7ef9a92.JPG",
  "4b161adc-d94c-4ce6-b1d1-45d4c586b730.JPG",
  "4cc15f9b-30f8-4dac-acaf-a9e24ad1d752.JPG",
  "537efc20-1255-44d8-bd03-ddebe1171e1b.JPG",
  "6350c719-4730-469f-86eb-6c115ea39f82.JPG",
  "64b24dba-359b-4bc5-92a9-1aaa6014d9b3.JPG",
  "66431683-f6c3-46dc-8cb9-df22d0aad66f.JPG",
  "6f332d2e-9883-473d-8911-15c1aa47a0ae.JPG",
  "71aaf7d9-4d1d-4fbd-a062-ba80988734ec.JPG",
  "7d7ef225-7949-4847-b5cf-3c37b555cf1c.JPG",
  "80bc8888-c50b-4605-a28a-63159c6dd5f1.JPG",
  "8817e605-7040-4d61-9725-62b791b42c97.JPG",
  "96204cb8-d0f4-4178-a011-9f3475ce9c00.JPG",
  "9f36900a-6f40-4e15-8846-115985f8cb50.JPG",
  "F6BACE20-E545-4A7D-A121-CF02DB186255.JPG",
  "IMG_0780.PNG",
  "IMG_0903.PNG",
  "IMG_1775.PNG",
  "IMG_1777.PNG",
  "IMG_1856.PNG",
  "IMG_1869.PNG",
  "IMG_1954.PNG",
  "IMG_1960.PNG",
  "IMG_1961.PNG",
  "IMG_1962.PNG",
  "IMG_2024.PNG",
  "IMG_3287.PNG",
  "Screenshot 2024-10-16 at 12.03.07 AM.PNG",
  "Screenshot 2024-10-24 at 11.27.50 PM.PNG",
  "Screenshot 2024-10-25 at 1.11.33 AM.PNG",
  "aa7406b0-b49c-48e9-807e-e975f7e90d2d.JPG",
  "b2e11f42-f757-4a69-83bf-108d08be10aa.JPG",
  "be00fc6b-f633-47f0-b3b7-38463199ac4c.JPG",
  "c81564ea-c0f0-402b-95cd-2ce5a6a2249d.JPG",
  "da93167e-1a68-4847-970f-f87c5f38a212.JPG",
  "e32e1a77-2ac9-431b-87dd-2310f6a235ca.JPG",
  "e3d6ed9b-8f88-438a-a510-1f98678d21c5.JPG",
  "ede10bac-34bf-4e2b-b59e-744cace260ce.JPG"
];

// Shuffle images for a dynamic feel
allImages.sort(() => Math.random() - 0.5);

if (parallaxContainer) {
  allImages.forEach((imgSrc, i) => {
    // Determine random positions and sizes
    const size = Math.random() * 15 + 15; // 15vw to 30vw
    const top = Math.random() * 90; // 0% to 90% top of the massive container
    const left = Math.random() * 80; // 0% to 80% left
    const speed = Math.random() * 0.5 + 0.1; // Parallax speed multiplier
    
    const div = document.createElement('div');
    div.className = 'parallax-item';
    div.style.width = `${size}vw`;
    div.style.height = `${size * 1.2}vw`; // slightly taller than wide
    div.style.top = `${top}%`;
    div.style.left = `${left}%`;
    div.dataset.speed = speed;
    
    const img = document.createElement('img');
    img.src = `${imagesFolder}${imgSrc}`;
    img.loading = 'lazy';
    
    div.appendChild(img);
    parallaxContainer.appendChild(div);
  });

  // Parallax Scroll Effect
  window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;
    const containerTop = parallaxContainer.offsetTop;
    const containerHeight = parallaxContainer.offsetHeight;
    
    // Only animate if in view
    if (scrollY + window.innerHeight > containerTop && scrollY < containerTop + containerHeight) {
      const items = document.querySelectorAll('.parallax-item');
      items.forEach(item => {
        const speed = parseFloat(item.dataset.speed);
        // Move opposite to scroll direction
        const yPos = -(scrollY * speed);
        item.style.transform = `translate3d(0, ${yPos}px, 0)`;
      });
    }
  });
}

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
  "The world is genuinely better because you're in it."
];

const reasonsList = document.getElementById('reasonsList');
if (reasonsList) {
  reasons.forEach((r, i) => {
    const card = document.createElement('div');
    card.className = 'r-card glass-card reveal-up';
    card.style.setProperty('--d', `${(i % 5) * 0.1}s`);
    card.innerHTML = `<span class="r-num">${String(i + 1).padStart(2, '0')}</span><span class="r-text">${r}</span>`;
    reasonsList.appendChild(card);
    observer.observe(card);
  });
}

// ─── Memories Carousel ───────────────────────────────────────
const memTrack = document.getElementById('memTrack');
const memPrev = document.getElementById('memPrev');
const memNext = document.getElementById('memNext');

if (memTrack && memPrev && memNext) {
  memPrev.addEventListener('click', () => {
    memTrack.scrollBy({ left: -350, behavior: 'smooth' });
  });
  memNext.addEventListener('click', () => {
    memTrack.scrollBy({ left: 350, behavior: 'smooth' });
  });
}

// ─── Candles & Cake ──────────────────────────────────────────
const cakeFlames = document.getElementById('cakeFlames');
const NUM_CANDLES = 6;
let candlesLit = true;

if (cakeFlames) {
  for (let i = 0; i < NUM_CANDLES; i++) {
    const div = document.createElement('div');
    div.className = 'candle';
    div.innerHTML = `<div class="flame" id="flame-${i}"></div>`;
    cakeFlames.appendChild(div);
  }
}

const blowBtn = document.getElementById('blowBtn');
const wishText = document.getElementById('wishText');

if (blowBtn) {
  blowBtn.addEventListener('click', () => {
    if (!candlesLit) {
      // Relight
      for (let i = 0; i < NUM_CANDLES; i++) {
        document.getElementById(`flame-${i}`).style.display = 'block';
      }
      candlesLit = true;
      blowBtn.textContent = '🎂 Blow the Candles';
      wishText.classList.remove('show');
      return;
    }

    // Blow out one by one
    for (let i = 0; i < NUM_CANDLES; i++) {
      setTimeout(() => {
        document.getElementById(`flame-${i}`).style.display = 'none';
        if (i === NUM_CANDLES - 1) {
          setTimeout(() => {
            wishText.textContent = '🌟 Your wish has been sent to the universe 🌟';
            wishText.classList.add('show');
            blowBtn.textContent = '🕯️ Relight Candles';
            candlesLit = false;
          }, 400);
        }
      }, i * 150);
    }
  });
}

// ─── Confetti ────────────────────────────────────────────────
function launchConfetti() {
  const container = document.getElementById('confettiZone');
  if (!container) return;
  const colors = ['#d4a843', '#fbe6a8', '#b83359', '#f9b4cc', '#ffffff'];
  
  for (let i = 0; i < 100; i++) {
    const piece = document.createElement('div');
    const size = Math.random() * 10 + 5;
    piece.style.cssText = `
      position: absolute;
      width: ${size}px;
      height: ${size}px;
      background: ${colors[Math.floor(Math.random() * colors.length)]};
      border-radius: ${Math.random() > 0.5 ? '50%' : '2px'};
      left: 50%;
      top: 100%;
      transform: translate(-50%, -50%);
      box-shadow: 0 0 10px rgba(255,255,255,0.5);
      animation: explode ${Math.random() * 1 + 1}s ease-out forwards;
      animation-delay: ${Math.random() * 0.2}s;
    `;
    
    // Custom animation injected
    const x = (Math.random() - 0.5) * window.innerWidth;
    const y = -(Math.random() * window.innerHeight);
    const rot = Math.random() * 720;
    
    piece.animate([
      { transform: 'translate(-50%, -50%) rotate(0deg)', opacity: 1 },
      { transform: `translate(${x}px, ${y}px) rotate(${rot}deg)`, opacity: 0 }
    ], {
      duration: Math.random() * 1000 + 1500,
      easing: 'cubic-bezier(0.2, 0.8, 0.2, 1)',
      fill: 'forwards',
      delay: Math.random() * 200
    });
    
    container.appendChild(piece);
    setTimeout(() => piece.remove(), 3000);
  }
}

const celebrateBtn = document.getElementById('celebrateBtn');
if (celebrateBtn) {
  celebrateBtn.addEventListener('click', () => {
    launchConfetti();
  });
}

// ─── Web Audio API (Ethereal Ambient Music) ──────────────────
const musicBtn = document.getElementById('musicBtn');
let audioCtx = null;
let musicNodes = [];
let musicPlaying = false;

function startMusic() {
  if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
  
  // A gentle, emotional chord progression arpeggio fitting the dark ethereal theme
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
    
    // Sine wave for soft, pure, ethereal tone
    osc.type = 'sine';
    osc.frequency.value = freq;
    
    // Add a bit of reverb illusion by extending release
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    
    const now = audioCtx.currentTime;
    gain.gain.setValueAtTime(0, now);
    gain.gain.linearRampToValueAtTime(0.08, now + 0.2); // softer attack
    gain.gain.exponentialRampToValueAtTime(0.001, now + 2.5); // long release
    
    osc.start(now);
    osc.stop(now + 2.6);
    
    musicNodes.push({ osc, gain });
    if (musicNodes.length > 20) musicNodes.shift();
    
    setTimeout(playNote, 600); // Slower, more deliberate pacing
  }
  
  musicPlaying = true;
  musicBtn.classList.add('playing');
  musicBtn.title = 'Pause music';
  playNote();
}

function stopMusic() {
  musicNodes.forEach(({ gain }) => {
    gain.gain.setTargetAtTime(0, audioCtx.currentTime, 0.5);
  });
  setTimeout(() => {
    musicNodes.forEach(({ osc }) => { try { osc.stop(); } catch(e){} });
    musicNodes = [];
  }, 1000);
  musicPlaying = false;
  musicBtn.classList.remove('playing');
  musicBtn.title = 'Play music';
}

if (musicBtn) {
  musicBtn.addEventListener('click', () => {
    if (musicPlaying) stopMusic();
    else startMusic();
  });
}
