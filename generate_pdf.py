import os
import base64
import zipfile
import io
from datetime import datetime

# Цветовая палитра "Канада" (Светлая тема)
LIGHT_BG = "#FDFBF7"           # Мягкий кремовый
LIGHT_TEXT = "#1E291B"         # Глубокий хвойный
LIGHT_BLOCK_BG = "#FFFFFF"     # Чистый белый для карточек
LIGHT_BORDER = "rgba(45, 90, 39, 0.15)"

# Цветовая палитра "Канадская ночь" (Тёмная тема)
DARK_BG = "#121A10"            # Очень тёмный хвойный
DARK_TEXT = "#F3EFE9"          # Мягкий светлый крем
DARK_BLOCK_BG = "#1A2418"      # Плотный хвойный для карточек
DARK_BORDER = "rgba(216, 34, 41, 0.2)"

# Общие акценты
COLOR_CANADIAN_RED = "#D82229"     # Канадский красный
COLOR_FOREST_GREEN = "#2D5A27"     # Лесной зелёный

# Игнорируем служебное
EXCLUDE_FILES = {
    "tracks_list.txt",
    "index.html",
    "generate_html.py",
    "midi_archive.zip",
    "meta_info.txt",
    ".git",
    ".github",
    "README.md",
    "LICENSE"
}

def parse_meta(filename):
    meta_dict = {}
    if not os.path.exists(filename):
        return meta_dict
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or '=' not in line:
                continue
            track, info = line.split('=', 1)
            clean_track = track.replace('.mid', '').replace('.MIDI', '').strip()
            meta_dict[clean_track] = info.strip()
    return meta_dict

def get_meta_hint(track_name, category_title, meta_dict):
    clean = track_name.replace('.mid', '').replace('.MIDI', '').strip()
    if clean in meta_dict:
        return f"{clean} — {meta_dict[clean]}"
    return f"Трек из категории: {category_title}"

def create_and_encode_zip():
    print("Собираем ZIP-архив в памяти...")
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for root, dirs, files in os.walk("."):
            if '.git' in root or '.github' in root:
                continue
            for file in files:
                if file in EXCLUDE_FILES:
                    continue
                if file.lower().endswith(('.mid', '.midi')):
                    file_path = os.path.join(root, file)
                    archive_name = os.path.relpath(file_path, ".")
                    zip_file.write(file_path, archive_name)
    zip_buffer.seek(0)
    encoded = base64.b64encode(zip_buffer.read()).decode('utf-8')
    return f"data:application/zip;base64,{encoded}"

def parse_tracks(filename):
    categories = {}
    root_tracks = []
    sponsor_line = None
    
    if not os.path.exists(filename):
        print(f"Ошибка: Файл {filename} не найден!")
        return root_tracks, categories, sponsor_line
        
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            if "спонсирован" in line.lower() and "мисс хаус" in line.lower():
                sponsor_line = line
                continue
            
            normalized_line = line.replace('/', '\\')
                
            if '\\' in normalized_line:
                cat, track = normalized_line.split('\\', 1)
                cat = cat.strip()
                if cat not in categories:
                    categories[cat] = []
                categories[cat].append(track.strip())
            else:
                root_tracks.append(normalized_line)
    return root_tracks, categories, sponsor_line

def split_list(lst):
    half = (len(lst) + 1) // 2
    return lst[:half], lst[half:]

print("Старт генерации страницы...")
root_tracks, categories, sponsor_line = parse_tracks('tracks_list.txt')
track_meta = parse_meta('meta_info.txt')

total_tracks = len(root_tracks) + sum(len(v) for v in categories.values())
if sponsor_line:
    total_tracks += 1

current_date = datetime.now().strftime("%d.%m.%Y")
archive_data_url = create_and_encode_zip()

