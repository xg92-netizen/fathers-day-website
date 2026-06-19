<script setup>
import { computed, onBeforeUnmount, ref } from 'vue'

const routes = {
  home: '/',
  letter: '/letter',
  wishes: '/wishes',
  card: '/card',
  timeline: '/timeline',
  auth: '/auth',
}

const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL || `${window.location.protocol}//${window.location.hostname}:8000`

const navItems = [
  { key: 'letter', label: '打开这封信', path: routes.letter },
  { key: 'wishes', label: '小小的叮嘱', path: routes.wishes },
  { key: 'card', label: '祝福卡', path: routes.card },
  { key: 'timeline', label: '时光碎片', path: routes.timeline },
]

const homeCards = [
  {
    path: routes.letter,
    title: '一封信',
    text: '把那些一直想说、却很少当面说出口的话，认真写下来。',
  },
  {
    path: routes.wishes,
    title: '几个心愿',
    text: '不是要求你更辛苦，而是希望你更轻松、更健康。',
  },
  {
    path: routes.timeline,
    title: '一些照片',
    text: '旧照片里的瞬间，都是我长大以后才更懂的珍贵。',
  },
]

const homeKeepsakes = [
  {
    label: '01',
    title: '把感谢说得郑重一点',
    text: '不是临时拼凑的祝福，而是认真整理过的心意。',
  },
  {
    label: '02',
    title: '把牵挂放得轻一点',
    text: '愿爸爸能从忙碌里抽身，也把自己照顾好。',
  },
  {
    label: '03',
    title: '把回忆留得久一点',
    text: '照片、话语和那些小瞬间，都值得被慢慢收藏。',
  },
]

const blessings = [
  '父亲节快乐，我最爱的爸爸。',
  '愿我的超人爸爸，岁岁平安，身体健康。',
  '希望你轻松一点，快乐一点，好好爱自己。',
  '谢谢你做我最坚实的后盾，托着我一路往前走。',
]

const dadTags = [
  {
    id: 'gentle',
    label: '温柔',
    note: '藏在细节里',
    title: '你给我的温柔，从来不是一句空话',
    text: '小时候那些零食、小礼物，还有很多被你记在心上的小事，都让我觉得自己一直被好好爱着。',
  },
  {
    id: 'favor',
    label: '偏爱',
    note: '悄悄给了我',
    title: '你把很多偏爱，都悄悄给了我',
    text: '你不一定会把爱说得很明显，但我知道，很多选择、很多承担、很多惦记，最后都落到了我身上。',
  },
  {
    id: 'support',
    label: '后盾',
    note: '一直在身后',
    title: '你一直是我最坚实的后盾',
    text: '我遇到麻烦、不知所措的时候，你总会第一时间帮我想办法。你努力工作、认真生活的样子，也是我一直很敬佩的样子。',
  },
]

const cardThemes = [
  { id: 'sage', label: '青绿', accent: '#476f68' },
  { id: 'gold', label: '暖金', accent: '#b9822e' },
  { id: 'blue', label: '雾蓝', accent: '#466c8f' },
]

const notes = [
  {
    title: '希望你少抽一点烟，少喝一点酒',
    text: '我知道成年人的生活很累，工作有压力，生活有奔波。所以我最朴素的心愿，是希望你好好爱自己。',
  },
  {
    title: '不用一直逞强',
    text: '不用永远做无所不能的超人。你可以好好休息，轻松一点、快乐一点。',
  },
  {
    title: '现在我也开始牵挂你',
    text: '以前一直是你守护我长大，现在我慢慢长大了，也开始学会牵挂你。',
  },
]

const letterMoments = [
  {
    label: '童年的心意',
    text: '你把惦记放进零食、小礼物和很多细小的照顾里。',
  },
  {
    label: '杭州的距离',
    text: '我来到你生活和奋斗的城市，也更真切地看见你的不容易。',
  },
  {
    label: '安稳的底气',
    text: '你默默承担很多，让我可以安心读书、慢慢长大。',
  },
  {
    label: '风雨里的后盾',
    text: '我不知所措的时候，你总会第一时间帮我想办法。',
  },
]

