/**
 * OPTOGENETICS YUKKURI-STYLE SLIDE & VISUAL LABORATORY
 * The 2026 Nobel Prize in Physiology or Medicine
 * High-performance Vanilla Canvas2D & Web Audio Architecture
 */

// ==========================================
// 1. SOUND SYNTHESIS ENGINE (Web Audio API)
// ==========================================
class SoundEngine {
  constructor() {
    this.ctx = null;
    this.isMuted = false;
  }

  init() {
    if (this.ctx) return;
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    this.ctx = new AudioContext();
  }

  toggleMute() {
    this.init();
    if (this.ctx && this.ctx.state === 'suspended') {
      this.ctx.resume();
    }
    this.isMuted = !this.isMuted;
    return this.isMuted;
  }

  // Yukkuri speech pop
  playPop() {
    if (this.isMuted) return;
    this.init();
    try {
      const now = this.ctx.currentTime;
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();

      osc.type = 'sine';
      osc.frequency.setValueAtTime(580, now);
      osc.frequency.exponentialRampToValueAtTime(880, now + 0.05);

      gain.gain.setValueAtTime(0.08, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.05);

      osc.connect(gain);
      gain.connect(this.ctx.destination);

      osc.start(now);
      osc.stop(now + 0.06);
    } catch (e) {}
  }

  // Laser beam shot
  playLaser(isBlue = true) {
    if (this.isMuted) return;
    this.init();
    try {
      const now = this.ctx.currentTime;
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();

      osc.type = isBlue ? 'sawtooth' : 'sine';
      osc.frequency.setValueAtTime(isBlue ? 1200 : 550, now);
      osc.frequency.exponentialRampToValueAtTime(isBlue ? 200 : 120, now + 0.12);

      gain.gain.setValueAtTime(0.12, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.12);

      osc.connect(gain);
      gain.connect(this.ctx.destination);

      osc.start(now);
      osc.stop(now + 0.13);
    } catch (e) {}
  }

  // Action potential spike
  playSpike() {
    if (this.isMuted) return;
    this.init();
    try {
      const now = this.ctx.currentTime;
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();

      osc.type = 'triangle';
      osc.frequency.setValueAtTime(2400, now);
      osc.frequency.exponentialRampToValueAtTime(200, now + 0.04);

      gain.gain.setValueAtTime(0.1, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.04);

      osc.connect(gain);
      gain.connect(this.ctx.destination);

      osc.start(now);
      osc.stop(now + 0.05);
    } catch (e) {}
  }

  // Eureka chime
  playChime() {
    if (this.isMuted) return;
    this.init();
    try {
      const now = this.ctx.currentTime;
      [523.25, 659.25, 783.99, 1046.50].forEach((f, i) => {
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(f, now + i * 0.05);

        gain.gain.setValueAtTime(0.06, now + i * 0.05);
        gain.gain.exponentialRampToValueAtTime(0.001, now + i * 0.05 + 0.22);

        osc.connect(gain);
        gain.connect(this.ctx.destination);

        osc.start(now + i * 0.05);
        osc.stop(now + i * 0.05 + 0.24);
      });
    } catch (e) {}
  }
}

const sound = new SoundEngine();

// ==========================================
// 2. BACKGROUND CANVAS: FLOATING SYNAPSES
// ==========================================
class BackgroundNetwork {
  constructor(canvasId) {
    this.canvas = document.getElementById(canvasId);
    this.ctx = this.canvas.getContext('2d');
    this.nodes = [];
    this.resize();
    this.initNodes();
  }

  resize() {
    this.canvas.width = window.innerWidth;
    this.canvas.height = window.innerHeight;
  }

  initNodes() {
    this.nodes = [];
    const count = Math.min(Math.floor((this.canvas.width * this.canvas.height) / 18000), 55);
    for (let i = 0; i < count; i++) {
      this.nodes.push({
        x: Math.random() * this.canvas.width,
        y: Math.random() * this.canvas.height,
        vx: (Math.random() - 0.5) * 0.4,
        vy: (Math.random() - 0.5) * 0.4,
        r: Math.random() * 2 + 1
      });
    }
  }

  draw() {
    const ctx = this.ctx;
    const w = this.canvas.width;
    const h = this.canvas.height;
    ctx.clearRect(0, 0, w, h);

    for (let node of this.nodes) {
      node.x += node.vx;
      node.y += node.vy;
      if (node.x < 0) node.x = w;
      if (node.x > w) node.x = 0;
      if (node.y < 0) node.y = h;
      if (node.y > h) node.y = 0;
    }

    // Connections
    for (let i = 0; i < this.nodes.length; i++) {
      for (let j = i + 1; j < this.nodes.length; j++) {
        const dx = this.nodes[i].x - this.nodes[j].x;
        const dy = this.nodes[i].y - this.nodes[j].y;
        const d = Math.sqrt(dx * dx + dy * dy);
        if (d < 140) {
          ctx.strokeStyle = `rgba(0, 240, 255, ${(1 - d / 140) * 0.18})`;
          ctx.beginPath();
          ctx.moveTo(this.nodes[i].x, this.nodes[i].y);
          ctx.lineTo(this.nodes[j].x, this.nodes[j].y);
          ctx.stroke();
        }
      }
      ctx.fillStyle = 'rgba(0, 240, 255, 0.4)';
      ctx.beginPath();
      ctx.arc(this.nodes[i].x, this.nodes[i].y, this.nodes[i].r, 0, Math.PI * 2);
      ctx.fill();
    }
  }
}

// ==========================================
// 3. SLIDE 0: HERO VISUAL (Nobel Laureates & Medal)
// ==========================================
class SlideHeroVisual {
  constructor(canvasId) {
    this.canvas = document.getElementById(canvasId);
    this.ctx = this.canvas.getContext('2d');
    this.time = 0;
    this.resize();
  }

