// THE ACADEMIC TIMES - Home Portal Interactive Controller
// Features: Date/Edition Switcher, Instant Archive & Back Number Search, Media Literacy Resources

const ALL_ARTICLES = typeof ARTICLES !== 'undefined' ? ARTICLES : [];

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
  const dateKeys = Object.keys(EDITIONS).sort().reverse(); // ["2026-10-14", "2026-10-13", ...]
  const latestDate = dateKeys[0] || '2026-10-14';
  let currentEditionDate = latestDate;

  // ==========================================================================
  // 1. DATE / EDITION SWITCHER
  // ==========================================================================
  function switchEdition(dateKey) {
    if (!EDITIONS[dateKey]) dateKey = latestDate;
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
      if (dateKey !== latestDate) {
        editionNotice.style.display = "block";
        editionNotice.innerHTML = `
          <span>📅 表示中：<strong>${ed.editionLabel}</strong> — ${ed.tagline}</span>
          <button type="button" class="btn-return-today" onclick="window.switchEdition('${latestDate}')">本日最新号に戻る ↺</button>
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
    
    let results = ALL_ARTICLES.filter(art => {
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
      archiveCount.textContent = `該当件数: ${totalCount} 件 (全${ALL_ARTICLES.length}件中)`;
    }

    if (!archiveGrid) return;

    if (totalCount === 0) {
      archiveGrid.className = 'archive-results-grid';
      archiveGrid.innerHTML = `
        <div style="grid-column: 1 / -1; text-align: center; padding: 3rem 1rem; color: var(--times-muted); font-family: var(--font-serif);">
          <div style="font-size: 2rem; margin-bottom: 0.5rem;">🔍</div>
          <div style="font-size: 1.1rem; font-weight: bold; color: var(--times-black);">条件に一致する過去記事が見つかりませんでした</div>
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
          <div class="archive-card">
            <div class="archive-card-meta">
              <div>
                ${foundationalBadge}
                <span class="category-tag">${art.category.toUpperCase()}</span>
              </div>
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
                <span class="category-tag" style="font-size: 0.65rem;">${art.category.toUpperCase()}</span>
              </div>
            </div>
            <div class="archive-list-main">
              <h4 class="archive-list-title"><a href="${art.path}">${art.title}</a></h4>
              <p class="archive-list-ja">${art.headline_ja}</p>
              <div class="archive-list-source">📰 ${art.source_name}</div>
            </div>
            <div class="archive-list-action">
              <a href="${art.path}" class="archive-read-link" style="font-size: 0.8rem; font-weight: bold;">読む →</a>
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
    if (EDITIONS[targetDate]) {
      switchEdition(targetDate);
    } else {
      switchEdition(defaultFromAttr || latestDate);
    }
  } else if (defaultFromAttr && EDITIONS[defaultFromAttr]) {
    switchEdition(defaultFromAttr);
  } else {
    switchEdition(latestDate);
  }

  filterAndRenderArchive();
  renderMediaResources();
  updateLiveReaderCounters();
});
