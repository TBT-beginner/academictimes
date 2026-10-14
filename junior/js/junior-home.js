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
  const dateKeys = Object.keys(JUNIOR_EDITIONS).sort().reverse(); // ["2026-10-14", "2026-10-13", ...]
  const latestDate = dateKeys[0] || '2026-10-14';
  let currentEditionDate = latestDate;

  // ==========================================================================
  // 1. DATE / EDITION SWITCHER
  // ==========================================================================
  function switchEdition(dateKey) {
    if (!JUNIOR_EDITIONS[dateKey]) dateKey = latestDate;
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
      if (dateKey !== latestDate) {
        editionNotice.style.display = "block";
        editionNotice.innerHTML = `
          <span>📅 表示中：<strong>${ed.editionLabel}</strong> — ${ed.tagline}</span>
          <button type="button" class="btn-return-today" onclick="window.switchEdition('${latestDate}')" style="background: var(--junior-green); color: #fff; border: none; padding: 0.25rem 0.65rem; border-radius: 3px; font-weight: 700; cursor: pointer; margin-left: 0.5rem;">本日最新号に戻る ↺</button>
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
  // 1-B. COLLAPSIBLE EDITIONS QUICK NAVIGATOR
  // ==========================================================================
  const btnToggleEditions = document.getElementById('btn-toggle-editions');
  const editionCollapsible = document.getElementById('edition-collapsible-content');
  const toggleEditionsIcon = document.getElementById('toggle-editions-icon');
  if (btnToggleEditions && editionCollapsible) {
    btnToggleEditions.addEventListener('click', () => {
      const isExpanded = editionCollapsible.classList.toggle('expanded');
      btnToggleEditions.setAttribute('aria-expanded', isExpanded);
      if (toggleEditionsIcon) toggleEditionsIcon.textContent = isExpanded ? '▴' : '▾';
    });
  }

  // ==========================================================================
  // 2. ENHANCED BACK NUMBER & ARCHIVE SEARCH ENGINE
  // ==========================================================================
  const periodPillBtns = document.querySelectorAll('.period-pill-btn');
  const btnViewCard = document.getElementById('btn-view-card');
  const btnViewList = document.getElementById('btn-view-list');
  const sortSelect = document.getElementById('archive-sort-select');
  const pageSizeSelect = document.getElementById('archive-pagesize-select');
  const statusText = document.getElementById('archive-status-text');
  const loadMoreWrap = document.getElementById('archive-load-more-wrap');
  const paginationWrap = document.getElementById('archive-pagination-wrap');

  let activePeriod = 'all';
  let activeSort = 'newest';
  let viewMode = 'card'; // 'card' | 'list'
  let pageSize = 12; // 12, 24, or 'all'
  let currentPage = 1;

  function filterAndRenderArchive() {
    const q = activeQuery.trim().toLowerCase();
    
    let results = JUNIOR_ARTICLES.filter(art => {
      // Category filter
      if (activeCategory !== 'all' && art.category !== activeCategory) {
        return false;
      }
      // Source filter
      if (activeSource !== 'all' && art.source_media_key !== activeSource) {
        return false;
      }
      // Period filter
      if (activePeriod === 'recent' && (art.date < '2026-10-08')) {
        return false;
      }
      if (activePeriod === 'early' && (art.date > '2026-10-07')) {
        return false;
      }
      if (activePeriod === 'foundational') {
        const isFoundational = (art.category_label && art.category_label.includes('過去の基礎論文')) ||
                               (art.slug && (art.slug.includes('solid-state-sodium-ion') || art.slug.includes('alzheimers-blood-biomarker')));
        if (!isFoundational) return false;
      }
      // Text query
      if (q) {
        const fullText = (
          art.title + ' ' + 
          art.headline_ja + ' ' + 
          art.subhead + ' ' + 
          art.source_name + ' ' + 
          art.lead_snippet + ' ' + 
          (art.category_label || '')
        ).toLowerCase();
        if (!fullText.includes(q)) return false;
      }
      return true;
    });

    // Sorting
    if (activeSort === 'newest') {
      results.sort((a, b) => (b.date || '').localeCompare(a.date || ''));
    } else if (activeSort === 'oldest') {
      results.sort((a, b) => (a.date || '').localeCompare(b.date || ''));
    } else if (activeSort === 'alpha') {
      results.sort((a, b) => (a.title || '').localeCompare(b.title || ''));
    }

    const totalCount = results.length;
    if (archiveCount) {
      archiveCount.textContent = `該当件数: ${totalCount} 件 (全${JUNIOR_ARTICLES.length}件中)`;
    }

    if (!archiveGrid) return;

    if (totalCount === 0) {
      archiveGrid.className = 'archive-results-grid';
      archiveGrid.innerHTML = `
        <div style="grid-column: 1 / -1; text-align: center; padding: 3rem 1rem; color: var(--times-muted); font-family: var(--font-serif);">
          <div style="font-size: 2rem; margin-bottom: 0.5rem;">🔍</div>
          <div style="font-size: 1.1rem; font-weight: bold; color: var(--times-black);">条件に一致するJunior記事が見つかりませんでした</div>
          <p style="font-size: 0.85rem; margin-top: 0.25rem;">キーワードを変えるか、フィルターを「全分野」「全期間」に設定してお試しください。</p>
        </div>
      `;
      if (statusText) statusText.innerHTML = `全 <strong>0</strong> 件中 <strong>0</strong> 件を表示`;
      if (loadMoreWrap) loadMoreWrap.innerHTML = '';
      if (paginationWrap) paginationWrap.innerHTML = '';
      return;
    }

    // Pagination Calculation
    const effectivePageSize = (pageSize === 'all') ? totalCount : Number(pageSize);
    const totalPages = Math.ceil(totalCount / effectivePageSize) || 1;
    if (currentPage > totalPages) currentPage = 1;
    const startIdx = (currentPage - 1) * effectivePageSize;
    const endIdx = Math.min(startIdx + effectivePageSize, totalCount);
    const visibleResults = results.slice(startIdx, endIdx);

    // Update Status Bar
    if (statusText) {
      statusText.innerHTML = `全 <strong class="archive-status-highlight">${totalCount}</strong> 件中 <strong>${startIdx + 1}〜${endIdx}</strong> 件を表示中（ページ ${currentPage} / ${totalPages}）`;
    }

    // Render Items according to viewMode
    if (viewMode === 'card') {
      archiveGrid.className = 'archive-results-grid';
      archiveGrid.innerHTML = visibleResults.map(art => {
        const isFoundational = (art.category_label && art.category_label.includes('過去の基礎論文')) ||
                               (art.slug && (art.slug.includes('solid-state-sodium-ion') || art.slug.includes('alzheimers-blood-biomarker')));
        const foundationalBadge = isFoundational ? `<span style="background: #8b0000; color: #fff; font-size: 0.68rem; padding: 0.1rem 0.4rem; font-weight: 700; border-radius: 2px; margin-right: 0.35rem;">過去の基礎論文</span>` : '';
        return `
          <div class="junior-catalog-card" style="border: 1px solid var(--times-light-border); padding: 1.25rem; background: #fff; margin-bottom: 1.25rem; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                <div>
                  ${foundationalBadge}
                  <span class="category-tag green-fill" style="padding: 0.15rem 0.45rem;">${art.category.toUpperCase()}</span>
                </div>
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
        `;
      }).join('');
    } else {
      // List View (Compact Table-Style)
      archiveGrid.className = 'archive-list-view';
      archiveGrid.innerHTML = visibleResults.map(art => {
        const isFoundational = (art.category_label && art.category_label.includes('過去の基礎論文')) ||
                               (art.slug && (art.slug.includes('solid-state-sodium-ion') || art.slug.includes('alzheimers-blood-biomarker')));
        const foundationalBadge = isFoundational ? `<span style="background: #8b0000; color: #fff; font-size: 0.65rem; padding: 0.05rem 0.35rem; font-weight: 700; border-radius: 2px; margin-right: 0.25rem;">基礎論文</span>` : '';
        return `
          <div class="archive-list-row">
            <div class="archive-list-meta">
              <span class="archive-date-tag" style="color: #222; font-weight: 700;">📅 ${art.date}</span>
              <div>
                ${foundationalBadge}
                <span class="category-tag green-fill" style="font-size: 0.65rem; padding: 0.1rem 0.35rem;">${art.category.toUpperCase()}</span>
              </div>
            </div>
            <div class="archive-list-main">
              <h4 class="archive-list-title"><a href="${art.path}">${art.title}</a></h4>
              <p class="archive-list-ja">${art.headline_ja}</p>
              <div class="archive-list-source">📰 ${art.source_name}</div>
            </div>
            <div class="archive-list-action" style="display: flex; gap: 0.6rem; align-items: center;">
              <a href="${art.path}" style="color: #235937; font-weight: 700; font-size: 0.8rem; text-decoration: underline;">Junior版 →</a>
              <a href="${art.senior_path}" style="color: #666; font-size: 0.75rem; text-decoration: none;">発展版 ↗</a>
            </div>
          </div>
        `;
      }).join('');
    }

    // Render Load More / Show All Wrap
    if (loadMoreWrap) {
      if (pageSize !== 'all' && endIdx < totalCount) {
        loadMoreWrap.innerHTML = `
          <button type="button" class="btn-load-more" id="btn-load-more-action">
            <span>さらに12件表示する（もっと見る ↓）</span>
          </button>
          <button type="button" class="btn-show-all" id="btn-show-all-action">
            全 ${totalCount} 件を一括表示
          </button>
        `;
        const btnMore = document.getElementById('btn-load-more-action');
        if (btnMore) {
          btnMore.addEventListener('click', () => {
            pageSize = Number(pageSize) + 12;
            if (pageSizeSelect) pageSizeSelect.value = '24';
            filterAndRenderArchive();
          });
        }
        const btnAll = document.getElementById('btn-show-all-action');
        if (btnAll) {
          btnAll.addEventListener('click', () => {
            pageSize = 'all';
            if (pageSizeSelect) pageSizeSelect.value = 'all';
            filterAndRenderArchive();
          });
        }
      } else if (pageSize === 'all' && totalCount > 12) {
        loadMoreWrap.innerHTML = `
          <button type="button" class="btn-show-all" id="btn-reset-pagesize-action">
            最初に戻す（12件ずつ表示に戻す ↺）
          </button>
        `;
        const btnReset = document.getElementById('btn-reset-pagesize-action');
        if (btnReset) {
          btnReset.addEventListener('click', () => {
            pageSize = 12;
            currentPage = 1;
            if (pageSizeSelect) pageSizeSelect.value = '12';
            filterAndRenderArchive();
            const sec = document.getElementById('section-archive');
            if (sec) sec.scrollIntoView({ behavior: 'smooth' });
          });
        }
      } else {
        loadMoreWrap.innerHTML = '';
      }
    }

    // Render Numbered Pagination (if more than 1 page and not 'all')
    if (paginationWrap) {
      if (pageSize !== 'all' && totalPages > 1) {
        let pagHtml = '';
        pagHtml += `<button type="button" class="pagination-btn" ${currentPage === 1 ? 'disabled' : ''} data-page="${currentPage - 1}">◀ 前へ</button>`;
        
        const startP = Math.max(1, currentPage - 2);
        const endP = Math.min(totalPages, currentPage + 2);
        if (startP > 1) {
          pagHtml += `<button type="button" class="pagination-btn ${currentPage === 1 ? 'active' : ''}" data-page="1">1</button>`;
          if (startP > 2) pagHtml += `<span class="pagination-ellipsis">…</span>`;
        }
        for (let p = startP; p <= endP; p++) {
          pagHtml += `<button type="button" class="pagination-btn ${p === currentPage ? 'active' : ''}" data-page="${p}">${p}</button>`;
        }
        if (endP < totalPages) {
          if (endP < totalPages - 1) pagHtml += `<span class="pagination-ellipsis">…</span>`;
          pagHtml += `<button type="button" class="pagination-btn ${currentPage === totalPages ? 'active' : ''}" data-page="${totalPages}">${totalPages}</button>`;
        }

        pagHtml += `<button type="button" class="pagination-btn" ${currentPage === totalPages ? 'disabled' : ''} data-page="${currentPage + 1}">次へ ▶</button>`;
        paginationWrap.innerHTML = pagHtml;

        paginationWrap.querySelectorAll('.pagination-btn').forEach(btn => {
          btn.addEventListener('click', () => {
            const targetP = Number(btn.getAttribute('data-page'));
            if (targetP && targetP !== currentPage && targetP >= 1 && targetP <= totalPages) {
              currentPage = targetP;
              filterAndRenderArchive();
              const sec = document.getElementById('section-archive');
              if (sec) sec.scrollIntoView({ behavior: 'smooth' });
            }
          });
        });
      } else {
        paginationWrap.innerHTML = '';
      }
    }
  }

  // Event Listeners for Archive Controls
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      activeQuery = e.target.value;
      currentPage = 1;
      filterAndRenderArchive();
    });
  }

  if (sourceFilter) {
    sourceFilter.addEventListener('change', (e) => {
      activeSource = e.target.value;
      currentPage = 1;
      filterAndRenderArchive();
    });
  }

  categoryFilters.forEach(btn => {
    btn.addEventListener('click', () => {
      categoryFilters.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      activeCategory = btn.getAttribute('data-cat');
      currentPage = 1;
      filterAndRenderArchive();
    });
  });

  periodPillBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      periodPillBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      activePeriod = btn.getAttribute('data-period');
      currentPage = 1;
      filterAndRenderArchive();
    });
  });

  if (btnViewCard && btnViewList) {
    btnViewCard.addEventListener('click', () => {
      viewMode = 'card';
      btnViewCard.classList.add('active');
      btnViewList.classList.remove('active');
      filterAndRenderArchive();
    });
    btnViewList.addEventListener('click', () => {
      viewMode = 'list';
      btnViewList.classList.add('active');
      btnViewCard.classList.remove('active');
      filterAndRenderArchive();
    });
  }

  if (sortSelect) {
    sortSelect.addEventListener('change', (e) => {
      activeSort = e.target.value;
      filterAndRenderArchive();
    });
  }

  if (pageSizeSelect) {
    pageSizeSelect.addEventListener('change', (e) => {
      pageSize = e.target.value;
      currentPage = 1;
      filterAndRenderArchive();
    });
  }

  // ==========================================================================
  // 3. STUDY RESOURCES RENDER
  // ==========================================================================
  function renderStudyResources() {
    const container = document.getElementById('media-resources-grid');
    if (!container || typeof JUNIOR_STUDY_RESOURCES === 'undefined') return;

    container.innerHTML = JUNIOR_STUDY_RESOURCES.map(media => {
      const titleEn = media.title_en || (media.name.includes(' (') ? media.name.split(' (')[0] : media.name);
      const titleJa = media.title_ja || (media.name.includes(' (') ? media.name.split(' (')[1].replace(')', '') : '');
      const tipHtml = media.tip ? `
        <div class="junior-media-footer">
          <span>💡 <strong>学習のコツ：</strong>${media.tip}</span>
        </div>
      ` : '';

      return `
        <div class="junior-media-card">
          <div class="junior-media-badge-wrap">
            <span class="junior-media-badge">${media.badge}</span>
          </div>
          <div class="junior-media-header">
            <h3 class="junior-media-title-en">${titleEn}</h3>
            ${titleJa ? `<div class="junior-media-title-ja">${titleJa}</div>` : ''}
          </div>
          <div class="junior-media-body">
            ${media.point}
          </div>
          ${tipHtml}
        </div>
      `;
    }).join('');
  }

  // Update Live Reader Counters from localStorage
  function updateLiveReaderCounters() {
    try {
      const store = JSON.parse(localStorage.getItem('academic_times_real_views') || '{}');
      document.querySelectorAll('.live-reader-count').forEach(el => {
        const slug = el.getAttribute('data-slug');
        if (slug) {
          const views = store[slug] || 1;
          el.textContent = views.toLocaleString();
        }
      });
    } catch(e) {}
  }

  // Initial Check for Hash Edition or data-default-edition
  const hash = window.location.hash;
  const defaultFromAttr = document.body ? document.body.getAttribute('data-default-edition') : null;
  if (hash && hash.startsWith('#date-')) {
    const targetDate = hash.replace('#date-', '');
    if (JUNIOR_EDITIONS[targetDate]) {
      switchEdition(targetDate);
    } else {
      switchEdition(defaultFromAttr || latestDate);
    }
  } else if (defaultFromAttr && JUNIOR_EDITIONS[defaultFromAttr]) {
    switchEdition(defaultFromAttr);
  } else {
    switchEdition(latestDate);
  }

  filterAndRenderArchive();
  renderStudyResources();
  updateLiveReaderCounters();
});