  resize() {
    if (!this.canvas) return;
    const rect = this.canvas.getBoundingClientRect();
    const dpr = window.devicePixelRatio || 1;
    this.width = rect.width || 600;
    this.height = rect.height || 360;
    this.canvas.width = this.width * dpr;
    this.canvas.height = this.height * dpr;
    this.ctx.setTransform(1, 0, 0, 1, 0, 0);
    this.ctx.scale(dpr, dpr);
  }

  draw() {
    if (!this.canvas) return;
    const ctx = this.ctx;
    const w = this.width;
    const h = this.height;
    ctx.clearRect(0, 0, w, h);
    this.time += 0.03;

    const cx = w / 2;
    const cy = h * 0.24;

    // Glowing Nobel Medal
    const glow = Math.sin(this.time * 2) * 8 + 20;
    ctx.fillStyle = '#ffd700';
    ctx.shadowColor = '#ffd700';
    ctx.shadowBlur = glow;
    ctx.font = '50px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('🏅', cx, cy - 8);
    ctx.shadowBlur = 0;

    // Title text
    ctx.font = '900 20px "M PLUS Rounded 1c", sans-serif';
    ctx.fillStyle = '#ffffff';
    ctx.fillText('2026年ノーベル生理学・医学賞', cx, cy + 34);

    ctx.font = '900 14px "M PLUS Rounded 1c", sans-serif';
    ctx.fillStyle = '#00f0ff';
    ctx.fillText('「光で開閉するイオンチャネルと光遺伝学に関する発見」', cx, cy + 58);
  }
}

// ==========================================
// 4. SLIDE 1: 3D DNA & TRANSCRIPTION
// ==========================================
class SlideDNAVisual {
  constructor(canvasId) {
    this.canvas = document.getElementById(canvasId);
    this.ctx = this.canvas.getContext('2d');
    this.angle = 0;
    this.riboPos = 0;
    this.resize();
  }

  resize() {
    if (!this.canvas) return;
    const rect = this.canvas.getBoundingClientRect();
    const dpr = window.devicePixelRatio || 1;
    this.width = rect.width || 600;
    this.height = rect.height || 360;
    this.canvas.width = this.width * dpr;
    this.canvas.height = this.height * dpr;
    this.ctx.setTransform(1, 0, 0, 1, 0, 0);
    this.ctx.scale(dpr, dpr);
  }

  draw() {
    if (!this.canvas) return;
    const ctx = this.ctx;
    const w = this.width;
    const h = this.height;
    ctx.clearRect(0, 0, w, h);

    this.angle += 0.025;
    this.riboPos = (this.riboPos + 0.007) % 1;

    const numBase = 22;
    const len = w * 0.75;
    const sx = (w - len) / 2;
    const cy = h * 0.4;
    const rad = 50;

    // Draw Double Helix
    for (let i = 0; i < numBase; i++) {
      const x = sx + (i / numBase) * len;
      const phi = this.angle + i * 0.45;
      const y1 = cy + Math.sin(phi) * rad;
      const y2 = cy + Math.sin(phi + Math.PI) * rad;
      const z = Math.cos(phi);

      ctx.strokeStyle = i % 2 === 0 ? 'rgba(0, 240, 255, 0.85)' : 'rgba(255, 215, 0, 0.85)';
      ctx.lineWidth = Math.max(1.5, 3 * (z + 1.2) * 0.5);
      ctx.beginPath();
      ctx.moveTo(x, y1);
      ctx.lineTo(x, y2);
      ctx.stroke();

      ctx.fillStyle = '#00f0ff';
      ctx.beginPath();
      ctx.arc(x, y1, 5, 0, Math.PI * 2);
      ctx.fill();

      ctx.fillStyle = '#ffd700';
      ctx.beginPath();
      ctx.arc(x, y2, 5, 0, Math.PI * 2);
      ctx.fill();
    }

    // Ribosome reading strip
    const ry = cy + 90;
    ctx.strokeStyle = 'rgba(0, 255, 136, 0.5)';
    ctx.setLineDash([6, 6]);
    ctx.beginPath();
    ctx.moveTo(sx, ry);
    ctx.lineTo(sx + len, ry);
    ctx.stroke();
    ctx.setLineDash([]);

    // Ribosome Unit
    const rx = sx + this.riboPos * len;
    ctx.fillStyle = '#00ff88';
    ctx.shadowColor = '#00ff88';
    ctx.shadowBlur = 15;
    ctx.beginPath();
    ctx.ellipse(rx, ry, 22, 16, 0, 0, Math.PI * 2);
    ctx.fill();
    ctx.shadowBlur = 0;

    // Protein beads
    ctx.strokeStyle = '#00f0ff';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(rx, ry + 15);
    for (let c = 1; c <= 4; c++) {
      const bx = rx + Math.sin(this.angle * 2 + c) * 14;
      const by = ry + 15 + c * 16;
      ctx.lineTo(bx, by);
      ctx.stroke();
      ctx.fillStyle = c % 2 === 0 ? '#00f0ff' : '#ffd700';
      ctx.beginPath();
      ctx.arc(bx, by, 5, 0, Math.PI * 2);
      ctx.fill();
    }

    ctx.font = '900 14px "M PLUS Rounded 1c", sans-serif';
    ctx.fillStyle = '#00ff88';
    ctx.textAlign = 'center';
    ctx.fillText('📖 レシピ本（遺伝子DNA） ➔ 現場の働くマシン（タンパク質）が完成！', w / 2, h - 20);
  }
}

// ==========================================
// 5. SLIDE 2: MEMBRANE & ACTION POTENTIAL
// ==========================================
class SlideMembraneVisual {
  constructor(canvasId) {
    this.canvas = document.getElementById(canvasId);
    this.ctx = this.canvas.getContext('2d');
    this.phase = 0;
    this.voltage = -70;
    this.isSpiking = false;
    this.ions = [];
    this.hudText = document.getElementById('membrane-mv-text');
    this.resize();
    this.initIons();
  }

