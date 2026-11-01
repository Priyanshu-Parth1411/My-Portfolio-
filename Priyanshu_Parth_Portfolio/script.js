const $ = (s, root=document) => root.querySelector(s);
const $$ = (s, root=document) => [...root.querySelectorAll(s)];
const nav = $('#nav'), menuToggle = $('#menuToggle');
menuToggle.addEventListener('click', () => {
  const open = nav.classList.toggle('open');
  menuToggle.setAttribute('aria-expanded', String(open));
});
$$('#nav a').forEach(a => a.addEventListener('click', () => {
  nav.classList.remove('open'); menuToggle.setAttribute('aria-expanded','false');
}));
$('#themeToggle').addEventListener('click', () => {
  document.body.classList.toggle('light');
  localStorage.setItem('portfolio-theme', document.body.classList.contains('light') ? 'light' : 'dark');
});
if (localStorage.getItem('portfolio-theme') === 'light') document.body.classList.add('light');
$('#year').textContent = new Date().getFullYear();

const projectData = {
  spider: {
    eyebrow:'CAPSTONE / ROBOTICS + COMPUTER VISION',
    title:'SPIDER — Pedestrian Intent Detection & Emergency Response',
    description:'A controlled robotic testbed for predicting pedestrian crossing intent and connecting that prediction to an emergency-response decision.',
    overview:'The documented pipeline uses YOLOv8 for pedestrian detection, ByteTrack for tracking, 15-frame motion features and a stacked LSTM classifier to estimate crossing intent. A front time-of-flight sensor provides an independent safety-stop layer. The platform uses a Duckiebot DB21M with Jetson Nano, ROS Noetic in Docker and rosbridge communication. The project poster reports JAAD test-split accuracy of 89.11% and AUC-ROC of 0.963; these are dataset evaluation metrics, not measured on-robot performance.',
    tech:'YOLOv8 · ByteTrack · Stacked LSTM · ROS Noetic · Docker · Jetson Nano · Duckiebot DB21M · IMX219 camera · ToF range sensor',
    resource:'assets/SPIDER-Project-Poster.pdf',
    resourceLabel:'Open SPIDER project poster',
    media:'<video controls preload="metadata" playsinline src="assets/SPIDER-Demo-Video.mp4"></video>'
  },
  sara: {
    eyebrow:'ROBOTICS / QUADRUPED PLATFORM',
    title:'SARA Quadruped Robot',
    description:'A four-legged robotic platform developed around embedded control and coordinated servo actuation.',
    overview:'SARA uses an ESP32 as its controller and as the host for its web dashboard. Eight MG90S micro servos actuate the four-legged mechanism. The dashboard provides directional motion controls, stand and sleep pose commands, save/load controls, gait speed and timing adjustments, and individual servo-centre and knee-lift angle controls. The supplied WhatsApp comparison identifies the sleep and active servo-angle configurations. No autonomous navigation or measured walking-performance claims are made here.',
    tech:'ESP32 · 8 × MG90S micro servos · Embedded C/C++ · Web dashboard · PWM servo control',
    resource:'#projects',
    resourceLabel:'SARA project overview',
    media:'<div class="media-gallery"><img src="assets/sara-robot-wide.jpg" alt="SARA quadruped robot"><img src="assets/sara-dashboard-wide.jpg" alt="SARA ESP32 web dashboard"><img src="assets/sara-sleep-angle.jpg" alt="SARA sleep servo angle settings"><img src="assets/sara-active-angle.jpg" alt="SARA active servo angle settings"></div>'
  },
  classroom: {
    eyebrow:'IoT / AUTOMATION',
    title:'IoT Smart Classroom Automation',
    description:'A connected classroom concept using sensor inputs and microcontroller-based automation.',
    overview:'The supplied terminal photographs show Raspberry Pi-based operation and a live ThingSpeak SmartClassroom channel (Channel ID 3360033) with temperature and humidity charts. The serial output includes temperature, humidity, PIR motion, LDR readings, relay states, fan state, energy values and AUTO/MANU mode. A multi-channel relay board is visible in the hardware setup. Exact sensor models and the full control mapping are not yet confirmed, so they are not named.',
    tech:'Raspberry Pi · ThingSpeak · IoT telemetry · Sensors · Relay module · Automatic/manual control',
    resource:'#projects',
    resourceLabel:'Project overview'
  },
  mimo: {
    eyebrow:'RESEARCH / DEEP LEARNING',
    title:'Deep Learning-Based Wireless Channel Estimation',
    description:'Research work exploring neural-network methods for wireless channel estimation.',
    overview:'The supplied code generates time-varying 128×128 Rayleigh channel matrices at a 28 GHz carrier frequency and a 120 km/h mobility setting, stores real and imaginary components, normalises the data, and trains a ConvLSTM2D network in TensorFlow. The evaluation scripts compare NMSE with a simulated LS baseline at SNR values of 0, 5, 10, 15 and 20 dB. The uploaded scripts use differing result arrays and a simplified synthetic baseline, so the plots are treated as preliminary experiment outputs rather than independently validated benchmark claims. The broader research also includes related residual-learning exploration, but this particular uploaded code bundle documents the ConvLSTM pipeline.',
    tech:'Python · NumPy · TensorFlow/Keras · ConvLSTM2D · NMSE · SNR · Massive MIMO · Matplotlib',
    resource:'#projects',
    resourceLabel:'Project overview'
  }
};
const modal = $('#projectModal');
$$('.details-btn').forEach(btn => btn.addEventListener('click', () => {
  const p = projectData[btn.dataset.project];
  $('#modalEyebrow').textContent = p.eyebrow;
  $('#modalTitle').textContent = p.title;
  $('#modalDescription').textContent = p.description;
  $('#modalOverview').textContent = p.overview;
  $('#modalTech').textContent = p.tech;
  $('#modalMedia').innerHTML = p.media || '';
  const link = $('#modalResource'); link.href = p.resource; link.textContent = p.resourceLabel + ' ↗';
  modal.classList.add('open'); modal.setAttribute('aria-hidden','false'); document.body.style.overflow='hidden';
}));
function closeModal(){modal.classList.remove('open');modal.setAttribute('aria-hidden','true');document.body.style.overflow=''}
$$('[data-close-modal]').forEach(el=>el.addEventListener('click',closeModal));
document.addEventListener('keydown',e=>{if(e.key==='Escape')closeModal()});

// Progressive gallery: uses existing original portfolio photographs.
let nextPhoto = 6;
$('#loadMorePhotos').addEventListener('click', () => {
  const grid = $('#galleryGrid');
  const end = Math.min(nextPhoto + 6, 47);
  for(let n=nextPhoto;n<end;n++){
    const fig=document.createElement('figure'); fig.className='gallery-item gallery-extra';
    const img=document.createElement('img'); img.src=`assets/${n}.jpg`; img.alt=`Photography gallery image ${n}`; img.loading='lazy';
    img.onerror=()=>fig.remove();
    const cap=document.createElement('figcaption'); cap.textContent=String(n).padStart(2,'0')+' / MOMENT';
    fig.append(img,cap); grid.append(fig);
  }
  nextPhoto=end;
  if(nextPhoto>=47) $('#loadMorePhotos').style.display='none';
});

// Highlight the current section in the navigation.
const sections = $$('main section[id]');
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver(entries => entries.forEach(entry => {
    if(entry.isIntersecting) {
      $$('#nav a').forEach(a=>a.classList.toggle('active',a.getAttribute('href')==='#'+entry.target.id));
    }
  }), {rootMargin:'-35% 0px -55% 0px'});
  sections.forEach(s=>observer.observe(s));
}
