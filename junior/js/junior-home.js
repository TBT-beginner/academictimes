// THE JUNIOR - Home Portal Interactive Controller
// Features: Date/Edition Switcher, Instant Archive & Back Number Search, High School Study Resources

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
  let currentEditionDate = '2026-10-08';

  const dateKeys = Object.keys(JUNIOR_EDITIONS).sort().reverse(); // ["2026-10-08", "2026-10-07", ...]

  // ==========================================================================
  // 1. DATE / EDITION SWITCHER
  // ==========================================================================
  function switchEdition(dateKey) {
    if (!JUNIOR_EDITIONS[dateKey]) dateKey = "2026-10-08";
    currentEditionDate = dateKey;
    const ed = JUNIOR_EDITIONS[dateKey];

    // Update Dropdown
    if (dateSelect) dateSelect.value = dateKey;

    // Update Top Date Bar
    if (topDateBar) {
      topDateBar.innerHTML = `${ed.dateStr} &nbsp;|&nbsp; Tokyo & London Editions &nbsp;•&nbsp; High School Eiken Pre-2 ~ 2 Broadsheet`;
    }

    // Prev / Next button states
    const idx = dateKeys.indexOf(dateKey);
    if (btnNext) btnNext.disabled = (idx <= 0);
    if (btnPrev) btnPrev.disabled = (idx >= dateKeys.length - 1);

    // Notice banner for past edition
    if (editionNotice) {
      if (dateKey !== "2026-10-08") {
        editionNotice.style.display = "block";
        editionNotice.innerHTML = `
          <span>📅 表示中：<strong>${ed.editionLabel}</strong> — ${ed.tagline}</span>
          <button type="button" class="btn-return-today" onclick="window.switchEdition('2026-10-08')" style="background: var(--junior-green); color: #fff; border: none; padding: 0.25rem 0.65rem; border-radius: 3px; font-weight: 700; cursor: pointer; margin-left: 0.5rem;">本日最新号に戻る ↺</button>
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
    JUNIOR_ARTICLES.forEach(a => { artMap[a.slug] = a; });

    // 1. Lead Story & Sub-leads in Center Column
    const lead = artMap[ed.topLeadSlug];
    const centerCol = document.querySelector('.home-col-center');
    if (centerCol && lead) {
      const subLeads = ed.subLeadSlugs.map(slug => artMap[slug]).filter(Boolean);
      centerCol.innerHTML = `
        <article class="junior-hero-lead-box">
          <div class="lead-image-wrap">
            <img src="${lead.image}" alt="${lead.title}" class="lead-image" onerror="this.src='https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=1000&auto=format&fit=crop&q=80'">
          </div>

          <span class="category-tag green-fill" style="padding: 0.2rem 0.5rem;">
            TODAY'S FEATURED LEAD • ${lead.category.toUpperCase()}
          </span>
          <h1 class="lead-story-title" style="font-size: 2.1rem; margin-top: 0.5rem; line-height: 1.25;">
            <a href="${lead.path}" style="color: var(--times-black); text-decoration: none;">
              ${lead.title}
            </a>
          </h1>
          <p style="font-size: 1.05rem; font-weight: 700; color: #222; margin: 0.5rem 0;">
            ${lead.headline_ja}
          </p>
          <p class="lead-story-lead">
            ${lead.lead_snippet}
          </p>
          <div style="margin-top: 1rem; display: flex; gap: 1rem; align-items: center; flex-wrap: wrap;">
            <a href="${lead.path}" class="btn-trial" style="background: #235937; border-color: #235937; color: #ffffff !important; text-decoration: none; padding: 0.45rem 1.1rem; font-weight: 700; border-radius: 3px;">
              🌱 この記事をJunior版で読む（音声・クイズ付） →
            </a>
            <a href="${lead.senior_path}" style="font-size: 0.82rem; color: #555; text-decoration: underline;">
              🏛️ 発展・難関大版で比較する ↗
            </a>
          </div>
        </article>

        <!-- Sub-leads inside Center Column -->
        <div class="sub-lead-grid">
          ${subLeads.map(sub => `
            <div class="sub-lead-item">
              <div style="height: 120px; overflow: hidden; margin-bottom: 0.5rem; background: #e9ecef;">
                <img src="${sub.image}" alt="${sub.title}" style="width: 100%; height: 100%; object-fit: cover;" onerror="this.style.display='none'">
              </div>
              <span class="category-tag green-fill" style="padding: 0.15rem 0.4rem;">${sub.category.toUpperCase()}</span>
              <h3 class="sub-lead-title" style="margin-top: 0.35rem;">
                <a href="${sub.path}" style="color: var(--times-black); text-decoration: none;">${sub.title}</a>
              </h3>
              <p style="font-size: 0.85rem; font-weight: 700; color: #222; margin-top: 0.25rem;">${sub.headline_ja}</p>
              <p style="font-size: 0.8rem; color: var(--times-muted); margin-top: 0.25rem; line-height: 1.5;">
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
      leftCol.innerHTML = `
        <div style="font-family: var(--font-headline); font-weight: 700; font-size: 0.9rem; border-bottom: 2px solid var(--times-black); padding-bottom: 0.3rem; margin-bottom: 1rem; color: #235937;">
          LATEST DISPATCHES • 注目の話題
        </div>
      ` + leftArticles.map((art, idx) => `
        <article class="left-story">
          <span class="badge-new green-fill">${idx === 0 ? 'NEW' : 'DISPATCH'} • ${art.category.toUpperCase()}</span>
          <h2 class="left-story-title">
            <a href="${art.path}">${art.title}</a>
          </h2>
          <p class="left-story-snippet">
            <strong>${art.headline_ja}</strong><br>${art.subhead}
          </p>
          <div class="article-source-meta" style="margin-top: 0.4rem;">
            <a href="${art.path}" style="font-weight: 700; color: #235937; text-decoration: underline; font-size: 0.82rem;">🌱 Junior版を読む →</a>
          </div>
        </article>
      `).join('');
    }

    // 3. Right Column Digest
    const rightCol = document.querySelector('.home-col-right');
    if (rightCol) {
      const rightArticles = ed.rightDigestSlugs.map(s => artMap[s]).filter(Boolean);
      rightCol.innerHTML = `
        <div style="background: #eef5f0; border-left: 3px solid #235937; padding: 0.75rem 1rem; margin-bottom: 1rem;">
          <div style="font-weight: 700; font-size: 0.82rem; color: #143820;">🌱 高校生ステップアップ学習</div>
          <div style="font-size: 0.75rem; color: #235937; margin-top: 0.2rem;">英検準2級〜2級の標準英文とゆっくり音声で読む厳選ダイジェスト</div>
        </div>
      ` + rightArticles.map(art => `
        <article class="right-story" style="display: flex; gap: 0.75rem; justify-content: space-between; border-bottom: 1px dotted #ccc; padding-bottom: 0.85rem; margin-bottom: 0.85rem;">
          <div class="right-story-body" style="flex: 1;">
            <span class="category-tag green-fill" style="padding: 0.1rem 0.35rem; font-size: 0.7rem;">${art.category.toUpperCase()}</span>
            <h3 class="right-story-title" style="font-size: 0.92rem; margin: 0.25rem 0;">
              <a href="${art.path}" style="color: var(--times-black); text-decoration: none;">${art.title}</a>
            </h3>
            <p style="font-size: 0.76rem; color: var(--times-muted); line-height: 1.4; margin: 0;">
              ${art.headline_ja}
            </p>
          </div>
          <div class="right-story-img" style="width: 70px; height: 70px; flex-shrink: 0; background: #e2e4e8; overflow: hidden; border-radius: 2px;">
            <img src="${art.image}" alt="${art.title}" style="width: 100%; height: 100%; object-fit: cover;" onerror="this.style.display='none'">
          </div>
        </article>
      `).join('') + `
        <div style="background: #111; color: #fff; padding: 1rem; margin-top: 1rem; border-radius: 2px;">
          <div style="font-weight: 700; font-size: 0.85rem; color: #fff; margin-bottom: 0.35rem;">🏛️ 難関大・発展版へステップアップ</div>
          <p style="font-size: 0.75rem; color: #ccc; line-height: 1.5; margin-bottom: 0.75rem;">
            東大・京大・早慶レベルの英文解釈に挑戦するなら、本家THE ACADEMIC TIMESへ移動してください。
          </p>
          <a href="../index.html" style="display: inline-block; background: #fff; color: #111; padding: 0.3rem 0.7rem; font-weight: 700; font-size: 0.75rem; text-decoration: none; border-radius: 2px;">
            発展版トップページへ ↗
          </a>
        </div>
      `;
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
    
    const results = JUNIOR_ARTICLES.filter(art => {
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
      archiveCount.textContent = `該当件数: ${results.length} 件 (全${JUNIOR_ARTICLES.length}件中)`;
    }

    if (!archiveGrid) return;

    if (results.length === 0) {
      archiveGrid.innerHTML = `
        <div style="grid-column: 1 / -1; text-align: center; padding: 3rem 1rem; color: var(--times-muted); font-family: var(--font-serif);">
          <div style="font-size: 2rem; margin-bottom: 0.5rem;">🔍</div>
          <div style="font-size: 1.1rem; font-weight: bold; color: var(--times-black);">条件に一致するJunior記事が見つかりませんでした</div>
          <p style="font-size: 0.85rem; margin-top: 0.25rem;">キーワードを変えるか、カテゴリフィルターを「全分野」に設定してお試しください。</p>
        </div>
      `;
      return;
    }

    archiveGrid.innerHTML = results.map(art => `
      <div class="junior-catalog-card" style="border: 1px solid var(--times-light-border); padding: 1.25rem; background: #fff; margin-bottom: 1.25rem; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <span class="category-tag green-fill" style="padding: 0.15rem 0.45rem;">${art.category.toUpperCase()}</span>
            <span style="font-size: 0.75rem; color: #235937; font-weight: 700;">英検準2級〜2級 • 📅 ${art.date}</span>
          </div>
          <h3 style="font-family: var(--font-headline); font-size: 1.15rem; margin-bottom: 0.35rem; line-height: 1.35;">
            <a href="${art.path}" style="color: var(--times-black); text-decoration: none;">
              ${art.title}
            </a>
          </h3>
          <p style="font-size: 0.85rem; font-weight: 700; color: #222; margin-bottom: 0.4rem;">
            ${art.headline_ja}
          </p>
          <p style="font-size: 0.8rem; color: var(--times-muted); line-height: 1.6;">
            ${art.subhead}
          </p>
        </div>
        <div style="margin-top: 1rem; padding-top: 0.75rem; border-top: 1px dashed #e0e0e0; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem;">
          <a href="${art.path}" style="color: #235937; font-weight: 700; font-size: 0.82rem; text-decoration: underline;">
            🌱 Junior版を読む（音声付） →
          </a>
          <a href="${art.senior_path}" style="color: #111; font-size: 0.78rem; text-decoration: none;">
            🏛️ 発展版（難関大） ↗
          </a>
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
  // 3. STUDY RESOURCES RENDER
  // ==========================================================================
  function renderStudyResources() {
    const container = document.getElementById('media-resources-grid');
    if (!container || typeof JUNIOR_STUDY_RESOURCES === 'undefined') return;

    container.innerHTML = JUNIOR_STUDY_RESOURCES.map(media => `
      <div class="media-card" style="border-top: 3px solid #235937; padding: 1.25rem; background: #fff; border: 1px solid var(--times-light-border); border-top: 3px solid #235937;">
        <div class="media-card-head" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
          <div class="media-card-title" style="font-weight: 700; font-family: var(--font-headline); font-size: 1.05rem; color: #143820;">${media.name}</div>
          <span class="media-badge" style="background: #eef5f0; color: #235937; border: 1px solid #c1decb; padding: 0.15rem 0.45rem; font-size: 0.72rem; font-weight: 700;">${media.badge}</span>
        </div>
        <div style="font-size: 0.82rem; line-height: 1.65; color: #333; margin-top: 0.5rem;">
          ${media.point}
        </div>
      </div>
    `).join('');
  }

  // Initial Check for Hash Edition or data-default-edition
  const hash = window.location.hash;
  const defaultFromAttr = document.body ? document.body.getAttribute('data-default-edition') : null;
  if (hash && hash.startsWith('#date-')) {
    const targetDate = hash.replace('#date-', '');
    if (JUNIOR_EDITIONS[targetDate]) {
      switchEdition(targetDate);
    } else {
      switchEdition(defaultFromAttr || '2026-10-08');
    }
  } else if (defaultFromAttr && JUNIOR_EDITIONS[defaultFromAttr]) {
    switchEdition(defaultFromAttr);
  } else {
    switchEdition('2026-10-08');
  }

  filterAndRenderArchive();
  renderStudyResources();
});