  resize() {
    if (!this.canvas) return;
    const rect = this.canvas.getBoundingClientRect();
    const dpr = window.devicePixelRatio || 1;
    this.width = rect.width || 600;
    this.height = rect.height || 360;
    this.canvas.width = this.width * dpr;
    this.canvas.height = this.height * dpr;
    this.ctx.setTransform(1, 0, 0, 1, 0, 0);
    this.ctx.scale(dpr, dpr);
  }

  initIons() {
    this.ions = [];
    for (let i = 0; i < 35; i++) {
      this.ions.push({
        x: Math.random() * 600,
        y: Math.random() * 80 + 20,
        vx: (Math.random() - 0.5) * 1,
        vy: Math.random() * 0.6 + 0.3
      });
    }
  }

  draw() {
    if (!this.canvas) return;
    const ctx = this.ctx;
    const w = this.width;
    const h = this.height;
    ctx.clearRect(0, 0, w, h);

    this.phase += 0.035;
    const cy = h * 0.52;

    // Membrane bilayer
    ctx.fillStyle = '#1c2848';
    ctx.fillRect(0, cy - 14, w, 28);

    // Gate cycle
    const gateOpen = (Math.sin(this.phase * 1.2) + 1) * 0.5;
    if (gateOpen > 0.8 && !this.isSpiking) {
      this.isSpiking = true;
      this.voltage = 30;
      sound.playSpike();
    } else if (gateOpen < 0.3) {
      this.isSpiking = false;
      this.voltage = Math.max(-70, this.voltage - 2);
    }

    if (this.hudText) {
      this.hudText.innerText = `${Math.round(this.voltage)} mV (${this.isSpiking ? '⚡ 発火中！' : '静止中'})`;
      this.hudText.style.color = this.isSpiking ? '#ff5599' : '#00f0ff';
    }

    // Gate drawing
    const gw = 70;
    const gx = w / 2 - gw / 2;
    ctx.fillStyle = '#ff5599';
    ctx.shadowColor = '#ff5599';
    ctx.shadowBlur = gateOpen * 18;
    ctx.fillRect(gx, cy - 20, (gw / 2) * (1 - gateOpen * 0.75), 40);
    ctx.fillRect(gx + gw - (gw / 2) * (1 - gateOpen * 0.75), cy - 20, (gw / 2) * (1 - gateOpen * 0.75), 40);
    ctx.shadowBlur = 0;

    // Ions
    for (let ion of this.ions) {
      if (gateOpen > 0.5 && Math.abs(ion.x - w / 2) < 50 && ion.y < cy) {
        ion.vy += 0.5;
        ion.vx = (w / 2 - ion.x) * 0.08;
      }
      ion.x += ion.vx;
      ion.y += ion.vy;
      if (ion.y > h - 20) {
        ion.y = Math.random() * 60 + 20;
        ion.x = Math.random() * w;
        ion.vy = Math.random() * 0.6 + 0.3;
      }
      if (ion.x < 0) ion.x = w;
      if (ion.x > w) ion.x = 0;

      ctx.fillStyle = '#00f0ff';
      ctx.beginPath();
      ctx.arc(ion.x, ion.y, 4.5, 0, Math.PI * 2);
      ctx.fill();

      ctx.font = '8px sans-serif';
      ctx.fillStyle = '#000';
      ctx.fillText('+', ion.x - 2, ion.y + 3);
    }
  }
}

// ==========================================
// 6. SLIDE 3: CHLAMYDOMONAS & LIGHT RESPONSE
// ==========================================
class SlideAlgaeVisual {
  constructor(canvasId) {
    this.canvas = document.getElementById(canvasId);
    this.ctx = this.canvas.getContext('2d');
    this.isFlashing = false;
    this.lightIntensity = 0;
    this.t = 0;
    this.algae = { x: 220, y: 180, angle: 0, targetAngle: 0 };
    this.resize();

    const btnFlash = document.getElementById('btn-flash-algae');
    if (btnFlash) {
      btnFlash.addEventListener('click', () => this.flash());
    }
  }

  resize() {
    if (!this.canvas) return;
    const rect = this.canvas.getBoundingClientRect();
    const dpr = window.devicePixelRatio || 1;
    this.width = rect.width || 600;
    this.height = rect.height || 360;
    this.canvas.width = this.width * dpr;
    this.canvas.height = this.height * dpr;
    this.ctx.setTransform(1, 0, 0, 1, 0, 0);
    this.ctx.scale(dpr, dpr);
    this.algae.x = this.width * 0.35;
    this.algae.y = this.height * 0.5;
  }

  flash() {
    this.isFlashing = true;
    this.lightIntensity = 1;
    sound.playLaser(true);
    sound.playChime();
    setTimeout(() => {
      this.isFlashing = false;
    }, 1600);
  }