const letterDetails = [
  {
    title: '那些没有说出口的谢谢',
    text: '很多照顾发生得太自然，以前不懂得郑重回应，现在想一件一件记下来。',
  },
  {
    title: '那些被你撑住的日子',
    text: '我能安心往前走，是因为知道身后始终有人替我把风雨挡住。',
  },
  {
    title: '那些以后想还给你的温柔',
    text: '等我再长大一点，也想成为能让你放心、能陪你慢下来的人。',
  },
]

const wishDetails = [
  '愿你不用把所有压力都藏起来。',
  '愿你每天能多一点自己的时间。',
  '愿你身体健康，睡得踏实，心里轻松。',
  '愿你知道，我一直很骄傲你是我的爸爸。',
]

const wishRhythm = [
  '少一点应酬，多一点好好吃饭。',
  '少一点熬夜，多一点真正睡踏实的晚上。',
  '少一点硬撑，多一点可以放心休息的时间。',
]

const cardLines = [
  '你不是只会沉默的人，你只是把爱放进了行动里。',
  '我长大以后才更明白，你以前做过的很多事都很不容易。',
  '谢谢你给我的底气，也谢谢你一直站在我身后。',
]

const cardPromises = [
  '常联系，不让关心只停在节日。',
  '认真生活，让你的辛苦更值得。',
  '慢慢长大，也慢慢学会照顾你。',
]

const memories = [
  {
    image: '/memories/memory-01.jpg',
    title: '掌心里的童年',
    text: '那时我只顾向前，你把每一步都护得安稳。',
  },
  {
    image: '/memories/memory-02.jpg',
    title: '藏在日常里的偏爱',
    text: '那些看似平常的小满足，都是你记在心上的温柔。',
  },
  {
    image: '/memories/memory-03.jpg',
    title: '并肩走过的路',
    text: '小时候以为陪伴理所当然，长大后才懂那份安心难得。',
  },
  {
    image: '/memories/memory-04.jpg',
    title: '背影里的照顾',
    text: '镜头没有拍下太多言语，却留下了你细致的惦念。',
  },
  {
    image: '/memories/memory-05.jpg',
    title: '旅途中的晴光',
    text: '普通的一天，因为有你在身边，后来都成了值得珍藏的片段。',
  },
  {
    image: '/memories/memory-06.jpg',
    title: '镜头前的郑重',
    text: '照片定格的是一瞬间，也定格了你认真做父亲的样子。',
  },
  {
    image: '/memories/memory-07.jpg',
    title: '身后的目光',
    text: '我在前面笑着长大，你在身后安静地托住整个世界。',
  },
]

const memoryIndex = [
  { value: '7', label: '张照片' },
  { value: '4', label: '段成长' },
  { value: '1', label: '份心意' },
]

const authSteps = [
  '确认身份',
  '打开信件',
  '进入回忆',
]

const registeredUsers = ref(readRegisteredUsers())
const savedUser = readSavedUser()
const validSavedUser = savedUser && savedUser.username && savedUser.phone
const isAuthenticated = ref(Boolean(validSavedUser))
const authUser = ref(validSavedUser ? savedUser : null)
const initialPath = normalizePath(window.location.pathname)
const currentPath = ref(isAuthenticated.value ? initialPath : routes.auth)
const blessingIndex = ref(0)
const activeTheme = ref(cardThemes[0])
const activeTag = ref(dadTags[0])
const activeNote = ref(0)
const activeMemory = ref(0)
const selectedCardLine = ref(cardLines[0])
const pointer = ref({
  x: 50,
  y: 50,
})
const authMode = ref('login')
const authForm = ref({
  username: '',
  phone: '',
})
const authSubmitted = ref(false)
const authError = ref('')
const authLoading = ref(false)
const isMusicPlaying = ref(false)
const musicError = ref('')

