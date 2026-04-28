import os

# --- Update index.html ---
with open('index.html', 'r') as f:
    html = f.read()

# Add new font
html = html.replace(
    '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Lato:wght@300;400;700&family=Dancing+Script:wght@400;600;700&family=Caveat:wght@400;700&display=swap" rel="stylesheet" />',
    '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Lato:wght@300;400;700&family=Dancing+Script:wght@400;600;700&family=Caveat:wght@400;700&display=swap" rel="stylesheet" />'
)

with open('index.html', 'w') as f:
    f.write(html)

# --- Update style.css ---
css_content = """
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Lato:wght@300;400;700&family=Dancing+Script:wght@400;600;700&family=Caveat:wght@400;700&display=swap');

/* ===== PREMIUM VARIABLES ===== */
:root {
  --pink: #f9b4cc;
  --pink-dark: #e06c95;
  --rose: #b83359;
  --gold: #d4a843;
  --gold-light: #fbe6a8;
  --cream: #fdfaf7;
  --dark: #1f1218;
  --text: #3d2430;
  
  /* Glassmorphism */
  --glass-bg: rgba(255, 255, 255, 0.45);
  --glass-border: rgba(255, 255, 255, 0.7);
  --glass-shadow: 0 12px 40px 0 rgba(184, 51, 89, 0.08);
  --glass-blur: blur(16px);
}

/* ===== RESET & BASE ===== */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; font-size: 16px; }
body {
  font-family: 'Lato', sans-serif;
  background: var(--cream);
  color: var(--text);
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
}

/* Base styles for components */
.container { max-width: 1100px; margin: 0 auto; padding: 0 1.5rem; }
.container-center { max-width: 800px; margin: 0 auto; padding: 0 1.5rem; text-align: center; }
.hidden { display: none !important; }
.gold-text { color: var(--gold); }

/* Typography */
h1, h2, h3, .section-title { font-family: 'Cormorant Garamond', serif; }
.section-title {
  font-size: clamp(2.5rem, 5vw, 4rem);
  color: var(--rose);
  margin-bottom: 1rem;
  text-align: center;
  font-weight: 600;
  letter-spacing: -0.5px;
}
.section-subtitle {
  text-align: center;
  color: var(--pink-dark);
  font-size: clamp(1.1rem, 2vw, 1.3rem);
  margin-bottom: 4rem;
  font-weight: 300;
  font-style: italic;
  font-family: 'Playfair Display', serif;
}

/* Animations */
.fade-in-up {
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 1s cubic-bezier(0.25, 1, 0.5, 1), transform 1s cubic-bezier(0.25, 1, 0.5, 1);
  transition-delay: var(--delay, 0s);
}
.fade-in-up.visible { opacity: 1; transform: translateY(0); }
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
@keyframes heartBeat { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.15); } }
@keyframes float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-15px); } }
@keyframes pulseGlow { 0%, 100% { opacity: 0.5; } 50% { opacity: 1; } }
@keyframes bounce { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(10px); } }
@keyframes fadeUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }

/* ===== CANVAS & PROGRESS ===== */
#petals { position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 0; }
.progress-bar { position: fixed; top: 0; left: 0; height: 4px; background: linear-gradient(90deg, var(--pink-dark), var(--gold)); width: 0%; z-index: 1000; transition: width 0.3s ease; }

/* ===== SECTIONS ===== */
.section { position: relative; min-height: 100vh; padding: 7rem 0; z-index: 1; }

/* Section 1: Hero */
.hero {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #fdfaf7 0%, #ffe9f0 50%, #fdfaf7 100%);
  position: relative;
  overflow: hidden;
}
.hero::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 80% 20%, rgba(249,180,204,0.3) 0%, transparent 50%),
              radial-gradient(circle at 20% 80%, rgba(212,168,67,0.15) 0%, transparent 50%);
  animation: pulseGlow 10s ease-in-out infinite;
}
.hero-inner { text-align: center; position: relative; z-index: 2; }
.heart-beat { font-size: 7rem; animation: heartBeat 1.8s ease-in-out infinite; cursor: pointer; transition: transform 0.3s; user-select: none; text-shadow: 0 0 40px rgba(224,108,149,0.6); }
.heart-beat:hover { transform: scale(1.2) rotate(-5deg); }
.tap-message { font-family: 'Dancing Script', cursive; font-size: 1.8rem; color: var(--rose); margin-top: 1.5rem; opacity: 0.8; }

/* Section 2: Title Reveal */
.title-reveal {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(180deg, #ffe9f0 0%, #fdfaf7 100%);
  position: relative;
}
.subtitle { font-family: 'Caveat', cursive; font-size: 2rem; color: var(--pink-dark); margin-bottom: 1.5rem; animation: fadeUp 1s ease 0.3s both; }
.main-title { font-family: 'Cormorant Garamond', serif; font-size: clamp(4rem, 12vw, 8rem); line-height: 1.1; color: var(--rose); text-shadow: 0 10px 40px rgba(184,51,89,0.15); animation: fadeUp 1s ease 0.6s both; }
.name-reveal { font-family: 'Dancing Script', cursive; font-size: clamp(2.5rem, 6vw, 4.5rem); color: var(--gold); margin-top: 2.5rem; animation: fadeUp 1s ease 0.9s both; }
.scroll-indicator { margin-top: 5rem; animation: fadeUp 1s ease 1.2s both; display: flex; flex-direction: column; align-items: center; }
.scroll-indicator span { font-size: 0.8rem; letter-spacing: 0.2em; text-transform: uppercase; color: var(--pink-dark); margin-bottom: 0.5rem; }
.scroll-arrow { font-size: 1.5rem; color: var(--pink-dark); animation: bounce 2s ease-in-out infinite; }

/* Glass Card Mixin */
.glass-card {
  background: var(--glass-bg);
  backdrop-filter: var(--glass-blur);
  -webkit-backdrop-filter: var(--glass-blur);
  border: 1px solid var(--glass-border);
  box-shadow: var(--glass-shadow);
  border-radius: 28px;
  position: relative;
  overflow: hidden;
}
.glass-card::before {
  content: ''; position: absolute; inset: 0;
  background: linear-gradient(135deg, rgba(255,255,255,0.4) 0%, rgba(255,255,255,0) 100%);
  pointer-events: none;
}

/* Section 3: Letter Section */
.letter-section { background: var(--cream); display: flex; align-items: center; }
.letter-card {
  padding: clamp(3rem, 6vw, 5rem);
  max-width: 800px;
  margin: 0 auto;
}
.letter-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 3rem; padding-bottom: 1.5rem; border-bottom: 1px solid rgba(224,108,149,0.2); position: relative; z-index: 2; }
.letter-date { font-size: 0.9rem; color: var(--pink-dark); letter-spacing: 0.15em; text-transform: uppercase; }
.letter-icon { font-size: 2.5rem; }
.letter-greeting { font-family: 'Playfair Display', serif; font-style: italic; font-size: 1.8rem; color: var(--rose); margin-bottom: 2rem; position: relative; z-index: 2; }
.letter-text { font-size: 1.15rem; line-height: 2; color: var(--text); margin-bottom: 1.5rem; font-weight: 300; position: relative; z-index: 2; }
.highlight-text { background: linear-gradient(135deg, rgba(249,180,204,0.1), rgba(249,180,204,0.05)); border-left: 3px solid var(--pink-dark); padding: 2rem; border-radius: 0 16px 16px 0; font-style: italic; color: var(--rose); margin: 2.5rem 0; font-family: 'Playfair Display', serif; font-size: 1.25rem; }
.letter-signature { margin-top: 4rem; font-family: 'Dancing Script', cursive; font-size: 2rem; color: var(--pink-dark); line-height: 1.5; position: relative; z-index: 2; }

/* Section 4: Qualities */
.about-section { background: linear-gradient(180deg, var(--cream) 0%, #fff 100%); }
.qualities-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2.5rem; }
.quality-card { padding: 3rem 2rem; text-align: center; transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.4s ease; }
.quality-card:hover { transform: translateY(-15px); box-shadow: 0 20px 50px rgba(184,51,89,0.12); border-color: rgba(255,255,255,0.9); }
.quality-icon { font-size: 3.5rem; margin-bottom: 1.5rem; animation: float 6s ease-in-out infinite; display: inline-block; }
.quality-card:nth-child(even) .quality-icon { animation-delay: -3s; }
.quality-card h3 { font-size: 1.8rem; color: var(--rose); margin-bottom: 1rem; }
.quality-card p { font-size: 1.05rem; line-height: 1.8; color: var(--text); font-weight: 300; }

/* Section 5: Gallery */
.gallery-section { background: #fff; }
.photo-gallery {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 2rem;
  padding: 1rem;
}
.gallery-item {
  position: relative;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: var(--glass-shadow);
  aspect-ratio: 3/4;
  cursor: pointer;
}
.gallery-item::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(184,51,89,0.4), transparent 50%);
  opacity: 0;
  transition: opacity 0.4s ease;
}
.gallery-item:hover::after { opacity: 1; }
.gallery-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.7s cubic-bezier(0.25, 1, 0.5, 1);
}
.gallery-item:hover img { transform: scale(1.08); }
.gallery-note { text-align: center; margin-top: 4rem; font-family: 'Playfair Display', serif; font-style: italic; font-size: 1.3rem; color: var(--pink-dark); }

/* Section 6: Timeline */
.timeline-section { background: linear-gradient(180deg, #fff 0%, var(--cream) 100%); }
.timeline { position: relative; max-width: 800px; margin: 0 auto; padding-left: 2rem; }
.timeline::before { content: ''; position: absolute; left: 0; top: 0; bottom: 0; width: 2px; background: linear-gradient(to bottom, var(--pink-dark), var(--gold-light)); }
.timeline-item { position: relative; margin-bottom: 4rem; padding-left: 3rem; }
.timeline-item:last-child { margin-bottom: 0; }
.timeline-marker { position: absolute; left: -14px; top: 0; width: 30px; height: 30px; background: #fff; border: 2px solid var(--pink-dark); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1rem; box-shadow: 0 0 15px rgba(224,108,149,0.3); z-index: 2; }
.timeline-content { background: var(--glass-bg); backdrop-filter: var(--glass-blur); -webkit-backdrop-filter: var(--glass-blur); border: 1px solid var(--glass-border); border-radius: 20px; padding: 2rem; box-shadow: var(--glass-shadow); transition: transform 0.3s ease; }
.timeline-content:hover { transform: translateX(10px); }
.timeline-content h3 { font-size: 1.6rem; color: var(--rose); margin-bottom: 0.8rem; }
.timeline-content p { font-size: 1.05rem; line-height: 1.7; font-weight: 300; }

/* Section 7: Cake */
.cake-section { background: var(--cream); position: relative; }
.cake-wrapper { position: relative; margin: 4rem auto; width: 280px; height: 300px; }
.cake { position: absolute; bottom: 0; width: 100%; display: flex; flex-direction: column; align-items: center; }
.cake-layer { background: linear-gradient(to right, #ffe1eb, #ffc2d6, #ffe1eb); border-radius: 10px; position: relative; border: 2px solid #fff; box-shadow: inset 0 -10px 20px rgba(0,0,0,0.05); }
.cake-bottom { width: 260px; height: 80px; z-index: 1; }
.cake-mid { width: 220px; height: 70px; margin-bottom: -10px; z-index: 2; }
.cake-top { width: 180px; height: 60px; margin-bottom: -10px; z-index: 3; display: flex; align-items: center; justify-content: center; }
.cake-plate { width: 320px; height: 15px; background: #e0e0e0; border-radius: 50%; position: absolute; bottom: -7px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); }
.cake-decoration { font-family: 'Playfair Display', serif; font-weight: 700; color: var(--rose); font-size: 1.5rem; }
.candles-row { position: absolute; top: 50px; left: 50%; transform: translateX(-50%); display: flex; gap: 15px; z-index: 4; }
.candle { width: 12px; height: 40px; position: relative; }
.candle-body { width: 100%; height: 100%; background: repeating-linear-gradient(45deg, #fff, #fff 4px, var(--pink-dark) 4px, var(--pink-dark) 8px); border-radius: 4px; box-shadow: 1px 1px 3px rgba(0,0,0,0.2); }
.candle-flame { position: absolute; top: -20px; left: 50%; transform: translateX(-50%); width: 14px; height: 22px; background: #ffdf00; border-radius: 50% 50% 20% 20%; box-shadow: 0 0 15px #ffdf00, 0 0 30px #ff9d00; animation: flicker 0.5s infinite alternate; transition: opacity 0.5s ease; }
@keyframes flicker { 0% { transform: translateX(-50%) scale(1); opacity: 0.9; } 100% { transform: translateX(-50%) scale(1.1); opacity: 1; } }
.btn-primary { background: linear-gradient(135deg, var(--rose), var(--pink-dark)); color: #fff; border: none; padding: 1.2rem 2.5rem; font-family: 'Lato', sans-serif; font-size: 1.1rem; font-weight: 700; border-radius: 50px; cursor: pointer; box-shadow: 0 10px 20px rgba(184,51,89,0.3); transition: all 0.3s ease; letter-spacing: 1px; text-transform: uppercase; margin-top: 2rem; }
.btn-primary:hover { transform: translateY(-3px); box-shadow: 0 15px 25px rgba(184,51,89,0.4); }
.wish-message { min-height: 30px; margin-top: 1.5rem; font-family: 'Dancing Script', cursive; font-size: 1.8rem; color: var(--gold); opacity: 0; transition: opacity 0.5s ease; }
.wish-message.show { opacity: 1; }

/* Section 8: Reasons */
.reasons-section { background: linear-gradient(180deg, var(--cream) 0%, #fff9fb 100%); }
.reasons-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; }
.reason-card { background: var(--glass-bg); backdrop-filter: var(--glass-blur); -webkit-backdrop-filter: var(--glass-blur); border: 1px solid var(--glass-border); border-radius: 16px; padding: 1.5rem; display: flex; align-items: flex-start; gap: 1rem; box-shadow: var(--glass-shadow); transition: transform 0.3s ease; }
.reason-card:hover { transform: translateY(-5px); border-color: var(--pink-dark); }
.reason-num { font-family: 'Playfair Display', serif; font-size: 1.5rem; font-weight: 700; color: var(--gold); opacity: 0.6; }
.reason-text { font-size: 1.05rem; line-height: 1.6; font-weight: 400; color: var(--text); padding-top: 0.2rem; }

/* Section 9: Memories Carousel */
.memories-section { background: #fff9fb; overflow: hidden; }
.memories-carousel { display: flex; gap: 2rem; overflow-x: auto; padding: 2rem 1rem 4rem; scroll-snap-type: x mandatory; scrollbar-width: none; }
.memories-carousel::-webkit-scrollbar { display: none; }
.memory-slide { min-width: 300px; max-width: 400px; scroll-snap-align: center; background: var(--glass-bg); backdrop-filter: var(--glass-blur); -webkit-backdrop-filter: var(--glass-blur); border: 1px solid var(--glass-border); border-radius: 24px; padding: 3rem 2rem; text-align: center; box-shadow: var(--glass-shadow); }
.memory-icon { font-size: 3rem; margin-bottom: 1.5rem; }
.memory-slide p { font-size: 1.1rem; line-height: 1.8; font-weight: 300; }
.carousel-controls { display: flex; justify-content: center; gap: 1rem; margin-top: -2rem; }
.carousel-btn { width: 50px; height: 50px; border-radius: 50%; background: #fff; border: 1px solid var(--glass-border); box-shadow: var(--glass-shadow); cursor: pointer; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; color: var(--rose); transition: all 0.3s ease; }
.carousel-btn:hover { background: var(--rose); color: #fff; }

/* Section 10: Forgiveness */
.forgiveness-section { background: linear-gradient(180deg, #fff9fb 0%, var(--cream) 100%); }
.forgiveness-card { background: rgba(255,255,255,0.7); backdrop-filter: var(--glass-blur); border-radius: 30px; padding: clamp(3rem, 6vw, 5rem); text-align: center; box-shadow: 0 20px 60px rgba(184,51,89,0.1); border: 1px solid rgba(255,255,255,0.8); max-width: 800px; margin: 0 auto; position: relative; }
.forgiveness-icon { font-size: 4rem; margin-bottom: 2rem; animation: float 5s ease-in-out infinite; }
.forgiveness-card h2 { font-size: 2.5rem; color: var(--rose); margin-bottom: 2rem; }
.forgiveness-card p { font-size: 1.15rem; line-height: 1.9; color: var(--text); margin-bottom: 1.5rem; font-weight: 300; }
.emphasis-text { font-family: 'Playfair Display', serif; font-size: 1.4rem !important; font-style: italic; color: var(--rose) !important; padding: 2rem 0; font-weight: 400 !important; }
.final-apology { font-family: 'Caveat', cursive; font-size: 2rem !important; color: var(--pink-dark) !important; margin-top: 3rem !important; }

/* Section 11: Wishes */
.wishes-section { background: var(--cream); }
.wishes-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem; }
.wish-card { background: #fff; border-radius: 20px; padding: 2.5rem 2rem; position: relative; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.03); transition: transform 0.3s ease; border: 1px solid rgba(249,180,204,0.2); }
.wish-card:hover { transform: translateY(-10px); box-shadow: 0 20px 40px rgba(184,51,89,0.08); }
.wish-number { position: absolute; top: -15px; right: 10px; font-family: 'Playfair Display', serif; font-size: 6rem; font-weight: 700; color: var(--cream); z-index: 0; pointer-events: none; }
.wish-card p { position: relative; z-index: 1; font-size: 1.1rem; line-height: 1.7; font-weight: 300; }

/* Section 12: Charity */
.charity-section { background: linear-gradient(180deg, var(--cream) 0%, #fff 100%); }
.charity-content { background: var(--glass-bg); backdrop-filter: var(--glass-blur); border-radius: 30px; padding: clamp(2rem, 5vw, 4rem); box-shadow: var(--glass-shadow); border: 1px solid var(--glass-border); }
.charity-icon { font-size: 3.5rem; text-align: center; margin-bottom: 1rem; }
.charity-title { text-align: center; font-size: 2.5rem; color: var(--gold); margin-bottom: 2rem; }
.charity-intro { font-size: 1.25rem; text-align: center; font-style: italic; color: var(--rose); margin-bottom: 2rem; font-family: 'Playfair Display', serif; }
.charity-text { font-size: 1.1rem; line-height: 1.8; margin-bottom: 1.5rem; font-weight: 300; }
.charity-quote { text-align: center; margin: 3rem 0; padding: 2rem; border-top: 1px solid rgba(212,168,67,0.3); border-bottom: 1px solid rgba(212,168,67,0.3); }
.charity-quote p { font-family: 'Playfair Display', serif; font-size: 1.6rem; font-style: italic; color: var(--rose); margin-bottom: 1rem; }
.charity-quote span { font-size: 1rem; color: var(--gold); text-transform: uppercase; letter-spacing: 2px; }
.charity-ideas h3 { font-size: 1.5rem; color: var(--rose); margin-bottom: 1.5rem; margin-top: 3rem; }
.charity-ideas ul { list-style: none; display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; }
.charity-ideas li { background: rgba(255,255,255,0.6); padding: 1rem 1.5rem; border-radius: 12px; font-size: 1.05rem; display: flex; align-items: center; gap: 10px; transition: transform 0.2s ease; }
.charity-ideas li:hover { transform: translateX(5px); background: #fff; box-shadow: 0 5px 15px rgba(0,0,0,0.05); }
.charity-closing { text-align: center; margin-top: 3rem; font-size: 1.15rem; line-height: 1.8; font-weight: 300; }
.charity-cta { text-align: center; margin-top: 3rem; }
.charity-cta-text { font-family: 'Dancing Script', cursive; font-size: 2.5rem; color: var(--gold); }

/* Section 13: Final */
.final-section { min-height: 80vh; display: flex; align-items: center; justify-content: center; background: linear-gradient(135deg, #fff 0%, #ffe9f0 100%); text-align: center; position: relative; overflow: hidden; }
.balloons-container { display: flex; justify-content: center; gap: 1rem; margin-bottom: 2rem; }
.balloon { font-size: 3rem; animation: float 4s ease-in-out infinite; animation-delay: var(--delay); }
.final-title { font-size: 4rem; color: var(--rose); margin-bottom: 1.5rem; }
.final-text { font-size: 1.2rem; line-height: 1.8; max-width: 600px; margin: 0 auto 1.5rem; font-weight: 300; }
.final-wish { font-family: 'Dancing Script', cursive; font-size: 3.5rem; color: var(--gold); margin: 3rem 0; }
.btn-celebrate { background: linear-gradient(135deg, var(--gold), #f3c25b); color: #fff; border: none; padding: 1.2rem 3rem; font-size: 1.2rem; font-weight: 700; border-radius: 50px; cursor: pointer; box-shadow: 0 10px 20px rgba(212,168,67,0.3); transition: all 0.3s ease; text-transform: uppercase; letter-spacing: 2px; position: relative; z-index: 10; }
.btn-celebrate:hover { transform: translateY(-5px); box-shadow: 0 15px 30px rgba(212,168,67,0.5); }
.confetti-container { position: absolute; inset: 0; pointer-events: none; z-index: 1; }

/* Music Toggle */
.music-toggle { position: fixed; bottom: 30px; right: 30px; width: 60px; height: 60px; border-radius: 50%; background: var(--glass-bg); backdrop-filter: var(--glass-blur); border: 1px solid var(--glass-border); box-shadow: 0 10px 25px rgba(0,0,0,0.1); display: flex; align-items: center; justify-content: center; font-size: 1.5rem; cursor: pointer; z-index: 1000; transition: all 0.3s ease; color: var(--rose); }
.music-toggle:hover { transform: scale(1.1); background: #fff; }
.music-toggle.playing { background: var(--rose); color: #fff; animation: pulseGlow 2s infinite; }

/* Responsive */
@media (max-width: 768px) {
  .heart-beat { font-size: 5rem; }
  .section { padding: 4rem 0; }
  .letter-card, .forgiveness-card { padding: 2rem; }
  .quality-card { padding: 2rem 1.5rem; }
  .timeline::before { left: 20px; }
  .timeline-item { padding-left: 50px; }
  .timeline-marker { left: 5px; }
  .music-toggle { bottom: 20px; right: 20px; width: 50px; height: 50px; font-size: 1.2rem; }
}

/* Fix for reason card loop */
.reason-card { animation: fadeUp 0.8s ease forwards; opacity: 0; }
"""

with open('style.css', 'w') as f:
    f.write(css_content)

# --- Update script.js ---
script_additions = """
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
"""

with open('script.js', 'r') as f:
    script = f.read()

# Replace the button id since it's `musicToggle` in index.html, not `musicBtn`
script = script.replace("const musicBtn = document.getElementById('musicBtn');", "const musicBtn = document.getElementById('musicToggle');")

# Fix button initialization
script = script.replace("document.getElementById('musicBtn')", "document.getElementById('musicToggle')")

# Append new logic
with open('script.js', 'w') as f:
    f.write(script + "\n" + script_additions)