html_content = f"""<!DOCTYPE html>
<html lang="ru" data-theme="light">
<head>
    <meta charset="utf-8">
    <title>Архив MIDI-треков Koranon'a71</title>
    <script src="https://cdn.jsdelivr.net/combine/npm/@html-midi-player/midi-player@1.5.0,npm/@html-midi-player/midi-player@1.5.0/dist/midi-player.min.js"></script>
    <style>
        :root[data-theme="light"] {{
            --bg-color: {LIGHT_BG};
            --text-color: {LIGHT_TEXT};
            --block-bg: {LIGHT_BLOCK_BG};
            --border-color: {LIGHT_BORDER};
            --header-mid-bg: #FFFFFF;
            --header-text-color: {LIGHT_TEXT};
            --dashed-color: rgba(45, 90, 39, 0.15);
            --toggle-border: {COLOR_CANADIAN_RED};
            --search-bg: #FFFFFF;
        }}
        :root[data-theme="dark"] {{
            --bg-color: {DARK_BG};
            --text-color: {DARK_TEXT};
            --block-bg: {DARK_BLOCK_BG};
            --border-color: {DARK_BORDER};
            --header-mid-bg: #1A2418;
            --header-text-color: {DARK_TEXT};
            --dashed-color: rgba(218, 34, 41, 0.25);
            --toggle-border: {COLOR_FOREST_GREEN};
            --search-bg: #1A2418;
        }}

        html, body {{
            margin: 0;
            padding: 0;
            background-color: var(--bg-color);
            font-family: 'Segoe UI', Arial, sans-serif;
            color: var(--text-color);
            transition: background-color 0.3s, color 0.3s;
        }}
        body {{
            padding: 40px 30px;
            max-width: 1200px;
            margin: 0 auto;
        }}
        * {{ box-sizing: border-box; }}
        
        .theme-toggle-btn {{
            position: fixed;
            top: 20px;
            right: 20px;
            background: var(--block-bg);
            border: 2px solid var(--toggle-border);
            color: var(--text-color);
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 9pt;
            font-weight: bold;
            text-transform: uppercase;
            cursor: pointer;
            box-shadow: 0 3px 10px rgba(0,0,0,0.1);
            transition: all 0.3s;
            z-index: 10000;
        }}
        .theme-toggle-btn:hover {{
            transform: translateY(-1px);
            box-shadow: 0 5px 12px rgba(0,0,0,0.15);
        }}
        
        .header-container {{
            border: 2px solid {COLOR_CANADIAN_RED};
            border-radius: 12px;
            background: linear-gradient(90deg, {COLOR_CANADIAN_RED} 0%, {COLOR_CANADIAN_RED} 15%, var(--header-mid-bg) 15%, var(--header-mid-bg) 85%, {COLOR_CANADIAN_RED} 85%, {COLOR_CANADIAN_RED} 100%);
            padding: 40px 30px;
            margin-bottom: 20px;
            text-align: center;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            position: relative;
            transition: background 0.3s;
        }}
        
        .header-container::before {{
            content: "🍁";
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 75pt;
            opacity: 0.08;
            pointer-events: none;
        }}
        
        h1 {{
            font-size: 26pt;
            margin: 0 0 10px 0;
            text-transform: uppercase;
            letter-spacing: 2px;
            font-weight: 900;
            color: var(--header-text-color);
        }}
        
        .badges-wrapper {{
            margin-bottom: 20px;
            display: flex;
            gap: 12px;
            justify-content: center;
            align-items: center;
            flex-wrap: wrap;
        }}
        
        .badge {{
            display: inline-block;
            background-color: {COLOR_FOREST_GREEN};
            color: #FFFFFF;
            padding: 6px 14px;
            border-radius: 20px;
            font-weight: bold;
            font-size: 9pt;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        
        .badge.date-badge {{
            background-color: var(--text-color);
            color: var(--bg-color);
            transition: background-color 0.3s, color 0.3s;
        }}
        
        .download-btn {{
            display: inline-block;
            background-color: {COLOR_CANADIAN_RED};
            color: #FFFFFF;
            padding: 7px 18px;
            border-radius: 20px;
            font-weight: bold;
            font-size: 9pt;
            text-transform: uppercase;
            text-decoration: none;
            transition: transform 0.2s, background-color 0.2s;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }}
        .download-btn:hover {{
            background-color: #b01b20;
            transform: translateY(-1px);
        }}
        
        .description {{
            font-size: 11pt;
            color: var(--header-text-color);
            margin-top: 15px;
            font-style: italic;
            line-height: 1.5;
        }}

        /* Стили поля живого поиска */
        .search-wrapper {{
            margin-bottom: 25px;
            position: relative;
        }}
        .search-input {{
            width: 100%;
            padding: 14px 20px;
            font-size: 11pt;
            border: 2px solid var(--border-color);
            border-radius: 8px;
            background-color: var(--search-bg);
            color: var(--text-color);
            box-shadow: 0 2px 8px rgba(0,0,0,0.02);
            outline: none;
            transition: all 0.2s;
        }}
        .search-input:focus {{
            border-color: {COLOR_FOREST_GREEN};
            box-shadow: 0 4px 12px rgba(45, 90, 39, 0.1);
        }}
        
        /* Блоки категорий */
        .category-block {{
            background-color: var(--block-bg);
            border: 1px solid var(--border-color);
            border-left: 5px solid {COLOR_FOREST_GREEN};
            border-radius: 6px;
            padding: 20px;
            margin-bottom: 25px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.02);
            transition: background-color 0.3s, border-color 0.3s;
        }}
        
        h2 {{
            font-size: 13pt;
            margin: 0 0 15px 0;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: {COLOR_FOREST_GREEN};
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 7px;
        }}
        
        .tracks-table {{ width: 100%; border-collapse: collapse; }}
        .tracks-td {{ width: 50%; vertical-align: top; padding-right: 20px; }}
        
        .track-row {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 6px 0;
            border-bottom: 1px dashed var(--dashed-color);
        }}
        
        .track-info-block {{
            display: flex;
            align-items: center;
            font-size: 10pt;
            color: var(--text-color);
            cursor: help;
            flex-grow: 1;
            padding-right: 10px;
        }}
        
        .track-marker {{ 
            color: {COLOR_CANADIAN_RED}; 
            font-size: 10pt; 
            margin-right: 8px; 
            font-weight: bold; 
        }}
        
        .play-inline-btn {{
            background: none;
            border: 1px solid {COLOR_FOREST_GREEN};
            color: {COLOR_FOREST_GREEN};
            border-radius: 4px;
            padding: 2px 8px;
            font-size: 8pt;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.2s;
            text-transform: uppercase;
        }}
        .play-inline-btn:hover {{
            background-color: {COLOR_FOREST_GREEN};
            color: #FFFFFF;
        }}
        .play-inline-btn.playing {{
            background-color: {COLOR_CANADIAN_RED};
            border-color: {COLOR_CANADIAN_RED};
            color: #FFFFFF;
        }}

        /* Фиксированный плеер */
        .global-player-panel {{
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            background: var(--block-bg);
            border: 2px solid {COLOR_FOREST_GREEN};
            padding: 10px 20px;
            border-radius: 30px;
            box-shadow: 0 5px 25px rgba(0,0,0,0.15);
            display: none;
            align-items: center;
            gap: 12px;
            z-index: 9999;
            width: 90%;
            max-width: 530px;
            transition: background-color 0.3s;
        }}
        
        /* Кнопка скролла к играющему треку */
        .scroll-to-track-btn {{
            background: none;
            border: 1px solid var(--border-color);
            font-size: 13px;
            cursor: pointer;
            padding: 4px 8px;
            border-radius: 50%;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .scroll-to-track-btn:hover {{
            background-color: var(--border-color);
            transform: scale(1.1);
        }}
        
        .global-player-title {{
            font-size: 9pt;
            font-weight: bold;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            max-width: 140px;
            color: var(--text-color);
        }}
        midi-player {{
            flex-grow: 1;
            background: transparent;
        }}
        midi-player::part(control-panel) {{
            background: transparent;
            border: none;
        }}
        
        :root[data-theme="dark"] midi-player::part(play-button),
        :root[data-theme="dark"] midi-player::part(time-text) {{
            filter: invert(1);
        }}
        
        .sponsor-footer {{
            text-align: center;
            margin-top: 60px;
            margin-bottom: 40px;
            padding: 20px;
            font-size: 11pt;
            font-style: italic;
            color: {COLOR_FOREST_GREEN};
            border-top: 1px solid var(--border-color);
            opacity: 0.85;
        }}
    </style>
</head>
<body>

    <button class="theme-toggle-btn" id="themeToggle" title="Сменить тему">🌙 Тёмная</button>

    <div class="header-container">
        <h1>Архив MIDI-треков Koranon'a71</h1>
        <div class="badges-wrapper">
            <div class="badge">Рекомендовано Саспенс</div>
            <div class="badge date-badge">Обновлено: {current_date}</div>
            <a href="{archive_data_url}" download="midi_archive.zip" class="download-btn">📥 Скачать .ZIP пак</a>
        </div>
        <div class="description">
            Полное собрание музыкального космоса.<br>
            В канадских лесах припрятано {total_tracks} треков для инструментов SS14.
        </div>
    </div>

    <div class="search-wrapper">
        <input type="text" id="searchInput" class="search-input" placeholder="🔍 Быстрый поиск трека по названию или описанию...">
    </div>
"""