let audioContext = null
let musicGain = null
let musicTimer = null
let chordIndex = 0

const gentleChords = [
  [196, 246.94, 293.66],
  [174.61, 220, 261.63],
  [164.81, 196, 246.94],
  [146.83, 196, 220],
]

if (!isAuthenticated.value && initialPath !== routes.auth) {
  window.history.replaceState({}, '', routes.auth)
}

if (savedUser && !validSavedUser) {
  window.localStorage.removeItem('fathersDayUser')
}

const currentPage = computed(() => {
  if (currentPath.value === routes.letter) return 'letter'
  if (currentPath.value === routes.wishes) return 'wishes'
  if (currentPath.value === routes.card) return 'card'
  if (currentPath.value === routes.timeline) return 'timeline'
  if (currentPath.value === routes.auth) return 'auth'
  return 'home'
})

function normalizePath(path) {
  const normalized = path.replace(/\/+$/, '') || '/'
  return Object.values(routes).includes(normalized) ? normalized : '/'
}

function readSavedUser() {
  try {
    const value = window.localStorage.getItem('fathersDayUser')
    return value ? JSON.parse(value) : null
  } catch {
    return null
  }
}

function readRegisteredUsers() {
  try {
    const value = window.localStorage.getItem('fathersDayRegisteredUsers')
    return value ? JSON.parse(value) : []
  } catch {
    return []
  }
}

function saveRegisteredUsers(users) {
  window.localStorage.setItem('fathersDayRegisteredUsers', JSON.stringify(users))
}

function isValidPhone(phone) {
  return /^1[3-9]\d{9}$/.test(phone)
}

