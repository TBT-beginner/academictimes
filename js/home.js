// THE ACADEMIC TIMES - Home Portal Interactive Controller
// Features: Date/Edition Switcher, Instant Archive & Back Number Search, Media Literacy Resources

document.addEventListener('DOMContentLoaded', () => {
  const dateSelect = document.getElementById('select-edition-date');
  const btnPrev = document.getElementById('btn-edition-prev');
  const btnNext = document.getElementById('btn-edition-next');
  const topDateBar = document.getElementById('top-date-bar-text');
  const editionNotice = document.getElementById('edition-notice-banner');
  
  const searchInput = document.getElementById('archive-search-input');
  const categoryFilters = document.querySelectorAll('.filter-category-btn');
  const sourceFilter = document.getElementById('archive-source-select');
  const archiveGrid = document.getElementById('archive-results-grid');
  const archiveCount = document.getElementById('archive-count-badge');

  let activeCategory = 'all';
  let activeSource = 'all';
  let activeQuery = '';
  let currentEditionDate = '2026-10-10';

  const dateKeys = Object.keys(EDITIONS).sort().reverse(); // ["2026-10-10", "2026-10-09", ...]

  // ==========================================================================
  // 1. DATE / EDITION SWITCHER
  // ==========================================================================
  function switchEdition(dateKey) {
    if (!EDITIONS[dateKey]) dateKey = "2026-10-10";
    currentEditionDate = dateKey;
    const ed = EDITIONS[dateKey];

    // Update Dropdown
    if (dateSelect) dateSelect.value = dateKey;

    // Update Top Date Bar
    if (topDateBar) {
      topDateBar.innerHTML = `${ed.dateStr} &nbsp;|&nbsp; Tokyo & London Editions &nbsp;•&nbsp; Daily University Exam Academic Digest`;
    }

    // Prev / Next button states
    const idx = dateKeys.indexOf(dateKey);
    if (btnNext) btnNext.disabled = (idx <= 0);
    if (btnPrev) btnPrev.disabled = (idx >= dateKeys.length - 1);

    // Notice banner for past edition
    if (editionNotice) {
      if (dateKey !== "2026-10-10") {
        editionNotice.style.display = "block";
        editionNotice.innerHTML = `
          <span>📅 表示中：<strong>${ed.editionLabel}</strong> — ${ed.tagline}</span>
          <button type="button" class="btn-return-today" onclick="window.switchEdition('2026-10-10')">本日最新号に戻る ↺</button>
        `;
      } else {
        editionNotice.style.display = "none";
      }
    }

    // Update Hero Section
    renderHeroSection(ed);

    // Update URL hash without scroll
    try {
      history.replaceState(null, null, `#date-${dateKey}`);
    } catch(e) {}
  }

  window.switchEdition = switchEdition;

  function renderHeroSection(ed) {
    const artMap = {};
    ALL_ARTICLES.forEach(a => { artMap[a.slug] = a; });

    // 1. Lead Story
    const lead = artMap[ed.topLeadSlug];
    const centerCol = document.querySelector('.home-col-center');
    if (centerCol && lead) {
      const subLeads = ed.subLeadSlugs.map(slug => artMap[slug]).filter(Boolean);
      centerCol.innerHTML = `
        <article>
          <div class="lead-image-wrap">
            <img src="${lead.image}" alt="${lead.title}" class="lead-image" onerror="this.src='https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=1000&auto=format&fit=crop&q=80'">
          </div>
          <span class="category-tag">TOP LEAD STORY • ${lead.category_label}</span>
          <h1 class="lead-story-title">
            <a href="${lead.path}">${lead.title}</a>
          </h1>
          <p class="lead-story-lead">
            ${lead.lead_snippet}
          </p>
          <div class="article-source-meta" style="margin-top: 0.75rem;">
            <strong>Source:</strong> <span>${lead.source_name}</span>
          </div>
        </article>

        <!-- Sub-leads inside Center Column -->
        <div class="sub-lead-grid">
          ${subLeads.map(sub => `
            <div class="sub-lead-item">
              <div style="height: 120px; overflow: hidden; margin-bottom: 0.5rem; background: #e9ecef;">
                <img src="${sub.image}" alt="${sub.title}" style="width: 100%; height: 100%; object-fit: cover;" onerror="this.style.display='none'">
              </div>
              <span class="category-tag">${sub.category_label}</span>
              <h3 class="sub-lead-title">
                <a href="${sub.path}">${sub.title}</a>
              </h3>
              <p style="font-size: 0.8rem; color: var(--times-muted); margin-top: 0.25rem;">
                ${sub.subhead}
              </p>
            </div>
          `).join('')}
        </div>
      `;
    }

    // 2. Left Column Dispatches
    const leftCol = document.querySelector('.home-col-left');
    if (leftCol) {
      const leftArticles = ed.leftDispatches.map(s => artMap[s]).filter(Boolean);
      leftCol.innerHTML = leftArticles.map((art, idx) => `
        <article class="left-story">
          <span class="${idx === 0 ? 'badge-new' : 'badge-updated'}">${idx === 0 ? 'NEW' : 'DISPATCH'} • ${art.category_label}</span>
          <h2 class="left-story-title">
            <a href="${art.path}">${art.title}</a>
          </h2>
          <p class="left-story-snippet">
            ${art.headline_ja}。${art.subhead}
          </p>
          <div class="article-source-meta">
            <span>According to ${art.source_name}</span>
          </div>
        </article>
      `).join('');
    }

    // 3. Right Column Digest
    const rightCol = document.querySelector('.home-col-right');
    if (rightCol) {
      const rightArticles = ed.rightDigestSlugs.map(s => artMap[s]).filter(Boolean);
      rightCol.innerHTML = rightArticles.map(art => `
        <article class="right-story">
          <div class="right-story-body">
            <span class="category-tag">${art.category_label}</span>
            <h3 class="right-story-title">
              <a href="${art.path}">${art.title}</a>
            </h3>
            <p style="font-size: 0.8rem; color: var(--times-muted);">
              ${art.headline_ja}
            </p>
          </div>
          <div class="right-story-img" style="background: #e2e4e8; overflow: hidden;">
            <img src="${art.image}" alt="${art.title}" style="width: 100%; height: 100%; object-fit: cover;" onerror="this.style.display='none'">
          </div>
        </article>
      `).join('');
    }
  }

  if (dateSelect) {
    dateSelect.addEventListener('change', (e) => {
      switchEdition(e.target.value);
    });
  }

  if (btnPrev) {
    btnPrev.addEventListener('click', () => {
      const idx = dateKeys.indexOf(currentEditionDate);
      if (idx < dateKeys.length - 1) {
        switchEdition(dateKeys[idx + 1]);
      }
    });
  }

  if (btnNext) {
    btnNext.addEventListener('click', () => {
      const idx = dateKeys.indexOf(currentEditionDate);
      if (idx > 0) {
        switchEdition(dateKeys[idx - 1]);
      }
    });
  }

  // ==========================================================================
  // 2. BACK NUMBER & ARCHIVE SEARCH ENGINE
  // ==========================================================================
  function filterAndRenderArchive() {
    const q = activeQuery.trim().toLowerCase();
    
    const results = ALL_ARTICLES.filter(art => {
      // Category filter
      if (activeCategory !== 'all' && art.category !== activeCategory) {
        return false;
      }
      // Source filter
      if (activeSource !== 'all' && art.source_media_key !== activeSource) {
        return false;
      }
      // Text query
      if (q) {
        const fullText = (
          art.title + ' ' + 
          art.headline_ja + ' ' + 
          art.subhead + ' ' + 
          art.source_name + ' ' + 
          art.lead_snippet + ' ' + 
          art.category_label
        ).toLowerCase();
        if (!fullText.includes(q)) return false;
      }
      return true;
    });

    if (archiveCount) {
      archiveCount.textContent = `該当件数: ${results.length} 件 (全${ALL_ARTICLES.length}件中)`;
    }

    if (!archiveGrid) return;

    if (results.length === 0) {
      archiveGrid.innerHTML = `
        <div style="grid-column: 1 / -1; text-align: center; padding: 3rem 1rem; color: var(--times-muted); font-family: var(--font-serif);">
          <div style="font-size: 2rem; margin-bottom: 0.5rem;">🔍</div>
          <div style="font-size: 1.1rem; font-weight: bold; color: var(--times-black);">条件に一致する過去記事が見つかりませんでした</div>
          <p style="font-size: 0.85rem; margin-top: 0.25rem;">キーワードを変えるか、カテゴリフィルターを「全分野」に設定してお試しください。</p>
        </div>
      `;
      return;
    }

    archiveGrid.innerHTML = results.map(art => `
      <div class="archive-card">
        <div class="archive-card-meta">
          <span class="category-tag">${art.category.toUpperCase()}</span>
          <span class="archive-date-tag">📅 ${art.date}</span>
        </div>
        <h3 class="archive-card-title">
          <a href="${art.path}">${art.title}</a>
        </h3>
        <p class="archive-card-ja">${art.headline_ja}</p>
        <p class="archive-card-snippet">${art.subhead}</p>
        <div class="archive-card-footer">
          <span class="archive-source-pill">📰 ${art.source_name}</span>
          <a href="${art.path}" class="archive-read-link">記事を読む →</a>
        </div>
      </div>
    `).join('');
  }

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      activeQuery = e.target.value;
      filterAndRenderArchive();
    });
  }

  if (sourceFilter) {
    sourceFilter.addEventListener('change', (e) => {
      activeSource = e.target.value;
      filterAndRenderArchive();
    });
  }

  categoryFilters.forEach(btn => {
    btn.addEventListener('click', () => {
      categoryFilters.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      activeCategory = btn.getAttribute('data-cat');
      filterAndRenderArchive();
    });
  });

  // ==========================================================================
  // 3. MEDIA LITERACY RESOURCES RENDER
  // ==========================================================================
  function renderMediaResources() {
    const container = document.getElementById('media-resources-grid');
    if (!container) return;

    container.innerHTML = MEDIA_RESOURCES.map(media => `
      <div class="media-card">
        <div class="media-card-head">
          <div class="media-card-title">${media.name}</div>
          <span class="media-badge">${media.badge}</span>
        </div>
        <div class="media-card-meta">
          <span>本拠: ${media.country}</span> • <span>創刊: ${media.founded}</span> • <span>スタンス: ${media.stance}</span>
        </div>
        <div class="media-section-block">
          <div class="media-block-label">🎓 高校生が知っておくべき理由</div>
          <div class="media-block-content">${media.whyHighSchoolersMustKnow}</div>
        </div>
        <div class="media-section-block">
          <div class="media-block-label">✍️ 大学入試での出題・活用価値</div>
          <div class="media-block-content">${media.examSignificance}</div>
        </div>
        <div class="media-card-topics">
          <strong>頻出テーマ例:</strong> ${media.sampleTopics}
        </div>
      </div>
    `).join('');
  }

  // Initial Check for Hash Edition or data-default-edition
  const hash = window.location.hash;
  const defaultFromAttr = document.body ? document.body.getAttribute('data-default-edition') : null;
  if (hash && hash.startsWith('#date-')) {
    const targetDate = hash.replace('#date-', '');
    if (EDITIONS[targetDate]) {
      switchEdition(targetDate);
    } else {
      switchEdition(defaultFromAttr || '2026-10-09');
    }
  } else if (defaultFromAttr && EDITIONS[defaultFromAttr]) {
    switchEdition(defaultFromAttr);
  } else {
    switchEdition('2026-10-09');
  }

  filterAndRenderArchive();
  renderMediaResources();
});
