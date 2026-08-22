// Generate EPUB from all HTML chapters
import pkg from 'epub-gen-memory';
const { EPub } = pkg;
import { readFileSync, writeFileSync, mkdirSync, readdirSync } from 'fs';
import { resolve, dirname, join } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const BASE = dirname(__dirname);
const OUT_DIR = join(BASE, 'dist');
const CHAPTERS_DIR = join(BASE, 'chapters');

mkdirSync(OUT_DIR, { recursive: true });

const PARTS = [
  'part1-foundation',
  'part2-javascript',
  'part3-react-basic',
  'part4-react-advanced',
  'part5-ecosystem',
];

const CHAPTER_TITLES = {
  'chapter-01': 'Chương 1: Làm quen với Web và Lập trình',
  'chapter-02': 'Chương 2: HTML — Xương sống trang web',
  'chapter-03': 'Chương 3: CSS — Trang điểm cho trang web',
  'chapter-04': 'Chương 4: JavaScript Nhập môn',
  'chapter-05': 'Chương 5: Hàm và Phạm vi biến',
  'chapter-06': 'Chương 6: Object và Array Nâng cao',
  'chapter-07': 'Chương 7: Lập trình Bất đồng bộ',
  'chapter-08': 'Chương 8: JavaScript Hiện đại (ES6+)',
  'chapter-09': 'Chương 9: Giới thiệu React',
  'chapter-10': 'Chương 10: JSX và Component',
  'chapter-11': 'Chương 11: State và Event',
  'chapter-12': 'Chương 12: useEffect và Vòng đời Component',
  'chapter-13': 'Chương 13: Styling trong React',
  'chapter-14': 'Chương 14: React Router',
  'chapter-15': 'Chương 15: Hooks Nâng cao',
  'chapter-16': 'Chương 16: Quản lý State Toàn cục',
  'chapter-17': 'Chương 17: Data Fetching với TanStack Query',
  'chapter-18': 'Chương 18: Form Nâng cao',
  'chapter-19': 'Chương 19: Tối ưu Hiệu năng',
  'chapter-20': 'Chương 20: Testing trong React',
  'chapter-21': 'Chương 21: TypeScript với React',
  'chapter-22': 'Chương 22: Next.js — React Framework',
  'chapter-23': 'Chương 23: Authentication và Authorization',
  'chapter-24': 'Chương 24: Deployment và CI/CD',
  'chapter-25': 'Chương 25: Dự án cuối khóa — Task Manager',
};

// Collect all chapters
const chapters = [];
for (const part of PARTS) {
  const partDir = join(CHAPTERS_DIR, part);
  const files = readdirSync(partDir)
    .filter(f => f.match(/^chapter-\d+\.html$/))
    .sort();

  for (const file of files) {
    const id = file.replace('.html', '');
    const html = readFileSync(join(partDir, file), 'utf-8');

    // Extract main content (between <main> tags)
    const mainMatch = html.match(/<main[^>]*>([\s\S]*?)<\/main>/i);
    const content = mainMatch ? mainMatch[1] : html;

    // Remove sidebar, scripts, progress bar divs
    const cleanContent = content
      .replace(/<script[\s\S]*?<\/script>/gi, '')
      .replace(/<div class="chapter-nav">[\s\S]*?<\/div>/gi, '');

    chapters.push({
      title: CHAPTER_TITLES[id] || id,
      content: cleanContent,
      filename: `${id}.xhtml`,
    });
  }
}

console.log(`Building EPUB with ${chapters.length} chapters...`);

const epub = new EPub({
  title: 'Lập Trình ReactJS — Từ Cơ Bản Đến Nâng Cao',
  author: 'Pham Tuan',
  publisher: 'Lập Trình ReactJS',
  description: 'Sách tiếng Việt hướng dẫn lập trình ReactJS từ cơ bản đến nâng cao dành cho người mới bắt đầu.',
  language: 'vi',

  tocTitle: 'Mục lục',
  css: `
    body { font-family: Georgia, serif; line-height: 1.8; color: #333; }
    h1, h2, h3 { color: #1a1a2e; }
    h1 { font-size: 1.8em; border-bottom: 2px solid #61dafb; padding-bottom: 8px; }
    h2 { font-size: 1.3em; color: #21a1c4; margin-top: 24px; }
    code, pre { font-family: monospace; background: #f4f4f4; padding: 2px 6px; border-radius: 3px; }
    pre { display: block; padding: 16px; overflow-x: auto; font-size: 0.85em; white-space: pre-wrap; }
    .callout { border-left: 4px solid #61dafb; padding: 12px 16px; margin: 16px 0; background: #f0faff; }
    .quiz { border: 1px solid #ddd; padding: 16px; margin: 16px 0; border-radius: 4px; }
    .answer { font-style: italic; color: #666; }
    .mermaid { display: none; }
  `,
}, chapters);

const epubBuffer = await epub.genEpub();
const outPath = join(OUT_DIR, 'lap-trinh-reactjs-full.epub');
writeFileSync(outPath, epubBuffer);

const sizeMB = (epubBuffer.length / 1024 / 1024).toFixed(1);
console.log(`EPUB created: ${outPath} (${sizeMB}MB)`);