async function requestEnterApi(action, userInfo) {
  const response = await fetch(`${API_BASE_URL}/api/enter/${action}/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(userInfo),
  })
  const result = await response.json()

  if (!response.ok || !result.success) {
    throw new Error(result.message || '提交失败，请稍后再试。')
  }

  return result.data
}

function navigate(path) {
  const normalized = normalizePath(path)
  if (!isAuthenticated.value && normalized !== routes.auth) {
    window.history.pushState({}, '', routes.auth)
    currentPath.value = routes.auth
    window.scrollTo({ top: 0, behavior: 'smooth' })
    return
  }
  if (normalized === currentPath.value) return
  window.history.pushState({}, '', normalized)
  currentPath.value = normalized
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

function onNav(event, path) {
  event.preventDefault()
  navigate(path)
}

function nextBlessing() {
  blessingIndex.value = (blessingIndex.value + 1) % blessings.length
}

function trackPointer(event) {
  pointer.value = {
    x: Number(((event.clientX / window.innerWidth) * 100).toFixed(2)),
    y: Number(((event.clientY / window.innerHeight) * 100).toFixed(2)),
  }
}

async function submitAuth() {
  authError.value = ''
  authSubmitted.value = false

  if (!isValidPhone(authForm.value.phone)) {
    authError.value = '请输入正确的 11 位手机号。'
    return
  }

  const userInfo = {
    username: authForm.value.username,
    phone: authForm.value.phone,
  }

  authLoading.value = true

  if (authMode.value === 'register') {
    try {
      const savedUser = await requestEnterApi('register', userInfo)
      registeredUsers.value = [...registeredUsers.value, savedUser]
      saveRegisteredUsers(registeredUsers.value)
      authUser.value = savedUser
      window.localStorage.setItem('fathersDayUser', JSON.stringify(savedUser))
      isAuthenticated.value = true
      authSubmitted.value = true
      navigate(routes.home)
    } catch (error) {
      authError.value = error.message
    } finally {
      authLoading.value = false
    }
    return
  }

  try {
    const matchedUser = await requestEnterApi('login', userInfo)
    authUser.value = matchedUser
    window.localStorage.setItem('fathersDayUser', JSON.stringify(matchedUser))
    isAuthenticated.value = true
    authSubmitted.value = true
    navigate(routes.home)
  } catch (error) {
    authError.value = error.message
  } finally {
    authLoading.value = false
  }
}

function switchAuthMode(mode) {
  authMode.value = mode
  authSubmitted.value = false
  authError.value = ''
}

function createMusicContext() {
  const AudioContext = window.AudioContext || window.webkitAudioContext
  if (!AudioContext) {
    musicError.value = '当前浏览器不支持背景音乐。'
    return false
  }

  if (!audioContext) {
    audioContext = new AudioContext()
    musicGain = audioContext.createGain()
    musicGain.gain.value = 0.045
    musicGain.connect(audioContext.destination)
  }

  return true
}

function playTone(frequency, startTime, duration, volume) {
  const oscillator = audioContext.createOscillator()
  const gain = audioContext.createGain()

  oscillator.type = 'sine'
  oscillator.frequency.setValueAtTime(frequency, startTime)
  gain.gain.setValueAtTime(0.0001, startTime)
  gain.gain.linearRampToValueAtTime(volume, startTime + 0.9)
  gain.gain.setValueAtTime(volume, startTime + duration - 1.2)
  gain.gain.linearRampToValueAtTime(0.0001, startTime + duration)

  oscillator.connect(gain)
  gain.connect(musicGain)
  oscillator.start(startTime)
  oscillator.stop(startTime + duration + 0.1)
}

function scheduleGentleChord() {
  if (!isMusicPlaying.value || !audioContext) return

  const startTime = audioContext.currentTime + 0.08
  const chord = gentleChords[chordIndex % gentleChords.length]

  chord.forEach((frequency, index) => {
    playTone(frequency, startTime + index * 0.18, 5.8, 0.16)
    playTone(frequency * 2, startTime + 1.2 + index * 0.2, 4.2, 0.035)
  })

  chordIndex += 1
  musicTimer = window.setTimeout(scheduleGentleChord, 5200)
}

async function toggleMusic() {
  musicError.value = ''

  if (isMusicPlaying.value) {
    isMusicPlaying.value = false
    window.clearTimeout(musicTimer)
    musicTimer = null
    musicGain?.gain.linearRampToValueAtTime(0.0001, audioContext.currentTime + 0.35)
    return
  }

  if (!createMusicContext()) return

  try {
    await audioContext.resume()
    musicGain.gain.cancelScheduledValues(audioContext.currentTime)
    musicGain.gain.setValueAtTime(0.0001, audioContext.currentTime)
    musicGain.gain.linearRampToValueAtTime(0.045, audioContext.currentTime + 0.8)
    isMusicPlaying.value = true
    scheduleGentleChord()
  } catch {
    musicError.value = '音乐暂时无法播放，请再点一次试试。'
  }
}

window.onpopstate = () => {
  const normalized = normalizePath(window.location.pathname)
  if (!isAuthenticated.value && normalized !== routes.auth) {
    window.history.replaceState({}, '', routes.auth)
    currentPath.value = routes.auth
    return
  }
  currentPath.value = normalized
}

function logout() {
  window.localStorage.removeItem('fathersDayUser')
  isAuthenticated.value = false
  authUser.value = null
  authSubmitted.value = false
  authError.value = ''
  authForm.value = {
    username: '',
    phone: '',
  }
  navigate(routes.auth)
}

onBeforeUnmount(() => {
  window.clearTimeout(musicTimer)
  audioContext?.close()
})
</script>

<template>
  <main
    :style="{ '--pointer-x': `${pointer.x}%`, '--pointer-y': `${pointer.y}%` }"
    @pointermove="trackPointer"
  >
    <div class="ambient-decor" aria-hidden="true">
      <span class="ambient-dot dot-one"></span>
      <span class="ambient-dot dot-two"></span>
      <span class="ambient-dot dot-three"></span>
      <span class="ambient-ribbon ribbon-one"></span>
      <span class="ambient-ribbon ribbon-two"></span>
      <span class="ambient-particle particle-one"></span>
      <span class="ambient-particle particle-two"></span>
      <span class="ambient-particle particle-three"></span>
      <span class="ambient-particle particle-four"></span>
    </div>
    <div class="editorial-collage" aria-hidden="true">
      <figure class="editorial-photo editorial-photo-one">
        <img src="/editorial/paper-light.jpg" alt="" />
      </figure>
      <figure class="editorial-photo editorial-photo-two">
        <img src="/editorial/book-coffee.jpg" alt="" />
      </figure>
      <figure class="editorial-photo editorial-photo-three">
        <img src="/editorial/camera-table.jpg" alt="" />
      </figure>
      <figure class="editorial-photo editorial-photo-four">
        <img src="/editorial/autumn-book.jpg" alt="" />
      </figure>
    </div>

    <nav class="nav site-nav" aria-label="主导航">
      <a class="brand" href="/" aria-label="父亲节网页首页" @click="onNav($event, routes.home)">
        <img class="brand-logo" src="/fathers-day-logo.svg" alt="Father's Day" />
      </a>
      <div v-if="isAuthenticated" class="nav-links">
        <a
          v-for="item in navItems"
          :key="item.key"
          :href="item.path"
          :class="{ active: currentPage === item.key }"
          @click="onNav($event, item.path)"
        >
          {{ item.label }}
        </a>
        <button class="logout-button" type="button" @click="logout">
          退出
        </button>
      </div>
      <div v-else class="nav-status">
        请先登录
      </div>
    </nav>
    <div class="music-panel">
      <button
        class="music-toggle"
        type="button"
        :class="{ active: isMusicPlaying }"
        :aria-pressed="isMusicPlaying"
        :title="isMusicPlaying ? '关闭背景音乐' : '播放背景音乐'"
        @click="toggleMusic"
      >
        <span class="music-icon" aria-hidden="true"></span>
        <span>{{ isMusicPlaying ? '音乐正在播放' : '点我播放轻音乐' }}</span>
      </button>
      <p v-if="musicError" class="music-error" role="status">
        {{ musicError }}
      </p>
    </div>

    <section v-if="currentPage === 'home'" class="hero page-view">
      <div class="page-motion home-motion" aria-hidden="true">
        <span></span>
        <span></span>
        <span></span>
      </div>
      <div class="hero-illustration" aria-hidden="true">
        <span class="paper paper-large"></span>
        <span class="paper paper-small"></span>
        <span class="seal"></span>
        <span class="moon"></span>
        <span class="star star-one"></span>
        <span class="star star-two"></span>
      </div>
      <div class="hero-content">
        <p class="eyebrow">For My Dad</p>
        <h1>致我最了不起的爸爸</h1>
        <p class="hero-lede">
          别人的父爱藏在沉默里，而你的爱，贯穿了我整个成长岁月，从来没有缺席。
        </p>
        <div class="hero-actions">
          <a class="button primary" href="/letter" @click="onNav($event, routes.letter)">读这封信</a>
          <a class="button secondary" href="/timeline" @click="onNav($event, routes.timeline)">看时光碎片</a>
        </div>
      </div>

      <div class="date-card" aria-label="父亲节日期">
        <span>Father's Day</span>
        <strong>06.21</strong>
        <small>送给爸爸的小网页</small>
      </div>

      <div class="home-entry-grid" aria-label="页面入口">
        <a
          v-for="(card, index) in homeCards"
          :key="card.path"
          :href="card.path"
          :class="`home-card-${index + 1}`"
          @click="onNav($event, card.path)"
        >
          <span>{{ card.title }}</span>
          <p>{{ card.text }}</p>
        </a>
      </div>

      <div class="home-keepsakes" aria-label="这份网页想留下的心意">
        <article v-for="item in homeKeepsakes" :key="item.title">
          <span>{{ item.label }}</span>
          <h3>{{ item.title }}</h3>
          <p>{{ item.text }}</p>
        </article>
      </div>
    </section>

    <section v-else-if="currentPage === 'letter'" class="intro band page-view">
      <div class="page-motion letter-motion" aria-hidden="true">
        <span></span>
        <span></span>
      </div>
      <div class="letter-backdrop" aria-hidden="true">
        <figure class="letter-photo-layer layer-book">
          <img src="/editorial/book-coffee.jpg" alt="" />
        </figure>
        <figure class="letter-photo-layer layer-envelope">
          <img src="/letter-photos/envelope.jpg" alt="" />
        </figure>
        <figure class="letter-photo-layer layer-light">
          <img src="/editorial/autumn-book.jpg" alt="" />
        </figure>
        <span class="letter-paper paper-a"></span>
        <span class="letter-paper paper-b"></span>
        <span class="letter-postmark"></span>
        <span class="letter-thread"></span>
      </div>
      <div class="section-heading">
        <p class="eyebrow">Dear Dad</p>
        <h2>这封信，写给你</h2>
      </div>
      <div class="letter-visual-strip" aria-hidden="true">
        <div class="visual-tile photo-tile envelope-photo">
          <img src="/letter-photos/envelope.jpg" alt="" />
        </div>
        <div class="visual-tile photo-tile city-photo">
          <img src="/letter-photos/city-water.jpg" alt="" />
        </div>
        <div class="visual-tile photo-tile book-photo">
          <img src="/letter-photos/open-book.jpg" alt="" />
        </div>
      </div>
      <div class="letter-card">
        <p>
          我的童年，一直都有你的温柔。小时候你总把惦记化作满满的心意，一箱箱零食、一件件小礼物，悄悄填满了我的童年时光。你一直用心宠爱我，让我从小到大，都活得很有底气。
        </p>
        <p>
          今年我来到杭州读大学，来到了你生活、奋斗的城市。距离变近了，你的照顾也从未停下。
        </p>
        <p>
          大学里的很多事情，你都默默替我操心，让我可以安心读书、无忧无虑地成长。我在陌生的城市遇到麻烦、不知所措的时候，永远是你第一时间帮我解决问题，替我挡风遮雨。空闲的时候你会带我吃饭、关心我的生活、叮嘱我的学业，细致又温柔。
        </p>
        <p>
          在我心里，你是真的超级厉害。你努力工作、认真生活，凭自己的能力撑起一切，是我从小到大最敬佩、最骄傲的人。你不善言辞，却把最好的生活、最多的偏爱，全都给了我。
        </p>
      </div>

      <div class="letter-moments" aria-label="信里的片段">
        <article
          v-for="(moment, index) in letterMoments"
          :key="moment.label"
          :class="`moment-card-${index + 1}`"
        >
          <span>{{ moment.label }}</span>
          <p>{{ moment.text }}</p>
        </article>
      </div>

      <div class="tag-panel letter-tags">
        <div class="tag-buttons" aria-label="关于爸爸的选择">
          <button
            v-for="(tag, index) in dadTags"
            :key="tag.id"
            type="button"
            :class="{ active: activeTag.id === tag.id }"
            @click="activeTag = tag"
          >
            <span class="tag-index">{{ String(index + 1).padStart(2, '0') }}</span>
            <span class="tag-name">{{ tag.label }}</span>
            <small>{{ tag.note }}</small>
          </button>
        </div>
        <article class="tag-card">
          <span>你在我心里的样子</span>
          <h3>{{ activeTag.title }}</h3>
          <p>{{ activeTag.text }}</p>
        </article>
      </div>

      <div class="letter-deepening" aria-label="信里更想说的话">
        <article v-for="detail in letterDetails" :key="detail.title">
          <span></span>
          <h3>{{ detail.title }}</h3>
          <p>{{ detail.text }}</p>
        </article>
      </div>
    </section>

    <section v-else-if="currentPage === 'wishes'" class="notes-section page-view">
      <div class="page-motion wishes-motion" aria-hidden="true">
        <span></span>
        <span></span>
        <span></span>
      </div>
      <div class="section-heading">
        <p class="eyebrow">My Wishes</p>
        <h2>我最朴素的心愿</h2>
      </div>
      <div class="wish-illustration">
        <div class="wish-photo-card" aria-hidden="true">
          <img src="/wishes/rest-moment.jpg" alt="" />
        </div>
        <div class="wish-hero-copy">
          <span>给爸爸的一点叮嘱</span>
          <p>希望你的日子不总是紧绷着，也能留一点轻松给自己。</p>
        </div>
        <div class="wish-meter" aria-label="心愿清单">
          <button
            v-for="(note, index) in notes"
            :key="note.title"
            type="button"
            :class="{ active: activeNote === index }"
            @click="activeNote = index"
          >
            <span>{{ `0${index + 1}` }}</span>
            {{ note.title }}
          </button>
        </div>
      </div>
      <div class="note-board">
        <div class="note-tabs" aria-label="几句话">
          <button
            v-for="(note, index) in notes"
            :key="note.title"
            type="button"
            :class="{ active: activeNote === index }"
            @click="activeNote = index"
          >
            {{ index + 1 }}
          </button>
        </div>
        <article class="note-card">
          <span>写给爸爸</span>
          <h3>{{ notes[activeNote].title }}</h3>
          <p>{{ notes[activeNote].text }}</p>
        </article>
      </div>
      <div class="wish-grid">
        <article v-for="(item, index) in wishDetails" :key="item" :class="`wish-card-${index + 1}`">
          <span>愿</span>
          <p>{{ item }}</p>
        </article>
      </div>
      <div class="wish-rhythm" aria-label="给爸爸的日常提醒">
        <article v-for="(item, index) in wishRhythm" :key="item">
          <span>{{ String(index + 1).padStart(2, '0') }}</span>
          <p>{{ item }}</p>
        </article>
      </div>
    </section>

    <section v-else-if="currentPage === 'card'" class="card-maker page-view">
      <div class="page-motion card-motion" aria-hidden="true">
        <span></span>
        <span></span>
      </div>
      <div class="card-sky" aria-hidden="true">
        <span></span>
        <span></span>
        <span></span>
      </div>
      <div class="card-copy">
        <p class="eyebrow">Blessing Card</p>
        <h2>最后，想把祝福郑重送给你</h2>
        <p>可以换一种颜色，也可以点一下面的按钮，看看下一句。</p>
        <div class="swatches" aria-label="卡片颜色">
          <button
            v-for="theme in cardThemes"
            :key="theme.id"
            type="button"
            :class="{ active: activeTheme.id === theme.id }"
            :style="{ '--swatch': theme.accent }"
            @click="activeTheme = theme"
          >
            {{ theme.label }}
          </button>
        </div>
        <button class="button primary" type="button" @click="nextBlessing">换一句</button>
        <div class="line-picker" aria-label="补充祝福">
          <button
            v-for="line in cardLines"
            :key="line"
            type="button"
            :class="{ active: selectedCardLine === line }"
            @click="selectedCardLine = line"
          >
            {{ line }}
          </button>
        </div>
      </div>
      <div class="preview-card" :style="{ '--accent': activeTheme.accent }">
        <span>To 爸爸</span>
        <strong>{{ blessings[blessingIndex] }}</strong>
        <p>{{ selectedCardLine }}</p>
        <small>Happy Father's Day</small>
      </div>
      <div class="card-promises" aria-label="写在祝福卡背面的几句话">
        <article v-for="promise in cardPromises" :key="promise">
          <span></span>
          <p>{{ promise }}</p>
        </article>
      </div>
    </section>

    <section v-else-if="currentPage === 'timeline'" class="timeline-page page-view">
      <div class="film-strip" aria-hidden="true"></div>
      <div class="memory-backdrop" aria-hidden="true">
        <span class="memory-glow glow-one"></span>
        <span class="memory-glow glow-two"></span>
        <span class="memory-thread thread-one"></span>
        <span class="memory-thread thread-two"></span>
        <span class="memory-stamp"></span>
      </div>
      <div class="section-heading">
        <p class="eyebrow">Memory Pieces</p>
        <h2>时光碎片</h2>
      </div>
      <div class="timeline-layout">
        <article class="memory-feature">
          <img :src="memories[activeMemory].image" :alt="memories[activeMemory].title" />
          <div>
            <span>{{ String(activeMemory + 1).padStart(2, '0') }}</span>
            <h3>{{ memories[activeMemory].title }}</h3>
            <p>{{ memories[activeMemory].text }}</p>
          </div>
        </article>
        <div class="memory-grid" aria-label="时光照片">
          <button
            v-for="(memory, index) in memories"
            :key="memory.image"
            type="button"
            :class="{ active: activeMemory === index }"
            @click="activeMemory = index"
          >
            <img :src="memory.image" :alt="memory.title" />
          </button>
        </div>
      </div>
      <div class="memory-captions">
        <article v-for="(memory, index) in memories" :key="memory.title">
          <span>{{ String(index + 1).padStart(2, '0') }}</span>
          <p>{{ memory.title }}</p>
        </article>
      </div>
      <div class="memory-index" aria-label="回忆索引">
        <article v-for="item in memoryIndex" :key="item.label">
          <strong>{{ item.value }}</strong>
          <span>{{ item.label }}</span>
        </article>
        <p>这些片段不负责讲完全部故事，只负责提醒我：那些被你守着长大的日子，一直都在。</p>
      </div>
    </section>

    <section v-else-if="currentPage === 'auth'" class="auth-page page-view">
      <div class="auth-backdrop" aria-hidden="true">
        <span class="auth-paper paper-one"></span>
        <span class="auth-paper paper-two"></span>
        <span class="auth-orbit"></span>
        <span class="auth-spark spark-one"></span>
        <span class="auth-spark spark-two"></span>
      </div>
      <div class="auth-illustration" aria-hidden="true">
        <span class="lock-body"></span>
        <span class="lock-ring"></span>
        <span class="key-line"></span>
      </div>
      <div class="auth-copy">
        <p class="eyebrow">Sign In</p>
        <h2>进入这份父亲节网页</h2>
        <p>
          这个网页想保留一点神秘感。第一次进入要先注册用户名和电话，之后用同一组信息登录，才能打开这封信、祝福卡和时光碎片。
        </p>
        <div class="auth-note">
          <span>Private Letter</span>
          <strong>只留给最重要的人</strong>
        </div>
        <div class="auth-badges">
          <span>登录后进入</span>
          <span>用户名</span>
          <span>电话</span>
        </div>
      </div>

      <form class="auth-form" @submit.prevent="submitAuth">
        <div class="mode-switch" aria-label="登录注册切换">
          <button type="button" :class="{ active: authMode === 'login' }" @click="switchAuthMode('login')">
            登录
          </button>
          <button type="button" :class="{ active: authMode === 'register' }" @click="switchAuthMode('register')">
            注册
          </button>
        </div>
        <label>
          用户名
          <input v-model.trim="authForm.username" type="text" name="username" required placeholder="请输入用户名" />
        </label>
        <label>
          电话
          <input
            v-model.trim="authForm.phone"
            type="tel"
            name="phone"
            required
            inputmode="numeric"
            maxlength="11"
            pattern="1[3-9][0-9]{9}"
            placeholder="请输入 11 位手机号"
          />
        </label>
        <button class="button primary" type="submit" :disabled="authLoading">
          {{ authLoading ? '提交中...' : authMode === 'login' ? '登录并进入' : '注册并进入' }}
        </button>
        <p v-if="authError" class="form-error">
          {{ authError }}
        </p>
        <p v-if="authSubmitted" class="form-result">
          {{ authMode === 'login' ? '登录' : '注册' }}信息已提交：{{ authForm.username }} / {{ authForm.phone }}
        </p>
      </form>
      <div class="auth-steps" aria-label="进入网页的步骤">
        <article v-for="(step, index) in authSteps" :key="step">
          <span>{{ String(index + 1).padStart(2, '0') }}</span>
          <p>{{ step }}</p>
        </article>
      </div>
    </section>
  </main>
</template>
