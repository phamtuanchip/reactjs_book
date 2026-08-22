"""Generate PDF from all chapters using headless Chrome. Run from project root."""
import subprocess, os, sys, glob

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(BASE, 'dist')
CHAPTERS_DIR = os.path.join(BASE, 'chapters')

os.makedirs(OUT_DIR, exist_ok=True)
sys.stdout.reconfigure(encoding='utf-8')

CHAPTER_ORDER = []
for part in ['part1-foundation', 'part2-javascript', 'part3-react-basic',
             'part4-react-advanced', 'part5-ecosystem']:
    part_dir = os.path.join(CHAPTERS_DIR, part)
    chapters = sorted(glob.glob(os.path.join(part_dir, 'chapter-*.html')))
    CHAPTER_ORDER.extend(chapters)

print(f'Found {len(CHAPTER_ORDER)} chapters')

pdf_files = []
for i, chapter_path in enumerate(CHAPTER_ORDER, 1):
    name = os.path.basename(chapter_path).replace('.html', '')
    pdf_out = os.path.join(OUT_DIR, f'{name}.pdf')
    file_url = 'file:///' + chapter_path.replace('\\', '/').replace(' ', '%20')

    print(f'[{i:2d}/25] {name}...', end=' ', flush=True)
    result = subprocess.run([
        CHROME,
        '--headless=new',
        '--disable-gpu',
        '--no-sandbox',
        '--run-all-compositor-stages-before-draw',
        '--print-to-pdf-no-header',
        f'--print-to-pdf={pdf_out}',
        '--virtual-time-budget=5000',
        file_url
    ], capture_output=True, timeout=30)

    if os.path.exists(pdf_out):
        size = os.path.getsize(pdf_out) // 1024
        print(f'OK ({size}KB)')
        pdf_files.append(pdf_out)
    else:
        print(f'FAILED: {result.stderr.decode()[:100]}')

# Merge all PDFs with pypdf
if pdf_files:
    print(f'\nMerging {len(pdf_files)} PDFs...')
    from pypdf import PdfWriter, PdfReader
    writer = PdfWriter()
    for pdf_path in pdf_files:
        try:
            reader = PdfReader(pdf_path)
            for page in reader.pages:
                writer.add_page(page)
        except Exception as e:
            print(f'  Warning: {os.path.basename(pdf_path)}: {e}')

    merged_path = os.path.join(OUT_DIR, 'lap-trinh-reactjs-full.pdf')
    with open(merged_path, 'wb') as f:
        writer.write(f)
    size_mb = os.path.getsize(merged_path) / 1024 / 1024
    print(f'Merged PDF: {merged_path} ({size_mb:.1f}MB)')
else:
    print('No PDFs to merge!')