  draw() {
    if (!this.canvas) return;
    const ctx = this.ctx;
    const w = this.width;
    const h = this.height;
    ctx.clearRect(0, 0, w, h);
    this.t += 0.05;

    if (!this.isFlashing && this.lightIntensity > 0) {
      this.lightIntensity = Math.max(0, this.lightIntensity - 0.03);
    }

    // Light beam from right
    if (this.lightIntensity > 0) {
      const grad = ctx.createRadialGradient(w, h / 2, 10, w, h / 2, w * 0.85);
      grad.addColorStop(0, `rgba(0, 240, 255, ${this.lightIntensity * 0.75})`);
      grad.addColorStop(1, 'rgba(0, 240, 255, 0)');
      ctx.fillStyle = grad;
      ctx.fillRect(0, 0, w, h);
    }

    // Steer towards light
    if (this.lightIntensity > 0.2) {
      this.algae.targetAngle = Math.atan2((h / 2) - this.algae.y, w - this.algae.x);
      this.algae.x += Math.cos(this.algae.angle) * 2.8;
      this.algae.y += Math.sin(this.algae.angle) * 2.8;
    } else {
      this.algae.targetAngle = Math.sin(this.t * 0.4) * 0.5;
      this.algae.x += Math.cos(this.algae.angle) * 1.0;
      this.algae.y += Math.sin(this.algae.angle) * 1.0;
    }
    this.algae.angle += (this.algae.targetAngle - this.algae.angle) * 0.08;

    if (this.algae.x > w - 80) this.algae.x = 80;
    if (this.algae.y > h - 60 || this.algae.y < 60) this.algae.y = h / 2;

    ctx.save();
    ctx.translate(this.algae.x, this.algae.y);
    ctx.rotate(this.algae.angle);

    // Flagella
    const flap = Math.sin(this.t * 5) * 0.6;
    ctx.strokeStyle = '#00ff88';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(30, -5);
    ctx.bezierCurveTo(55, -35 + flap * 25, 75, -15, 85, -25);
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(30, 5);
    ctx.bezierCurveTo(55, 35 + flap * 25, 75, 15, 85, 25);
    ctx.stroke();

    // Body
    ctx.fillStyle = '#0a3d24';
    ctx.strokeStyle = '#00ff88';
    ctx.lineWidth = 3;
    ctx.shadowColor = '#00ff88';
    ctx.shadowBlur = 12;
    ctx.beginPath();
    ctx.ellipse(0, 0, 42, 28, 0, 0, Math.PI * 2);
    ctx.fill();
    ctx.stroke();
    ctx.shadowBlur = 0;

    // Photoreceptor eye (Channelrhodopsin)
    const eyeGlow = this.lightIntensity > 0.2 ? '#00f0ff' : '#ff5533';
    ctx.fillStyle = eyeGlow;
    ctx.shadowColor = eyeGlow;
    ctx.shadowBlur = 15;
    ctx.beginPath();
    ctx.arc(18, -12, 7, 0, Math.PI * 2);
    ctx.fill();
    ctx.shadowBlur = 0;

    ctx.restore();
  }
}

// ==========================================
// 7. SLIDE 4: VIRAL DELIVERY & ASSEMBLY
// ==========================================
class SlideDeliveryVisual {
  constructor(canvasId) {
    this.canvas = document.getElementById(canvasId);
    this.ctx = this.canvas.getContext('2d');
    this.time = 0;
    this.resize();
  }

  resize() {
    if (!this.canvas) return;
    const rect = this.canvas.getBoundingClientRect();
    const dpr = window.devicePixelRatio || 1;
    this.width = rect.width || 600;
    this.height = rect.height || 360;
    this.canvas.width = this.width * dpr;
    this.canvas.height = this.height * dpr;
    this.ctx.setTransform(1, 0, 0, 1, 0, 0);
    this.ctx.scale(dpr, dpr);
  }

  draw() {
    if (!this.canvas) return;
    const ctx = this.ctx;
    const w = this.width;
    const h = this.height;
    ctx.clearRect(0, 0, w, h);
    this.time += 0.035;

    const cx = w / 2;
    const cy = h / 2;

    // Large Neuron Body
    ctx.fillStyle = '#0b1c3b';
    ctx.strokeStyle = '#00f0ff';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.arc(cx, cy + 10, 75, 0, Math.PI * 2);
    ctx.fill();
    ctx.stroke();

    // Embedded optical switches on membrane
    for (let k = 0; k < 8; k++) {
      const th = (k / 8) * Math.PI * 2;
      const sx = cx + Math.cos(th) * 75;
      const sy = (cy + 10) + Math.sin(th) * 75;

      ctx.fillStyle = '#00f0ff';
      ctx.shadowColor = '#00f0ff';
      ctx.shadowBlur = 12;
      ctx.beginPath();
      ctx.arc(sx, sy, 8, 0, Math.PI * 2);
      ctx.fill();
      ctx.shadowBlur = 0;
    }

    // Delivery Capsule floating down into neuron
    const capY = cy - 60 + Math.sin(this.time * 2) * 15;
    ctx.strokeStyle = '#ffd700';
    ctx.fillStyle = 'rgba(255, 215, 0, 0.25)';
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    for (let a = 0; a < 6; a++) {
      const ang = (a / 6) * Math.PI * 2 + this.time;
      const px = cx + Math.cos(ang) * 32;
      const py = capY + Math.sin(ang) * 32;
      if (a === 0) ctx.moveTo(px, py);
      else ctx.lineTo(px, py);
    }
    ctx.closePath();
    ctx.fill();
    ctx.stroke();

    ctx.font = '900 12px "JetBrains Mono", sans-serif';
    ctx.fillStyle = '#00f0ff';
    ctx.textAlign = 'center';
    ctx.fillText('ChR2 GENE', cx, capY + 4);

    ctx.font = '900 15px "M PLUS Rounded 1c", sans-serif';
    ctx.fillStyle = '#ffd700';
    ctx.fillText('藻の設計図を導入 ➔ 神経細胞が「青色光スイッチ」を装備！', cx, h - 20);
  }
}

// ==========================================
// 8. SLIDE 5: LASER EXPERIMENT & OSCILLOSCOPE
// ==========================================
class SlideLaserLabVisual {
  constructor(canvasId, scopeCanvasId) {
    this.canvas = document.getElementById(canvasId);
    this.ctx = this.canvas.getContext('2d');
    this.scopeCanvas = document.getElementById(scopeCanvasId);
    this.scopeCtx = this.scopeCanvas ? this.scopeCanvas.getContext('2d') : null;

    this.activeLaser = null; // 'blue' | 'yellow' | null
    this.membranePotential = -70;
    this.spikeHistory = new Array(120).fill(-70);
    this.statusText = document.getElementById('scope-status');

    this.resize();
    this.initButtons();
  }

