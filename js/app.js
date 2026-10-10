// THE ACADEMIC TIMES & THE JUNIOR - Master Interactive Controller
// Features: Dynamic Continuous Audio Sequencer, Dialogue Continuous Play, Speed Control,
// Sticky Article Header, Table of Contents, Mobile Tooltips, Interactive Quiz with Score & Retry,
// Japanese Translation Toggle, Keyboard Navigation

document.addEventListener('DOMContentLoaded', () => {
  let currentAudio = null;
  let currentActiveBtn = null;
  let isSequencePlaying = false;
  let activePlaylist = [];
  let sequenceIndex = 0;
  let currentPlaybackRate = 1.0;
  let activeMasterBtn = null;

  // ==========================================================================
  // 1. SPEED CONTROLLER (0.8x, 1.0x, 1.2x, 1.5x)
  // ==========================================================================
  window.setSpeed = function(rate, btnElement) {
    currentPlaybackRate = parseFloat(rate);
    if (currentAudio) {
      try {
        currentAudio.playbackRate = currentPlaybackRate;
      } catch (e) {}
    }
    document.querySelectorAll('.btn-speed-opt').forEach(btn => {
      const bSpeed = parseFloat(btn.getAttribute('data-speed'));
      btn.classList.toggle('active-speed', bSpeed === currentPlaybackRate);
    });
  };

  document.querySelectorAll('.btn-speed-opt').forEach(btn => {
    btn.addEventListener('click', () => {
      const rate = btn.getAttribute('data-speed');
      window.setSpeed(rate, btn);
    });
  });

  // ==========================================================================
  // 2. CORE AUDIO PLAYBACK
  // ==========================================================================
  window.stopAllAudio = function() {
    if (currentAudio) {
      currentAudio.pause();
      currentAudio.currentTime = 0;
      currentAudio = null;
    }
    if (currentActiveBtn) {
      currentActiveBtn.classList.remove('playing');
      const icon = currentActiveBtn.querySelector('.audio-state-icon');
      if (icon) icon.textContent = '▶';
      currentActiveBtn = null;
    }
    document.querySelectorAll('.dlg-turn').forEach(el => el.classList.remove('active-turn'));
    document.querySelectorAll('.article-sentence').forEach(el => el.classList.remove('sentence-playing', 'playing'));
    const headlineBlock = document.getElementById('article-headline-block');
    if (headlineBlock) headlineBlock.classList.remove('active-turn');

    if (activeMasterBtn) {
      activeMasterBtn.classList.remove('playing');
      const icon = activeMasterBtn.querySelector('.audio-state-icon');
      if (icon) icon.textContent = '▶';
      const label = activeMasterBtn.querySelector('.audio-btn-label');
      if (label) label.textContent = '英語朗読 ＋ 日本語対話解説を続けて聴く';
      activeMasterBtn = null;
    }
    isSequencePlaying = false;
  };

  window.playAudio = function(src, btnElement, onEndedCallback) {
    if (currentAudio && currentActiveBtn === btnElement && !currentAudio.paused) {
      window.stopAllAudio();
      return;
    }
    window.stopAllAudio();

    const audio = new Audio(src);
    audio.playbackRate = currentPlaybackRate;
    currentAudio = audio;
    currentActiveBtn = btnElement;

    if (btnElement) {
      btnElement.classList.add('playing');
      const icon = btnElement.querySelector('.audio-state-icon');
      if (icon) icon.textContent = '⏸';
    }

    audio.play().catch(e => {
      console.warn("Audio playback interrupted or failed:", e);
      if (onEndedCallback) onEndedCallback();
    });

    audio.addEventListener('ended', () => {
      if (btnElement) {
        btnElement.classList.remove('playing');
        const icon = btnElement.querySelector('.audio-state-icon');
        if (icon) icon.textContent = '▶';
      }
      currentAudio = null;
      currentActiveBtn = null;
      if (onEndedCallback) onEndedCallback();
    });
  };

  // ==========================================================================
  // 3. DYNAMIC CONTINUOUS PLAYLIST SEQUENCER
  // ==========================================================================
  function buildDynamicPlaylist(onlyDialogue = false) {
    const list = [];
    if (!onlyDialogue) {
      const headlineBlock = document.getElementById('article-headline-block');
      list.push({
        src: 'audio/headline.mp3',
        targetId: 'article-headline-block',
        label: 'タイトル朗読'
      });
      list.push({
        src: 'audio/full_body.mp3',
        targetId: 'full-body-banner',
        label: '英文本文朗読'
      });
    }

    const dlgTurns = document.querySelectorAll('.dlg-turn');
    dlgTurns.forEach((turn, idx) => {
      const playBtn = turn.querySelector('[data-dlg-audio]');
      if (!playBtn) return;
      const audioSrc = playBtn.getAttribute('data-dlg-audio');
      const nameEl = turn.querySelector('.dlg-name');
      const speakerName = nameEl ? nameEl.textContent.trim() : `解説 ${idx + 1}`;
      list.push({
        src: audioSrc,
        targetId: turn.id || `dlg-${idx + 1}`,
        label: speakerName,
        turnElement: turn
      });
    });
    return list;
  }

  function playSequenceStep(index, masterBtn) {
    if (!isSequencePlaying || index >= activePlaylist.length) {
      window.stopAllAudio();
      return;
    }

    sequenceIndex = index;
    const item = activePlaylist[index];

    // Reset visual highlights
    document.querySelectorAll('.dlg-turn').forEach(el => el.classList.remove('active-turn'));
    const headlineBlock = document.getElementById('article-headline-block');
    if (headlineBlock) headlineBlock.classList.remove('active-turn');

    const targetEl = document.getElementById(item.targetId);
    if (targetEl) {
      targetEl.classList.add('active-turn');
      targetEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }

    if (masterBtn) {
      const label = masterBtn.querySelector('.audio-btn-label');
      if (label) {
        label.textContent = `再生中: ${item.label} (${index + 1}/${activePlaylist.length})`;
      }
    }

    const audio = new Audio(item.src);
    audio.playbackRate = currentPlaybackRate;
    currentAudio = audio;

    audio.play().catch(e => {
      console.warn("Sequence audio missing or interrupted, skipping to next:", item.src, e);
      // Automatically advance to next track if missing (e.g. headline.mp3)
      setTimeout(() => {
        if (isSequencePlaying) playSequenceStep(index + 1, masterBtn);
      }, 300);
    });

    audio.addEventListener('ended', () => {
      setTimeout(() => {
        if (isSequencePlaying) {
          playSequenceStep(index + 1, masterBtn);
        }
      }, 400);
    });
  }

  const continuousBtn = document.getElementById('btn-play-continuous');
  if (continuousBtn) {
    continuousBtn.addEventListener('click', () => {
      if (isSequencePlaying && activeMasterBtn === continuousBtn) {
        window.stopAllAudio();
        return;
      }

      window.stopAllAudio();
      isSequencePlaying = true;
      activeMasterBtn = continuousBtn;
      activePlaylist = buildDynamicPlaylist(false);

      continuousBtn.classList.add('playing');
      const icon = continuousBtn.querySelector('.audio-state-icon');
      if (icon) icon.textContent = '⏸';

      playSequenceStep(0, continuousBtn);
    });
  }

  const dialogueContinuousBtn = document.getElementById('btn-play-dialogue-all');
  if (dialogueContinuousBtn) {
    dialogueContinuousBtn.addEventListener('click', () => {
      if (isSequencePlaying && activeMasterBtn === dialogueContinuousBtn) {
        window.stopAllAudio();
        return;
      }

      window.stopAllAudio();
      isSequencePlaying = true;
      activeMasterBtn = dialogueContinuousBtn;
      activePlaylist = buildDynamicPlaylist(true);

      dialogueContinuousBtn.classList.add('playing');
      const icon = dialogueContinuousBtn.querySelector('.audio-state-icon');
      if (icon) icon.textContent = '⏸';

      playSequenceStep(0, dialogueContinuousBtn);
    });
  }

  // Individual sentence click-to-play
  document.querySelectorAll('[data-sentence-audio]').forEach(btn => {
    btn.addEventListener('click', (e) => {
      if (e.target.closest('.tooltip-bubble')) return;
      const src = btn.getAttribute('data-sentence-audio');
      window.playAudio(src, btn, () => {
        btn.classList.remove('sentence-playing', 'playing');
      });
      btn.classList.add('sentence-playing');
    });
  });

  // Individual dialogue click-to-play
  document.querySelectorAll('[data-dlg-audio]').forEach(btn => {
    btn.addEventListener('click', () => {
      const src = btn.getAttribute('data-dlg-audio');
      const turnEl = btn.closest('.dlg-turn');
      
      document.querySelectorAll('.dlg-turn').forEach(el => el.classList.remove('active-turn'));
      if (turnEl) turnEl.classList.add('active-turn');

      window.playAudio(src, btn, () => {
        if (turnEl) turnEl.classList.remove('active-turn');
      });
    });
  });

  const fullAudioBtn = document.getElementById('btn-play-full');
  if (fullAudioBtn) {
    fullAudioBtn.addEventListener('click', () => {
      const src = fullAudioBtn.getAttribute('data-audio-src');
      window.playAudio(src, fullAudioBtn);
    });
  }

  // ==========================================================================
  // 4. JAPANESE TRANSLATION TOGGLE
  // ==========================================================================
  const toggleJaBtn = document.getElementById('btn-toggle-ja');
  let areTranslationsVisible = false;

  if (toggleJaBtn) {
    toggleJaBtn.addEventListener('click', () => {
      areTranslationsVisible = !areTranslationsVisible;
      document.querySelectorAll('.ja-translation').forEach(el => {
        if (areTranslationsVisible) {
          el.classList.add('revealed');
        } else {
          el.classList.remove('revealed');
        }
      });
      toggleJaBtn.classList.toggle('active-ja', areTranslationsVisible);
      const label = toggleJaBtn.querySelector('.toggle-ja-label');
      if (label) {
        label.textContent = areTranslationsVisible ? '日本語訳を隠す' : '日本語訳を表示する';
      }
    });
  }

  // Click individual sentence block to toggle that sentence's translation
  document.querySelectorAll('.en-sentence-block').forEach(block => {
    block.addEventListener('click', (e) => {
      if (e.target.closest('button') || e.target.closest('.vocab-tip')) return;
      const jaTrans = block.querySelector('.ja-translation');
      if (jaTrans) {
        jaTrans.classList.toggle('revealed');
      }
    });
  });

  // ==========================================================================
  // 5. STICKY ARTICLE TITLE BAR & READING PROGRESS TRACKER
  // ==========================================================================
  const stickyBar = document.getElementById('sticky-article-bar');
  const progressBar = document.getElementById('reading-progress');
  const mainHeader = document.querySelector('.article-header') || document.querySelector('.hero-header');

  window.addEventListener('scroll', () => {
    const scrollY = window.scrollY || window.pageYOffset;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    
    if (progressBar && docHeight > 0) {
      const progressPercent = Math.min(100, Math.max(0, (scrollY / docHeight) * 100));
      progressBar.style.width = `${progressPercent}%`;
    }

    if (stickyBar) {
      const headerThreshold = mainHeader ? (mainHeader.offsetTop + mainHeader.offsetHeight) : 280;
      if (scrollY > headerThreshold) {
        stickyBar.classList.add('visible');
      } else {
        stickyBar.classList.remove('visible');
      }
    }
  }, { passive: true });

  // ==========================================================================
  // 6. FLOATING TABLE OF CONTENTS (TOC)
  // ==========================================================================
  const tocBtn = document.getElementById('btn-floating-toc');
  const tocPanel = document.getElementById('floating-toc-panel');

  if (tocBtn && tocPanel) {
    tocBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      tocPanel.classList.toggle('active');
    });

    document.querySelectorAll('.toc-link').forEach(link => {
      link.addEventListener('click', () => {
        tocPanel.classList.remove('active');
      });
    });

    document.addEventListener('click', (e) => {
      if (!tocPanel.contains(e.target) && e.target !== tocBtn) {
        tocPanel.classList.remove('active');
      }
    });
  }

  // ==========================================================================
  // 7. VOCABULARY TOOLTIPS (Tap support for Touch / Mobile)
  // ==========================================================================
  document.querySelectorAll('.vocab-tip').forEach(tip => {
    tip.addEventListener('click', (e) => {
      e.stopPropagation();
      const isAlreadyOpen = tip.classList.contains('show-tip');
      document.querySelectorAll('.vocab-tip').forEach(t => t.classList.remove('show-tip'));
      if (!isAlreadyOpen) {
        tip.classList.add('show-tip');
      }
    });
  });

  document.addEventListener('click', () => {
    document.querySelectorAll('.vocab-tip').forEach(t => t.classList.remove('show-tip'));
  });

  // ==========================================================================
  // 8. INTERACTIVE QUIZ ENGINE WITH SCORE TALLY & RETRY
  // ==========================================================================
  const quizItems = document.querySelectorAll('.quiz-item, .quiz-card');
  const quizSection = document.getElementById('section-quiz');

  function updateQuizSummary() {
    if (!quizSection || quizItems.length === 0) return;
    const answeredCount = Array.from(quizItems).filter(item => item.dataset.answered === "true").length;
    const correctCount = Array.from(quizItems).filter(item => item.dataset.correctAnswered === "true").length;

    let banner = document.getElementById('quiz-completion-banner');
    if (answeredCount === quizItems.length) {
      if (!banner) {
        banner = document.createElement('div');
        banner.id = 'quiz-completion-banner';
        banner.className = 'quiz-completion-banner';
        quizSection.appendChild(banner);
      }
      const percent = Math.round((correctCount / quizItems.length) * 100);
      banner.innerHTML = `
        <div class="quiz-completion-title">
          🎉 確認クイズ全${quizItems.length}問 完了！ スコア: ${correctCount} / ${quizItems.length} 正解 (${percent}%)
        </div>
        <p class="quiz-completion-desc">
          ${correctCount === quizItems.length ? '完璧です！重要構文と文脈理解が完全に身についています。' : '間違えた設問の解説をもう一度読み直して復習してみましょう。'}
        </p>
        <button type="button" class="btn-retry-quiz" id="btn-retry-quiz">
          🔄 もう一度挑戦する (Retry Quiz)
        </button>
      `;

      const retryBtn = document.getElementById('btn-retry-quiz');
      if (retryBtn) {
        retryBtn.addEventListener('click', resetQuiz);
      }
    } else if (banner) {
      banner.remove();
    }
  }

  function resetQuiz() {
    quizItems.forEach(quizItem => {
      delete quizItem.dataset.answered;
      delete quizItem.dataset.correctAnswered;
      quizItem.querySelectorAll('.quiz-btn').forEach(btn => {
        btn.classList.remove('correct', 'wrong');
      });
      const explanation = quizItem.querySelector('.quiz-explanation');
      if (explanation) explanation.style.display = 'none';
    });
    const banner = document.getElementById('quiz-completion-banner');
    if (banner) banner.remove();
  }

  quizItems.forEach(quizItem => {
    const buttons = quizItem.querySelectorAll('.quiz-btn');
    const explanation = quizItem.querySelector('.quiz-explanation');

    buttons.forEach(btn => {
      btn.addEventListener('click', () => {
        if (quizItem.dataset.answered === "true") return;
        quizItem.dataset.answered = "true";

        const isCorrect = btn.getAttribute('data-correct') === "true";
        if (isCorrect) {
          quizItem.dataset.correctAnswered = "true";
        }

        buttons.forEach(b => {
          if (b.getAttribute('data-correct') === "true") {
            b.classList.add('correct');
          } else if (b === btn && !isCorrect) {
            b.classList.add('wrong');
          }
        });

        if (explanation) {
          explanation.style.display = 'block';
        }

        updateQuizSummary();
      });
    });
  });

  // ==========================================================================
  // 9. HERO TITLE MOUSE SCROLL & CUE INTERACTION
  // ==========================================================================
  const heroCue = document.getElementById('hero-scroll-cue');
  const articleSection = document.getElementById('section-article');

  function scrollToArticleTop() {
    if (!articleSection) return;
    const navBar = document.querySelector('.nav-bar');
    const navHeight = navBar ? navBar.offsetHeight : 48;
    const targetY = articleSection.getBoundingClientRect().top + window.pageYOffset - navHeight - 24;
    window.scrollTo({
      top: Math.max(0, Math.round(targetY)),
      behavior: 'smooth'
    });
  }

  if (heroCue && articleSection) {
    heroCue.addEventListener('click', (e) => {
      e.preventDefault();
      scrollToArticleTop();
    });
  }

  let isGlidingDown = false;
  window.addEventListener('wheel', (e) => {
    if (window.scrollY < 120 && e.deltaY > 15 && !isGlidingDown) {
      if (articleSection) {
        isGlidingDown = true;
        scrollToArticleTop();
        setTimeout(() => {
          isGlidingDown = false;
        }, 900);
      }
    }
  }, { passive: true });

  // ==========================================================================
  // 11. REAL READER ACCESS TRACKER (実読者アクセス数集計)
  // ==========================================================================
  try {
    const pathParts = window.location.pathname.split('/').filter(Boolean);
    let currentSlug = '';
    for (let i = 0; i < pathParts.length; i++) {
      if (pathParts[i] === 'index.html' && i > 0) {
        currentSlug = pathParts[i - 1];
        break;
      }
    }
    if (!currentSlug && pathParts.length >= 1) {
      currentSlug = pathParts[pathParts.length - 1].replace('.html', '');
      if (currentSlug === 'index' && pathParts.length >= 2) {
        currentSlug = pathParts[pathParts.length - 2];
      }
    }
    const ignoreNames = ['news_portal', 'junior', 'academictimes', 'culture', 'entertainment', 'law', 'science', 'society', 'world'];
    if (currentSlug && !ignoreNames.includes(currentSlug)) {
      const storageKey = 'academic_times_real_views';
      const viewsObj = JSON.parse(localStorage.getItem(storageKey) || '{}');
      viewsObj[currentSlug] = (viewsObj[currentSlug] || 0) + 1;
      localStorage.setItem(storageKey, JSON.stringify(viewsObj));
    }
  } catch(e) {}
});