def render_tracks_table(tracks_list, current_category, meta_data, cat_folder=""):
    left, right = split_list(sorted(tracks_list, key=str.lower))
    table_html = '<table class="tracks-table"><tr><td class="tracks-td">'
    
    for side in [left, right]:
        for track in side:
            clean_track = track.replace('.mid', '').replace('.MIDI', '')
            hint = get_meta_hint(clean_track, current_category, meta_data)
            
            if cat_folder:
                file_url = f"{cat_folder}/{track}"
            else:
                file_url = track
                
            table_html += f"""
            <div class="track-row" data-search-string="{clean_track.lower()} {hint.lower()}">
                <div class="track-info-block" title="{hint}">
                    <span class="track-marker">🍁</span> {clean_track}
                </div>
                <button class="play-inline-btn" data-url="{file_url}" data-title="{clean_track}">Слушать</button>
            </div>"""
        if side == left:
            table_html += '</td><td class="tracks-td">'
            
    table_html += '</td></tr></table>'
    return table_html

if root_tracks:
    html_content += f"""
    <div class="category-block">
        <h2>Основные государственные гимны</h2>
        {render_tracks_table(root_tracks, "Основные государственные гимны", track_meta)}
    </div>
    """

for cat in sorted(categories.keys()):
    friendly_title = cat.replace('_', ' ')
    html_content += f"""
    <div class="category-block">
        <h2>{friendly_title}</h2>
        {render_tracks_table(categories[cat], friendly_title, track_meta, cat_folder=cat)}
    </div>
    """