  resize() {
    if (!this.canvas || !this.scopeCanvas) return;
    const dpr = window.devicePixelRatio || 1;

    const rect = this.canvas.getBoundingClientRect();
    this.width = rect.width || 600;
    this.height = rect.height || 360;
    this.canvas.width = this.width * dpr;
    this.canvas.height = this.height * dpr;
    this.ctx.setTransform(1, 0, 0, 1, 0, 0);
    this.ctx.scale(dpr, dpr);

    const sRect = this.scopeCanvas.getBoundingClientRect();
    this.scopeWidth = sRect.width || 600;
    this.scopeHeight = 48;
    this.scopeCanvas.width = this.scopeWidth * dpr;
    this.scopeCanvas.height = this.scopeHeight * dpr;
    this.scopeCtx.setTransform(1, 0, 0, 1, 0, 0);
    this.scopeCtx.scale(dpr, dpr);
  }

  initButtons() {
    const btnBlue = document.getElementById('btn-laser-blue');
    const btnYellow = document.getElementById('btn-laser-yellow');

    if (btnBlue) {
      btnBlue.addEventListener('mousedown', () => this.fireLaser('blue'));
      btnBlue.addEventListener('mouseup', () => this.stopLaser());
      btnBlue.addEventListener('touchstart', (e) => { e.preventDefault(); this.fireLaser('blue'); });
      btnBlue.addEventListener('touchend', () => this.stopLaser());
    }

    if (btnYellow) {
      btnYellow.addEventListener('mousedown', () => this.fireLaser('yellow'));
      btnYellow.addEventListener('mouseup', () => this.stopLaser());
      btnYellow.addEventListener('touchstart', (e) => { e.preventDefault(); this.fireLaser('yellow'); });
      btnYellow.addEventListener('touchend', () => this.stopLaser());
    }
  }

  fireLaser(color) {
    this.activeLaser = color;
    sound.playLaser(color === 'blue');

    if (color === 'blue') {
      sound.playSpike();
      this.membranePotential = 35;
      if (this.statusText) {
        this.statusText.innerText = '⚡ ACTIVE SPIKE : +35mV (発火！)';
        this.statusText.style.color = '#00f0ff';
      }
    } else {
      this.membranePotential = -88;
      if (this.statusText) {
        this.statusText.innerText = '🛑 INHIBITED : -88mV (過分極・停止)';
        this.statusText.style.color = '#ffb700';
      }
    }
  }

  stopLaser() {
    this.activeLaser = null;
    if (this.statusText) {
      this.statusText.innerText = 'RESTING : -70mV (通常)';
      this.statusText.style.color = '#8ea3bf';
    }
  }

  draw() {
    if (!this.canvas) return;
    const ctx = this.ctx;
    const w = this.width;
    const h = this.height;
    ctx.clearRect(0, 0, w, h);

    const cx = w / 2;
    const cy = h * 0.48;

    // Decay voltage
    if (this.activeLaser === 'yellow') {
      this.membranePotential = Math.max(-88, this.membranePotential - 1);
    } else {
      if (this.membranePotential > -70) {
        this.membranePotential -= 4.5;
        if (this.membranePotential < -70) this.membranePotential = -70;
      }
    }

    // Oscilloscope update
    this.spikeHistory.shift();
    const noise = (Math.random() - 0.5) * 2;
    this.spikeHistory.push(this.membranePotential + noise);

    // Laser Beam from top
    if (this.activeLaser) {
      const beamGrad = ctx.createLinearGradient(cx, 10, cx, cy);
      const c = this.activeLaser === 'blue' ? '0, 240, 255' : '255, 183, 0';
      beamGrad.addColorStop(0, `rgba(${c}, 0.8)`);
      beamGrad.addColorStop(1, `rgba(${c}, 0.1)`);
      ctx.fillStyle = beamGrad;
      ctx.beginPath();
      ctx.moveTo(cx, 10);
      ctx.lineTo(cx - 45, cy);
      ctx.lineTo(cx + 45, cy);
      ctx.fill();
    }

    // Optical fiber cable
    ctx.fillStyle = '#445566';
    ctx.fillRect(cx - 5, 0, 10, 45);

    // Neuron
    const isExcited = this.membranePotential > -40;
    ctx.fillStyle = isExcited ? 'rgba(0, 240, 255, 0.3)' : 'rgba(12, 22, 45, 0.9)';
    ctx.strokeStyle = isExcited ? '#00f0ff' : 'rgba(0, 240, 255, 0.4)';
    ctx.lineWidth = 3;
    ctx.shadowColor = isExcited ? '#00f0ff' : 'transparent';
    ctx.shadowBlur = isExcited ? 25 : 0;
    ctx.beginPath();
    ctx.arc(cx, cy, 60, 0, Math.PI * 2);
    ctx.fill();
    ctx.stroke();
    ctx.shadowBlur = 0;

    // Dendrites
    ctx.strokeStyle = isExcited ? '#00f0ff' : 'rgba(0, 240, 255, 0.3)';
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    ctx.moveTo(cx - 55, cy - 20);
    ctx.lineTo(cx - 130, cy - 60);
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(cx + 55, cy - 20);
    ctx.lineTo(cx + 130, cy - 60);
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(cx, cy + 60);
    ctx.lineTo(cx, cy + 120);
    ctx.stroke();

    // Draw Oscilloscope
    this.drawScope();
  }

