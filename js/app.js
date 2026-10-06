// Interactive Audio Player, Dialogue Sequencer, Speed Controller, Sticky Title Bar, TOC & Quiz Controller

document.addEventListener('DOMContentLoaded', () => {
  let currentAudio = null;
  let currentActiveBtn = null;
  let isSequencePlaying = false;
  let sequenceIndex = 0;
  let currentPlaybackRate = 1.0;

  // ==========================================================================
  // 1. SPEED CONTROL
  // ==========================================================================
  window.setSpeed = function(rate, btnElement) {
    currentPlaybackRate = parseFloat(rate);
    if (currentAudio) {
      currentAudio.playbackRate = currentPlaybackRate;
    }
    document.querySelectorAll('.btn-speed-opt').forEach(btn => {
      btn.classList.remove('active-speed');
    });
    if (btnElement) {
      btnElement.classList.add('active-speed');
    }
  };

  document.querySelectorAll('.btn-speed-opt').forEach(btn => {
    btn.addEventListener('click', () => {
      const rate = btn.getAttribute('data-speed');
      window.setSpeed(rate, btn);
    });
  });

  // ==========================================================================
  // 2. AUDIO PLAYBACK (Single & Continuous Playlist)
  // ==========================================================================
  window.stopAllAudio = function() {
    if (currentAudio) {
      currentAudio.pause();
      currentAudio = null;
    }
    if (currentActiveBtn) {
      currentActiveBtn.classList.remove('playing');
      const icon = currentActiveBtn.querySelector('.audio-state-icon');
      if (icon) icon.textContent = '▶';
      currentActiveBtn = null;
    }
    document.querySelectorAll('.dlg-turn').forEach(el => el.classList.remove('active-turn'));
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

  // Continuous Sequence: Title -> English Body -> Keita & Nanami Dialogue
  const sequencePlaylist = [
    { src: 'audio/headline.mp3', targetId: 'article-headline-block', label: '記事タイトル朗読' },
    { src: 'audio/full_body.mp3', targetId: 'full-body-banner', label: '英文本文朗読' },
    { src: 'audio/dlg_01.mp3', targetId: 'dlg-1', label: 'Nanamiの質問' },
    { src: 'audio/dlg_02.mp3', targetId: 'dlg-2', label: 'Keita先生の解説' },
    { src: 'audio/dlg_03.mp3', targetId: 'dlg-3', label: 'Nanamiの疑問' },
    { src: 'audio/dlg_04.mp3', targetId: 'dlg-4', label: 'Keita先生（思考の余白）' },
    { src: 'audio/dlg_05.mp3', targetId: 'dlg-5', label: 'Nanami（見知らぬ人との関わり）' },
    { src: 'audio/dlg_06.mp3', targetId: 'dlg-6', label: 'Keita先生（日常の温もり）' },
    { src: 'audio/dlg_07.mp3', targetId: 'dlg-7', label: 'Nanamiのまとめ' }
  ];

  function playSequenceStep(index, masterBtn) {
    if (!isSequencePlaying || index >= sequencePlaylist.length) {
      isSequencePlaying = false;
      if (masterBtn) {
        masterBtn.classList.remove('playing');
        const icon = masterBtn.querySelector('.audio-state-icon');
        if (icon) icon.textContent = '▶';
        const label = masterBtn.querySelector('.audio-btn-label');
        if (label) label.textContent = '英語朗読 ＋ 日本語対話解説を続けて聴く';
      }
      document.querySelectorAll('.dlg-turn').forEach(el => el.classList.remove('active-turn'));
      const headlineBlock = document.getElementById('article-headline-block');
      if (headlineBlock) headlineBlock.classList.remove('active-turn');
      return;
    }

    sequenceIndex = index;
    const item = sequencePlaylist[index];

    document.querySelectorAll('.dlg-turn').forEach(el => el.classList.remove('active-turn'));
    const headlineBlock = document.getElementById('article-headline-block');
    if (headlineBlock) headlineBlock.classList.remove('active-turn');

    const targetEl = document.getElementById(item.targetId);
    if (targetEl) {
      targetEl.classList.add('active-turn');
      targetEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    if (masterBtn) {
      const label = masterBtn.querySelector('.audio-btn-label');
      if (label) label.textContent = `再生中: ${item.label} (${index + 1}/${sequencePlaylist.length})`;
    }

    const audio = new Audio(item.src);
    audio.playbackRate = currentPlaybackRate;
    currentAudio = audio;

    audio.play().catch(e => {
      console.warn("Sequence audio error:", e);
      playSequenceStep(index + 1, masterBtn);
    });

    audio.addEventListener('ended', () => {
      setTimeout(() => {
        playSequenceStep(index + 1, masterBtn);
      }, 500);
    });
  }

  const continuousBtn = document.getElementById('btn-play-continuous');
  if (continuousBtn) {
    continuousBtn.addEventListener('click', () => {
      if (isSequencePlaying) {
        window.stopAllAudio();
        continuousBtn.classList.remove('playing');
        const icon = continuousBtn.querySelector('.audio-state-icon');
        if (icon) icon.textContent = '▶';
        const label = continuousBtn.querySelector('.audio-btn-label');
        if (label) label.textContent = '英語朗読 ＋ 日本語対話解説を続けて聴く';
        return;
      }

      window.stopAllAudio();
      isSequencePlaying = true;
      continuousBtn.classList.add('playing');
      const icon = continuousBtn.querySelector('.audio-state-icon');
      if (icon) icon.textContent = '⏸';

      playSequenceStep(0, continuousBtn);
    });
  }

  const dialogueContinuousBtn = document.getElementById('btn-play-dialogue-all');
  if (dialogueContinuousBtn) {
    dialogueContinuousBtn.addEventListener('click', () => {
      if (isSequencePlaying) {
        window.stopAllAudio();
        dialogueContinuousBtn.classList.remove('playing');
        const icon = dialogueContinuousBtn.querySelector('.audio-state-icon');
        if (icon) icon.textContent = '▶';
        return;
      }

      window.stopAllAudio();
      isSequencePlaying = true;
      dialogueContinuousBtn.classList.add('playing');
      const icon = dialogueContinuousBtn.querySelector('.audio-state-icon');
      if (icon) icon.textContent = '⏸';

      playSequenceStep(2, dialogueContinuousBtn);
    });
  }

  document.querySelectorAll('[data-sentence-audio]').forEach(btn => {
    btn.addEventListener('click', (e) => {
      if (e.target.closest('.tooltip-bubble')) return;
      const src = btn.getAttribute('data-sentence-audio');
      window.playAudio(src, btn);
    });
  });

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
  // 3. JAPANESE TRANSLATION TOGGLE
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
  // 4. STICKY ARTICLE TITLE BAR & READING PROGRESS
  // ==========================================================================
  const stickyBar = document.getElementById('sticky-article-bar');
  const progressBar = document.getElementById('reading-progress');
  const mainHeader = document.querySelector('.article-header');

  window.addEventListener('scroll', () => {
    const scrollY = window.scrollY || window.pageYOffset;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    
    // Progress calculation
    if (progressBar && docHeight > 0) {
      const progressPercent = Math.min(100, Math.max(0, (scrollY / docHeight) * 100));
      progressBar.style.width = `${progressPercent}%`;
    }

    // Sticky bar visibility
    if (stickyBar && mainHeader) {
      const headerBottom = mainHeader.offsetTop + mainHeader.offsetHeight;
      if (scrollY > headerBottom) {
        stickyBar.classList.add('visible');
      } else {
        stickyBar.classList.remove('visible');
      }
    }
  }, { passive: true });

  // ==========================================================================
  // 5. FLOATING TABLE OF CONTENTS (TOC)
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
  // 6. VOCABULARY TOOLTIPS FOR MOBILE (Tap support)
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
  // 7. INTERACTIVE QUIZ
  // ==========================================================================
  document.querySelectorAll('.quiz-item').forEach(quizItem => {
    const buttons = quizItem.querySelectorAll('.quiz-btn');
    const explanation = quizItem.querySelector('.quiz-explanation');

    buttons.forEach(btn => {
      btn.addEventListener('click', () => {
        if (quizItem.dataset.answered === "true") return;
        quizItem.dataset.answered = "true";

        const isCorrect = btn.getAttribute('data-correct') === "true";

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
      });
    });
  });

  // ==========================================================================
  // 8. HERO TITLE MOUSE SCROLL INTERACTION (マウススクロールで記事上部へ移動)
  // ==========================================================================
  const heroCue = document.getElementById('hero-scroll-cue');
  const articleSection = document.getElementById('section-article');

  function scrollToArticleTop() {
    if (!articleSection) return;
    const navBar = document.querySelector('.nav-bar');
    const navHeight = navBar ? navBar.offsetHeight : 48;
    // Calculate exact target position: top of articleSection minus navBar height and 24px breathing margin
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
    // When the user is looking at the initial hero title and scrolls downward
    if (window.scrollY < 120 && e.deltaY > 10 && !isGlidingDown) {
      if (articleSection) {
        isGlidingDown = true;
        scrollToArticleTop();
        setTimeout(() => {
          isGlidingDown = false;
        }, 900);
      }
    }
  }, { passive: true });
});