if sponsor_line:
    clean_sponsor = sponsor_line.replace('.mid', '').replace('.MIDI', '')
    hint = get_meta_hint(clean_sponsor, "Благодарности", track_meta)
    html_content += f"""<div class="sponsor-footer" title="{hint}">🌲 {clean_sponsor} 🌲</div>"""

html_content += """
    <div class="global-player-panel" id="playerPanel">
        <button class="scroll-to-track-btn" id="scrollToTrackBtn" title="Найти трек на странице">🎯</button>
        <div class="global-player-title" id="playerTitle">Загрузка...</div>
        <midi-player id="midiPlayer" sound-font="https://storage.googleapis.com/magentadata/js/soundfonts/sgm_plus"></midi-player>
    </div>

    <script>
        // Скрипт переключения тем
        const themeToggle = document.getElementById('themeToggle');
        const htmlDoc = document.documentElement;

        const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        const savedTheme = localStorage.getItem('theme');
        
        if (savedTheme) {
            htmlDoc.setAttribute('data-theme', savedTheme);
            updateToggleButton(savedTheme);
        } else if (systemPrefersDark) {
            htmlDoc.setAttribute('data-theme', 'dark');
            updateToggleButton('dark');
        }

        themeToggle.addEventListener('click', () => {
            const currentTheme = htmlDoc.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            
            htmlDoc.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            updateToggleButton(newTheme);
        });

        function updateToggleButton(theme) {
            if (theme === 'dark') {
                themeToggle.textContent = '☀️ Светлая';
            } else {
                themeToggle.textContent = '🌙 Тёмная';
            }
        }

        // Логика живого поиска
        const searchInput = document.getElementById('searchInput');
        const categoryBlocks = document.querySelectorAll('.category-block');

        searchInput.addEventListener('input', function() {
            const query = this.value.toLowerCase().strip ? this.value.toLowerCase().strip() : this.value.toLowerCase().trim();
            
            categoryBlocks.forEach(block => {
                const rows = block.querySelectorAll('.track-row');
                let visibleRowsInBlock = 0;
                
                rows.forEach(row => {
                    const searchData = row.getAttribute('data-search-string');
                    if (searchData.includes(query)) {
                        row.style.setProperty('display', 'flex', 'important');
                        visibleRowsInBlock++;
                    } else {
                        row.style.setProperty('display', 'none', 'important');
                    }
                });
                
                // Если в блоке не осталось подходящих строк - скрываем категорию целиком
                if (query !== "" && visibleRowsInBlock === 0) {
                    block.style.display = 'none';
                } else {
                    block.style.display = 'block';
                }
            });
        });

        // Логика плеера
        const buttons = document.querySelectorAll('.play-inline-btn');
        const playerPanel = document.getElementById('playerPanel');
        const playerTitle = document.getElementById('playerTitle');
        const midiPlayer = document.getElementById('midiPlayer');
        const scrollToTrackBtn = document.getElementById('scrollToTrackBtn');
        let currentBtn = null;

        buttons.forEach(btn => {
            btn.addEventListener('click', () => {
                const url = btn.getAttribute('data-url');
                const title = btn.getAttribute('data-title');

                if (currentBtn === btn) {
                    if (midiPlayer.playing) {
                        midiPlayer.stop();
                        btn.classList.remove('playing');
                        btn.textContent = 'Слушать';
                    } else {
                        midiPlayer.start();
                        btn.classList.add('playing');
                        btn.textContent = 'Стоп';
                    }
                    return;
                }

                if (currentBtn) {
                    currentBtn.classList.remove('playing');
                    currentBtn.textContent = 'Слушать';
                }

                currentBtn = btn;
                btn.classList.add('playing');
                btn.textContent = 'Стоп';
                
                playerTitle.textContent = title;
                playerPanel.style.display = 'flex';
                
                midiPlayer.src = url.split('/').map(encodeURIComponent).join('/');
                
                setTimeout(() => {
                    midiPlayer.start();
                }, 300);
            });
        });

        midiPlayer.addEventListener('stop', () => {
            if (currentBtn && !midiPlayer.playing) {
                currentBtn.classList.remove('playing');
                currentBtn.textContent = 'Слушать';
            }
        });

        // Плавный скролл к текущему играющему треку
        scrollToTrackBtn.addEventListener('click', () => {
            if (currentBtn) {
                currentBtn.scrollIntoView({ behavior: 'smooth', block: 'center' });
                
                // Легкое визуальное подмигивание строке, чтобы точно заметить её глазами
                const targetRow = currentBtn.closest('.track-row');
                if (targetRow) {
                    targetRow.style.transition = 'background-color 0.3s';
                    const oldBg = targetRow.style.backgroundColor;
                    targetRow.style.backgroundColor = 'rgba(216, 34, 41, 0.15)';
                    setTimeout(() => {
                        targetRow.style.backgroundColor = oldBg;
                    }, 800);
                }
            }
        });
    </script>
</body>
</html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"[Успех] Скрипт обновлен. Поиск и фокус-скролл к треку добавлены!")