  drawScope() {
    if (!this.scopeCtx) return;
    const sCtx = this.scopeCtx;
    const sw = this.scopeWidth;
    const sh = this.scopeHeight;
    sCtx.clearRect(0, 0, sw, sh);

    sCtx.strokeStyle = 'rgba(0, 240, 255, 0.15)';
    sCtx.lineWidth = 1;
    sCtx.beginPath();
    for (let x = 0; x < sw; x += 35) {
      sCtx.moveTo(x, 0);
      sCtx.lineTo(x, sh);
    }
    sCtx.stroke();

    sCtx.strokeStyle = '#00f0ff';
    sCtx.lineWidth = 2.5;
    sCtx.shadowColor = '#00f0ff';
    sCtx.shadowBlur = 8;
    sCtx.beginPath();

    const minV = -90;
    const maxV = 50;
    for (let i = 0; i < this.spikeHistory.length; i++) {
      const x = (i / (this.spikeHistory.length - 1)) * sw;
      const v = this.spikeHistory[i];
      const normY = (v - minV) / (maxV - minV);
      const y = sh - (normY * sh);
      if (i === 0) sCtx.moveTo(x, y);
      else sCtx.lineTo(x, y);
    }
    sCtx.stroke();
    sCtx.shadowBlur = 0;
  }
}

// ==========================================
// 9. SLIDE 6: TRIUMPH & RESIDUAL GLOW
// ==========================================
class SlideTriumphVisual {
  constructor(canvasId) {
    this.canvas = document.getElementById(canvasId);
    this.ctx = this.canvas.getContext('2d');
    this.time = 0;
    this.resize();
  }

  resize() {
    if (!this.canvas) return;
    const rect = this.canvas.getBoundingClientRect();
    const dpr = window.devicePixelRatio || 1;
    this.width = rect.width || 600;
    this.height = rect.height || 360;
    this.canvas.width = this.width * dpr;
    this.canvas.height = this.height * dpr;
    this.ctx.setTransform(1, 0, 0, 1, 0, 0);
    this.ctx.scale(dpr, dpr);
  }

  draw() {
    if (!this.canvas) return;
    const ctx = this.ctx;
    const w = this.width;
    const h = this.height;
    ctx.clearRect(0, 0, w, h);
    this.time += 0.035;

    const cx = w / 2;
    const cy = h * 0.38;

    // Resonating Brain Network
    for (let i = 0; i < 24; i++) {
      const ang = (i / 24) * Math.PI * 2 + this.time * 0.8;
      const r = 60 + Math.sin(this.time * 2 + i) * 20;
      const px = cx + Math.cos(ang) * r;
      const py = cy + Math.sin(ang) * r;

      ctx.fillStyle = i % 2 === 0 ? '#ffd700' : '#00f0ff';
      ctx.shadowColor = ctx.fillStyle;
      ctx.shadowBlur = 12;
      ctx.beginPath();
      ctx.arc(px, py, 4.5, 0, Math.PI * 2);
      ctx.fill();
      ctx.shadowBlur = 0;
    }

    ctx.font = '900 24px "M PLUS Rounded 1c", sans-serif';
    ctx.fillStyle = '#ffd700';
    ctx.textAlign = 'center';
    ctx.fillText('脳科学の歴史を塗り替えた「光遺伝学」', cx, cy + 10);
  }
}

// ==========================================
// 10. YUKKURI SLIDE & SUBTITLE CONTROLLER
// ==========================================
class YukkuriSlideDeckController {
  constructor() {
    this.currentSlide = 0;
    this.currentSubStep = 0;
    this.totalSlides = 7;
    this.isAutoPlay = false;
    this.autoTimer = null;

    // Slide Dialogues (各スライドごとに複数の大きなセリフ)
    this.slideDialogues = [
      // SLIDE 0: 速報
      [
        {
          speaker: 'aoi',
          emotion: '❓',
          text: '先生！スマホの速報見ました！ノーベル賞の<strong>「光遺伝学」</strong>って何ですか！？ 漢字ばっかりで意味不明です！'
        },
        {
          speaker: 'sato',
          emotion: '💡',
          text: '光を当てるだけで、狙った脳神経のスイッチを<strong>1000分の1秒でON/OFFする</strong>人類最大の革命だよ！'
        }
      ],
      // SLIDE 1: 遺伝子ってなに？
      [
        {
          speaker: 'aoi',
          emotion: '❓',
          text: 'そもそも<strong>「遺伝子」</strong>って何なんですか？ テストで丸暗記しただけでサッパリ分かってないんです…'
        },
        {
          speaker: 'sato',
          emotion: '💡',
          text: 'ズバリ<strong>「料理のレシピ本（設計図）」</strong>だ！ からだの道具を作る指示書が遺伝子なんだよ。'
        },
        {
          speaker: 'aoi',
          emotion: '✨',
          text: 'レシピ本！ じゃあそのレシピで作られる料理（完成品）は体の中で何なんですか？'
        },
        {
          speaker: 'sato',
          emotion: '🔬',
          text: 'それが<strong>「タンパク質」</strong>だ！ 新しいレシピ（遺伝子）を細胞に渡せば、<strong>新しい特殊な道具を作らせることができる</strong>んだ！'
        }
      ],
      // SLIDE 2: 脳はどう動く？
      [
        {
          speaker: 'aoi',
          emotion: '❓',
          text: 'なるほど！ でも先生、脳神経ってどうやって電気を流してるんですか？'
        },
        {
          speaker: 'sato',
          emotion: '⚡',
          text: '細胞膜の「門（チャネル）」が開くと、プラスのイオンが流れ込んで<strong>「パチッ！」と電気が走る（神経発火）</strong>んだ。'
        },
        {
          speaker: 'aoi',
          emotion: '💡',
          text: '電気コードみたい！ じゃあ電極の針を刺して電気を流せばいいんじゃないですか？'
        },
        {
          speaker: 'sato',
          emotion: '😲',
          text: '電極だと<strong>周りの何千個もの細胞まで全員感電しちゃう！</strong> 狙った1本だけを動かす道具が必要だったんだ。'
        }
      ],
      // SLIDE 3: 池の藻の奇跡
      [
        {
          speaker: 'sato',
          emotion: '🔬',
          text: 'そこで科学者が見つけたのが…なんと<strong>池にすむ緑の藻「クラミドモナス」</strong>だった！'
        },
        {
          speaker: 'aoi',
          emotion: '😲',
          text: 'ええっ！？ 池の藻！？ 脳の研究なのに植物プランクトンなんですか！？'
        },
        {
          speaker: 'sato',
          emotion: '✨',
          text: '藻は光を求めて泳ぐ。そのために<strong>「青い光（470nm）を浴びると一瞬で開く門（チャネルロドプシン）」</strong>を持っていたんだ！'
        }
      ],
      // SLIDE 4: ダイセロスの大革命！
      [
        {
          speaker: 'sato',
          emotion: '🎯',
          text: 'ダイセロス教授は閃いた。「この藻の門のレシピ（遺伝子）を<strong>脳神経に届けてみたらどうなる？</strong>」とね。'
        },
        {
          speaker: 'aoi',
          emotion: '😲',
          text: 'あっ！！ 脳神経が、藻の青色光ドアを<strong>自分で作っちゃう</strong>んですか！？'
        },
        {
          speaker: 'sato',
          emotion: '💡',
          text: 'その通り！ 運び屋ウイルスで届けると、<strong>青い光を当てるだけで狙い撃ちで動く神経</strong>が完成したんだ！'
        }
      ],
      // SLIDE 5: 光で撃て！実験室
      [
        {
          speaker: 'sato',
          emotion: '⚡',
          text: 'さあアオイ、右上の<strong>「青色光ボタン」</strong>を押して、光をパルス照射してみてごらん！'
        },
        {
          speaker: 'aoi',
          emotion: '😲',
          text: 'わああっ！ 光った瞬間に神経が発火して、オシロスコープが跳ね上がりました！ <strong>黄色い光だとピタッと止まります！</strong>'
        },
        {
          speaker: 'sato',
          emotion: '💡',
          text: '青でアクセル（興奮）、黄色でブレーキ（抑制）。1000分の1秒で自由自在に脳を操作できるんだ！'
        }
      ],
      // SLIDE 6: なぜノーベル賞なのか？
      [
        {
          speaker: 'aoi',
          emotion: '❓',
          text: '先生、この技術のおかげで私たちの未来はどう変わるんですか？'
        },
        {
          speaker: 'sato',
          emotion: '🔬',
          text: 'うつ病やパーキンソン病の回路解明、そして<strong>「失明した人の目に光を取り戻す」臨床応用</strong>まで進んでいるんだ。'
        },
        {
          speaker: 'aoi',
          emotion: '✨',
          text: '池の藻の発見が、人類の未来をこんなにも明るく救うんですね！ 科学ってすごい！'
        },
        {
          speaker: 'sato',
          emotion: '😊',
          text: 'ダイセロス、ヘーゲマン、ナーゲルの3人に心から拍手だね！ アオイ、これで君も光遺伝学マスターだ！'
        }
      ]
    ];

    this.initDOM();
    this.render();
  }

  initDOM() {
    // Buttons
    const btnNext = document.getElementById('btn-talk-next');
    const btnPrev = document.getElementById('btn-talk-prev');
    const btnNextSlide = document.getElementById('btn-next-slide');
    const btnPrevSlide = document.getElementById('btn-prev-slide');
    const speechBubble = document.getElementById('speech-bubble-box');
    const btnAuto = document.getElementById('btn-auto-play');
    const btnSound = document.getElementById('btn-sound-toggle');
    const soundIcon = document.getElementById('sound-icon');

    // Speech Box Click triggers Next Talk Step
    if (speechBubble) {
      speechBubble.addEventListener('click', () => this.stepForward());
    }
    if (btnNext) {
      btnNext.addEventListener('click', () => this.stepForward());
    }
    if (btnPrev) {
      btnPrev.addEventListener('click', () => this.stepBackward());
    }

    // Side Navigation Arrows
    if (btnNextSlide) {
      btnNextSlide.addEventListener('click', () => this.goToSlide(this.currentSlide + 1));
    }
    if (btnPrevSlide) {
      btnPrevSlide.addEventListener('click', () => this.goToSlide(this.currentSlide - 1));
    }

    // Dots
    const dots = document.querySelectorAll('.s-dot');
    dots.forEach(dot => {
      dot.addEventListener('click', () => {
        const s = parseInt(dot.getAttribute('data-s'));
        this.goToSlide(s);
      });
    });

    // Auto Play Toggle
    if (btnAuto) {
      btnAuto.addEventListener('click', () => {
        this.isAutoPlay = !this.isAutoPlay;
        btnAuto.classList.toggle('active', this.isAutoPlay);
        btnAuto.innerHTML = `<span class="pill-dot"></span> 自動送り: ${this.isAutoPlay ? 'ON' : 'OFF'}`;
        if (this.isAutoPlay) {
          this.startAutoPlay();
        } else {
          this.stopAutoPlay();
        }
      });
    }

    // Sound Toggle
    if (btnSound) {
      btnSound.addEventListener('click', () => {
        const muted = sound.toggleMute();
        if (soundIcon) soundIcon.innerText = muted ? '🔇' : '🔊';
      });
    }

    // Mouse Wheel Snapping
    let wheelCooldown = false;
    window.addEventListener('wheel', (e) => {
      if (wheelCooldown) return;
      if (e.deltaY > 30) {
        wheelCooldown = true;
        this.stepForward();
        setTimeout(() => { wheelCooldown = false; }, 400);
      } else if (e.deltaY < -30) {
        wheelCooldown = true;
        this.stepBackward();
        setTimeout(() => { wheelCooldown = false; }, 400);
      }
    }, { passive: true });

    // Keyboard Arrow Keys
    window.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight' || e.key === 'ArrowDown' || e.key === ' ') {
        this.stepForward();
      } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
        this.stepBackward();
      }
    });
  }

  startAutoPlay() {
    this.stopAutoPlay();
    this.autoTimer = setInterval(() => {
      if (!this.isAutoPlay) return;
      this.stepForward();
    }, 4800);
  }

  stopAutoPlay() {
    if (this.autoTimer) {
      clearInterval(this.autoTimer);
      this.autoTimer = null;
    }
  }

  stepForward() {
    sound.playPop();
    const talks = this.slideDialogues[this.currentSlide];
    if (this.currentSubStep < talks.length - 1) {
      this.currentSubStep++;
      this.render();
    } else {
      if (this.currentSlide < this.totalSlides - 1) {
        this.goToSlide(this.currentSlide + 1);
      } else {
        // loop back to start
        this.goToSlide(0);
      }
    }
  }

  stepBackward() {
    sound.playPop();
    if (this.currentSubStep > 0) {
      this.currentSubStep--;
      this.render();
    } else {
      if (this.currentSlide > 0) {
        this.currentSlide--;
        this.currentSubStep = this.slideDialogues[this.currentSlide].length - 1;
        this.render();
      }
    }
  }

  goToSlide(slideIndex) {
    if (slideIndex < 0) slideIndex = 0;
    if (slideIndex >= this.totalSlides) slideIndex = this.totalSlides - 1;

    this.currentSlide = slideIndex;
    this.currentSubStep = 0;
    sound.playChime();
    this.render();
  }

  render() {
    // 1. Update Slide Visibility
    const slides = document.querySelectorAll('.slide-page');
    slides.forEach((sl, idx) => {
      sl.classList.toggle('active', idx === this.currentSlide);
    });

    // 2. Update HUD Counter
    const numDisplay = document.getElementById('current-slide-num');
    if (numDisplay) {
      numDisplay.innerText = String(this.currentSlide + 1).padStart(2, '0');
    }

    // 3. Update Dots
    const dots = document.querySelectorAll('.s-dot');
    dots.forEach((d, idx) => {
      d.classList.toggle('active', idx === this.currentSlide);
    });

    // 4. Update Yukkuri Dialogue Subtitle
    const talks = this.slideDialogues[this.currentSlide];
    const curTalk = talks[this.currentSubStep] || talks[0];

    const speakerAoi = document.getElementById('speaker-aoi');
    const speakerSato = document.getElementById('speaker-sato');
    const aoiEmotion = document.getElementById('aoi-badge-emotion');
    const satoEmotion = document.getElementById('sato-badge-emotion');
    const pill = document.getElementById('speech-speaker-name');
    const textEl = document.getElementById('yukkuri-text');

    const isAoi = curTalk.speaker === 'aoi';

    if (speakerAoi && speakerSato) {
      speakerAoi.classList.toggle('active', isAoi);
      speakerSato.classList.toggle('active', !isAoi);
    }

    if (isAoi && aoiEmotion) {
      aoiEmotion.innerText = curTalk.emotion;
    } else if (!isAoi && satoEmotion) {
      satoEmotion.innerText = curTalk.emotion;
    }

    if (pill) {
      pill.className = `speaker-pill ${isAoi ? 'aoi' : 'sato'}`;
      pill.innerText = isAoi ? 'アオイ' : 'Dr. サトウ';
    }

    if (textEl) {
      textEl.innerHTML = curTalk.text;
    }

    // Trigger visual reactions on slide change
    if (this.currentSlide === 3 && window.slideAlgae) {
      setTimeout(() => window.slideAlgae.flash(), 600);
    }
    if (this.currentSlide === 5 && window.slideLaserLab) {
      setTimeout(() => {
        window.slideLaserLab.fireLaser('blue');
        setTimeout(() => window.slideLaserLab.stopLaser(), 1000);
      }, 700);
    }
  }
}

// ==========================================
// 11. ENTRY POINT & ANIMATION LOOP
// ==========================================
window.addEventListener('DOMContentLoaded', () => {
  // Background
  const bg = new BackgroundNetwork('bg-canvas');

  // Slide Visual Stages
  const slideHero = new SlideHeroVisual('canvas-hero');
  const slideDNA = new SlideDNAVisual('canvas-dna');
  const slideMembrane = new SlideMembraneVisual('canvas-membrane');
  window.slideAlgae = new SlideAlgaeVisual('canvas-algae');
  const slideDelivery = new SlideDeliveryVisual('canvas-delivery');
  window.slideLaserLab = new SlideLaserLabVisual('canvas-laser', 'canvas-scope');
  const slideTriumph = new SlideTriumphVisual('canvas-triumph');

  // Deck Controller
  const deck = new YukkuriSlideDeckController();

  function triggerResizeAll() {
    bg.resize();
    slideHero.resize();
    slideDNA.resize();
    slideMembrane.resize();
    window.slideAlgae.resize();
    slideDelivery.resize();
    window.slideLaserLab.resize();
    slideTriumph.resize();
  }

  window.addEventListener('resize', triggerResizeAll);
  window.addEventListener('load', triggerResizeAll);
  setTimeout(triggerResizeAll, 200);

  // 60FPS RAF Render Loop
  function loop() {
    bg.draw();

    // Render only the active slide's visual to maximize 60fps performance
    switch (deck.currentSlide) {
      case 0: slideHero.draw(); break;
      case 1: slideDNA.draw(); break;
      case 2: slideMembrane.draw(); break;
      case 3: window.slideAlgae.draw(); break;
      case 4: slideDelivery.draw(); break;
      case 5: window.slideLaserLab.draw(); break;
      case 6: slideTriumph.draw(); break;
    }

    requestAnimationFrame(loop);
  }

  requestAnimationFrame(loop);
});
